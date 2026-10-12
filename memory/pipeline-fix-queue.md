# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20261012-1715-research-notes-gate-false-tech
status: open
run_date: 2026-10-12
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-ili-kitaya-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` помечал non-tech авто-тему как `technical_topic=true` и требовал 3 GitHub URL.
- Причина: substring-match коротких маркеров (`ai`, `ии`) внутри обязательного поля `reader_pain` и обычных русских слов.
- Дополнительно gate считал только литералы `accessed_at:` и падал, если в `source_table` даты были без префикса ключа.

### How the agent recovered this run
- Починил `is_technical_topic`: word-boundary для маркеров длиной ≤3; скан lead notes укорочен, чтобы не цеплять секцию `github_evidence`.
- В `research-notes.md` проставил `accessed_at: 2026-10-12` в строках `source_table`.
- Повторный gate: PASS; `technical_topic=false`.
- Перед commit заменил `PUBLIC_SITE_URL` в `research-serp.json` на `OWN_SITE/...` (pre-commit secret scanner).
- Для pre-commit отфильтровал невалидные имена из `CLOUD_AGENT_INJECTED_SECRET_NAMES` (тот же класс проблемы, что у Scout).

### Durable fix needed before next run
- Закрепить word-boundary логику в gate + короткий regression-тест (fixture с `reader_pain` / авто-нишей без GitHub).
- В skill/research template явно писать даты source_table как `accessed_at: YYYY-MM-DD` либо научить gate считать колонку дат.
- `research_start` / serp writer должен сразу писать own-site как `OWN_SITE/...`, не полный `PUBLIC_SITE_URL`.
- Восстановить `scripts/excalibur_blog_filter_secret_names.py` (см. INC Scout).

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `scripts/excalibur_blog_research_start.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `agents/excalibur-blog-research.md`
- `scripts/excalibur_blog_filter_secret_names.py`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261012-1706-director-doctor-blog-path
status: open
run_date: 2026-10-12
role: excalibur-blog-director
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-ili-kitaya-2026
severity: medium
category: script

### What went wrong
- `python3 scripts/excalibur_blog_doctor.py` SUMMARY errors=1: FAIL «llms generator supports --blog-path».
- Actual CLI `scripts/excalibur_blog_llms_generator.py --help` exposes `--blog-dir` only (intentional after INC-1346 lineage).

### How the agent recovered this run
- Continued pipeline: Scout → utility gate PASS → research_start reserved B01; doctor stale check treated as non-blocking for article work; deferred durable fix to fixer.

### Durable fix needed before next run
- Update `scripts/excalibur_blog_doctor.py` to assert `--blog-dir` in llms generator help (not `--blog-path`).
- Ensure doctor/docs/skills stay aligned with indexer CLI.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_llms_generator.py`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261012-1704-scout-wp-mcp-wrong-site
status: open
run_date: 2026-10-12
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: env

### What went wrong
- MCP-KV `wordpress_get_posts` / `wordpress_search_posts` вернули посты с другого сайта (tamopro.ru), а не live блог Авто-Сейлс.
- Для анти-каннибализации это ложный сигнал: recent slugs Авто-Сейлс из брифа Cron не видны через MCP WP.
- Pre-commit secret scanner падал: в `CLOUD_AGENT_INJECTED_SECRET_NAMES` есть имя, невалидное как bash identifier (`${!SECRET_NAME}` → invalid variable name). Скрипт `scripts/excalibur_blog_filter_secret_names.py` в этом workspace отсутствует.

### How the agent recovered this run
- Анти-каннибализацию строил по списку live WP slugs из контекста прогона + `memory/topics/blog-topics.md` + ledger, без доверия к MCP WP как к источнику истины для Авто-Сейлс.
- Тему выбрал вне списка: `avto-iz-korei-ili-kitaya-2026` / primary `авто из кореи или китая`.
- Перед commit отфильтровал SECRET_NAMES до `^[A-Za-z_][A-Za-z0-9_]*$` через локальный python one-liner.

### Durable fix needed before next run
- Привязать MCP WordPress к PUBLIC_SITE_URL Авто-Сейлс либо явно документировать в scout skill: при mismatch домена WP MCP игнорировать MCP WP и использовать бриф/ledger/live slug list.
- Добавить в scout helper опциональный `--deny-slugs` / чтение deny-list из brief, чтобы helper ловил overlap с live WP даже при сброшенном ledger.
- Восстановить `scripts/excalibur_blog_filter_secret_names.py --export` в репо и/или почистить Dashboard secret names до валидных identifiers.

### Suggested files to inspect/change
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_filter_secret_names.py` (missing)
- Cursor Dashboard MCP / WordPress credentials for Авто-Сейлс

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
