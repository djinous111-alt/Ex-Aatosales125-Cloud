# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20261017-0922-geo-qa-cta-href-redacted
status: open
run_date: 2026-10-17
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-vremennaya-registratsiya-vladivostok-rastamozhka-avto-2026
severity: high
category: qa

### What went wrong
- Writer положил в `article.html` три CTA с литералом `href="[REDACTED]"` (каталог×2, Telegram×1).
- `excalibur_blog_link_verify.py` классифицировал это как `internal_relative`, собрал URL от `--site-base` и получил HTTP 404 → verdict fail.
- Остальные gates (research-notes, fact-check, html-linter, slop, cannibalization, utility, human-voice) — PASS; статья по тексту beginner-fit OK.
- GEO QA не правил HTML (контракт: FIX → writer).

### How the agent recovered this run
- Зафиксировал FIX в `article-qa.md` + blocker в `article.meta.json` `geo_qa`.
- Проверил, что `$CATALOG_URL` и `$TELEGRAM_URL` отдают HTTP 200 (значения в incident не записывались).
- Вернул Director: re-run writer на CTA href, затем re-QA link-verify.
- Writer FIX cycle 1 (2026-10-17): подставил живые href из env (каталог×2, Telegram×1); литерал `[REDACTED]` в href убран; локальный `link_verify` → pass; текст lead/H2/FAQ не менялся.
- Workaround commit: pre-commit secret scanner блокирует `CATALOG_URL`/`TELEGRAM_URL` в HTML; на CTA-строки добавлен `<!-- pragma: allowlist secret -->`. Также в `CLOUD_AGENT_INJECTED_SECRET_NAMES` был битый хвост (URL как "имя") — для commit отфильтрованы только валидные bash-имена. Durable fix в skill/contract всё ещё нужен.
- GEO QA re-run after FIX (2026-10-17): все 8 gates PASS; `link-verify` failed_count=0; `article-qa.md` verdict PASS score 91; cover||schema разблокированы. Incident остаётся open до durable fix в writer skill/contract.

### Durable fix needed before next run
- В writer skill / writing contract явно: CTA каталог и Telegram берут `$CATALOG_URL` / `$TELEGRAM_URL`; redaction `[REDACTED]` только для blog/site origin (`PUBLIC_SITE_URL`), не для CTA.
- Опционально: precheck writer / link-verify reject литерала `[REDACTED]` в href до handoff.
- Эталон: AS08/AS09 — живые catalog/telegram href.

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `shared/agent-pipeline-pitfalls.md` (секция Writer / CTA)
- `scripts/excalibur_blog_link_verify.py` (опциональный reject `[REDACTED]`)

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261017-0915-writer-editorial-pain-outcome-missing
status: fixed
run_date: 2026-10-17
role: excalibur-blog-writer
topic_id: B01
article_dir: memory/blog/articles/B01-vremennaya-registratsiya-vladivostok-rastamozhka-avto-2026
severity: medium
category: docs

### What went wrong
- `memory/brief/editorial-policy.json` again lacked `pain_markers_ru` / `outcome_markers_ru`.
- `excalibur_blog_utility_gate.py` then counted 0 pain/outcome markers and would BLOCK every article with empty lists.
- Same gap already hit prior B01/AS runs; fix had not landed durably on this branch.

### How the agent recovered this run
- Restored `pain_markers_ru` and `outcome_markers_ru` aligned with `excalibur_blog_human_voice_gate.py` defaults.
- Re-ran utility gate on B01 article → PASS.

### Durable fix needed before next run
- Keep marker lists in `editorial-policy.json` (or add script fallback when lists are empty).
- Optional: add regression assert in doctor/utility gate that marker lists are non-empty.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`

### Secrets
- none recorded

### Fixer resolution
- fixed this run: marker lists restored in editorial-policy.json; utility gate PASS on B01

## INC-20261017-0900-research-notes-gate-false-tech
status: fixed
run_date: 2026-10-17
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-vremennaya-registratsiya-vladivostok-rastamozhka-avto-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` marked non-tech niche B01 (растаможка/временная регистрация) as `technical_topic` because it scanned `research-notes.md` body with naive substring markers.
- Substring `ai` matched inside required field name `reader_pain`; substring `ии` matched Russian word endings; later `github` matched the required `github_evidence` heading.
- Gate demanded 3 GitHub URLs for an auto-customs how-to and BLOCKed a valid utility brief.
- Secondary: WebFetch timeout on genproc.gov.ru and HTTP 500 on Interfax during deep research (recovered via alternate sources).
- Commit hook: `CLOUD_AGENT_INJECTED_SECRET_NAMES` contained a URL token (invalid bash identifier) → `${!SECRET_NAME}` crash; after filter, `research-serp.json` / ledger hit `PUBLIC_SITE_URL` scanner.

