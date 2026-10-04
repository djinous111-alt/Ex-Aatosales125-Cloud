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
- `--suggest-next` учитывает ledger (`published`/`in_progress`) + `memory/blog/articles/Bxx-*`, не только карточки в `blog-topics.md`. После publish B-серии строка ledger обязательна.
- Cannibalization/dedupe: предпочитай `EXCALIBUR_RECENT_WP_POSTS` из today.py; `published-live-*.json` может отставать.

## Research notes gate

- `technical_topic` определяется word-boundary маркерами по topic card; имена полей вроде `reader_pain` / `github_evidence` не делают тему technical.
- Для non-tech (auto/legal/how-to без стека) GitHub ≥3 не обязателен; достаточно official docs + community.
- `accessed_at` считается и из колонки source_table, не только из `accessed_at:`.

## Secret scan / git commit

- Перед commit: `source scripts/sanitize_cloud_secret_names.sh` или `bash scripts/excalibur_git.sh commit ...` (install хукает shell rc).
- В Dashboard secret *names* — только bash-identifiers; URL как «имя» ломает pre-commit (`invalid variable name`).
- Публичные brand URL в артефактах для git: `[REDACTED]` / `[CATALOG_URL]` / `[TELEGRAM_URL]`; publish и link_verify сами expand из env.

## GEO QA / utility policy

- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru`, `outcome_markers_ru` и `min_*` (doctor проверяет). Не вычищать при rebrand/sync.
- CTA в HTML лучше писать токенами `[CATALOG_URL]`/`[TELEGRAM_URL]`; `link_verify` expand-ит env и redact-ит отчёт.

## Publish

- HTTP/nginx **504** после большого bootstrap ≠ hard fail: скрипт ждёт fallback дольше и делает REST soft-success по slug (`modified` свежий + `featured_media`). Не запускай второй bootstrap/curl параллельно — будут orphan media `-2`/`-3`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms/interlink/promotion: redact site base для git, restore/expand перед publish.
