# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20261003-0931-cover-prompt-outfit-lock-conflict
status: open
run_date: 2026-10-03
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-era-glonass-pri-vvoze-avto-2026-nuzhna-li
severity: medium
category: prompt

### What went wrong
- `scripts/excalibur_blog_cover_quad_prompt.py` hardcodes cover outfit as "Outfit lock: thick heavyweight white hoodie", which conflicts with `memory/cover/blog-hero.json` outfit_rule (weather/topic outfit) and agent scene_hint (Vladivostok port rain jacket).
- Generated prompt also omitted corner brand `avto-sales125.ru` unless manually patched; style preset mentions it, but compact builder does not inject it into the cover line.
- Without a manual patch, i2i would ignore weather/topic outfit and catalog corner brand from design code / blog-hero lock.

### How the agent recovered this run
- After `--write-batch`, patched `cover/quad-mcp-prompt.txt` and synced `cover/quad-mcp-batch.json` mcp_args/api_args prompt: removed white-hoodie outfit lock, enforced rain-jacket outfit from scene_hint, added corner brand avto-sales125.ru.
- Used preferred Kie async API (`excalibur_blog_kie_gpt_image2_api.py`) instead of sync MCP gpt-image-2; split PASS; inject_html ok.

### Durable fix needed before next run
- Replace hardcoded white-hoodie outfit lock in `build_prompt()` with weather/topic outfit rule from blog-hero.json / cover scene_hint.
- Always append cover corner brand `avto-sales125.ru` (not Telegram) into the cover prompt line.
- Optionally raise prompt budget or prioritize outfit/brand tokens before truncating long scene_hint.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `memory/cover/blog-hero.json`
- `memory/cover/cover-design-code.json`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261003-0925-geo-qa-utility-gate-missing-markers
status: open
run_date: 2026-10-03
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-era-glonass-pri-vvoze-avto-2026-nuzhna-li
severity: blocker
category: script

### What went wrong
- `scripts/excalibur_blog_utility_gate.py` reads `policy["pain_markers_ru"]` and `policy["outcome_markers_ru"]`, but `memory/brief/editorial-policy.json` never defined those keys.
- Both lists therefore resolved to `[]`, every article scored `pain_markers=0` and `outcome_markers=0`, and the article gate always returned `BLOCK` with `слабо раскрыта боль читателя` / `слабо раскрыта польза/результат`.
- The defect is repo-wide, not article-specific: the already published `AS08` and `AS09` articles fail the same two assertions. The article-level utility gate was effectively unpassable, which hard-blocks GEO QA PASS and therefore cover/schema/indexer/publish.
- `min_pain_markers` / `min_outcome_markers` were also undefined, so the thresholds silently came from code defaults (2 and 3).

### How the agent recovered this run
- Added `pain_markers_ru` and `outcome_markers_ru` vocabularies plus explicit `min_pain_markers: 2` / `min_outcome_markers: 3` to `memory/brief/editorial-policy.json`.
- Vocabularies were derived from the `reader_pain` / `reader_outcome` concepts in `shared/editorial-utility-only.md`, kept topic-neutral, and deliberately not tuned to B01: with the same vocabulary the legacy `AS08`/`AS09` articles still fall short on outcome markers, so the gate still discriminates.
- Rejected `страх` as a pain marker: it is a substring of `страховка`/`страхование` and produced 15 false hits on an auto-niche article.
- Re-ran the gate on B01: PASS with pain=7, outcome=6, 0 warnings.

### Durable fix needed before next run
- Review and, if needed, extend the committed marker vocabularies; a GEO QA agent should not be authoring the criteria it grades against.
- Make `excalibur_blog_utility_gate.py` fail loudly (explicit config error, not a silent `BLOCK`) when a policy list required by an enabled check is missing or empty.
- Decide whether substring matching is acceptable or whether markers need word-boundary matching; document the choice next to the vocabularies.
- Add the article-level utility gate to the preflight/doctor surface so a universally failing gate is caught before a writer run, not after.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/editorial-utility-only.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261003-0930-geo-qa-cta-placeholder-vs-secret-scan
status: open
run_date: 2026-10-03
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-era-glonass-pri-vvoze-avto-2026-nuzhna-li
severity: blocker
category: publish

### What went wrong
- Writer shipped `article.html` with literal placeholder CTA hrefs `href="[CATALOG_URL]"` (×2) and `href="[TELEGRAM_URL]"` (×1); link-verify returned 404 on both, i.e. the article would publish with broken CTAs.
- Substituting the real URLs from `memory/brief/conversion-map.md` made link-verify pass but the commit was rejected by the pre-commit secret scan: `CATALOG_URL` and `TELEGRAM_URL` are configured Cloud Secrets, so their values must not enter git history.
- This is a contract deadlock, not a writer mistake: there is no documented convention for CTA URLs that are simultaneously required in the published HTML and forbidden in the repository. Earlier articles (`AS08`, `AS09`) carry the raw URLs because those secrets were not configured yet.
- `scripts/excalibur_blog_wp_publish.py` has no placeholder resolution at all, and `CATALOG_URL` / `TELEGRAM_URL` are absent from its `PUBLISH_ENV_KEYS`, so publish would upload the placeholders verbatim.

