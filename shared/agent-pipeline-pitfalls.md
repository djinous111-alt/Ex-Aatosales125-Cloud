# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types (часто нет typed `excalibur-blog-geo-qa`) → сразу fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; один Task = одна роль.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research_notes_gate`: короткие TECH_MARKERS (`ai`/`ии`/`api`) — только whole-word; `workflow` убран из TECH_MARKERS; `search_intent` не сканируется на tech. Авто-темы не требуют GitHub.
- Source table: пиши `accessed_at: YYYY-MM-DD`; gate также засчитывает ISO-даты в колонке `accessed_at`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Secrets / pre-commit

- Имена Cloud Secrets — только bash-safe: `[A-Za-z_][A-Za-z0-9_]*` (без пробелов, `/`, URL-shaped имён).
- Pre-commit `invalid variable name` = platform hook разворачивает невалидное имя секрета. Перед commit: sanitize `CLOUD_AGENT_INJECTED_SECRET_NAMES` / проверь `python3 scripts/excalibur_blog_check_secret_names.py`. Durable: переименуй/удали URL-as-name в Cursor Dashboard Secrets.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Utility маркеры боли/результата/action — в `memory/brief/editorial-policy.json`; `utility_gate` имеет built-in DEFAULT, если списки пусты. Recommendation literals: `Делать:` / `Не делать:` / `чек-лист`.

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
