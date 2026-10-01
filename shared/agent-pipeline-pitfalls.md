# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → сразу `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (включая geo-qa). Не крутить retry typed enum.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- `CLOUD_AGENT_INJECTED_SECRET_NAMES` должен содержать только bash identifiers (`^[A-Za-z_][A-Za-z0-9_]*$`), не URL-значения. Перед commit фильтруй список, иначе pre-commit падает на `${!SECRET_NAME}`.
- Git push 401 (Invalid username or token) → Cloud GitHub write credentials; локальный commit ок, нужен human refresh token/App.

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
- `paramiko` обязателен для SSH publish (`requirements.txt` + `.cursor/cloud-agent-install.sh`).
- `site.env.local`: `SSH_ROOT=.` без кавычек. Publish `load_article()` снимает pragma allowlist и раскрывает `${CATALOG_URL}`/`[REDACTED]` только в payload.
- link-verify по умолчанию redact'ит env URL в JSON (`${CATALOG_URL}` и т.п.).

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
- Не hardcode white hoodie outfit lock: одежда из `blog-hero.json` `outfit_rule` + `scene_hint`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- MCP-KV `wordpress_*` может смотреть на чужой WP host. Dedupe/slug inventory только через `PUBLIC_SITE_URL/wp-json` (`scout_helper.py --live-wp-slugs`).

## Research gate

- `accessed_at` считается и из literal `accessed_at:` ключей, и из ISO-дат в markdown `source_table` с колонкой accessed_at.
- Секция `github_evidence` / слово github не делает тему technical сама по себе.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Для commit предпочитай `--site-base "[REDACTED]"`; live URL строки получают pragma allowlist автоматически.
