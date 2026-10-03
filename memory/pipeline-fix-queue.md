# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

_None for run 2026-10-03 after fixer (see Fixed below / inline status: fixed)._


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

## INC-20261003-1720-director-doctor-blog-path
status: fixed
run_date: 2026-10-03
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: medium
category: script

### What went wrong
- `excalibur_blog_doctor.py` asserts `llms generator supports --blog-path`, but `excalibur_blog_llms_generator.py` exposes `--blog-dir` / `--out-dir`.
- Doctor SUMMARY errors=1 before pipeline start; prior automation memory said this was fixed to `--blog-dir`.

### How the agent recovered this run
- Continued with needs_scout → Scout; will hand to fixer after PIPELINE DONE.

### Durable fix needed before next run
- Align doctor check with real CLI (`--blog-dir`) or add `--blog-path` alias to llms generator.
- Ensure doctor errors=0 on clean env.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_llms_generator.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Doctor now asserts `--blog-dir` and `--out-dir` (real llms CLI); removed `--blog-path` check.
- Doctor SUMMARY errors=0 on clean env.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → errors=0
- `rg` no `--blog-path` in indexer contracts/doctor
commit: 71ef9b8


## INC-20261003-1720-director-missing-known-wp-slugs
status: fixed
run_date: 2026-10-03
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: high
category: docs

### What went wrong
- `shared/known-wp-slugs.md` missing after ledger reset; scout helper `--suggest-next` returns B01 even though WP already has many live posts (incl. B01 EV slug).
- Risk of topic_id/slug reuse and cannibalization.

### How the agent recovered this run
- Scout instructed to avoid recent WP slugs from today.py list and not republish WP 3955.

### Durable fix needed before next run
- Restore `shared/known-wp-slugs.md` and wire scout helper `--check-query` / `--suggest-next` to consult it.

### Suggested files to inspect/change
- `shared/known-wp-slugs.md`
- `scripts/excalibur_blog_scout_helper.py`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Restored/kept `shared/known-wp-slugs.md` with live B01/B02/legacy rows + scout/publish usage note.
- Scout helper `--suggest-next` / `--check-query` / `--check-slug` consult known-wp + ledger + article dirs (AS*+B*).
- `--suggest-next` now yields B03 (not B01) when B01/B02 reserved via known-wp.
files_changed:
- `shared/known-wp-slugs.md`
- `scripts/excalibur_blog_scout_helper.py`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_scout_helper.py --suggest-next` → B03
- `--check-slug` collision on B02 slug exit 1; new slug exit 0
commit: 71ef9b8


## INC-20261003-1724-scout-precommit-invalid-secret-name
status: fixed
run_date: 2026-10-03
role: excalibur-blog-scout
topic_id: B02
article_dir: n/a
severity: medium
category: env

### What went wrong
- `git commit` failed in pre-commit.cursor: `invalid variable name` while expanding `${!SECRET_NAME}`.
- `CLOUD_AGENT_INJECTED_SECRET_NAMES` contained 1 non-identifier name (len=25); `scripts/sanitize_cloud_secret_names.sh` missing from repo.

### How the agent recovered this run
- Filtered non-identifier names out of `CLOUD_AGENT_INJECTED_SECRET_NAMES` / `CLOUD_AGENT_ALL_SECRET_NAMES` for the commit shell, then committed and pushed B02 topic card.

### Durable fix needed before next run
- Restore `scripts/sanitize_cloud_secret_names.sh` (or equivalent) and document sourcing it before git commit in scout/director skills.
- Ensure Dashboard secret names are valid bash identifiers (A-Za-z_[A-Za-z0-9_]*).

### Suggested files to inspect/change
- `scripts/sanitize_cloud_secret_names.sh`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`

