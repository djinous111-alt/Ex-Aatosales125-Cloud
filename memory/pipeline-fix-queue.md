# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

_none — Honda Fit 2026-10-25 fixer closed all open incidents below._

## Fixed this run (2026-10-25 B01 Honda Fit)

## INC-20261025-2205-publish-http-fallback-504-reconstruct
status: fixed
run_date: 2026-10-25
role: excalibur-blog-publish
topic_id: B01
article_dir: memory/blog/articles/B01-honda-fit-iz-yaponii-komplektatsii-lovushki-2026
severity: medium
category: publish

### What went wrong
- SSH bootstrap upload OK; local HTTP trigger timed out (120s); FALLBACK curl returned nginx 504; overlapping triggers created duplicate media.

### How the agent recovered this run
- Did not republish. Verified LIVE REST post 4513; reconstructed wp-publish-result.json.

### Durable fix needed before next run
- Increase HTTP timeout; reject 504 HTML; REST reconstruct by slug before second trigger.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- HTTP trigger timeout 300s; FALLBACK poll 180s; nginx 504/HTML rejected as success.
- REST reconstruct by slug before second overlapping trigger; publish_method `ssh+rest-reconstruct`.
- Publish skill + pitfalls document no-republish / no 504-as-OK.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py`
- unit checks for is_gateway_error_html / HTTP_TRIGGER_TIMEOUT_SEC
commit: d5ba4660

## INC-20261024-2148-indexer-skill-llms-blog-path-stale
status: fixed
run_date: 2026-10-25
role: excalibur-blog-indexer
topic_id: B01
severity: medium
category: docs

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- Indexer skill/agent: `--blog-dir` / `--out-dir` / `--site-base ""`; removed `--blog-path` from commands.
- Doctor aligned (same as INC-2112). Pitfalls Indexer section expanded.
files_changed:
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → errors=0
- `rg` confirms no stale CLI `--blog-path` requirement in doctor
commit: d5ba4660

## INC-20261024-2144-cover-mcp-kv-unavailable-kie-fallback
status: fixed
run_date: 2026-10-25
role: excalibur-blog-cover
topic_id: B01
severity: medium
category: api

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- Cover skill: MCP-KV `namespaceStatus: error` → immediately Kie async `excalibur_blog_kie_gpt_image2_api.py` (not only -32001).
- Pitfalls Cover section documents Kie fallback; MCP OAuth restore remains ops outside repo.
files_changed:
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` for Kie/MCP-KV fallback wording in cover skill
commit: d5ba4660

## INC-20261024-2145-cover-missing-corner-brand-pil
status: fixed
run_date: 2026-10-25
role: excalibur-blog-cover
topic_id: B01
severity: low
category: prompt

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- `excalibur_blog_cover_quad_split.py` PIL-stamps `avto-sales125.ru` on cover.png (+ TL canvas) by default (`--stamp-corner-brand`, opt-out `--no-stamp-corner-brand`).
- Cover skill documents post-split corner brand step.
files_changed:
- `scripts/excalibur_blog_cover_quad_split.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_split.py`
- `--help` shows stamp flags
commit: d5ba4660

## INC-20261025-2130-geo-qa-utility-pain-markers-empty
status: fixed
run_date: 2026-10-25
role: excalibur-blog-geo-qa
topic_id: B01
severity: blocker
category: qa

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- `editorial-policy.json`: `pain_markers_ru` / `outcome_markers_ru` aligned with human-voice; mins under `article_required_signals`.
- `utility_gate.py`: empty lists → warn+skip (no hard BLOCK on defaults).
- GEO QA skill notes shared marker source.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- Fit article utility gate PASS (pain=8, outcome=13)
commit: d5ba4660

