# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents


## INC-20260719-0926-cover-hero-host-upload
status: open
run_date: 2026-07-19
role: excalibur-blog-cover
topic_id: AS01
article_dir: memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026
severity: low
category: tooling

### What went wrong
- `excalibur_blog_hero_reference_url.py --force` failed: catbox HTTP 412, 0x0 HTTP 503.
- Could not refresh hosted face PNG for i2i; existing `reference_url_hosted` on avtosales125.ru was reused.

### How the agent recovered this run
- Kept prior `reference_url_hosted` (blueprint face URL on site).
- Generated ONE quad via `excalibur_blog_kie_gpt_image2_api.py` (KIE_API_KEY) with `input_urls`; split+inject PASS.

### Durable fix needed before next run
- Add fallback host (e.g. temporary WP media upload / imgbb / Cloudflare R2) when catbox/0x0 unavailable.
- Document in cover skill that existing site URL is acceptable if force-upload fails and URL still serves face reference.

### Suggested files to inspect/change
- `scripts/excalibur_blog_hero_reference_url.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20260719-0922-schema-secret-scan-urls
status: open
run_date: 2026-07-19
role: excalibur-blog-schema
topic_id: AS01
article_dir: memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026
severity: medium
category: tooling

### What went wrong
- First `git commit` of `schema.jsonld` blocked by Cursor secret-scan: `PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL` appear in BlogPosting/author/publisher/`sameAs` (required for live JSON-LD).
- Schema skill does not document commit hygiene vs publish-ready URLs (AS04 used redacted commit; AS08/AS09 still have live hosts in git history).

### How the agent recovered this run
- Rebuilt schema with live URLs from env + authors-registry.
- Committed redacted `schema.jsonld` (`[REDACTED]` placeholders, AS04 pattern).
- Restored live `schema.jsonld` in working tree for Publish (not re-committed).

### Durable fix needed before next run
- Document in schema skill: build live schema → commit redacted copy → keep live file for publish; or teach publish to rehydrate `[REDACTED]` from env before WP meta upload.
- Optional: `pragma: allowlist secret` path if JSON-safe allowlisting is supported.

### Suggested files to inspect/change
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_wp_publish.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20260719-0915-geo-qa-utility-pain-markers-empty
status: open
run_date: 2026-07-19
role: excalibur-blog-geo-qa
topic_id: AS01
article_dir: memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026
severity: blocker
category: script

### What went wrong
- `excalibur_blog_utility_gate.py` always BLOCKs articles: `pain_markers=0 < 2` and `outcome_markers=0 < 3`.
- `memory/brief/editorial-policy.json` has no `pain_markers_ru` / `outcome_markers_ru` and no `min_pain_markers` / `min_outcome_markers`, but the script defaults mins to 2/3 against empty lists.
- Same BLOCK reproduces on previously published AS09 when re-run.

### How the agent recovered this run
- Confirmed human-voice gate PASS (its own PAIN/OUTCOME_MARKERS find hits in AS01).
- Did not invent article filler; recorded FAIL in `article-qa.md` and returned FIX to Fixer/Director for policy/script.

### Durable fix needed before next run
- Either skip pain/outcome checks when marker lists are empty, or populate `pain_markers_ru` / `outcome_markers_ru` (+ mins) in `editorial-policy.json` aligned with human-voice markers.
- Add regression: AS09 (or fixture) must PASS utility article gate after fix.

### Suggested files to inspect/change
- `scripts/excalibur_blog_utility_gate.py`
- `memory/brief/editorial-policy.json`
- `shared/editorial-utility-only.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20260719-0915-geo-qa-cta-literal-redacted
status: open
run_date: 2026-07-19
role: excalibur-blog-geo-qa
topic_id: AS01
article_dir: memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026
severity: high
category: qa