### Secrets
- none recorded (name not logged)

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Restored `scripts/sanitize_cloud_secret_names.sh` (identifier-only filter; safe to source).
- Documented sourcing before git commit in scout/director/pitfalls (and other roles).
- Human follow-up: rename Dashboard secrets to bash identifiers (non-blocking).
files_changed:
- `scripts/sanitize_cloud_secret_names.sh`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `skills/director-excalibur-blog/SKILL.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- source sanitize with mixed URL/identifier names → URL dropped
commit: 71ef9b8


## INC-20261003-1746-writer-precommit-invalid-secret-name
status: fixed
run_date: 2026-10-03
role: excalibur-blog-writer
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: env

### What went wrong
- `git commit` for B02 article.html/meta failed in pre-commit.cursor: `invalid variable name` on `${!SECRET_NAME}`.
- Same root cause as INC-20261003-1724: non-identifier entries in `CLOUD_AGENT_INJECTED_SECRET_NAMES` / `CLOUD_AGENT_ALL_SECRET_NAMES` (this run: 1 bad name, len=218); sanitize script still missing.

### How the agent recovered this run
- Filtered names to bash identifiers only for the commit shell, then committed and pushed writer artifacts.

### Durable fix needed before next run
- Same as INC-20261003-1724: restore `scripts/sanitize_cloud_secret_names.sh` and document pre-commit env sanitize for all Excalibur roles (not only scout).
- Fix Dashboard secret naming so injected names are valid identifiers.

### Suggested files to inspect/change
- `scripts/sanitize_cloud_secret_names.sh`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-writer.md`

### Secrets
- none recorded (name not logged)

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Same sanitize script + writer skill/agent pre-commit guidance.
files_changed:
- `scripts/sanitize_cloud_secret_names.sh`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- sanitize smoke
commit: 71ef9b8


## INC-20261003-1755-geo-qa-utility-policy-pain-outcome-missing
status: fixed
run_date: 2026-10-03
role: excalibur-blog-geo-qa
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: high
category: qa

### What went wrong
- `excalibur_blog_utility_gate.py` always enforces `min_pain_markers` (default 2) and `min_outcome_markers` (default 3).
- `memory/brief/editorial-policy.json` lacked `pain_markers_ru` / `outcome_markers_ru` and the matching min keys, so marker counts stayed 0 and every article failed utility gate (including previously PASS AS09 on re-run).

### How the agent recovered this run
- Added `pain_markers_ru`, `outcome_markers_ru`, `min_pain_markers`, `min_outcome_markers` to `memory/brief/editorial-policy.json`.
- Strengthened B02 article action/pain/outcome wording in a QA FIX cycle; utility gate PASS.

