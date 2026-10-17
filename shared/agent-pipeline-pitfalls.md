# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- source_table: даты как `accessed_at: YYYY-MM-DD`; pain_solution_map rows с pain/боль|solution/решение|result/результат.
- `research_notes_gate` technical_topic: только bounded markers (`\bai\b`, `make.com`); `reader_pain` на авто-теме ≠ technical.
- `research_start` редактирует host `PUBLIC_SITE_URL` в `research-serp.json` → `[REDACTED]` перед записью.

## Git / secret-scan

- `CLOUD_AGENT_INJECTED_SECRET_NAMES` иногда содержит URL вместо имени переменной → pre-commit `invalid variable name`.
- Коммить через `bash scripts/excalibur_git.sh commit …` (фильтр bash-safe identifiers). Не `--no-verify`.
- Альтернатива: `export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(python3 scripts/excalibur_filter_commit_secret_env.py)"`.
- Secret-scan workaround ≠ оставлять `$CATALOG_URL` placeholders в HTML.

## Writer / CTA

- CTA href = живые публичные URL из env `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL` до GEO QA.
- Literal `$CATALOG_URL` / `$TELEGRAM_URL` / `$MAX_URL` → link-verify FAIL; placeholders ≠ publish-ready.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `min_pain_markers` / `min_outcome_markers` применяются только если списки `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` непустые; иначе skip (не false-BLOCK).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Ниша: Авто-Сейлс (не Cursor/Make/AI).
- `--suggest-next` учитывает ledger + `memory/topics/live-reserved.json` + article dirs; не клонируй live-занятый B01/slug.
- `--check-slug` против reserved slugs.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (+ `--site-base`), **не** `--blog-path` (флага нет).

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP 504 / timeout: сразу WebFetch/curl `FALLBACK_TRIGGER_URL` → `memory/webfetch-response.txt`; wait **300s**; success только с literal `OK post=` (HTML 504/404 ≠ OK). Не republish; reconstruct via REST slug; не трогай foreign denylist IDs.
