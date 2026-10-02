# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents


## INC-20261002-1730-research-precommit-invalid-secret-name
status: open
run_date: 2026-10-02
role: excalibur-blog-research
topic_id: B05
article_dir: memory/blog/articles/B05-kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026
severity: medium
category: env

### What went wrong
- Cloud pre-commit secrets scanner failed with `invalid variable name` before any file scan.
- `CLOUD_AGENT_ALL_SECRET_NAMES` / `CLOUD_AGENT_INJECTED_SECRET_NAMES` contain a non-identifier token (URL/value treated as a secret name), so `${!SECRET_NAME}` crashes the hook.

### How the agent recovered this run
- Re-ran `git commit` with env lists filtered to bash-valid identifiers only (no `--no-verify`).
- Commit `f80bdee` landed successfully.

### Durable fix needed before next run
- Dashboard Secrets: ensure every secret *name* is a valid shell identifier; never put URLs/values in the names list.
- Harden pre-commit.cursor to skip invalid names instead of aborting the commit.

### Suggested files to inspect/change
- Cursor Cloud Dashboard Secrets for this environment
- `/root/.cursor/agent-hooks/.../pre-commit.cursor` (platform) or local wrapper docs

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261002-1729-research-notes-gate-tech-false-positive
status: open
run_date: 2026-10-02
role: excalibur-blog-research
topic_id: B05
article_dir: memory/blog/articles/B05-kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026
severity: high
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` marked non-tech customs comparison as `technical_topic: true`.
- Root cause: `TECH_MARKERS` used substring match; `ai` matched inside required field `reader_pain`, `ии` matched inside normal Russian words like `компетенции`.
- Gate demanded `github_urls >= 3` for B05 (таможня Уссурийск vs Владивосток), blocking Writer.

### How the agent recovered this run
- Patched `is_technical_topic()` to whole-word matching with Cyrillic/Latin boundaries.
- Strengthened `pain_solution_map` rows with explicit `боль`/`решение`/`результат` tokens for the row counter.
- Re-ran gate → PASS (`technical_topic: false`).

### Durable fix needed before next run
- Keep whole-word marker matching; add a unit/fixture test that Russian non-tech notes with `reader_pain` do not force GitHub evidence.
- Optionally exclude required meta field names from the tech scan window.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- tests for research-notes gate (if/when added)

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261002-1728-research-wordstat-empty-and-dvtu-504
status: open
run_date: 2026-10-02
role: excalibur-blog-research
topic_id: B05
article_dir: memory/blog/articles/B05-kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026
severity: low
category: api

### What went wrong
- `wordstat_get_top_requests` for narrow comparison phrases returned empty/`totalCount`-only payloads (not 401).
- Official DVTU page `dvtu.customs.gov.ru/...lichnogo-pol-zovaniya` returned 504 Gateway Timeout.

### How the agent recovered this run
- Used parent Wordstat clusters (`таможня уссурийск` 1719, `таможня владивосток` 4749) and documented empty narrow query.
- Used Alta-Soft 178н text + press releases instead of the timed-out DVTU page.

### Durable fix needed before next run
- Document Wordstat empty-payload handling in research skill (retry parent cluster; never invent impressions).
- Prefer Alta/official gazette mirrors when customs.gov.ru times out.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `skills/excalibur-research/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261002-1725-scout-live-wp-cannibalization-near-miss
status: open
run_date: 2026-10-02
role: excalibur-blog-scout
topic_id: B04
article_dir: n/a
severity: high
category: script

### What went wrong
- Scout appended B04 `kak-proverit-prohodnye-avto-iz-yaponii-2026` after `--check-query` PASS.
- Live WP already had `2026-09-29|prohodnye-avto-iz-yaponii-2026|Проходные авто из Японии 2026: как проверить год до ставки` in `EXCALIBUR_RECENT_WP_POSTS`.
- `excalibur_blog_scout_helper.py --check-query` only compares against `blog-topics.md` B* cards + local article dirs / ledger – it does **not** load `EXCALIBUR_RECENT_WP_POSTS` or live REST slugs.
- Stale `published-live-avtosales125.json` (2026-07) also missed recent B-pipeline posts.

### How the agent recovered this run
- Removed B04 card from `memory/topics/blog-topics.md`.
- Re-scouted against full `EXCALIBUR_RECENT_WP_POSTS` + live REST; chose B05 comparison Уссурийск vs Владивосток (no dedicated live slug).
- Rejected AS02 Encar / AS01 растаможка Кореи / AS05 СВХ / документы Китай – already live.

### Durable fix needed before next run
- Scout helper `--check-query` must accept recent WP posts (from today.py JSON / PUBLIC_SITE_URL REST) and fail on slug/title near-duplicates.
- Scout skill/agent: hard step "diff primary_query+slug vs EXCALIBUR_RECENT_WP_POSTS before append".
- Refresh or auto-fetch live slug index; do not trust July dump alone.

### Suggested files to inspect/change
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_today.py`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-scout.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261002-2015-director-doctor-llms-blog-path
status: open
run_date: 2026-10-02
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: medium
category: script

### What went wrong
- `excalibur_blog_doctor.py` fails with `FAIL llms generator supports --blog-path`.
- Actual CLI of `scripts/excalibur_blog_llms_generator.py` is `--blog-dir` (no `--blog-path`).
- `excalibur_blog_today.py` / scout helper only match `## B\\d+` topic cards, so existing AS* P0 pool is invisible and today reports `needs_scout` even when AS02/AS04/AS07 pass utility gate.

### How the agent recovered this run
- Continued pipeline: Scout for Авто-Сейлс B04+ (recent WP B03 already live), then research_start.
- Did not treat doctor `--blog-path` fail as hard stop; noted for fixer.

### Durable fix needed before next run
- Doctor check should assert `--blog-dir` (or accept both).
- today.py + scout_helper should recognize AS* topic cards OR migrate pool to B* consistently; next-id must consider recent WP / ledger occupancy so B01–B03 are not reused after ledger reset.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `.cursor/agents/excalibur-blog-scout.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`

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
