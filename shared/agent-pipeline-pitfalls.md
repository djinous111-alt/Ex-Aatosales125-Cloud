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
- Пустой `{}` / «unexpected response format» от Wordstat на узком запросе — тот же recoverable quirk: parent + sibling phrases, не abort Scout.
- `--suggest-next` пропускает ID из `shared/published-articles.md` и локальных `memory/blog/articles/Bxx-*`.

## Research notes gate

- Подстрока `ai` внутри `reader_pain` / слова `pain` **не** делает тему technical: gate использует word-boundary и выкидывает meta-поля из scan blob.
- `accessed_at` можно давать колонкой таблицы (ISO-даты) или ≥5 строк `accessed_at: YYYY-MM-DD`.
- GitHub ≥3 URL обязателен только для technical topics.

## Commit / secrets env

- Перед любым `git commit` в Cloud: `eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export --empty-ok)"`.
- Placeholder `[REDACTED]` в `CLOUD_AGENT_*_SECRET_NAMES` ломает pre-commit (`invalid variable name`).
- `CATALOG_URL` / `TELEGRAM_URL` — публичные CTA; sanitize убирает их из scanned name lists, чтобы article CTA не блокировались.

## Writer / CTA

- В `article.html` запрещён литерал `href="[REDACTED]"`; CTA только из env `CATALOG_URL`/`TELEGRAM_URL`.
- Transcript/Read может показывать live URL как `[REDACTED]` — проверяй байты файла, не копируй из чата.
- Utility gate читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json`; пустые списки = skip check + warning, не silent zero-count BLOCK навсегда без markers.

## Cover

- Outfit только из `scene_hint` + `outfit_rule`; не хардкодить white hoodie.
- Токсичные стикеры банятся абстрактно (не вставляй запрещённые слова в prompt).
- Hero upload: retries catbox/0x0; при фейле keep existing `reference_url_hosted`, не подменяй face lock не-face WP cover.
- Предпочитай Kie direct API вместо sync MCP gpt-image-2 (timeout).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- Для commit-tracked `memory/blog/llms*.txt` используй `--site-base '[REDACTED]'`; live URL — на publish.

## Publish timeouts

- HTTP bootstrap trigger timeout ≥300s; WebFetch fallback wait ≥180s.
- После cleanup bootstrap повторный fetch даёт 404 — сначала live verify, не третий republish.
- `paramiko` ставится через `.cursor/cloud-agent-install.sh`.
