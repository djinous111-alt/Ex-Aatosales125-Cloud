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

## Scout / topic IDs

- Topic id regex: `AS\d+|B\d+` (AVTO SALES + legacy). `scout_helper` / `today.py` обязаны видеть оба префикса; `Total topics in pool: 0` при AS-пуле = баг старого кода.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal; не выдумывай impressions.

## Research

- `research_notes_gate` technical_topic смотрит только topic card (h1/primary_query/…), не тело notes / секцию `github_evidence`.
- Self-site URL (`PUBLIC_SITE_URL`) не коммить в serp/ledger — path-only или placeholder.

## Writer / utility policy

- `memory/brief/editorial-policy.json` обязан держать непустые `pain_markers_ru` и `outcome_markers_ru`. Пустые списки → utility gate WARN+skip (не false-BLOCK), но doctor FAIL.

## Schema / secrets

- Публичные brand URL в `schema.jsonld` → `"_comment": "pragma: allowlist secret"` на той же строке. Publish strip'ает `_comment` перед WP meta.
- Перед commit: `export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(bash scripts/excalibur_blog_filter_secret_names.sh)"` (сырые URL в env ломают `${!name}`).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Commit-safe llms/interlink: `--site-base ""` (relative `/blog/<slug>/`). CLI flag — `--blog-dir`, не `--blog-path`. Не коммить absolute `$PUBLIC_SITE_URL` в llms/interlink-report.

## Publish deps

- `paramiko` обязателен для SSH publish; bake в Dockerfile + `cloud-agent-install.sh`. Preflight: `python3 -c 'import paramiko'`.