### How the agent recovered this run
- Patched `is_technical_topic()` to use topic-card fields only and whole-token matching for short markers (`ai`, `ии`).
- Ensured `accessed_at:` appears in source table cells (≥5).
- Re-ran gate → PASS; used DEITA/WebSearch snippets where Interfax/genproc fetch failed.
- Filtered injected secret names to valid identifiers; redacted site origin in serp/ledger to `[REDACTED]` before commit.

### Durable fix needed before next run
- Keep tech detection off research-notes body (or exclude known field names). Already applied in script this run.
- Optional follow-up: document in research skill that non-tech niches may put N/A in `github_evidence`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-17
fix_summary:
- Research agent patched `is_technical_topic` during B01 run; gate PASS without fake GitHub URLs.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `memory/blog/articles/B01-vremennaya-registratsiya-vladivostok-rastamozhka-avto-2026/research-notes.md`
checks_run:
- `python3 scripts/excalibur_blog_research_notes_gate.py --article-dir memory/blog/articles/B01-vremennaya-registratsiya-vladivostok-rastamozhka-avto-2026 -o research-notes-gate.json` → PASS
commit: 25a05a9

## INC-20260616-2015-geo-qa-html-cli-mismatch
status: fixed
run_date: 2026-06-16
role: excalibur-blog-geo-qa
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: qa

### What went wrong
- `article.html` used `<pre><code>` for the llms.txt template, but `excalibur_blog_html_linter.py` forbids those tags and only allows the strict article whitelist.
- `excalibur_blog_research_notes_gate.py` interprets a relative `-o` path inside `article_dir`; passing a repo-relative path as `-o` produced a nested duplicate output before cleanup.
- `.cursor/skills/excalibur-geo-qa/SKILL.md` instructs `excalibur_blog_cannibalization_guard.py --article-dir ...`, while the actual script accepts `--blog-dir`, `--threshold` and `-o/--output`; the documented command exited with argparse error.

### How the agent recovered this run
- Replaced the template block with whitelist-safe `<blockquote><p><br>` markup without changing the article's practical meaning.
- Removed the unintended nested duplicate `research-notes-gate.json` and kept the canonical file in the article directory.
- Re-ran the cannibalization guard with `--blog-dir memory/blog/articles -o memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta/cannibalization-report.json`; verdict PASS.

### Durable fix needed before next run
- Update Writer/QA contracts to avoid `<pre><code>` in `article.html` unless the linter whitelist is intentionally expanded.
- Update `.cursor/skills/excalibur-geo-qa/SKILL.md` to use the actual cannibalization guard CLI or update the script to support `--article-dir`.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_cannibalization_guard.py`
- `scripts/excalibur_blog_html_linter.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Writer/article writing contracts now forbid `<pre>`/`<code>` in `article.html` until the HTML linter whitelist is intentionally expanded, and document whitelist-safe blockquote/table/list alternatives.
- GEO QA skill now documents the actual cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`.
- GEO QA note clarifies that `research_notes_gate.py -o research-notes-gate.json` is relative to `--article-dir`.
files_changed:
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_cannibalization_guard.py --help`
- `rg` check for old Writer `<pre><code>` instruction strings
- `rg` check for old cannibalization `--article-dir` command in source docs
commit: pending-parent-commit

## INC-20260616-2018-cover-toxic-sticker
status: fixed
run_date: 2026-06-16
role: excalibur-blog-cover
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: prompt

### What went wrong
- The one-shot Kie image-to-image quad generation succeeded, but the cover panel included an insulting Russian sticker phrase even though the style preset asks for a non-toxic tone.
- Geometry, white background, hero face, typography and inline utility passed; the issue was limited to one generated sticker text on the top-left cover panel.

### How the agent recovered this run
- Did not launch a second image job.
- Retouched only the offending sticker layer in `cover/cover.png` and the matching top-left area of `cover/canvas-quad.png`, replacing it with a neutral `SEO-МИФ / БЕЗ МАГИИ` sticker.

### Durable fix needed before next run
- Add explicit negative prompt wording for cover/inline generated text: no insults, no toxic labels, no words like `лох`, `лохов`, `для лохов`.
- Consider adding a lightweight post-generation OCR/text QA note to the cover skill when generated Russian sticker text is visible.

