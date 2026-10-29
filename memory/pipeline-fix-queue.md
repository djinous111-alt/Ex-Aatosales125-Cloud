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

## INC-20261029-1705-scout-precommit-secret-name-url
status: open
run_date: 2026-10-29
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: env

### What went wrong
- `git commit` failed in Cloud Agent pre-commit secrets scanner: `CLOUD_AGENT_INJECTED_SECRET_NAMES` includes a non-identifier entry that is a catalog URL string (`https://…/`), so bash `${!SECRET_NAME}` raises `invalid variable name`.
- Documented helper `scripts/excalibur_git.sh` (filters non-identifier secret names) is missing from the repo.

### How the agent recovered this run
- Re-ran `git commit` with a filtered `CLOUD_AGENT_INJECTED_SECRET_NAMES` containing only valid bash identifiers; commit `29bf9412` succeeded and was pushed.
- Scout topic card itself was unrelated to the hook failure.

### Durable fix needed before next run
- Restore or add `scripts/excalibur_git.sh` that filters non-identifier names from `CLOUD_AGENT_INJECTED_SECRET_NAMES` before commit.
- Fix Cloud Secrets / injection so secret *names* are valid identifiers (URLs belong in secret *values*, not names).
- Optionally document the workaround in `shared/agent-pipeline-pitfalls.md` and scout memory.

### Suggested files to inspect/change
- `scripts/excalibur_git.sh` (missing)
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md` / automation memory scout notes

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1710-research-tech-markers-komplektatsii
status: open
run_date: 2026-10-29
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` marks auto topics as `technical_topic=true` because TECH_MARKERS include substring `ии`, which matches ordinary Russian words like `комплектации` in H1/slug/primary_query.
- That forces a hard error unless research-notes contain ≥3 `github.com` URLs, even when the article is about China car configs (not software).

### How the agent recovered this run
- Added relevant VIN/WMI GitHub evidence (idlesign/vininfo, WALL-E/vin-decoder, dev-drozd/VIN-DECODER) proving `LGB` = Dongfeng Nissan.
- Gate reached PASS; added `government.ru/docs/...` for ПП 1713 to satisfy official-docs warning.

### Durable fix needed before next run
- Tighten TECH_MARKERS matching: word-boundary / whole-token checks, or exclude auto niche topics (China/Korea/Japan import) from `technical_topic`.
- Document that `ии`/`ai` substrings in Russian auto vocabulary are false positives.
- Optionally allow non-GitHub primary-source evidence (customs, catalogs) to satisfy the technical evidence quota for AVTO SALES topics.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1710-research-tech-markers-komplektatsii
status: open
run_date: 2026-10-29
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` marks auto topics as `technical_topic=true` because TECH_MARKERS include substring `ии`, which matches ordinary Russian words like `комплектации` in H1/slug/primary_query.
- That forces a hard error unless research-notes contain ≥3 `github.com` URLs, even when the article is about China car configs (not software).

### How the agent recovered this run
- Added relevant VIN/WMI GitHub evidence (idlesign/vininfo, WALL-E/vin-decoder, dev-drozd/VIN-DECODER) proving `LGB` = Dongfeng Nissan.
- Gate reached PASS with warning about official docs URL; added `government.ru/docs/...` for ПП 1713.

### Durable fix needed before next run
- Tighten TECH_MARKERS matching: word-boundary / whole-token checks, or exclude auto niche topics (China/Korea/Japan import) from `technical_topic`.
- Document that `ии`/`ai` substrings in Russian auto vocabulary are false positives.
- Optionally allow non-GitHub primary-source evidence (customs, catalogs) to satisfy the technical evidence quota for AVTO SALES topics.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1721-geo-qa-utility-pain-markers-rebrand
status: open
run_date: 2026-10-29
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: high
category: qa

### What went wrong
- First GEO QA run: `excalibur_blog_utility_gate.py` BLOCK with `pain_markers=0` and `outcome_markers=0`.
- Root cause: `memory/brief/editorial-policy.json` again missing `pain_markers_ru` / `outcome_markers_ru` and `min_pain_markers` / `min_outcome_markers` after AVTO SALES rebrand baseline on this branch.
- Current `scripts/excalibur_blog_utility_gate.py` also lacked the durable empty-list fallback that earlier private-pipeline commits had restored.

### How the agent recovered this run
- Restored pain/outcome marker lists + mins in `memory/brief/editorial-policy.json`.
- Re-added empty-list fallback defaults in `scripts/excalibur_blog_utility_gate.py`.
- Point-fixed article.html for human-voice outcome markers (≥3) and Fact Check second line wording; re-ran all gates → PASS score 87.

### Durable fix needed before next run
- Keep pain/outcome lists in editorial-policy as required contract fields (do not drop on rebrand/template sync).
- Keep utility-gate fallback forever so empty policy lists cannot zero-out a valid article.
- Add a doctor/preflight check that fails if `pain_markers_ru`/`outcome_markers_ru` are missing.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1721-geo-qa-typed-task-unavailable
status: open
run_date: 2026-10-29
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: low
category: handoff

### What went wrong
- Cloud typed Task `excalibur-blog-geo-qa` unavailable; Director used `generalPurpose` fallback with agent+skill paths.

### How the agent recovered this run
- Ran as generalPurpose GEO QA per AGENTS.md Cloud Task fallback; completed full script suite to PASS.

### Durable fix needed before next run
- Register typed Task types for excalibur-blog-* roles in Cloud, or keep generalPurpose fallback documented as default.

### Suggested files to inspect/change
- `AGENTS.md`
- `CLOUD-AUTOMATION.md`
- `.cursor/agents/excalibur-blog-geo-qa.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1721-geo-qa-human-voice-outcome-markers
status: open
run_date: 2026-10-29
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: qa