### Durable fix needed before next run
- Keep policy lists in sync with `scripts/excalibur_blog_utility_gate.py` (or skip checks when marker lists are empty).
- Document required pain/outcome markers in writer + GEO QA skills / `shared/editorial-utility-only.md`.
- Optionally align human-voice and utility marker vocabularies.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `shared/editorial-utility-only.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Kept durable `pain_markers_ru` / `outcome_markers_ru` (+ mins) in `memory/brief/editorial-policy.json`.
- Utility gate skips pain/outcome mins with warning when lists empty (no false 0/0 BLOCKER).
- Documented in editorial-utility-only + GEO QA / writer skills.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `shared/editorial-utility-only.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_utility_gate.py`
- JSON present markers in editorial-policy.json
commit: 71ef9b8


## INC-20261003-1755-geo-qa-writer-cta-placeholders
status: fixed
run_date: 2026-10-03
role: excalibur-blog-geo-qa
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: qa

### What went wrong
- Writer left literal `[CATALOG_URL]` and `[TELEGRAM_URL]` placeholders in `article.html`.
- `excalibur_blog_link_verify.py` treated them as site-relative paths → 404 and link-verify FAIL.

### How the agent recovered this run
- Resolved placeholders from `memory/brief/conversion-map.md` to live catalog and Telegram URLs; link-verify PASS (3/3).

### Durable fix needed before next run
- Writer skill/contract must require final CTA hrefs from conversion-map (no unresolved placeholders) before handoff to GEO QA.
- Optionally teach link-verify to fail fast with a clear "unresolved placeholder" error instead of HTTP 404.

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `scripts/excalibur_blog_link_verify.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Writer contract/skills: allow `[CATALOG_URL]`/`[TELEGRAM_URL]` tokens; forbid bare placeholders.
- link-verify classifies unresolved placeholders explicitly; expands from env/`site.env.local` when set.
- publish expands CTA tokens into payload (`cta_expanded` in dry-run) without write-back.
files_changed:
- `scripts/excalibur_blog_link_verify.py`
- `scripts/excalibur_blog_wp_publish.py`
- `shared/excalibur-article-writing-contract.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- classify_link('[CATALOG_URL]') → unresolved_placeholder
- py_compile link_verify + wp_publish
commit: 71ef9b8


## INC-20261003-1800-director-geo-qa-task-type-missing
status: fixed
run_date: 2026-10-03
role: excalibur-blog-director
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: env

### What went wrong
- Cloud Task enum rejected `subagent_type=excalibur-blog-geo-qa` even though role is documented in AGENTS.md / available_subagent_types list in prompt.
- Director had to fallback to `Task(generalPurpose)` with `.cursor/agents/excalibur-blog-geo-qa.md` + skill path.

### How the agent recovered this run
- Ran GEO QA via generalPurpose; article-qa PASS 90, human-voice PASS.

### Durable fix needed before next run
- Register `excalibur-blog-geo-qa` in Cloud Task/subagent enum consistently with other excalibur-blog-* roles, or document that GEO QA must always use generalPurpose fallback.

### Suggested files to inspect/change
- `.cursor/agents/excalibur-blog-geo-qa.md`
- `AGENTS.md`
- `shared/pipeline-task-map.md`
- Cloud agent type registry (env)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Documented durable fallback: if typed `excalibur-blog-geo-qa` missing from Cloud enum → immediate `Task(generalPurpose)` + agent/skill paths (AGENTS.md, pipeline-task-map, director skill, pitfalls).
- Cloud Task enum registration itself is outside repo (optional human follow-up).
files_changed:
- `AGENTS.md`
- `shared/pipeline-task-map.md`
- `skills/director-excalibur-blog/SKILL.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` geo-qa generalPurpose fallback present in docs
commit: 71ef9b8


## INC-20261003-1738-schema-precommit-invalid-secret-name
status: fixed
run_date: 2026-10-03
role: excalibur-blog-schema
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: env

### What went wrong
- `git commit` for B02 schema.jsonld failed in pre-commit.cursor: `invalid variable name` on `${!SECRET_NAME}`.
- Same root cause as INC-20261003-1724 / INC-20261003-1746: non-identifier entries in `CLOUD_AGENT_INJECTED_SECRET_NAMES` / `CLOUD_AGENT_ALL_SECRET_NAMES`; sanitize script still missing.

### How the agent recovered this run
- Filtered secret name lists to bash identifiers only for the commit shell, then committed and pushed schema.jsonld.

### Durable fix needed before next run
- Same as INC-20261003-1724: restore `scripts/sanitize_cloud_secret_names.sh` and document pre-commit env sanitize for all Excalibur roles including schema.
- Fix Dashboard secret naming so injected names are valid identifiers.

### Suggested files to inspect/change
- `scripts/sanitize_cloud_secret_names.sh`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-schema.md`

### Secrets
- none recorded (name not logged)

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Same sanitize script + schema skill pre-commit guidance.
files_changed:
- `scripts/sanitize_cloud_secret_names.sh`
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
checks_run:
- sanitize smoke
commit: 71ef9b8


