# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

_none_

## Needs-human

## INC-20261105-2215-publish-ssh-tcp22-timeout-as22
status: needs-human
run_date: 2026-11-05
role: excalibur-blog-publish
topic_id: AS22
article_dir: memory/blog/articles/AS22-changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026
severity: blocker
category: publish
fixed_at: 2026-11-05

### What went wrong
- `--env-check` reported `ssh.dns.resolved=true` but `ssh.tcp22.reachable=false` (`ssh_tcp22_timeout`).
- Same class as AS21 / AS15 / AS10 (2026-11-04).

### How the agent recovered this run
- No LIVE SSH/WP write; ledger `publish_blocked`; denylist LIVE posts untouched.

### Fixer resolution
status: needs-human
reason:
- Cloud→WP SSH TCP/22 not reachable from this environment; cannot verify real TCP in fixer.
needed_decision_or_secret:
- Restore Beget/SSH egress TCP/22 **or** inject human-verified `SSH_HOST_IP` Cloud Secret (plus working `SSH_HOST`/`SSH_PORT`).
- Re-run publish **only** for NEW free slug `changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026` after TCP/22 works; do not overwrite foreign LIVE posts (4758/4746/4740/3430/3394/4717/4711).
files_changed:
- `skills/publish-excalibur-blog/SKILL.md` (+ `.cursor` sync) — env-check TCP/22 blocker path documented
- `shared/agent-pipeline-pitfalls.md` — DNS≠TCP; needs-human rule
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → errors=0
- `python3 scripts/excalibur_blog_fixer_regression_smoke.py` → PASS
commit: 738b2d80 (scripts/pins); docs commit follows

## Fixed this run (AS22 / 2026-11-05)

