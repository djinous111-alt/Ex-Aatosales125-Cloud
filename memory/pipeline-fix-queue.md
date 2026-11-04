# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

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

## INC-20261104-1206-director-sanitizer-wipe-as-b
status: open
run_date: 2026-11-04
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: high
category: script

### What went wrong
- Cron boot found wiped durable pins: `today.py`/`scout_helper` only matched `B\d+`, doctor FAIL on llms `--blog-path`, missing `excalibur_git.sh` / smoke / Kie upload helpers, scout niche docs drifted.
- `EXCALIBUR_TOPIC_SELECTION=needs_scout` despite AS01–AS14 pool; LIVE WP REST SSL handshake timeout again.

### How the agent recovered this run
- Restored durable pack from `a9db2e63` + `today.py`/topics/pitfalls from `c0b1a833`.
- Restored ledger from `b9e96bf5` and appended Sienta `publish_blocked`; appended AS11–AS14 topic cards with LIVE status_note.
- Doctor SUMMARY errors=0; next scout id AS15.

### Durable fix needed before next run
- Prevent sanitizer from wiping AS|B / llms aliases / git filter / cover Kie helpers (CI pin or smoke on boot).
- Keep WP SSL timeout denylist fallback documented when REST handshake times out.

### Suggested files to inspect/change
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261104-0908-scout-wordstat-denylist-fallback
status: open
run_date: 2026-11-04
role: excalibur-blog-scout
topic_id: AS15
article_dir: n/a
severity: medium
category: api

### What went wrong
- MCP-KV Wordstat unavailable (`namespaceStatus: error`); cannot call `wordstat_get_top_requests`.
- `shared/wp-slug-denylist.json` missing at scout start (sanitizer wipe / incomplete restore).
- WP REST for `EXCALIBUR_RECENT_WP_POSTS` failed with SSL handshake timeout — LIVE slug list not refreshable from Cloud egress.

### How the agent recovered this run
- Set `wordstat_status: UNAVAILABLE` on AS15; used WebSearch (Arrizo 8 lots/trim tables) + Metrika/Дзен China-cluster semantic tail; no invented impression counts.
- Rebuilt `shared/wp-slug-denylist.json` from git snapshot `30a770a6` + `published-live` + ledger + topic slugs (1235 entries); deduped against denylist models (Haval M6, Omoda C5, Jetour T2, Tiggo 7 Pro, Jaecoo J7, Sienta, Encar, utilsbor, AS01–AS09).
- Chose free model Chery Arrizo 8; `--check-query "арризо 8 комплектации"` clean before append; utility gate AS15 PASS.

### Durable fix needed before next run
- Restore or pin Wordstat MCP-KV auth/discovery for Cloud scout runs.
- Ensure denylist file is regenerated or restored on boot when WP REST SSL times out (doctor/smoke check for non-empty `shared/wp-slug-denylist.json`).
- Optionally teach `scout_helper --check-query` to load denylist slug collisions explicitly (skill claims it; current script only checks topic pool).

### Suggested files to inspect/change
- `shared/wp-slug-denylist.json`
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_today.py`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261104-0935-geo-qa-typed-task-fallback
status: open
run_date: 2026-11-04
role: excalibur-blog-geo-qa
topic_id: AS15
article_dir: memory/blog/articles/AS15-chery-arrizo-8-iz-kitaya-komplektatsii-lovushki-2026
severity: low
category: handoff

### What went wrong
- Typed Cloud Task `excalibur-blog-geo-qa` unavailable in Cloud Task enum; Director launched role via `Task(generalPurpose)` + `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md`.

### How the agent recovered this run
- Executed full GEO QA script set with `python3`; all gates PASS (research-notes, utility, human-voice, html-linter, slop, fact-check, cannibalization, link-verify with catalog_ssl soft-pass).
- Wrote `article-qa.md` verdict PASS score 88; no HTML/meta FIX needed.
- Noted generalPurpose fallback in handoff GEO QA block.

### Durable fix needed before next run
- Register typed Task `excalibur-blog-geo-qa` in Cloud Task enum when platform allows, or keep documented generalPurpose pin in AGENTS.md / agent file (already partially documented).

### Suggested files to inspect/change
- `AGENTS.md`
- `.cursor/agents/excalibur-blog-geo-qa.md`
- `agents/excalibur-blog-geo-qa.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261104-0951-cover-kie-force-local-hero-flag-missing
status: open
run_date: 2026-11-04
role: excalibur-blog-cover
topic_id: AS15
article_dir: memory/blog/articles/AS15-chery-arrizo-8-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: script