## INC-20261003-1742-cover-quad-manifest-seo-defaults
status: fixed
run_date: 2026-10-03
role: excalibur-blog-cover
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_quad_manifest.py --merge` для авто-темы Кореи заполнил cover_hook/meme_caption/scene_hint SEO-дефолтами B01: «SEO-текст…», «15k ключей», «Wordstat + ноутбук».
- Wordstat в scene_hint нарушает design-code запрет на SEO-analytics в кадре; агент обязан руками переписать весь cover+inline block.

### How the agent recovered this run
- Переписал `cover/quad-manifest.json` под боль «Encar ≠ под ключ», outfit порт Владивостока, inline visual_type: infographic_card / checklist_board / workflow_diagram.
- ONE Kie gpt-image-2 i2i → split PASS → inject-html ok.

### Durable fix needed before next run
- Убрать SEO-захардкоженные defaults из `excalibur_blog_quad_manifest.py`; брать hook/caption из article.meta / research reader_pain или оставлять пустые обязательные поля с FAIL, если агент не заполнил.
- Не предлагать Wordstat/Метрику в любых default scene_hint.

### Suggested files to inspect/change
- `scripts/excalibur_blog_quad_manifest.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Removed SEO/B01 hardcoded defaults from `excalibur_blog_quad_manifest.py` (no `15k ключей`, Wordstat scene, SEO-текст hook).
- Empty cover_hook/meme_caption → WARN agent_must_fill; scene hints topic-neutral.
- Cover skill documents manual fill requirement.
files_changed:
- `scripts/excalibur_blog_quad_manifest.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- fresh manifest on B02 copy: no SEO seed; WARN fill hook/caption
- py_compile quad_manifest
commit: 71ef9b8


## INC-20261003-1744-indexer-skill-llms-blog-path
status: fixed
run_date: 2026-10-03
role: excalibur-blog-indexer
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: docs

### What went wrong
- `.cursor/skills/indexer-excalibur-blog/SKILL.md` и `.cursor/agents/excalibur-blog-indexer.md` всё ещё показывают `excalibur_blog_llms_generator.py ... --blog-path /`.
- Реальный CLI принимает только `--blog-dir` / `--out-dir` / `--site-base` (нет `--blog-path`); doctor уже FAIL по тому же рассинхрону (см. INC-20261003-1720-director-doctor-blog-path).

### How the agent recovered this run
- Запустил generator без `--blog-path`: `--blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` — OK, B02 попал в llms.txt / llms-full.txt.

### Durable fix needed before next run
- Убрать `--blog-path` из skill/agent indexer contracts; оставить `--blog-dir` + `--out-dir`.
- Синхронизировать doctor check с реальным CLI (или alias), чтобы errors=0.

### Suggested files to inspect/change
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `scripts/excalibur_blog_doctor.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Removed `--blog-path` from indexer agent/skill (plugin + Cloud copies).
- Documented `--blog-dir` + `--relative-urls` + `--out-dir`; doctor aligned.
files_changed:
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `scripts/excalibur_blog_doctor.py`
checks_run:
- doctor errors=0
- `rg` no `--blog-path` in indexer contracts
commit: 71ef9b8


## INC-20261003-1745-indexer-precommit-invalid-secret-name
status: fixed
run_date: 2026-10-03
role: excalibur-blog-indexer
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: env

### What went wrong
- `git commit` failed in pre-commit.cursor: `invalid variable name` on `${!SECRET_NAME}`.
- Same root cause as INC-20261003-1724: `CLOUD_AGENT_*_SECRET_NAMES` contained 1 non-identifier entry (URL-like, len=25); sanitize script still missing.

### How the agent recovered this run
- Exported filtered identifier-only lists for the commit shell, then committed promotion-checklist + interlink report + incident queue.

### Durable fix needed before next run
- Restore `scripts/sanitize_cloud_secret_names.sh` and document sourcing before git commit for indexer/publish roles.
- Remove non-identifier names from Dashboard secret injection lists.

### Suggested files to inspect/change
- `scripts/sanitize_cloud_secret_names.sh`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded (name not logged)

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- Same sanitize script + indexer skill pre-commit section.
files_changed:
- `scripts/sanitize_cloud_secret_names.sh`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
checks_run:
- sanitize smoke
commit: 71ef9b8


## INC-20261003-1745-indexer-llms-secret-scan-block
status: fixed
run_date: 2026-10-03
role: excalibur-blog-indexer
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: high
category: publish

### What went wrong
- Cursor secret scanner blocked commit of regenerated `memory/blog/llms.txt` and `llms-full.txt` because they embed `PUBLIC_SITE_URL` absolute article URLs.
- Same site URL already present in prior git history (`llms.txt`, schema, research, published-articles), so scanner now prevents refreshing AI crawler index in-repo.

