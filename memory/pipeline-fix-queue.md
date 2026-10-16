# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20261016-0930-writer-cta-env-and-ol-five-regex
status: open
run_date: 2026-10-16
role: excalibur-blog-writer
topic_id: B01
article_dir: memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026
severity: medium
category: docs

### What went wrong
- После GEO QA FAIL: CTA в article.html были литералами `[REDACTED]` / невалидный join с site-base → link-verify fail; в `conversion-map.md` URL тоже замаскированы
- Маркеры «Делать/Не делать» не считаются в `recommendation_markers_ru` (нужны императивы «сделайте/не делайте»)
- `human_voice_gate` regex `exactly_five_lists` срабатывает на любой `<ol>` с ≥5 `<li>` и на span нескольких списков → ложный warn даже при длинах 4/6/10/7

### How the agent recovered this run
- Подставил реальные CTA из env `CATALOG_URL` + `TELEGRAM_URL` (каталог×2, Telegram×1)
- Переписал рекомендации на маркеры policy; добавил outcome «результат/получите/сможете/соберите»
- Убрал ярлык TL;DR; оставил один `<ol>` (чеклист 10), остальные шаги в `<ul>` с «Шаг N»
- Локально: human-voice PASS, utility PASS, link-verify pass, char_count 9447

### Durable fix needed before next run
- В writer skill/contract: при `[REDACTED]` в conversion-map брать CTA из `CATALOG_URL`/`TELEGRAM_URL`, не писать литерал `[REDACTED]` в href
- Явно: «Делать/Не делать» ≠ маркеры; использовать «сделайте/не делайте/проверьте/чеклист/шаг »
- Починить regex `exactly_five_lists` в `excalibur_blog_human_voice_gate.py` (считать точное число `<li>` внутри каждого `<ol>`, не `{5}` non-greedy span)

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `scripts/excalibur_blog_human_voice_gate.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261016-0915-research-notes-gate-accessed-at-count
status: open
run_date: 2026-10-16
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026
severity: medium
category: qa

### What went wrong
- `excalibur_blog_research_notes_gate.py` BLOCK: `accessed_at=1 < 5` even when `source_table` had many URL rows with date column `accessed_at`
- Gate counts only literal `accessed_at:` field matches (`\baccessed_at\b\s*:`), not table cells
- Skill/agent format shows table column `accessed_at` without requiring repeated `accessed_at:` labels

### How the agent recovered this run
- Added `## sources_accessed` block with 10 explicit `accessed_at: 2026-10-16` lines; gate PASS on retry
- Also noted: mentioning `github`/`mcp` in notes flips `technical_topic=true` and can demand extra GitHub URLs

### Durable fix needed before next run
- Document in research skill/agent that gate needs >=5 literal `accessed_at:` labels (table header alone is not enough)
- Or relax gate to count `accessed_at` dates inside `source_table` rows
- Optionally exclude research meta words (`mcp`, `github_evidence`) from `TECH_MARKERS` false positives on non-tech topics

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `.cursor/agents/excalibur-blog-research.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261016-0915-research-gibdd-webfetch-504
status: open
run_date: 2026-10-16
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026
severity: low
category: api

### What went wrong
- WebFetch to `gibdd.ru/check/auto` and punycode mirror returned HTTP 504 Gateway Timeout
- Blocked direct confirmation of live GIBDD UI copy during research

### How the agent recovered this run
- Used ConsultantPlus documented procedure for GIBDD VIN check + Autonews/FNP sources for pledge check
- Did not invent GIBDD UI text; cited secondary official/legal sources with `accessed_at`

### Durable fix needed before next run
- Research skill: if official portal times out, allow documented secondary official mirrors (ConsultantPlus, notariat) and record soft-fail
- Optional retry/backoff note for WebFetch 5xx on government hosts

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261016-0924-geo-qa-utility-policy-markers-missing
status: fixed
fixed_at: 2026-10-16
run_date: 2026-10-16
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026
severity: blocker
category: qa

### What went wrong
- `pain_markers_ru` / `outcome_markers_ru` отсутствовали в `editorial-policy.json` → false BLOCK на любой статье

### Fixer resolution
status: fixed
fixed_at: 2026-10-16
fix_summary:
- Восстановлены `pain_markers_ru` (12) и `outcome_markers_ru` (10) в sync с `human_voice_gate` PAIN/OUTCOME_MARKERS
- utility_gate fail-fast при пустых списках; doctor assert non-empty ≥3
- Writer contract/skill/pitfalls: точные recommendation markers + CTA не `[REDACTED]`
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/excalibur-article-writing-contract.md`
- `shared/agent-pipeline-pitfalls.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
checks_run:
- `utility_gate B01` → PASS
- `utility_gate AS09` → PASS
- empty-policy dry-run → BLOCK with fail-fast errors
- `doctor` → errors=0 warnings=1 (paramiko)
commit: 3180d1a

## INC-20261016-0921-writer-precommit-secret-names-csv
status: fixed
fixed_at: 2026-10-16
run_date: 2026-10-16
role: excalibur-blog-writer
topic_id: B01
severity: medium
category: env

### Fixer resolution
status: fixed
fixed_at: 2026-10-16
fix_summary:
- Восстановлен `scripts/excalibur_blog_filter_commit_secret_env.sh` (CSV, identifier-only, drop marketing URL secret names)
- Pitfalls: sanitize must stay CSV `a,b,c`
files_changed:
- `scripts/excalibur_blog_filter_commit_secret_env.sh`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- isolated filter: strips `https://…` and `PUBLIC_SITE_URL`
commit: 3180d1a

## INC-20261016-0905-scout-precommit-invalid-secret-name
status: fixed
fixed_at: 2026-10-16
run_date: 2026-10-16
role: excalibur-blog-scout
topic_id: B01
severity: medium
category: env

### Fixer resolution
status: fixed
fixed_at: 2026-10-16
fix_summary:
- Same durable fix as INC-0921: filter script + pitfalls CSV note
files_changed:
- `scripts/excalibur_blog_filter_commit_secret_env.sh`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `bash -n` + isolated filter test
commit: 3180d1a

## INC-20261016-0903-director-doctor-llms-blog-path
status: fixed
fixed_at: 2026-10-16
run_date: 2026-10-16
role: excalibur-blog-director
severity: low
category: script

### Fixer resolution
status: fixed
fixed_at: 2026-10-16
fix_summary:
- Doctor asserts `--blog-dir` and warns/fails if stale `--blog-path` present
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `doctor` OK llms `--blog-dir`; no stale `--blog-path`
commit: 3180d1a

## INC-20261016-0903-scout-niche-drift-ai-prompts
status: fixed
fixed_at: 2026-10-16
run_date: 2026-10-16
role: excalibur-blog-scout
severity: medium
category: docs

### Fixer resolution
status: fixed
fixed_at: 2026-10-16
fix_summary:
- Scout agent/skill (both trees) → Авто-Сейлс clusters from site-brief; AI/Make/n8n priority removed
- scout_helper + today.py recognize AS*|B*
files_changed:
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_today.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `scout_helper --suggest-next` sees AS08/AS09/B01
- rg: no Cursor AI priority lists in scout prompts (only forbid notes)
commit: 3180d1a

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