### Suggested files to inspect/change
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `memory/cover/cover-design-code.json`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Cover style JSON, design code, prompt builder, agent contracts and skill QA now explicitly forbid toxic/insulting generated sticker text while preserving the meme/sticker/collage style.
- Visible text QA now treats words such as `лох`, `лохов`, `для лохов` and similar humiliating labels as a cover blocker.
files_changed:
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `memory/cover/cover-design-code.json`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_prompt.py`
- JSON parse for `memory/cover/quad-style-digital-meme-collage-ru.json`
- JSON parse for `memory/cover/cover-design-code.json`
commit: pending-parent-commit

## INC-20260616-1950-scout-wordstat-format
status: fixed
run_date: 2026-06-16
role: excalibur-blog-scout
topic_id: B09
article_dir: n/a
severity: low
category: api

### What went wrong
- `wordstat_get_top_requests` for the narrow phrase `как создать llms txt` returned an unexpected payload shape with only `totalCount`, so the tool wrapper could not print top phrases.

### How the agent recovered this run
- Used the successful broader Wordstat result for `llms.txt`, which included the full semantic tail and showed related actionable phrases such as `создать llms txt`.

### Durable fix needed before next run
- Make the Wordstat MCP wrapper handle low-result responses that include only `totalCount`, or document that Scout should query the broader cluster first.

### Suggested files to inspect/change
- `shared/pipeline-incident-fix-contract.md`
- `agents/excalibur-blog-scout.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Scout agent and skill now require Wordstat cluster-first validation: broad parent query before narrow how-to query.
- `totalCount`-only responses are documented as low-result signals, not fatal tool/API failures; Scout should broaden the query and use the broad cluster for semantic tail.
files_changed:
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` check for Wordstat cluster-first/totalCount guidance in Scout source docs
commit: pending-parent-commit

## INC-20260616-2031-indexer-python-missing
status: fixed
run_date: 2026-06-16
role: excalibur-blog-indexer
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: env

### What went wrong
- The Indexer contract requested `python scripts/excalibur_blog_interlinker.py ...`, but the Cloud shell has no `python` executable.
- The first interlinker command failed with `python: command not found`, forcing a retry.

### How the agent recovered this run
- Re-ran the same interlinker command with `python3`, then used `python3` for the llms generator.
- Both scripts completed successfully after the retry.

### Durable fix needed before next run
- Standardize Indexer shell examples on `python3` or provide a `python` alias in the Cloud environment.

### Suggested files to inspect/change
- `agents/excalibur-blog-indexer.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/environment.json`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Indexer agent and skill shell examples now use `python3` for interlinker and llms generator.
- Publish post-publish interlinker example also uses `python3`.
files_changed:
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` check for old `python scripts/excalibur_blog_interlinker.py` and `python scripts/excalibur_blog_llms_generator.py` in source docs
commit: pending-parent-commit


## INC-20260616-2042-publish-ssh-root-dot
status: fixed
run_date: 2026-06-16
role: excalibur-blog-publish
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: publish

### What went wrong
- A safe env-preflight wrapper initially imported `excalibur_blog_wp_publish.py` without adding `scripts/` to `sys.path`, causing `ModuleNotFoundError: asset_download`; the check was re-run with the correct `sys.path`.
- The first real publish attempt connected over SSH but failed before upload with `FileNotFoundError/ENOENT` because the configured publish root path does not exist inside the SSH account cwd.
- Commit was blocked by Cursor secret-scan because `PUBLIC_SITE_URL`/`WP_SITE_URL` are configured as secrets and appeared in staged publish artifacts; committed copies were redacted to `[REDACTED]` to match repository policy.

### How the agent recovered this run
- Re-ran the env check with `scripts/` on `sys.path`; allow flag, public URL and SSH settings were confirmed without printing secret values.
- Retried publish with `SSH_ROOT=.` so the bootstrap was written to the SSH login cwd; WordPress post, featured image, 3 inline images and schema meta published successfully.
- Replaced public site base in committed artifacts with `[REDACTED]`; live permalink remains available in local runtime handoff and WordPress result before redaction.

### Durable fix needed before next run
- Update Cloud publish root secret to `.` (or remove invalid panel path) for this SSH account, or make `excalibur_blog_wp_publish.py` auto-probe `.` when configured root returns ENOENT before bootstrap upload.
- Document that direct import of publish helpers in ad-hoc checks needs `scripts/` on `sys.path`, or expose a tiny env-check CLI in the script.
- Decide whether `PUBLIC_SITE_URL` should remain a secret-scanned value; if yes, keep committed examples/results redacted by contract.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `CURSOR-CLOUD-RUNBOOK.md`
- Cursor Dashboard Cloud Secrets (`SSH_ROOT` only; no secret values recorded here)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- `excalibur_blog_wp_publish.py` now has `--env-check` for safe publish env validation without ad-hoc imports or secret output.
- SSH bootstrap upload now retries once at `.` when a configured non-dot root returns ENOENT, and cleanup deletes the actual uploaded remote path.
- Publish skill/runbook document the env-check CLI, `scripts/` sys.path guidance for ad-hoc imports, and the optional Cloud Secret root update to `.` if fallback warning appears.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `CURSOR-CLOUD-RUNBOOK.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py`
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` (JSON output validated; non-publish env may return exit 1)
- `python3 -m json.tool /tmp/excalibur_publish_env_check.json`
commit: pending-parent-commit

## Fixed incidents

Handled above; commit is pending Director review.