## INC-20261105-2215-publish-load-article-re-shadow
status: fixed
run_date: 2026-11-05
role: excalibur-blog-publish
topic_id: AS22
severity: medium
category: script
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Confirmed module-level `re` only in `load_article` (no local import); stripped UTF-8 BOM from publish script.
- Smoke asserts no nested `import re` and no BOM.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
- `skills/publish-excalibur-blog/SKILL.md`
checks_run:
- py_compile + fixer regression smoke PASS
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2211-indexer-precommit-invalid-secret-name
status: fixed
run_date: 2026-11-05
role: excalibur-blog-indexer
topic_id: AS22
severity: medium
category: env
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Verified `scripts/excalibur_git.sh` + `excalibur_blog_filter_commit_secret_env.sh` present; doctor/smoke pin them.
- Indexer/schema/writer/scout skills instruct commits via `excalibur_git.sh`.
files_changed:
- `agents/excalibur-blog-indexer.md`, `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`, `.cursor/skills/...`
- `skills/schema-excalibur-blog/SKILL.md`, writer/scout skills
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- doctor OK git.sh + filter; smoke OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2210-indexer-llms-skill-absolute-vs-relative
status: fixed
run_date: 2026-11-05
role: excalibur-blog-indexer
topic_id: AS22
severity: low
category: docs
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Indexer skill/agent: commit-safe `--site-base "" --blog-path / --relative-urls`; absolute PUBLIC_SITE_URL only for live/runtime.
files_changed:
- `skills/indexer-excalibur-blog/SKILL.md` (+ `.cursor`)
- `agents/excalibur-blog-indexer.md` (+ `.cursor`)
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- doctor relative-urls check OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2205-cover-mcp-kv-down-kie-fallback
status: fixed
run_date: 2026-11-05
role: excalibur-blog-cover
topic_id: AS22
severity: medium
category: api
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Cover skill: MCP-KV primary + first-class Kie fallback (`hero --force --provider kie`, kie gpt-image2 api); python3; WP hero HEAD fail → Kie tempfile.
- MCP Dashboard restore remains optional human follow-up for native gpt-image-2; agent path no longer blocked.
files_changed:
- `skills/cover-excalibur-blog/SKILL.md` (+ `.cursor`)
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- doctor Kie tempfile + hero upload pins OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2205-schema-precommit-invalid-secret-name
status: fixed
run_date: 2026-11-05
role: excalibur-blog-schema
topic_id: AS22
severity: medium
category: env
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Same durable git secret-name filter as indexer/writer; schema skill documents `excalibur_git.sh`.
files_changed:
- `skills/schema-excalibur-blog/SKILL.md` (+ `.cursor`)
- `scripts/excalibur_git.sh` (verified present)
checks_run:
- doctor/smoke git filter OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2148-writer-catalog-host-hyphen-vs-public-site
status: fixed
run_date: 2026-11-05
role: excalibur-blog-writer
topic_id: AS22
severity: medium
category: docs
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- conversion-map note: catalog host = PUBLIC_SITE_URL (`avtosales125.ru`), not hyphen host; Writer skill/agent CTA rule.
files_changed:
- `memory/brief/conversion-map.md`
- `skills/writer-excalibur-blog/SKILL.md` (+ `.cursor`)
- `agents/excalibur-blog-writer.md` (+ `.cursor`)
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- rg/docs review; doctor errors=0
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2145-director-sanitizer-wiped-durable-pins
status: fixed
run_date: 2026-11-05
role: excalibur-blog-director
topic_id: AS22
severity: high
category: script
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Restored/pinned editorial markers, utility empty-list skip, link_verify soft-pass, llms CLI, doctor marker/denylist/git checks; pitfalls warn about sanitizer wipe + doctor preflight.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_link_verify.py`
- `scripts/excalibur_blog_llms_generator.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- doctor errors=0; smoke PASS
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2140-geo-qa-utility-empty-pain-outcome-markers
status: fixed
run_date: 2026-11-05
role: excalibur-blog-geo-qa
topic_id: AS22
severity: high
category: script
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Restored `pain_markers_ru`/`outcome_markers_ru` + `_markers_pinned`; utility skips mins when lists empty; recommendation aliases; editorial-utility + writer tokens synced.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `shared/editorial-utility-only.md`
- writer skills
checks_run:
- smoke utility empty-list skip OK; doctor markers OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2141-geo-qa-catalog-ssl-timeout-no-softpass
status: fixed
run_date: 2026-11-05
role: excalibur-blog-geo-qa
topic_id: AS22
severity: high
category: qa
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Restored `classify_soft_pass` catalog/site SSL/DNS/5xx soft-pass; GEO QA + publish skills document soft-pass OK.
files_changed:
- `scripts/excalibur_blog_link_verify.py`
- `skills/excalibur-geo-qa/SKILL.md` (+ `.cursor`)
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- doctor/smoke soft-pass pins OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2142-geo-qa-html-linter-faq-substring-false-positive
status: fixed
run_date: 2026-11-05
role: excalibur-blog-geo-qa
topic_id: AS22
severity: medium
category: script
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- FAQ linter uses `_is_faq_section_heading` (exact FAQ titles); smoke asserts outcome-before-FAQ H2 OK.
files_changed:
- `scripts/excalibur_blog_html_linter.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
- `shared/excalibur-article-writing-contract.md`
- writer skills
checks_run:
- smoke FAQ strict match PASS
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2143-geo-qa-typed-task-fallback
status: fixed
run_date: 2026-11-05
role: excalibur-blog-geo-qa
topic_id: AS22
severity: low
category: other
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Confirmed Director/AGENTS already document generalPurpose fallback; GEO QA skill notes typed-task unavailability.
files_changed:
- `skills/excalibur-geo-qa/SKILL.md` (+ `.cursor`)
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- rg director generalPurpose fallback present
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2125-writer-precommit-invalid-secret-name
status: fixed
run_date: 2026-11-05
role: excalibur-blog-writer
topic_id: AS22
severity: medium
category: env
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Writer skill/agent require `excalibur_git.sh`; filter wrapper verified.
files_changed:
- writer skills/agents; pitfalls
checks_run:
- doctor/smoke git filter OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2115-research-wordstat-mcp-unavailable
status: fixed
run_date: 2026-11-05
role: excalibur-blog-research
topic_id: AS22
severity: medium
category: api
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Research skill: MCP-KV UNAVAILABLE → warning table, no fabricated shows, incident + continue WebSearch.
- Restoring MCP auth is optional human follow-up; agent contract durable.
files_changed:
- `skills/excalibur-research/SKILL.md` (+ `.cursor`)
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- docs rg UNAVAILABLE
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-2116-research-notes-gate-false-technical
status: fixed
run_date: 2026-11-05
role: excalibur-blog-research
topic_id: AS22
severity: medium
category: script
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Verified `_tech_marker_hit` word-boundaries + `notes_without_github_evidence`; doctor/smoke pin helpers.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py` (verified)
- research skill note for AS## auto-import
checks_run:
- doctor/smoke tech-marker helpers OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-0013-scout-precommit-invalid-secret-name
status: fixed
run_date: 2026-11-05
role: excalibur-blog-scout
topic_id: AS22
severity: medium
category: env
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Scout agent/skill: commits via `excalibur_git.sh`; filter present.
files_changed:
- scout skills/agents; pitfalls
checks_run:
- doctor/smoke OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-0010-scout-helper-b-only-suggest-next
status: fixed
run_date: 2026-11-05
role: excalibur-blog-scout
topic_id: AS22
severity: medium
category: script
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Scout helper already AS|B; `--suggest-next` → AS23 with pool>0; Scout docs Autosalas AS##.
files_changed:
- `scripts/excalibur_blog_scout_helper.py` (verified)
- scout skills/agents
checks_run:
- smoke scout AS* pool OK
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-0011-scout-wordstat-mcp-unavailable
status: fixed
run_date: 2026-11-05
role: excalibur-blog-scout
topic_id: AS22
severity: medium
category: api
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Scout skill: UNAVAILABLE = WebSearch-only + incident, never fabricate shows; Autosalas niche queries.
files_changed:
- `skills/scout-excalibur-blog/SKILL.md` (+ `.cursor`)
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- docs review
commit: 738b2d80 (scripts/pins); docs commit follows

## INC-20261105-0012-scout-denylist-missing
status: fixed
run_date: 2026-11-05
role: excalibur-blog-scout
topic_id: AS22
severity: high
category: docs
fixed_at: 2026-11-05

### Fixer resolution
status: fixed
fix_summary:
- Doctor fail-closed if denylist missing/empty (<50 slugs); file present (1254); Scout skill rebuild recipe; smoke asserts denylist.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_fixer_regression_smoke.py`
- `shared/wp-slug-denylist.json` (verified)
- scout skill/pitfalls
checks_run:
- doctor denylist OK; smoke 1254 slugs
commit: 738b2d80 (scripts/pins); docs commit follows

## Historical fixed incidents

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