### What went wrong
- `shared/kie-gpt-image-api-contract.md` and cover skill document `--force-local-hero` / auto-rehost inside `excalibur_blog_kie_gpt_image2_api.py`, but the script argparse has no such flags and no file-base64-upload rehost path.
- MCP-KV namespaceStatus=error; Cover used Kie-first as required.

### How the agent recovered this run
- Uploaded local `memory/cover/assets/blog-hero-reference.png` via `scripts/excalibur_blog_kie_file_base64_upload.py` → `cover/kie-hero-upload.json`.
- Patched `cover/quad-mcp-batch.json` `input_urls` to Kie tempfile host before ONE `createTask`.
- Split PASS + corner brand stamp + inject 3 figures.

### Durable fix needed before next run
- Wire `--force-local-hero` / auto-rehost into `excalibur_blog_kie_gpt_image2_api.py` per contract, or update skill/contract to document the separate CLI upload step as the canonical path.

### Suggested files to inspect/change
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `shared/kie-gpt-image-api-contract.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_kie_file_base64_upload.py`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261104-1013-publish-ssh-tcp22-timeout-as15
status: open
run_date: 2026-11-04
role: excalibur-blog-publish
topic_id: AS15
article_dir: memory/blog/articles/AS15-chery-arrizo-8-iz-kitaya-komplektatsii-lovushki-2026
severity: blocker
category: env

### What went wrong
- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`; link-verify PASS; dry-run PASS for NEW slug `chery-arrizo-8-iz-kitaya-komplektatsii-lovushki-2026`.
- `--env-check`: ssh.dns.resolved=true, paramiko_available=true after pip workaround, but `ssh.tcp22` → `ssh_tcp22_timeout` via `SSH_HOST`.
- `SSH_HOST_IP` unset. DNS A for SSH_HOST probed (~8s TimeoutError). PUBLIC_SITE_URL IP differs from SSH A and was NOT used as SSH fallback (contract).
- Same Cloud egress class as AS10 Sienta publish_blocked.
- Dry-run initially crashed: local `import re` inside `load_article` shadowed module `re` and broke earlier `re.sub` on schema (UnboundLocalError).

### How the agent recovered this run
- Installed paramiko via pip workaround; re-ran env-check (paramiko true; tcp22 still missing).
- Removed shadowing local `import re` in `scripts/excalibur_blog_wp_publish.py`; dry-run then PASS (PHP ~6.87MB, correct slug).
- Did **not** attempt LIVE SSH publish; no denylist/LIVE posts rewritten.
- Ledger AS15 → `publish_blocked`; wp-publish-result.json + log + handoff blocker recorded.

### Durable fix needed before next run
- Human: restore Beget SSH listener/firewall TCP/22 for Cloud egress, **or** add verified Cloud Secret `SSH_HOST_IP` with open TCP/22 (never invent / never use PUBLIC_SITE_URL IP).
- After connectivity restored: republish ONLY slug `chery-arrizo-8-iz-kitaya-komplektatsii-lovushki-2026` (never 4758/4746/4740/3430/3394/4717/4711 or foreign slugs).
- Keep local-`import re` removed (already patched this run); pin paramiko in image so Cloud agents do not need pip workaround.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py` (tcp22 gate; re-import shadow — fixed)
- `shared/excalibur-wp-publish-contract.md`
- `skills/publish-excalibur-blog/SKILL.md`
- Cursor Dashboard Cloud Secrets (`SSH_HOST_IP` only; no values recorded)
- Beget panel SSH/firewall for hostname behind `SSH_HOST`

### Secrets
- none recorded

### Fixer resolution
- pending

