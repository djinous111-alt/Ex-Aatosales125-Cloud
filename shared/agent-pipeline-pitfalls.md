# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата / topic IDs

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `today.py` / scout helper распознают topic id **`AS##` и `B##`**. Новые scout-карточки продолжают серию `B##`; AS — legacy pool.
- Перед выбором slug сверяй `EXCALIBUR_RECENT_WP_POSTS` / `EXCALIBUR_SLUG_LIVE_HIT`. `research_start` пишет `live_wp_slug` в context и при hit сидирует `wp_post_id` в meta — publish **обновляет** тот же post, не создаёт параллельный.

## Git / secrets scanner

- Cloud `pre-commit.cursor` падает на `invalid variable name`, если в `CLOUD_AGENT_*_SECRET_NAMES` есть `[REDACTED]` или другой non-identifier.
- Коммить через `scripts/excalibur_git.sh commit …` (фильтрует имена до `^[A-Za-z_][A-Za-z0-9_]*$`).
- URL/CTA, совпадающие с secret values: суффикс `// pragma: allowlist secret` (или HTML `<!-- pragma: allowlist secret -->`) на той же строке.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP trigger timeout до 300s; fallback ждёт `memory/webfetch-response.txt` до 300s и параллельно Poll WP REST по slug (soft-success). **Не** запускай второй bootstrap/curl trigger — иначе orphan media `-2`.
- Существующий live slug → update того же `post_id` (нормально). Cover alt: registry key `alt` предпочтительнее stale `article.meta.json` `cover_alt`.

## Writer / CTA / Fact Check Box

- CTA в `article.html`: сразу абсолютные URL из env/`conversion-map` (`CATALOG_URL`, `TELEGRAM_URL`). **Запрещены** литералы `href="[CATALOG_URL]"` / `[TELEGRAM_URL]`.
- На CTA-строках с secret-совпадающими URL — `<!-- pragma: allowlist secret -->`.
- `link_verify` помечает placeholder CTA как `cta_placeholder` fail (не как internal 404). Опция `--expand-cta-env` только для диагностики.
- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA / utility markers

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Если GEO QA / utility падает на pain/outcome: сначала проверь `memory/brief/editorial-policy.json` (`pain_markers_ru` / `outcome_markers_ru` + min thresholds). Пустые списки = skip-when-empty warning, не слепой рерайт статьи. Doctor проверяет непустые маркеры.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Research / notes gate

- `pain_solution_map`: gate считает markdown data-rows таблицы под секцией (маркеры `pain:` в каждой ячейке не обязательны).
- Technical topic определяется по полям topic card (h1/primary_query/…); слово `github` в секции `github_evidence` само по себе **не** делает тему technical.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: **`--blog-dir`**, не `--blog-path` (флага нет). Doctor проверяет `--blog-dir`.
