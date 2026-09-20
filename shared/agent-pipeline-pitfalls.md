# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud часто не принимает typed `excalibur-blog-*` (в т.ч. `excalibur-blog-geo-qa`) → это не blocker: `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path на **каждую** роль.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Git / secret-scan pre-commit

- `CLOUD_AGENT_INJECTED_SECRET_NAMES` — **только** comma-separated имена env vars (`CATALOG_URL,TELEGRAM_URL,…`), никогда URL-значения и никогда space-join.
- Невалидный идентификатор в списке → bash `${!SECRET_NAME}` → `invalid variable name` в `pre-commit.cursor` **и** `commit-msg.cursor`. Harden: `scripts/excalibur_blog_patch_cursor_precommit.sh` (вызывается из `.cursor/cloud-agent-install.sh`).
- В Dashboard Secrets: secret *name* = `CATALOG_URL`, не `https://…`.

## Writer / CTA href

- В `article.html` CTA `href` бери из env `CATALOG_URL` / `TELEGRAM_URL` (или публичный brand host без trailing slash, если env совпадает с secret-scan).
- **Запрещено** копировать `[REDACTED]` из `conversion-map.md` / `site-brief.md` в `href` (битые ссылки в RSS/Дзен).
- Публичные catalog / `t.me` / brand hosts в runtime HTML до publish — ок; secret-scan redaction — для committed publish artifacts с `PUBLIC_SITE_URL`, не для живых CTA в draft HTML.

## Research / notes gate

- `research-notes-gate` technical_topic смотрит **только** topic-card поля (h1/query/slug), word-boundary маркеры. Авто-ниша («из Японии») не должна требовать 3× github.com.
- Wordstat MCP: ответ `{}` или только `{"totalCount":N}` без списка фраз — не 401 и не fatal; cluster-first (широкий parent → узкий how-to), без выдуманных показов.

## Topics / utility markers

- В карточке темы `h1` **и** `primary_query` обязаны содержать utility-маркер (`как` / `чек-лист` / `сравнение` / …) согласованный с `search_intent`.
- Перед `needs_scout` / research_start: `python3 scripts/excalibur_blog_utility_gate.py --topic-id <AS|B id>` на unpublished P0.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
