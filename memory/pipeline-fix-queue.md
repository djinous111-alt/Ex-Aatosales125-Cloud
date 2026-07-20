# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

_none — all 2026-07-20 AS11 incidents fixed below._

## Recently fixed (2026-07-20 AS11)

## INC-20260720-1735-publish-paramiko-missing
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Cloud install now installs `paramiko` from requirements.txt with apt `python3-paramiko` fallback.
- `excalibur_blog_wp_publish.py --env-check` reports `paramiko_installed` + install hint.
- Publish skill + pitfalls document the recovery path.
files_changed:
- `.cursor/cloud-agent-install.sh`
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py`
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` → paramiko_installed=true
- bash `.cursor/cloud-agent-install.sh` → paramiko ok
commit: pending-parent-commit

### What went wrong
- `excalibur_blog_wp_publish.py` failed on first live run: `ModuleNotFoundError: No module named 'paramiko'`.
- `paramiko` is listed in `requirements.txt`, but Cloud runtime did not have it installed (PEP 668 blocked plain `pip3 install`).

### How the agent recovered this run
- Installed `python3-paramiko` via apt (`2.12.0`) and retried publish → PASS (SSH + HTTP trigger).

### Durable fix needed before next run
- Ensure Cloud/agent bootstrap installs `paramiko` from `requirements.txt` (or `python3-paramiko` via apt) before publish step.
- `excalibur_blog_wp_publish.py --env-check` should warn if `paramiko` import fails (not only SSH env vars).
- Document in publish skill / pitfalls: missing paramiko → apt/pip before retry, not silent FAIL.

### Suggested files to inspect/change
- `requirements.txt`
- `.cursor/environment.json`
- `scripts/cloud-agent-install.sh` (or equivalent install hook)
- `scripts/excalibur_blog_wp_publish.py` (`--env-check`)
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- see status/fix_summary above

## INC-20260720-1732-cover-mcp-sync-timeout-kie-api
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Cover skill/agent default to Kie API script; MCP sync documented as legacy; `-32001` not terminal when API available.
- Hero host script: HTTPS prefer + litterbox fallback after catbox/0x0; optional fetch check.
- Prompt builder allowlists litterbox/catbox/0x0 + preferred HTTPS host; kie contract updated.
files_changed:
- `scripts/excalibur_blog_hero_reference_url.py`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/kie-gpt-image-api-contract.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_hero_reference_url.py scripts/excalibur_blog_cover_quad_prompt.py`
- `python3 scripts/excalibur_blog_hero_reference_url.py --help` (litterbox in choices)
commit: pending-parent-commit

### What went wrong
- Sync MCP `gpt-image-2` returned `-32001 Request timed out` (i2i 2K and even 1K / short prompt).
- Earlier attempt with `http://avtosales125.ru/...` hero URL failed fast: `image fetch failed` (Kie cannot reliably fetch that host; HTTP→HTTPS redirect).
- `excalibur_blog_hero_reference_url.py --force` failed: catbox 412, 0x0 503.

### How the agent recovered this run
- Rehosted local `blog-hero-reference.png` to litterbox (`https://litter.catbox.moe/...`).
- Used preferred path `scripts/excalibur_blog_kie_gpt_image2_api.py` (createTask → poll recordInfo) → ONE quad success → `quad_apply --inject-html`.

### Durable fix needed before next run
- Cover runbook / Cloud skill: default to Kie API script; MCP sync only as legacy.
- Hero host script: prefer HTTPS; add litterbox fallback when catbox/0x0 fail; validate Kie can fetch URL.
- Document that `-32001` is not terminal if Kie API path is available.

### Suggested files to inspect/change
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `scripts/excalibur_blog_hero_reference_url.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/kie-gpt-image-api-contract.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- see status/fix_summary above

## INC-20260720-1732-cover-outfit-lock-white-hoodie
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Replaced hardcoded white-hoodie Outfit lock with `blog-hero.json` outfit_rule + cover scene_hint / topic_outfit_hint.
- Explicit negative: never force thick heavyweight white hoodie.
files_changed:
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_prompt.py`
- `rg` confirms only negative white-hoodie wording remains
commit: pending-parent-commit

### What went wrong
- `scripts/excalibur_blog_cover_quad_prompt.py` hardcodes `Outfit lock: thick heavyweight white hoodie`, conflicting with `blog-hero.json` outfit_rule and agent instruction (outfit from scene weather/topic; NOT white hoodie lock).

### How the agent recovered this run
- Patched generated `quad-mcp-prompt.txt` + `quad-mcp-batch.json` before Kie create: rain jacket + charcoal sweater for Vladivostok port; explicit NOT white hoodie.

### Durable fix needed before next run
- Replace hardcoded outfit lock with blog-hero `outfit_rule` / scene_hint weather-topic wording in the prompt builder.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `memory/cover/blog-hero.json`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- see status/fix_summary above

