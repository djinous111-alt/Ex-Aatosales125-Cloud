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
- `editorial-policy.json` обязан содержать `pain_markers_ru` / `outcome_markers_ru` (sync с human_voice_gate); иначе utility gate ломается.
- CTA в git часто `[CATALOG_URL]` / `[TELEGRAM_URL]`; `link_verify` обязан expand из env и redact URL в JSON.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- LLMs generator CLI: только `--blog-dir` / `--out-dir` / `--site-base`. Флага `--blog-path` нет (doctor проверяет `--blog-dir`).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `--check-query` обязан учитывать `shared/known-wp-slugs.md` + ledger slugs + article dirs; ledger reset ≠ «можно повторить старый WP slug». Передавай `--slug`.

## Research

- `research_start` редact'ит site/catalog URL в `research-serp.json` перед записью.
- Tech gate: word-boundary маркеры по topic card, не substring `ai`/`ии` внутри `reader_pain`.
- `publication.pravo.gov.ru` 5xx → сразу URL из WebSearch/SERP, research не блокировать.

## Secrets / git

- Перед commit: `source scripts/sanitize_cloud_secret_names.sh` (URL-as-secret-name ломает `${!NAME}`).
- `git push` 401 / `Invalid username or token` / `gh auth status` invalid → **env/auth needs-human** (обновить Cloud GitHub credentials). Repo docs не чинят токен.

## Cover / Publish

- Hero host: catbox → 0x0 → SSH WP uploads; stale winter-cars/blueprint URL = re-host face lock.
- Publish expands `[CATALOG_URL]`/`[TELEGRAM_URL]`/`[REDACTED]` in memory only; SSH bootstrap cleanup retries banner/EOF.
- `paramiko` должен быть в install/requirements.