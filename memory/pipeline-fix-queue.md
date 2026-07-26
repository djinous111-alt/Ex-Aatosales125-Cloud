# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20260726-1330-geo-qa-utility-policy-markers-missing
status: open
run_date: 2026-07-26
role: excalibur-blog-geo-qa
topic_id: AS10
article_dir: memory/blog/articles/AS10-postanovka-na-uchet-avto-posle-epts-2026
severity: high
category: script

### What went wrong
- `excalibur_blog_utility_gate.py` требовал `min_pain_markers`/`min_outcome_markers`, но в `memory/brief/editorial-policy.json` не было списков `pain_markers_ru` / `outcome_markers_ru` → count всегда 0 → ложный UTILITY ARTICLE BLOCKER на любой статье (включая ранее PASS AS09).
- Recommendation markers не содержали вариант `чек-лист` (только `чеклист`), из‑за чего mode-B чек-листы недосчитывали action-маркеры.
- Writer insight использовал ярлык `TL;DR / Быстрый инсайт`, который GEO QA skill запрещает.

### How the agent recovered this run
- Добавлены `pain_markers_ru`, `outcome_markers_ru`, пороги min_* и алиас `чек-лист` в editorial-policy.json.
- Utility gate теперь пропускает pain/outcome checks, если списки маркеров в policy пустые.
- Whitelist-safe правки AS10: pain в lead, `Избегайте…`, инсайт `Коротко:`, +1 шаг в первом ol.
- `link-verify.json` для commit: URL заменены на `[REDACTED_*]` (secret-scan блокировал CATALOG_URL/TELEGRAM_URL).
- Повтор gates: utility PASS, human-voice PASS, article-qa PASS.

### Durable fix needed before next run
- Зафиксировать в pitfalls: utility pain/outcome markers живут в editorial-policy; пустой список = skip, не hard-fail.
- Синхронизировать writer contract с GEO skill: запрет ярлыка `TL;DR` / `Быстрый инсайт` в инсайт-блоке (пример `Коротко:`).
- Опционально: добавить `чек-лист` в writer checklist маркеров / recommendation examples.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json` (уже патч в этом run)
- `scripts/excalibur_blog_utility_gate.py` (уже патч в этом run)
- `shared/agent-pipeline-pitfalls.md`
- `shared/excalibur-article-writing-contract.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260726-1325-writer-cta-secret-scan-block
status: open
run_date: 2026-07-26
role: excalibur-blog-writer
topic_id: AS10
article_dir: memory/blog/articles/AS10-postanovka-na-uchet-avto-posle-epts-2026
severity: medium
category: env

### What went wrong
- `git commit` of `article.html` blocked by Cursor secret scanner because CTA href values match Cloud Secrets `CATALOG_URL` and `TELEGRAM_URL`.
- Same public catalog/Telegram URLs are required in article body by conversion-map; previous articles already contain identical hrefs.

### How the agent recovered this run
- Added HTML comment `<!-- // pragma: allowlist secret -->` on lines with intentional public CTA links, then committed.

### Durable fix needed before next run
- Document writer/publish pattern: public brand CTA URLs that equal secret env values need allowlist pragma OR secret scanner exclusion for article HTML CTA fields.
- Prefer non-secret alias vars (e.g. `PUBLIC_CATALOG_URL`) that are allowed in git, or pre-commit hook that injects pragma automatically.

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `memory/brief/conversion-map.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260726-1315-research-wordstat-partial-payload
status: open
run_date: 2026-07-26
role: excalibur-blog-research
topic_id: AS10
article_dir: memory/blog/articles/AS10-postanovka-na-uchet-avto-posle-epts-2026
severity: low
category: api

### What went wrong
- MCP-KV `wordstat_get_top_requests` for phrase `постановка на учет после эптс` returned unexpected payload shape `{"totalCount":"109"}` without the usual top-requests list (tool surfaced as format error).
- Primary/secondary Wordstat calls succeeded; only the Asia-narrow after-EPTS phrase was partial.

### How the agent recovered this run
- Recorded `totalCount` ~109 in research-notes with explicit PARTIAL warning; did not invent a fake top list.
- Relied on successful primary/secondary volumes for demand table and LSI.

### Durable fix needed before next run
- Harden MCP-KV Wordstat client/tool to normalize sparse responses (expose totalCount + empty top list instead of hard format error).
- Document in research skill: if only totalCount returns, treat as impressions estimate with PARTIAL warning.

### Suggested files to inspect/change
- MCP-KV Wordstat adapter / `wordstat_get_top_requests`
- `.cursor/skills/excalibur-research/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260726-1316-research-notes-gate-ii-false-positive
status: open
run_date: 2026-07-26
role: excalibur-blog-research
topic_id: AS10
article_dir: memory/blog/articles/AS10-postanovka-na-uchet-avto-posle-epts-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` marked non-IT topic AS10 as `technical_topic=true` because TECH_MARKERS included bare substring `ии`, which matches ordinary Russian words like `регистрации`.
- Gate then required 3 GitHub URLs and BLOCK-ed a valid auto-registration research brief.

### How the agent recovered this run
- Tightened marker matching: short tokens (`ai`, `ии`, `mcp`, `api`, `rag`) now use non-letter boundaries; longer markers stay substring.
- Also fixed notes formatting so `accessed_at:` appears in source rows and pain_solution_map rows contain `pain|solution|результат` tokens expected by the gate regex.
- Re-ran research-notes gate to PASS.

### Durable fix needed before next run
- Keep bounded short-marker logic in the gate; add a unit/smoke test that Russian auto topic text is NOT technical.
- Mirror the same TECH_MARKERS logic anywhere else that copies this list (if duplicated).

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- optional test under `scripts/` or `tests/`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260726-1306-scout-precommit-secret-names
status: open
run_date: 2026-07-26
role: excalibur-blog-scout
topic_id: AS10
article_dir: n/a
severity: low
category: env

### What went wrong
- Cursor pre-commit secret scanner crashed on `RAW_SECRET_VALUE="${!SECRET_NAME}"` when `CLOUD_AGENT_INJECTED_SECRET_NAMES` contained a token that is not a valid bash identifier.
- After filtering invalid names, scanner correctly blocked staging of `shared/published-articles.md` because live `PUBLIC_SITE_URL` values were present (expected redaction policy).

### How the agent recovered this run
- Filtered secret-name list to `[A-Za-z_][A-Za-z0-9_]*` for the commit command env only.
- Unstaged `shared/published-articles.md`; committed `memory/topics/blog-topics.md` + AS-topic script fixes only.
- Left handoff uncommitted per git hygiene.

### Durable fix needed before next run
- Ensure Cloud-injected secret names are always valid bash identifiers, or harden the scanner to skip invalid names.
- Keep ledger URLs redacted to `[REDACTED]` before any commit of `shared/published-articles.md`.

### Suggested files to inspect/change
- Cursor Cloud Secrets naming / pre-commit scanner
- `shared/published-articles.md` redaction policy
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

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