### What went wrong
- AS01 `article.html` contains three CTA anchors with literal `href="[REDACTED]"` (on-disk bytes, len=10), not real catalog/Telegram URLs.
- `link-verify` FAIL: unique `[REDACTED]` treated as relative path → HTTP 404 against site base.
- Likely Writer over-redacted after secret-scan lessons instead of writing public CTA URLs.

### How the agent recovered this run
- Did not rewrite article.html (GEO QA report-only); FIX list to Writer: restore catalog + Telegram hrefs from fact-bank/site brief.
- Overall article-qa verdict FAIL; cover/schema blocked.
- Writer FIX (same run): replaced 3 literal href placeholders with public catalog URL and Telegram URL; on-disk placeholder count=0; ready for link-verify re-run.

### Durable fix needed before next run
- Writer/skill contract: public CTA (site catalog, Telegram handle) must never be written as the placeholder string `[REDACTED]` in `article.html`.
- Pitfalls: redact secrets in SERP/env dumps, not marketing CTA URLs.
- Optional linter/gate: fail if `href="[REDACTED]"` or `href` equals placeholder.

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `shared/agent-pipeline-pitfalls.md`
- `scripts/excalibur_blog_link_verify.py` (optional placeholder detect)

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20260719-0910-research-secret-scan-serp
status: open
run_date: 2026-07-19
role: excalibur-blog-research
topic_id: AS01
article_dir: memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026
severity: medium
category: env

### What went wrong
- Pre-commit secrets scanner crashed when `CLOUD_AGENT_INJECTED_SECRET_NAMES` contained a non-bash-identifier name (looks like a URL), via `${!SECRET_NAME}`.
- After filtering invalid names, commit was blocked because `research-serp.json` from `research_start` contained the value of `PUBLIC_SITE_URL` in a SERP hit URL.

### How the agent recovered this run
- Filtered secret names to valid Python/bash identifiers before re-running the hook.
- Replaced the site URL value in `research-serp.json` with `[REDACTED]` and committed only AS01 research artifacts.
- Left director-touched ledger/topics/fix-queue unstaged for the director.

### Durable fix needed before next run
- `excalibur_blog_research_start.py` (or SERP writer) must redact `PUBLIC_SITE_URL` / site host from `research-serp.json` before write.
- Pre-commit / Cloud secrets injection: skip non-identifier names in `CLOUD_AGENT_INJECTED_SECRET_NAMES` instead of crashing.
- Pitfalls note: do not commit raw SERP dumps that embed the public site host as a "secret" collision.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_start.py`
- `shared/agent-pipeline-pitfalls.md`
- `/root/.cursor/agent-hooks/` pre-commit secrets scanner (env injection)

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20260719-1203-director-as-topic-regex
status: open
run_date: 2026-07-19
role: excalibur-blog-director
topic_id: AS01
article_dir: memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_today.py` и `excalibur_blog_scout_helper.py` матчат только `B\d+`, поэтому пул AS01–AS09 в `blog-topics.md` невидим → ложный `needs_scout`.
- AS08/AS09 article dirs тоже не считаются active (`(B\d+)-` only).
- AS01/AS03/AS05 не на WP, но utility gate блокировал AS01 из‑за h1 без маркера «как/чек-лист».

### How the agent recovered this run
- Выставлен `EXCALIBUR_TOPIC_ID=AS01`.
- В карточке AS01 h1 добавлен маркер «Как проходит…».
- `utility_gate` PASS → `research_start` зарезервировал AS01 in_progress.

### Durable fix needed before next run
- Regex topic IDs: `(?:AS|B)\d+` в today.py, scout_helper.py (парсинг pool + active dirs + next B/AS id).
- Документировать в pitfalls: AS-пул Авто-Сейлс; не запускать Scout, пока есть unpublished AS P0.
- Опционально: utility gate / editorial — допускать how_to intent без слова «как» в h1, если search_intent=how_to|checklist|comparison.

### Suggested files to inspect/change
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `shared/agent-pipeline-pitfalls.md`
- `memory/topics/blog-topics.md` (AS03/AS05 h1 markers)

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