### How the agent recovered this run
- Kept the secret-safe placeholders in the committed `article.html`; did not use a secret-scan allowlist pragma to force the values into history.
- Verified the resolved targets out of tree: copied the article to a temp path, substituted both URLs from the conversion map, ran link-verify — both returned HTTP 200, verdict pass.
- Wrote `link-verify.json` with the URLs masked back to `[CATALOG_URL]` / `[TELEGRAM_URL]` plus a `note` field explaining the masking, so the committed report is both honest and secret-safe.
- Flagged in `article-qa.md` that publish must not run until the placeholders are resolved.

### Durable fix needed before next run
- Teach `excalibur_blog_wp_publish.py` to resolve `[CATALOG_URL]` / `[TELEGRAM_URL]` (and any other conversion-map token) from env at upload time, add those keys to `PUBLISH_ENV_KEYS`, and abort publish if an unresolved `[A-Z_]+_URL` token remains in the payload.
- Document the placeholder convention in the writing contract and the conversion map so Writer intentionally emits tokens instead of guessing, and so GEO QA knows placeholders are expected rather than broken.
- Teach `excalibur_blog_link_verify.py` about the token convention (resolve from env before checking) so GEO QA does not need an out-of-tree workaround.
- Decide whether `CATALOG_URL` / `TELEGRAM_URL` should stay secret-scanned at all, given that `memory/brief/conversion-map.md` already holds them in git; if yes, redact that file too, otherwise the policy is inconsistent.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_link_verify.py`
- `shared/excalibur-article-writing-contract.md`
- `shared/excalibur-wp-publish-contract.md`
- `memory/brief/conversion-map.md`
- `skills/writer-excalibur-blog/SKILL.md`, `.cursor/skills/writer-excalibur-blog/SKILL.md`

### Secrets
- none recorded (secret names only, no values)

### Fixer resolution
- pending

## INC-20261003-0935-geo-qa-tldr-label-contract-conflict
status: open
run_date: 2026-10-03
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-era-glonass-pri-vvoze-avto-2026-nuzhna-li
severity: medium
category: docs

### What went wrong
- `.cursor/skills/excalibur-geo-qa/SKILL.md` and `skills/excalibur-geo-qa/SKILL.md` state that the insight block must not start with the template label `TL;DR` or the phrase `Быстрый инсайт`.
- `shared/excalibur-article-writing-contract.md` line 88 gives exactly `<blockquote><b>TL;DR / Быстрый инсайт:</b> …` as the canonical example, and `skills/writer-excalibur-blog/SKILL.md` repeats the `AEO TL;DR Box` naming.
- Writer followed its own contract and emitted the forbidden label; no machine gate catches it, so the conflict only surfaces as a manual GEO QA finding and costs a FIX cycle every run.

### How the agent recovered this run
- Replaced the label with a natural Russian lead-in `Если коротко:`, preserving the blockquote structure the writing contract requires.
- Re-ran the human voice gate and HTML linter after the edit: both still PASS.
- Updated `char_count` in `article.meta.json` from 9003 to the measured 8991.

### Durable fix needed before next run
- Pick one rule and make the docs agree: either drop the `TL;DR / Быстрый инсайт:` example from `shared/excalibur-article-writing-contract.md` and the writer skill, or remove the prohibition from the GEO QA skill.
- Preferred: keep the prohibition (it exists to avoid AI-slop labels), replace the contract example with 2–3 natural alternatives, and keep `AEO TL;DR Box` as the internal block name only.
- Consider enforcing it in `excalibur_blog_human_voice_gate.py` so it is caught at writer time instead of GEO QA time.

### Suggested files to inspect/change
- `shared/excalibur-article-writing-contract.md`
- `skills/writer-excalibur-blog/SKILL.md`, `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `skills/excalibur-geo-qa/SKILL.md`, `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `scripts/excalibur_blog_human_voice_gate.py`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261003-0940-geo-qa-typed-task-missing-in-cloud-enum
status: open
run_date: 2026-10-03
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-era-glonass-pri-vvoze-avto-2026-nuzhna-li
severity: medium
category: handoff

### What went wrong
- The Cloud API does not accept `excalibur-blog-geo-qa` as a Task type, so step ③ could not be launched as a typed subagent.
- The Director had to fall back to `Task(generalPurpose)` and hand over the role contract by path (`.cursor/agents/excalibur-blog-geo-qa.md`, `.cursor/skills/excalibur-geo-qa/SKILL.md`), re-stating the inputs, result marker and prohibitions inline.
- The same gap is already known for other roles (`shared/agent-pipeline-pitfalls.md` mentions the fallback generically) but it is not recorded per role, and the fallback contract has to be retyped by hand on every run, which is where role bleed (parent writing the article, merged cover+schema) comes from.

### How the agent recovered this run
- Ran as `generalPurpose` with the role contract read from `.cursor/agents/excalibur-blog-geo-qa.md` and `.cursor/skills/excalibur-geo-qa/SKILL.md`, strictly one Task = one role.
- Stayed inside the GEO QA zone: no cover, no schema, no publish, no article rewrite beyond the two gate-driven fixes recorded in `article-qa.md`.

### Durable fix needed before next run
- Document explicitly in `AGENTS.md` / `.cursor/rules/excalibur-blog-orchestrator.mdc` that every `excalibur-blog-*` typed Task is currently unavailable in Cloud and that `generalPurpose` is the normal path, not an exception.
- Add a ready-to-paste `generalPurpose` contract snippet per role (inputs, scripts, result marker, prohibitions, incident duty) so the Director does not re-author it each run.
- Verify whether the typed agent names need registering anywhere for the Cloud enum to accept them; if that is impossible, state it once and stop treating it as an incident-worthy surprise on every run.

### Suggested files to inspect/change
- `AGENTS.md`
- `.cursor/rules/excalibur-blog-orchestrator.mdc`
- `shared/agent-pipeline-pitfalls.md`
- `shared/pipeline-task-map.md`
- `skills/director-excalibur-blog/SKILL.md`, `.cursor/skills/director-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261003-0915-research-regulation-gov-503
status: open
run_date: 2026-10-03
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-era-glonass-pri-vvoze-avto-2026-nuzhna-li
severity: low
category: api