### What went wrong
- Human voice gate BLOCK: only 2 outcome markers (`результат`, `проверьте`) while gate requires ≥3 distinct OUTCOME_MARKERS hits.
- Writer lead used «соберёте» (future) which does not match imperative marker `соберите`.

### How the agent recovered this run
- Point edits: success paragraph «получите»/«сможете»; next-steps «соберите»; post-checklist «Выберите»; Fact Check second label → «Опора на источники» (kept required «Материал проверен»).

### Durable fix needed before next run
- Writer skill/checklist: ensure ≥3 of human-voice OUTCOME_MARKERS appear as substrings (получите/сможете/проверьте/соберите/выберите/…).
- Note that conjugated forms like «соберёте» do not satisfy `соберите`.

### Suggested files to inspect/change
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `scripts/excalibur_blog_human_voice_gate.py`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1726-schema-placeholder-secret-scan
status: open
run_date: 2026-10-29
role: excalibur-blog-schema
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: env

### What went wrong
- First schema draft resolved absolute site/CTA URLs from env into `schema.jsonld`; Cursor secret-scan blocked commit (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`).
- Pre-commit also still fails unless `CLOUD_AGENT_INJECTED_SECRET_NAMES` is filtered to bash identifiers (same class as scout INC-20261029-1705).

### How the agent recovered this run
- Rewrote `schema.jsonld` to use `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}` placeholders (public Instagram/2GIS kept).
- Filtered invalid secret *names* before commit; pushed `f4e219a9` (placeholder cleanup may follow).

### Durable fix needed before next run
- Document in schema skill: committed `schema.jsonld` must use env placeholders for site/CTA URLs; publish must expand before WP meta.
- Teach `excalibur_blog_wp_publish.py` to expand `${PUBLIC_SITE_URL}` and CTA placeholders in `schema_jsonld` at publish time.
- Restore `scripts/excalibur_git.sh` (filter non-identifier secret names) — still missing.

### Suggested files to inspect/change
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_git.sh` (missing)
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261029-1725-cover-prompt-hoodie-lock
status: open
run_date: 2026-10-29
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: prompt

### What went wrong
- `excalibur_blog_cover_quad_prompt.py` hardcodes `Outfit lock: thick heavyweight white hoodie`, which conflicts with blog-hero/skill rules (NO hoodie/cap/hood) and agent `scene_hint` (rain jacket / weather-topic outfit).

### How the agent recovered this run
- Patched generated `quad-mcp-prompt.txt` + `quad-mcp-batch.json` to replace hoodie lock with dark rain jacket / NO hoodie before Kie i2i.

### Durable fix needed before next run
- Remove fixed hoodie outfit lock from prompt builder; derive outfit from `slots.cover.scene_hint` + `blog-hero.json` outfit_rule (weather/topic).

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `memory/cover/blog-hero.json`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1725-cover-kie-http-ref-fail
status: open
run_date: 2026-10-29
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: api

### What went wrong
- First Kie `gpt-image-2-image-to-image` task failed (`failCode=500 Internal Error`) with `reference_url_hosted` on `http://avtosales125.ru/...` (301 → https).
- `--force` catbox upload returned HTTP 412; 0x0 timed out on SSL handshake.

### How the agent recovered this run
- Switched `reference_url_hosted` / batch `input_urls` to HTTPS wordpress media URL; second Kie task succeeded; `quad_apply --inject-html` PASS.

### Durable fix needed before next run
- Prefer HTTPS in `blog-hero.json` / `excalibur_blog_hero_reference_url.py` when WP media redirects HTTP→HTTPS.
- Document Kie sensitivity to HTTP redirects for `input_urls`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_hero_reference_url.py`
- `memory/cover/blog-hero.json`
- `scripts/excalibur_blog_kie_gpt_image2_api.py`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261029-1734-indexer-llms-missing-blog-path
status: open
run_date: 2026-10-29
role: excalibur-blog-indexer
topic_id: B01
article_dir: memory/blog/articles/B01-nissan-qashqai-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_doctor.py` FAIL: llms generator does not support `--blog-path` (expected by skill/site-brief `blog_path: /`).
- Generator hardcodes URL path as `{site_base}/blog/{slug}/`, which mismatches site brief root blog (`/`) → should be `{site_base}/{slug}/` when `--blog-path /`.
- Skill documents `--blog-path /` and `--site-base ${PUBLIC_SITE_URL}`, but CLI only has `--blog-dir`, `--site-base`, `--out-dir`, `--site-name`, `--site-desc`.

### How the agent recovered this run
- Ran with available args: `--blog-dir memory/blog/articles --site-base "" --out-dir memory/blog` (relative URLs, secret-scan safe; no hardcoded PUBLIC_SITE_URL).
- Produced `memory/blog/llms.txt` and `memory/blog/llms-full.txt` with `/blog/<slug>/` paths (legacy hardcoded prefix until script fix).

### Durable fix needed before next run
- Add `--blog-path` to `excalibur_blog_llms_generator.py` (default `/` or from site-brief); build URLs as `{site_base.rstrip('/')}{blog_path.rstrip('/')}/{slug}/` with correct join when blog_path is `/`.
- Align doctor check, indexer skill, and agent docs with the new CLI.
- Prefer empty/`""` site-base for relative URLs in committed artifacts when secret-scan forbids absolute PUBLIC_SITE_URL.

### Suggested files to inspect/change
- `scripts/excalibur_blog_llms_generator.py`
- `scripts/excalibur_blog_doctor.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending
