# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20260722-0926-schema-precommit-secret-redact
status: open
run_date: 2026-07-22
role: excalibur-blog-schema
topic_id: AS20
article_dir: memory/blog/articles/AS20-levyj-rul-iz-korei-2026-kak-kupit
severity: medium
category: env

### What went wrong
- `git commit` of safe `schema.jsonld` failed: Cloud pre-commit secrets scanner expands redacted env into bash and errors with `invalid variable name`.
- Same root cause as INC-20260722-0910-scout-precommit-secret-redact and INC-20260722-0920-writer-precommit-secret-redact (recurrence on schema step).

### How the agent recovered this run
- Verified staged file was only `schema.jsonld` (no handoff/fragments/secrets), then `git commit --no-verify` per schema skill and push.

### Durable fix needed before next run
- Fix Cloud pre-commit secret-redact hook so empty/redacted secret names do not break bash.
- Keep documented `--no-verify` path for article/schema commits when only this error appears (already in schema skill).

### Suggested files to inspect/change
- Cloud Agent pre-commit secrets scanner (environment hook)
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260722-0925-geo-qa-utility-human-voice-markers
status: open
run_date: 2026-07-22
role: excalibur-blog-geo-qa
topic_id: AS20
article_dir: memory/blog/articles/AS20-levyj-rul-iz-korei-2026-kak-kupit
severity: medium
category: qa

### What went wrong
- First GEO QA run: utility gate BLOCK (`action_markers=2 < 8`, `pain_markers=1 < 2`) and human-voice BLOCK (`reader pain is weak`).
- Writer used UI labels «Делать/Не делать» and hyphen «чек-лист», which do not match policy tokens `сделайте` / `не делайте` / `чеклист`.
- CTA `href` were literal `[REDACTED]` placeholders → link-verify treated them as internal relative and failed until restored to live catalog/Telegram URLs.
- Typed Task `excalibur-blog-geo-qa` unavailable in this Cloud run; role executed via `generalPurpose` with agent/skill paths (known Cloud enum gap).

### How the agent recovered this run
- Minimal article.html FIX: pain words in lead, recommendation markers, checklist spelling, varied ol sizes, restored CTA hrefs; re-ran all gates → PASS (score 87).
- Wrote `article-qa.md` and updated `article.meta.json` geo_qa.

### Durable fix needed before next run
- Writer skill/contract: map «Делать/Не делать» examples to exact `recommendation_markers_ru` tokens (`сделайте`, `не делайте`, `чеклист`, `шаг `, `проверьте`, …).
- Writer must not leave literal `[REDACTED]` in `href` for publishable HTML; use real catalog/Telegram URLs (redact only in committed ledgers if secret-scan requires).
- Keep Cloud fallback: geo-qa via `Task(generalPurpose)` + `.cursor/agents/excalibur-blog-geo-qa.md` when typed Task missing.

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `shared/agent-pipeline-pitfalls.md`
- `memory/brief/editorial-policy.json` (marker lists already aligned with human_voice_gate)

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260722-0915-research-notes-gate-accessed-pain-markers
status: open
run_date: 2026-07-22
role: excalibur-blog-research
topic_id: AS20
article_dir: memory/blog/articles/AS20-levyj-rul-iz-korei-2026-kak-kupit
severity: low
category: docs

### What went wrong
- First `research-notes.md` followed the agent template (`accessed_at` as a table column date + plain pain/solution rows) and got BLOCK: `accessed_at=1 < 5` and `pain_solution_map rows=1 < 3`.
- Gate counts only literal `accessed_at:` (with colon), and pain-map rows only if the line contains `pain|solution|result|боль|решение|результат` – bare table cells without those tokens do not count.
- Agent template / skill example does not spell out these marker requirements, so notes had to be rewritten after validation.

### How the agent recovered this run
- Rewrote `source_table` cells to `accessed_at: 2026-07-22` and prefixed pain-map cells with `pain:` / `solution:` / `reader_result:`; gate PASS on retry.

### Durable fix needed before next run
- Document in research skill/agent that: (1) each source row should include the literal token `accessed_at: YYYY-MM-DD` (not only a date column); (2) each `pain_solution_map` data row must contain the gate keywords (`pain`/`solution`/`result` or RU equivalents).
- Optionally soften the gate to count markdown table dates / header-aligned columns without forcing English prefixes.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `.cursor/agents/excalibur-blog-research.md`
- `scripts/excalibur_blog_research_notes_gate.py`
- `shared/editorial-utility-only.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260722-0910-scout-precommit-secret-redact
status: open
run_date: 2026-07-22
role: excalibur-blog-scout
topic_id: AS20
article_dir: n/a
severity: medium
category: env

### What went wrong
- `git commit` failed in Cloud Agent pre-commit secrets scanner: `invalid variable name` when the hook expands redacted secret env values into bash variables.
- Blocked commit of safe topic card `memory/topics/blog-topics.md` (AS20) despite no secrets in the diff.

### How the agent recovered this run
- Committed with `--no-verify` (same workaround noted in automation memory from AS19), then pushed.

### Durable fix needed before next run
- Fix Cloud Agent pre-commit secret-redact hook so redacted/empty secret names do not break bash (`invalid variable name`).
- Prefer documenting safe commit path in scout/director skills if `--no-verify` remains required in this environment.

### Suggested files to inspect/change
- Cloud Agent pre-commit secrets scanner (environment hook)
- `shared/agent-pipeline-pitfalls.md` (note the workaround)
- `.cursor/skills/scout-excalibur-blog/SKILL.md` (commit hygiene note)

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260722-0902-director-main-missing-as19-fixes
status: open
run_date: 2026-07-22
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: blocker
category: docs

### What went wrong
- Cron automation branch started from `main` without AS19 durable fixes (`excalibur_topic_ids.py`, AS*|B* parsing in today/scout, doctor `--blog-dir`).
- Doctor failed (`llms generator supports --blog-path`); today/scout only saw `B*` → `needs_scout` / wrong next id `B01` despite live AS series through AS19.

### How the agent recovered this run
- Restored durable files from commit `ac670d2` (AS19 fixer) onto this branch; appended AS19 topic card + ledger row; doctor errors=0; scout next `AS20`.

### Durable fix needed before next run
- Merge AS19 fixer commit(s) into `main` so next cron does not re-pay restore cost.
- Keep `scripts/excalibur_topic_ids.py` and AS*|B* parsing in today/scout/research_start.
- Doctor must check `--blog-dir` (not `--blog-path`) for llms generator.

### Suggested files to inspect/change
- `scripts/excalibur_topic_ids.py`
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/published-articles.md` (sync with live WP)
- PR merge to `main`

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

## INC-20260722-0920-writer-precommit-secret-redact
status: open
run_date: 2026-07-22
role: excalibur-blog-writer
topic_id: AS20
article_dir: memory/blog/articles/AS20-levyj-rul-iz-korei-2026-kak-kupit
severity: medium
category: env

### What went wrong
- `git commit` of safe article artifacts failed: Cloud pre-commit secrets scanner expands redacted env into bash and errors with `invalid variable name`.
- Same root cause as INC-20260722-0910-scout-precommit-secret-redact (recurrence on writer step).

### How the agent recovered this run
- Verified staged files were only `article.html` and `article.meta.json`, then `git commit --no-verify` and push.

### Durable fix needed before next run
- Fix Cloud pre-commit secret-redact hook so empty/redacted secret names do not break bash.
- Keep documented `--no-verify` path for article/schema commits when only this error appears (already in pitfalls/writer skill).

### Suggested files to inspect/change
- Cloud Agent pre-commit secrets scanner (environment hook)
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending
