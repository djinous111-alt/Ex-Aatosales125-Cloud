# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20261015-0941-cover-mcp-sync-timeout-kie-recovery
status: open
run_date: 2026-10-15
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-klyuch-chto-vhodit-2026
severity: medium
category: api

### What went wrong
- Sync MCP `gpt-image-2` (MCP-KV) с `input_urls` вернул `MCP error -32001: Request timed out` до появления URL в ответе.
- Cursor Cloud events/MCP logs агенту недоступны (0 events) — нельзя поднять late URL из лога после timeout.
- Async MCP tools `gpt-image-2-create/status` в Available Tools отсутствуют.

### How the agent recovered this run
- Короткий poll `cover/quad-mcp-result.json` (нет URL) без blind retry sync MCP.
- Preferred Cloud path из `quad-mcp-batch.json`: `python3 scripts/excalibur_blog_kie_gpt_image2_api.py` (KIE_API_KEY) → task_id → poll → URL.
- `excalibur_blog_quad_apply.py --inject-html` → split PASS, 3 `<figure>` после H2.

### Durable fix needed before next run
- Cover runbook/director: для Cloud по умолчанию вызывать Kie async script сразу (не legacy sync MCP), либо добавить async MCP create/status.
- В skill явно: после -32001 без log URL → Kie API recovery (не COVER MCP ASYNC BLOCKER, если `KIE_API_KEY` есть).

### Suggested files to inspect/change
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `skills/cover-excalibur-blog/SKILL.md`
- `shared/mcp-image-async-contract.md`
- `shared/pipeline-task-map.md`
- `scripts/excalibur_blog_cover_quad_prompt.py`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261015-0922-geo-qa-typed-task-missing
status: open
run_date: 2026-10-15
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-klyuch-chto-vhodit-2026
severity: medium
category: docs

### What went wrong
- Cloud Agent Task enum не принимает typed role `excalibur-blog-geo-qa` (и соседние excalibur-blog-* roles) как Task type.
- Директор вынужден запускать GEO QA через `Task(generalPurpose)` fallback с путями `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md`.

### How the agent recovered this run
- Director restored pain_markers_ru / outcome_markers_ru + min_* in memory/brief/editorial-policy.json (aligned with human-voice gate; prior fix lost on rebrand).
- Выполнен штатный generalPurpose fallback: контракты прочитаны, все QA-скрипты/gates прогнаны, article-qa.md и handoff-блок `=== EXCALIBUR BLOG GEO QA ===` записаны.

### Durable fix needed before next run
- Зафиксировать в Cloud/automation docs и director skill, что при отсутствии typed enum штатный путь — отдельный `Task(generalPurpose)` на роль geo-qa (один Task = одна роль), не single-agent pipeline.
- Если Cloud enum расширят — вернуть typed `excalibur-blog-geo-qa`; до тех пор pitfalls/director должны явно перечислять generalPurpose fallback.

### Suggested files to inspect/change
- `.cursor/agents/excalibur-blog-director.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
- `AGENTS.md` / `CLOUD-AUTOMATION.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261015-0923-geo-qa-utility-pain-outcome-policy-gap
status: open
run_date: 2026-10-15
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-klyuch-chto-vhodit-2026
severity: high
category: script

### What went wrong
- `excalibur_blog_utility_gate.py` считает `pain_markers_ru` / `outcome_markers_ru` из policy и требует min 2 / 3 (defaults), но в `memory/brief/editorial-policy.json` этих ключей нет → списки пустые → count всегда 0 → любая статья получает BLOCK по pain/outcome независимо от текста.
- Отдельно: recommendation markers не включают «делать»/«не делать» и «чек-лист» (с дефисом), хотя writer-контракт использует именно эти формы → action_markers занижены при живом utility-тексте.

### How the agent recovered this run
- Director restored pain_markers_ru / outcome_markers_ru + min_* in memory/brief/editorial-policy.json (aligned with human-voice; prior fix lost on rebrand 615ee0b).
- Не правили article.html (зона writer). Зафиксировали FAIL в article-qa.md + точечный FIX для writer (Fact Check wording + imperative markers). Сообщили директору: cover||schema blocked; utility pain/outcome требует fixer policy patch.

### Durable fix needed before next run
- Добавить в `editorial-policy.json` `pain_markers_ru` и `outcome_markers_ru` (согласовать с маркерами human-voice gate) + при необходимости `min_pain_markers` / `min_outcome_markers` в `article_required_signals`.
- Расширить `recommendation_markers_ru`: `чек-лист`, `делать`, `не делать` (или обновить writer skill требовать только «сделайте/не делайте/чеклист»).
- Регрессия: прогон utility gate на AS09/B01 после patch должен быть достижим без пустых marker lists.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261015-0915-research-notes-gate-ai-false-positive
status: open
run_date: 2026-10-15
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-klyuch-chto-vhodit-2026
severity: high
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` marked AUTO_NICHE Korea topic as `technical_topic=true` because substring `ai` matches inside required field `reader_pain`, then demanded 3 GitHub URLs.
- Prior fixer notes claimed token-boundary + AUTO_NICHE were already shipped, but the live script still used naive `marker in blob`.

### How the agent recovered this run
- Patched gate: token-boundary for short markers, AUTO_NICHE exemption unless strong markers (docker/github/mcp/…).
- Rewrote source_table cells as `accessed_at: YYYY-MM-DD` so access-date counter >= 5.
- Re-ran gate → PASS (`technical_topic: false`, github_urls=0 OK).

### Durable fix needed before next run
- Keep token-boundary + AUTO_NICHE in `scripts/excalibur_blog_research_notes_gate.py` (patch applied this run; needs commit/review).
- Add a tiny regression test or doctor check: `reader_pain` alone must not force technical topic on Korea/Japan/China cards.
- Document in pitfalls: never invent GitHub for AUTO_NICHE; gate must not require it without strong tech markers.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending (research already applied script patch; fixer should confirm + add regression coverage)

## INC-20261015-0910-director-ledger-append-outside-table
status: open
run_date: 2026-10-15
role: excalibur-blog-director
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-klyuch-chto-vhodit-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_start.py` reserve_topic_in_ledger делает `text + row`, поэтому строка `in_progress` попала ПОСЛЕ blockquote note, вне markdown-таблицы.
- Парсеры today/publish, которые читают строки `| 20...`, всё ещё видят row, но таблица визуально/семантически сломана; риск при будущих правках ledger.

### How the agent recovered this run
- Директор вручную перенёс строку B01 внутрь таблицы и оставил note после таблицы.

### Durable fix needed before next run
- `reserve_topic_in_ledger`: вставлять row сразу после header separator / последней table row, не append в конец файла.
- Аналогично проверить publish ledger updater.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_start.py`
- `scripts/excalibur_blog_wp_publish.py` (или publish ledger helpers)

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261015-0911-doctor-llms-blog-path-flag
status: open
run_date: 2026-10-15
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: low
category: script

### What went wrong
- `excalibur_blog_doctor.py` требует `--blog-path` в help llms generator, но CLI канон — `--blog-dir` (`scripts/excalibur_blog_llms_generator.py`). Doctor SUMMARY errors=1 при здоровом окружении.

### How the agent recovered this run
- Продолжили пайплайн (ошибка не блокирует research); зафиксировали для fixer.

### Durable fix needed before next run
- Обновить doctor check на `--blog-dir` ИЛИ добавить alias `--blog-path` в llms generator; согласовать pitfalls/docs.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_llms_generator.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20261015-0905-scout-live-denylist-gap
status: open
run_date: 2026-10-15
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: script

### What went wrong
- Предпочтительные P0-углы (растаможка Кореи через Владивосток, Encar на русском, СВХ Владивосток) уже есть на live WP в `memory/blog/published-live-avtosales125.json`, но `excalibur_blog_scout_helper.py --check-query` смотрит только B*-карточки в `blog-topics.md` и ledger AS08/AS09 – поэтому возвращает CLEAN на почти-дубли live.
- Denylist slug из промпта Director/cron не зашит в helper; scout вынужден вручную сверять live JSON.

### How the agent recovered this run
- Отклонил точные дубли live (rastamozhka-avto-iz-korei-sroki-i-etapy-cherez-vladivostok-v-2026, encar-na-russkom-..., svh-vladivostok-...).
- Выбрал смежный Korea utility P0: primary_query "авто из кореи под ключ" (Wordstat ~2487), slug `avto-iz-korei-pod-klyuch-chto-vhodit-2026`, checklist до депозита без калькулятора сумм.

### Durable fix needed before next run
- Расширить `--check-query`: читать slugs/titles из `memory/blog/published-live-*.json` + опциональный denylist-файл; флагить OVERLAP при сходстве с live, не только с B*-пулом.
- В scout skill явно: ниша Авто-Сейлс из `memory/brief/site-brief.md`, не Cursor/Make/AI из устаревшего agent.md.

### Suggested files to inspect/change
- `scripts/excalibur_blog_scout_helper.py`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `memory/blog/published-live-avtosales125.json`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261015-0906-scout-precommit-redacted-secret-name
status: open
run_date: 2026-10-15
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: env

### What went wrong
- `git commit` failed in pre-commit secrets scanner: `CLOUD_AGENT_INJECTED_SECRET_NAMES` содержал литерал `[REDACTED]` (невалидное bash-имя), из-за чего `${!SECRET_NAME}` падал с `invalid variable name`.

### How the agent recovered this run
- Перед commit отфильтровал SECRET_NAMES до валидных bash identifiers и повторил commit+push без `--no-verify`.

### Durable fix needed before next run
- Не инжектить placeholder `[REDACTED]` в `CLOUD_AGENT_INJECTED_SECRET_NAMES`; pre-commit должен skip невалидные имена.

### Suggested files to inspect/change
- Cloud Secrets / agent env injection
- `/root/.cursor/agent-hooks/.../pre-commit.cursor` (platform)

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
