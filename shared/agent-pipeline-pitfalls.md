# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (один Task = одна роль).
- Если typed catalog есть частично, но `excalibur-blog-geo-qa` отсутствует → сразу `generalPurpose` с geo-qa agent+skill; не блокируй шаг.
- Перед Cloud `git commit`: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit ...` (нормализует space→comma secret names и выкидывает public URL names / non-identifiers).
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
- `memory/site.env.local` gitignored: auto-write из Cloud Secrets в `load_env` / install; канон `SSH_ROOT=.` (не полагайся только на `SSH_PATH`). Нужен пакет `paramiko` (requirements / cloud-agent-install / Dockerfile).
- Не оставляй `<img src="assets/...">` без реального локального файла — publish WARN и skip upload.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `utility_gate` читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json`; канон = `PAIN_MARKERS` / `OUTCOME_MARKERS` в `excalibur_blog_human_voice_gate.py`. Пустые списки → fail-soft warning, не BLOCK; не удаляй ключи из policy.
- Doctor/llms: флаг каталога статей — `--blog-dir`, не `--blog-path`. Для git `llms*.txt` — `--site-base ""`.
- Запрещён литерал `href="[REDACTED]"` в article.html; CTA = live env `CATALOG_URL`/`TELEGRAM_URL` (+ `<!-- pragma: allowlist secret -->`). conversion-map может быть уже заредакчен — не копируй placeholder.

## Scout / denylist

- `shared/wp-slug-denylist.json` обязателен в tip (LIVE WP slugs). Без файла doctor FAIL; scout перед выбором темы сверяет denylist + ledger, иначе риск дубля LIVE-поста.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.

## Research gate

- `technical_topic` определяется word-boundary маркерами по topic card (slug/h1/query). Подстрока `ai` внутри `raize` / `pain` не должна требовать GitHub evidence.

## Schema / pre-commit

- Absolute public URLs в `schema.jsonld` обязательны; перед commit используй `excalibur_blog_filter_commit_secret_env.sh` (исключает PUBLIC_SITE_URL/CATALOG_URL/TELEGRAM_URL/MAX_URL из scan). Не пиши `[REDACTED]` в JSON-LD.

## Cover / hero reference

- Pin `reference_url_hosted` на WordPress media (`avtosales125.ru`). Если `--force` catbox/0x0 fail — скрипт сохраняет существующий WP URL.