## INC-20261025-0017-research-mcp-kv-wordstat-unavailable
status: fixed
run_date: 2026-10-25
role: excalibur-blog-research
topic_id: B01
severity: medium
category: api

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- Research skill: MCP-KV `namespaceStatus: error` = non-blocking Wordstat fallback (`n/a` + warning + incident), aligned with Scout.
- MCP OAuth restore remains Cursor Dashboard / ops (outside repo).
files_changed:
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` for MCP-KV error fallback in research skill
commit: d5ba4660

## INC-20261025-0018-research-notes-gate-false-technical
status: fixed
run_date: 2026-10-25
role: excalibur-blog-research
topic_id: B01
severity: medium
category: script

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- TECH markers `ai`/`ии` use Cyrillic-safe word-boundary match; Honda Fit / «Японии» / «pain» no longer force technical_topic + github_urls≥3.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- unit: Honda Fit notes → technical_topic=False; MCP agent topic → True
commit: d5ba4660

## INC-20261025-2112-director-doctor-llms-blog-path
status: fixed
run_date: 2026-10-25
role: excalibur-blog-director
topic_id: B01
severity: medium
category: script

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- Doctor checks `--blog-dir` / `--out-dir` / `--site-base` (not `--blog-path`).
files_changed:
- `scripts/excalibur_blog_doctor.py`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → SUMMARY errors=0 warnings=0
commit: d5ba4660

## INC-20261025-2113-director-paramiko-missing-main
status: fixed
run_date: 2026-10-25
role: excalibur-blog-director
topic_id: B01
severity: blocker
category: env

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- `paramiko` in `requirements.txt`, `.cursor/cloud-agent-install.sh` (verify), `.cursor/Dockerfile`.
- Doctor warns without paramiko; `--publish` hard-fails. Denylist restored separately (INC-2106).
files_changed:
- `requirements.txt`
- `.cursor/cloud-agent-install.sh`
- `.cursor/Dockerfile`
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_wp_publish.py`
checks_run:
- doctor paramiko OK; `import paramiko`
commit: d5ba4660

## INC-20261025-2105-scout-mcp-kv-wordstat-unavailable
status: fixed
run_date: 2026-10-25
role: excalibur-blog-scout
topic_id: B01
severity: medium
category: api

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- Scout skill/agent: MCP-KV error → non-blocking fallback (denylist + Autostat/WebSearch) + incident; no invented impressions.
files_changed:
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` MCP-KV fallback in scout skill/agent
commit: d5ba4660

## INC-20261025-2110-scout-precommit-invalid-secret-name
status: fixed
run_date: 2026-10-25
role: excalibur-blog-scout
topic_id: B01
severity: medium
category: env

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- Restored `scripts/excalibur_blog_filter_secret_names.sh` (INJECTED + ALL secret name lists) and `scripts/excalibur_git.sh` wrapper.
- Pitfalls + Scout skill document `source` before Cloud commit.
files_changed:
- `scripts/excalibur_blog_filter_secret_names.sh`
- `scripts/excalibur_git.sh`
- `shared/agent-pipeline-pitfalls.md`
- `skills/scout-excalibur-blog/SKILL.md`
checks_run:
- sourced filter: invalid names skipped; valid kept
- `scripts/excalibur_git.sh status` runs
commit: d5ba4660

## INC-20261025-2106-scout-missing-wp-slug-denylist
status: fixed
run_date: 2026-10-25
role: excalibur-blog-scout
topic_id: B01
severity: medium
category: docs

### Fixer resolution
status: fixed
fixed_at: 2026-10-25
fix_summary:
- Restored `shared/wp-slug-denylist.json` from LIVE WP REST (1217 slugs incl. honda-fit + jimny) + `scripts/excalibur_blog_wp_slug_denylist.py --rebuild/--check`.
- Doctor FAIL without denylist; Scout skill/agent require rebuild when missing.
files_changed:
- `shared/wp-slug-denylist.json`
- `scripts/excalibur_blog_wp_slug_denylist.py`
- `scripts/excalibur_blog_doctor.py`
- `skills/scout-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-scout.md`
checks_run:
- denylist --check ok; doctor denylist OK; Fit/Jimny slugs present
commit: d5ba4660


## Fixed incidents (historical)

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
commit: 1d48df53

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
commit: 1d48df53

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
commit: 1d48df53

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
commit: 1d48df53


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
commit: 1d48df53

## Fixed incidents

Handled above; commit is pending Director review.
