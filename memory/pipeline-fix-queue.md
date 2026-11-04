# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20261104-1405-publish-ssh-tcp-timeout
status: needs-human
run_date: 2026-11-04
role: excalibur-blog-publish
topic_id: AS10
article_dir: memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026
severity: blocker
category: env

### What went wrong
- Preflight link-verify PASS and dry-run PASS for new slug `gac-gs3-iz-kitaya-komplektatsii-lovushki-2026`.
- Live publish blocked: TCP connect to `SSH_HOST:22` timed out (15s and 30s).
- `SSH_HOST_IP` is not present in Cloud Secrets / env, so skill alternate probe path was unavailable.
- Agent refused to guess host/IP/credentials or rewrite foreign denylist LIVE posts.

### How the agent recovered this run
- Stopped before SSH upload / bootstrap trigger.
- Wrote `wp-publish-result.json` with verdict fail / status publish_blocked.
- Updated ledger row AS10 → `publish_blocked`, wp-publish-log, handoff PUBLISH BLOCKER, promotion checklist note.

### Durable fix needed before next run
- Restore SSH egress to the WordPress host on TCP/22 from Cloud Agent, or inject `SSH_HOST_IP` (reachable alternate) into Cloud Secrets.
- Keep denylist untouched; only publish free new slugs after SSH connectivity is confirmed.

### Suggested files to inspect/change
- `skills/publish-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_wp_publish.py`
- `shared/agent-pipeline-pitfalls.md`
- Cursor Cloud Secrets (`SSH_HOST` / `SSH_HOST_IP` / network allowlist)

### Secrets
- none recorded

### Fixer resolution
status: needs-human
fixed_at: 2026-11-04
reason:
- Cloud→Beget SSH TCP/22 still unreachable (`ssh.tcp22.error=ssh_tcp22_timeout` via SSH_HOST; DNS resolves).
- `SSH_HOST_IP` not configured in Cloud Secrets — durable code cannot open the port.
needed_decision_or_secret:
- Restore egress allowlist for Beget SSH :22 from Cursor Cloud Agent, OR inject verified reachable `SSH_HOST_IP`.
- Re-run publish ONLY for NEW slug `gac-gs3-iz-kitaya-komplektatsii-lovushki-2026` (denylist LIVE untouched).
fix_summary:
- Restored durable TCP/22 + SSH_HOST_IP probe in `--env-check` (FAIL-fast before live upload).
- Documented probe order / needs-human path in publish skill, WP contract, pitfalls.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/excalibur-wp-publish-contract.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` → missing `ssh_tcp22`
- doctor errors=0; fixer_regression_smoke PASS
commit: pending-parent-commit


## INC-20261104-1358-indexer-secret-names-url-value
status: fixed
run_date: 2026-11-04
role: excalibur-blog-indexer
topic_id: AS10
article_dir: memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: env

### What went wrong
- Pre-commit secrets scanner crashed with `invalid variable name` (URL token in `CLOUD_AGENT_*_SECRET_NAMES`).

### How the agent recovered this run
- Filtered secret-name lists in the commit shell; commit succeeded without `--no-verify`.

### Durable fix needed before next run
- Commit wrapper that filters non-identifier secret names; document for Indexer.

### Suggested files to inspect/change
- `scripts/excalibur_blog_filter_commit_secret_env.sh`
- `scripts/excalibur_git.sh`
- `skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Restored `excalibur_blog_filter_commit_secret_env.sh` + `excalibur_git.sh`; Indexer/Schema agents+skills pin `bash scripts/excalibur_git.sh commit`.
- Pitfalls note: subshell filter without export is a no-op; URL tokens among SECRET_NAMES must be stripped.
files_changed:
- `scripts/excalibur_blog_filter_commit_secret_env.sh`
- `scripts/excalibur_git.sh`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- filter unit: URL token dropped from FOO,https://…,BAR → FOO,BAR
- doctor + smoke assert git/filter scripts present
commit: pending-parent-commit


## INC-20261104-1350-cover-mcp-kv-down-kie-fallback
status: fixed
run_date: 2026-11-04
role: excalibur-blog-cover
topic_id: AS10
article_dir: memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026
severity: high
category: api

### What went wrong
- MCP-KV down; sanitizer wiped Kie hero helpers / tempfile allowlist; `--force-local-hero` missing.

### How the agent recovered this run
- Restored Kie path; ONE image job; `--force --provider kie` workaround.

### Durable fix needed before next run
- Pin Kie-first cover path + `--force-local-hero` + tempfile allowlist in doctor/smoke.