## INC-20260720-1720-geo-qa-utility-pain-markers-empty
status: fixed
run_date: 2026-07-20
role: excalibur-blog-geo-qa
topic_id: AS11
article_dir: memory/blog/articles/AS11-privezti-elektromobil-iz-kitaya-2026
severity: high
category: script
fixed_at: 2026-07-20
fix_summary:
- Restored `pain_markers_ru` / `outcome_markers_ru` (+ min_* thresholds) in `memory/brief/editorial-policy.json`.
- Added fallback defaults in `scripts/excalibur_blog_utility_gate.py` when policy lists are empty (otherwise every article BLOCK).
- Minimal lead edit for human-voice pain markers; insight label `Коротко:` instead of `TL;DR / Быстрый инсайт`.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `memory/blog/articles/AS11-privezti-elektromobil-iz-kitaya-2026/article.html`
checks_run:
- `python3 scripts/excalibur_blog_utility_gate.py --article-dir …AS11…` → PASS
- `python3 scripts/excalibur_blog_human_voice_gate.py --article-dir …AS11…` → PASS
- sanity: AS09 utility gate PASS with same policy
commit: pending-parent-commit

### What went wrong
- Utility gate required `min_pain_markers=2` / `min_outcome_markers=3` but `editorial-policy.json` had empty/missing `pain_markers_ru` / `outcome_markers_ru` → pain_count=0 / outcome_count=0 for every article (AS08/AS09/AS11).
- Regression of AS05 INC-20260719-1710-writer-utility-pain-markers-empty.
- Human-voice also needed ≥2 pain markers; lead had only `ошиб`.

### How the agent recovered this run
- Restored policy marker lists + script fallback; minimal lead wording for pain/outcome; re-ran gates → PASS.

### Durable fix needed before next run
- Keep policy lists + script fallback; document in pitfalls that empty marker lists must not silently BLOCK; sync Cloud skill note if needed.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Verified policy marker lists + utility_gate fallback remain; pitfalls document empty-marker silent BLOCK risk.
files_changed:
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- policy JSON has pain_markers_ru/outcome_markers_ru
commit: pending-parent-commit

## INC-20260720-1720-geo-qa-cta-urls-script-missing
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Added `scripts/excalibur_blog_cta_urls.py` (reinject/redact from CATALOG_URL/TELEGRAM_URL env).
- Wired into GEO QA and Publish skills; documented in pitfalls.
files_changed:
- `scripts/excalibur_blog_cta_urls.py`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cta_urls.py`
- `python3 scripts/excalibur_blog_cta_urls.py --help`
commit: pending-parent-commit

### What went wrong
- Writer left CTA `href="[REDACTED]"` placeholders; memory/runbook expects `scripts/excalibur_blog_cta_urls.py` for reinject before link-verify / publish.
- Script absent on current branch and `origin/main` → link-verify would fail without workaround.

### How the agent recovered this run
- Context-aware reinject from env `CATALOG_URL` / `TELEGRAM_URL` into `article.html`; link-verify PASS (2 unique URLs).

### Durable fix needed before next run
- Add `scripts/excalibur_blog_cta_urls.py` (reinject + optional re-redact) and call it from GEO QA / publish skills; document in pitfalls.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cta_urls.py` (create)
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- see status/fix_summary above