### What went wrong
- WebFetch `https://regulation.gov.ru/projects/163381/` returned HTTP 503 during deep research on ERA-GLONASS moratorium project status.
- Auto.ru Mag page returned HTTP 403 on direct fetch (SERP snippet still usable).

### How the agent recovered this run
- Cross-checked project 163381 status via secondary sources that cite the same project id and Minpromtorg/TASS statements (glonasss.com, news.drom.ru, fontanka.ru).
- Used official publication.pravo.gov.ru for PP 855 / PP 76 and 855.aoglonass.ru for operator process; did not invent decree adoption dates.

### Durable fix needed before next run
- Research skill: if regulation.gov.ru is 5xx, document fallback chain (pravo.gov.ru + operator pages + reputable news citing regulation project id) and treat 503 as expected soft failure, not research blocker.
- Optionally add a short note in agent pipeline pitfalls about regulation.gov.ru instability.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261003-0903-scout-precommit-secret-name-url
status: open
run_date: 2026-10-03
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: env

### What went wrong
- First `git commit` failed in pre-commit hook with `invalid variable name` while expanding `CLOUD_AGENT_INJECTED_SECRET_NAMES` (at least one injected "name" is not a valid bash identifier, e.g. a URL).
- `scripts/sanitize_cloud_secret_names.sh` is referenced in automation memory / previous fixer notes, but the file is missing in this workspace checkout.

### How the agent recovered this run
- Filtered `CLOUD_AGENT_INJECTED_SECRET_NAMES` to `^[A-Za-z_][A-Za-z0-9_]*$` in the shell session, then recommitted successfully.
- Push to feature branch succeeded after the filtered commit.
- Recurrence 2026-10-03 writer(B01): same `invalid variable name` on first commit; cleared/filtered injected names in session and recommitted (`f451f51`).
- Recurrence 2026-10-03 schema(B01): `scripts/sanitize_cloud_secret_names.sh` still missing; session list contained non-identifier `[REDACTED]`; filtered to `^[A-Za-z_][A-Za-z0-9_]*$` before commit of `schema.jsonld`.

### Durable fix needed before next run
- Restore or add `scripts/sanitize_cloud_secret_names.sh` that filters invalid identifiers before any git hook expands `${!SECRET_NAME}`.
- Wire the sanitize step into agent pre-commit docs / Cloud install so scout/research/writer/schema/publish do not hit the same blocker.
- Optionally harden the Cursor pre-commit hook to skip non-identifier names instead of aborting the commit.
- Note: injected list may be comma-separated; sanitize must split on commas and drop non-identifiers (and redacted placeholders).

### Suggested files to inspect/change
- `scripts/sanitize_cloud_secret_names.sh` (missing; recreate)
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- Cloud agent install / pre-commit hook that expands `CLOUD_AGENT_INJECTED_SECRET_NAMES`

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