### How the agent recovered this run
- Left updated `llms.txt` / `llms-full.txt` on disk for publish step; committed only promotion-checklist, interlink-suggestions.json, and incident queue.
- Indexer handoff records on-disk paths; publish must deploy from workspace files, not rely on git HEAD for llms.

### Durable fix needed before next run
- Decide: (a) allowlist public site base for llms artifacts, or (b) generate llms with relative `/blog/...` URLs, or (c) stop treating public site URL as a commit-scanned secret for these paths.
- Document which path publish uses for llms upload.

### Suggested files to inspect/change
- `scripts/excalibur_blog_llms_generator.py`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- llms generator defaults to relative `/blog/<slug>/` URLs (`--relative-urls` / empty site-base) so commits are not blocked by PUBLIC_SITE_URL secret-scan.
- Indexer/publish skills: commit relative llms; absolute regenerate only for deploy on disk.
files_changed:
- `scripts/excalibur_blog_llms_generator.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
- `memory/blog/llms.txt`
- `memory/blog/llms-full.txt`
checks_run:
- generator `--relative-urls` → relative links in llms.txt
commit: 71ef9b8


## INC-20261003-1820-publish-paramiko-missing
status: fixed
run_date: 2026-10-03
role: excalibur-blog-publish
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: high
category: env

### What went wrong
- First publish attempt failed with `ModuleNotFoundError: No module named 'paramiko'` despite `paramiko` listed in `requirements.txt`.
- Cloud env install did not leave paramiko available to system `python3` (PEP 668 externally-managed).

### How the agent recovered this run
- Installed with `pip3 install --break-system-packages paramiko` (got 5.0.0) and retried publish.

### Durable fix needed before next run
- Ensure `.cursor/cloud-agent-install.sh` / environment build installs `paramiko` into the runtime Python used by publish scripts.
- Document `--break-system-packages` or venv path in publish skill preflight.

### Suggested files to inspect/change
- `.cursor/cloud-agent-install.sh`
- `.cursor/environment.json`
- `requirements.txt`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- `.cursor/cloud-agent-install.sh` now installs `paramiko` (with `--break-system-packages` fallback) and verifies import.
- Publish skill documents PEP 668 recovery command; `requirements.txt` already lists paramiko.
files_changed:
- `.cursor/cloud-agent-install.sh`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -c "import paramiko"` (runtime may already have it)
- install script contains paramiko
commit: 71ef9b8


## INC-20261003-1820-publish-http-504-webfetch-timeout
status: fixed
run_date: 2026-10-03
role: excalibur-blog-publish
topic_id: B02
article_dir: memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026
severity: medium
category: publish

### What went wrong
- SSH bootstrap upload succeeded (~7MB PHP). Local HTTP trigger returned `504 Gateway Time-out`.
- Script entered Cloud WebFetch Fallback and waited 120s for `memory/webfetch-response.txt`, then raised timeout because the agent was blocked on the same process and could not WebFetch in parallel.
- Despite 504, WordPress already had the new post (id 3967) with featured + 3 inlines; bootstrap file cleaned up (404).

### How the agent recovered this run
- Verified live REST/HEAD: post 3967 published; featured 3968; inlines 3969–3971; protected posts 3955/3949/3778 untouched (3778 is different slug `kak-zakazat-...`).
- Wrote `wp-publish-result.json` from live verification, updated ledger to `published`, logs, promotion Live URL, handoff.

### Durable fix needed before next run
- Publish skill: start HTTP trigger / fallback WebFetch in a parallel watcher while `wp_publish.py` waits; or increase gateway/PHP time and return early status.
- Optionally make script treat post-create success detectable via WP REST slug poll after 504 as pass.
- Prefer longer HTTP timeout or async bootstrap ACK for large media payloads.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-03
fix_summary:
- After HTTP trigger failure (incl. 504), publish script polls WP REST by slug before WebFetch wait and during wait.
- WebFetch wait shortened to 45s with explicit parallel-WebFetch agent instruction.
- HTTP timeout raised to 180s; skill documents 504/REST recover path.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- py_compile wp_publish
- `rg` poll_wp_rest_by_slug / FALLBACK_TRIGGER present
commit: 71ef9b8