## INC-20260720-1715-research-pain-map-row-regex
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Gate now counts markdown table data-rows under `## pain_solution_map` (header/separator excluded).
- Research agent/skill document ≥3 data-rows; keyword prefixes recommended but not required.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `agents/excalibur-blog-research.md`
- `.cursor/agents/excalibur-blog-research.md`
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_research_notes_gate.py --article-dir …AS11…` → PASS pain_solution_rows=5
commit: pending-parent-commit

### What went wrong
- First `excalibur_blog_research_notes_gate.py` run BLOCKED: `pain_solution_map too thin: rows=1 < 3`.
- Gate counts only markdown table rows that contain keywords боль|pain|решение|solution|result|результат; a normal header+data table without those words in each data cell counts as 1 (header only).

### How the agent recovered this run
- Rewrote `pain_solution_map` rows with explicit `боль:` / `решение:` / `результат:` prefixes; gate PASS.

### Durable fix needed before next run
- Document in research skill/agent that each pain_solution_map data row must include those keywords, OR relax gate to count any table row under `## pain_solution_map` (minus header separator).

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py` (pain_map_rows regex)
- `.cursor/skills/excalibur-research/SKILL.md`
- `.cursor/agents/excalibur-blog-research.md`

### Secrets
- none recorded

### Fixer resolution
- see status/fix_summary above

## INC-20260720-1710-scout-precommit-invalid-secret-name
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Added `scripts/excalibur_sanitize_injected_secret_names.sh` and install-time sanitize + patch of Cursor `pre-commit.cursor` to skip non-identifier names.
- Scout skill documents eval-before-commit recovery.
files_changed:
- `scripts/excalibur_sanitize_injected_secret_names.sh`
- `.cursor/cloud-agent-install.sh`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- bash `.cursor/cloud-agent-install.sh` → patched pre-commit sanitize
- bash `scripts/excalibur_sanitize_injected_secret_names.sh` (empty OK)
commit: pending-parent-commit

### What went wrong
- `git commit` failed in Cloud pre-commit secrets scanner: bash `${!SECRET_NAME}` with an entry from `CLOUD_AGENT_INJECTED_SECRET_NAMES` that is not a valid shell identifier.
- Blocked commit of AS11 topic card until names were sanitized.

### How the agent recovered this run
- Filtered `CLOUD_AGENT_INJECTED_SECRET_NAMES` to valid `[A-Za-z_][A-Za-z0-9_]*` identifiers, then re-ran commit/push.

### Durable fix needed before next run
- Sanitize secret-name injection before hooks run, or make pre-commit skip non-identifier names instead of aborting.

### Suggested files to inspect/change
- Cloud agent hook `pre-commit.cursor` (secrets scanner loop)
- Dashboard / env injection of `CLOUD_AGENT_INJECTED_SECRET_NAMES`

### Secrets
- none recorded

### Fixer resolution
- see status/fix_summary above

## INC-20260720-1703-doctor-llms-blog-path
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Doctor checks `--blog-dir` / `--out-dir` / `--site-base` (removed `--blog-path` expectation).
- Indexer agent/skill examples aligned; no invented `--redact-site-base`.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → SUMMARY errors=0
- `python3 scripts/excalibur_blog_llms_generator.py --help`
commit: pending-parent-commit

### What went wrong
- `excalibur_blog_doctor.py` checks for `--blog-path` in llms generator help, but `excalibur_blog_llms_generator.py` exposes `--blog-dir` / `--out-dir` / `--site-base` (default `[REDACTED]`).
- Earlier note wrongly claimed `--redact-site-base`; that flag does **not** exist on the generator.
- Doctor SUMMARY errors=1 blocks clean preflight even when publish env is OK.
- Indexer agent contracts still document `--blog-path /` (stale).

### How the agent recovered this run
- Continued pipeline after documenting FAIL; did not change doctor mid-run before scout.
- Indexer AS11 (2026-07-20): used `--blog-dir` / `--out-dir` / `--site-base [REDACTED]`; ignored stale `--blog-path` and nonexistent `--redact-site-base`.

### Durable fix needed before next run
- Align doctor check with actual CLI (`--blog-dir`, optionally `--out-dir` / `--site-base`) — remove `--blog-path` expectation.
- Sync indexer agent/skill examples: drop `--blog-path`; document `--site-base` (commit-safe `[REDACTED]` or `${PUBLIC_SITE_URL}` for live).
- Do not invent `--redact-site-base` unless implemented as an alias.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_llms_generator.py`
- `.cursor/agents/excalibur-blog-indexer.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

## INC-20260720-1703-as-topic-id-regex
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Restored `(?:AS|B)\d+` parsing in today.py and scout_helper.py (dirs, topic cards, next-id AS* preference).
files_changed:
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_scout_helper.py --suggest-next` → Next AS12, pool=10
- `python3 scripts/excalibur_blog_today.py` parses AS ledger rows
commit: pending-parent-commit

### What went wrong
- `excalibur_blog_today.py` and `excalibur_blog_scout_helper.py` only match `B\\d+` topic cards; Auto-Sales pool uses `AS\\d+`.
- Result: `EXCALIBUR_TOPIC_SELECTION=needs_scout`, scout_helper reports 0 topics / next B01, while AS01–AS09 exist in blog-topics.md.
- Prior run memory claimed `(?:AS|B)` fix, but current scripts regressed.

### How the agent recovered this run
- Forced scout for fresh AS11-class topic; will pass explicit `--topic-id` to research_start.

### Durable fix needed before next run
- Restore `(?:AS|B)\\d+` parsing in today.py, scout_helper.py (and active article dir regex).

### Suggested files to inspect/change
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`

### Secrets
- none recorded

## INC-20260720-1703-ledger-gap-as01-as10
status: fixed
fixed_at: 2026-07-20
fix_summary:
- Backfilled AS01–AS07 + AS10 into `shared/published-articles.md` from live WP slugs with `[REDACTED]` URLs.
files_changed:
- `shared/published-articles.md`
checks_run:
- `python3 scripts/excalibur_blog_today.py` shows AS01–AS11 in published list
- scout helper: unwritten topic IDs empty; next AS12
commit: pending-parent-commit

### What went wrong
- `shared/published-articles.md` only lists AS08/AS09, but live WP recent posts include slugs for AS01–AS07 and AS10 (СБКТС/ЭПТС).
- Risk: tomorrow/today may re-select cannibalizing topics if AS regex is restored without ledger backfill.

### How the agent recovered this run
- Will avoid AS01–AS10 topics; scout for new AS11+; publish step must append ledger correctly.

### Durable fix needed before next run
- Backfill ledger rows for live WP AS01–AS07 and AS10 from site posts (status=published), keep REDACTED URLs.

### Suggested files to inspect/change
- `shared/published-articles.md`
- optionally `scripts/excalibur_blog_today.py` WP slug dedupe

### Secrets
- none recorded


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