### Suggested files to inspect/change
- `scripts/excalibur_blog_hero_reference_url.py`
- `scripts/excalibur_blog_kie_*`
- cover skills/agents

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Added `--force-local-hero` to hero_reference_url (alias force+kie) and kie_gpt_image2_api.
- Doctor/smoke pin tempfile host, kie_file_base64_upload.py, force-local-hero flags.
- Cover agent/skill: MCP absence alone ≠ blocker if Kie path works.
files_changed:
- `scripts/excalibur_blog_hero_reference_url.py`
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/kie-gpt-image-api-contract.md`
checks_run:
- `--help` shows `--force-local-hero` on both CLIs
- doctor + smoke PASS
commit: pending-parent-commit


## INC-20261104-1345-schema-secret-names-url-value
status: fixed
run_date: 2026-11-04
role: excalibur-blog-schema
topic_id: AS10
article_dir: memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: env

### What went wrong
- Same SECRET_NAMES URL-token pre-commit crash while committing schema.jsonld.

### How the agent recovered this run
- Filtered bash-safe ids in commit shell; placeholders only in JSON-LD.

### Durable fix needed before next run
- Same as Indexer: git wrapper + schema skill commit hygiene.

### Suggested files to inspect/change
- `scripts/excalibur_git.sh`
- `skills/schema-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Schema skill/agent document placeholders + `excalibur_git.sh commit`.
- Shared secret-name filter restored (same root cause as Indexer).
files_changed:
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-schema.md`
- `.cursor/agents/excalibur-blog-schema.md`
- `scripts/excalibur_blog_filter_commit_secret_env.sh`
- `scripts/excalibur_git.sh`
checks_run:
- filter unit PASS; doctor/smoke PASS
commit: pending-parent-commit


## INC-20261104-1340-geo-qa-typed-task-fallback
status: fixed
run_date: 2026-11-04
role: excalibur-blog-geo-qa
topic_id: AS10
article_dir: memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: env

### What went wrong
- Typed Task `excalibur-blog-geo-qa` unavailable; generalPurpose fallback used.

### How the agent recovered this run
- Ran as generalPurpose with agent+skill paths; article-qa PASS.

### Durable fix needed before next run
- Keep generalPurpose pin first-class in director/AGENTS/pitfalls.

### Suggested files to inspect/change
- director skill/agent, AGENTS.md, pitfalls

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Re-pinned Cloud Task fallback: typed missing → `Task(generalPurpose)` per role; one Task = one role; single-agent pipeline forbidden.
- GEO QA agent restored with durable notes from prior fix.
files_changed:
- `skills/director-excalibur-blog/SKILL.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-geo-qa.md`
- `.cursor/agents/excalibur-blog-geo-qa.md`
- `shared/agent-pipeline-pitfalls.md`
- `AGENTS.md` (already had fallback; verified)
checks_run:
- rg generalPurpose pin in director skill + pitfalls
commit: pending-parent-commit


## INC-20261104-1341-geo-qa-catalog-softpass-wiped
status: fixed
run_date: 2026-11-04
role: excalibur-blog-geo-qa
topic_id: AS10
article_dir: memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026
severity: high
category: script

### What went wrong
- Sanitizer wiped link-verify catalog/site soft-pass and human-voice TL;DR / ol counter.

### How the agent recovered this run
- Restored soft-pass + TL;DR ban; re-ran gates PASS.

### Durable fix needed before next run
- Doctor/smoke assert classify_soft_pass / catalog_ssl / TL;DR ban.

### Suggested files to inspect/change
- `scripts/excalibur_blog_link_verify.py`
- `scripts/excalibur_blog_human_voice_gate.py`
- doctor/smoke

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Soft-pass + redaction remain in link_verify; TL;DR / «Быстрый инсайт» ban in human_voice.
- Doctor/smoke FAIL if symbols wiped again; pitfalls document catalog_ssl/site_ssl.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- doctor pins classify_soft_pass/catalog_ssl/site_ssl/TL;DR
- smoke PASS
commit: pending-parent-commit


## INC-20261104-1325-writer-utility-markers-wiped
status: fixed
run_date: 2026-11-04
role: excalibur-blog-writer
topic_id: AS10
article_dir: memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: docs

### What went wrong
- editorial-policy markers wiped; utility_gate empty-list skip lost → every article BLOCK.

### How the agent recovered this run
- Restored markers + empty-list skip; utility gate PASS.

### Durable fix needed before next run
- Doctor pin markers; keep empty-list skip.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- doctor

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Markers remain `_markers_pinned` with non-empty lists; utility_gate empty-list skip restored.
- Doctor/smoke assert pain/outcome markers ≥5 and empty-list skip.
files_changed:
- `memory/brief/editorial-policy.json` (already restored; verified)
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
checks_run:
- doctor editorial-policy pins OK; smoke OK
commit: pending-parent-commit


## INC-20261104-1608-scout-wordstat-mcp-unavailable
status: fixed
run_date: 2026-11-04
role: excalibur-blog-scout
topic_id: AS10
article_dir: n/a
severity: medium
category: api

### What went wrong
- MCP-KV error; Wordstat tool unavailable; inventing counts forbidden.

### How the agent recovered this run
- `wordstat_status=UNAVAILABLE` + WebSearch; denylist check clean.

### Durable fix needed before next run
- Document Scout UNAVAILABLE path; keep AVTO niche.

### Suggested files to inspect/change
- scout skill/agent, pitfalls

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Scout skill/agent: MCP-KV error → `wordstat_status=UNAVAILABLE` + WebSearch; never invent shows.
- Pitfalls Research/Scout sections pin the same rule.
files_changed:
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- rg UNAVAILABLE in scout skill/agent
commit: pending-parent-commit


## INC-20261104-1604-director-sanitizer-wipe-as-b-llms
status: fixed
run_date: 2026-11-04
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: high
category: script

### What went wrong
- Sanitizer wipe: llms `--blog-path` missing; today/scout only `B\d+`; scout niche drift; denylist missing.

### How the agent recovered this run
- Restored AS|B regex, `--blog-path`, AVTO scout, denylist; doctor errors=0.

### Durable fix needed before next run
- Pin AS|B + `--blog-path` + denylist in doctor/smoke.

### Suggested files to inspect/change
- doctor, smoke, today, scout_helper, llms, denylist, scout agents

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-11-04
fix_summary:
- Doctor/smoke pin AS|B, llms `--blog-path`, denylist presence, scout AVTO niche retained.
- Restored regression smoke script wiped by sanitizer.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
- `scripts/excalibur_blog_today.py` (verified AS|B)
- `scripts/excalibur_blog_scout_helper.py` (verified AS|B)
- `scripts/excalibur_blog_llms_generator.py` (verified --blog-path)
- `shared/wp-slug-denylist.json` (verified present)
- scout agents/skills (AVTO)
checks_run:
- doctor SUMMARY errors=0 warnings=0
- smoke PASS (AS pool visible)
commit: pending-parent-commit


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
