# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (постоянный Cloud path).
- Если typed catalog есть частично, но `excalibur-blog-geo-qa` отсутствует → сразу `generalPurpose` с geo-qa agent+skill; не блокируй шаг.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- `CLOUD_AGENT_INJECTED_SECRET_NAMES` должен содержать только bash identifiers. Если pre-commit падает на `invalid variable name`, отфильтруй non-identifier (URL-like) имена или перезапусти install (патчит hook).

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
- `memory/site.env.local` gitignored: при отсутствии собери из Cloud Secrets (`SSH_ROOT=.`, unquoted). Нужен пакет `paramiko` (requirements / cloud-agent-install / Dockerfile).
- WebFetch fallback wait = **300s** в `excalibur_blog_wp_publish.py`; не урезать до 120.
- `upsert_publish_ledger` пишет дату из `EXCALIBUR_RUN_DATE`, не из VM `date.today()`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` обязан иметь непустые `pain_markers_ru` / `outcome_markers_ru`; пустые списки → utility gate fail-fast «policy incomplete», не silent BLOCK по нулям.
- Запрещён `href="[REDACTED]"` в article.html; CTA = live env URL + `<!-- pragma: allowlist secret -->`.
- `link_verify` сам делает IRI→URI encode (кириллица в path 2GIS и т.п.); не валить gate на ascii codec.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- MCP gpt-image-2 `-32001` без url/task_id → сразу Kie API (`excalibur_blog_kie_gpt_image2_api.py`), не blind-retry sync MCP. Канон Cloud = Kie async first; sync MCP = optional probe.
- Outfit lock берётся из `blog-hero.json` / `scene_hint` (softshell/crewneck/…); **запрещён** hardcoded white hoodie.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Пустой `{}` от Wordstat ≠ 401: помечай EMPTY PAYLOAD и иди fallback primary → short how-to → brand/parent; не выдумывай показы.
- Korea export >2.0L и LIVE Cyrillic WP slugs: не доверяй только exact Latin kebab — `--check-slug` + REST search.
- AVTO SALES: кроме `--check-query` обязателен `--check-slug` против `shared/wp-slug-denylist.json` (при отсутствии — `--rebuild-denylist`).

## Research

- `research_notes_gate` определяет technical topic по word-boundary маркерам в topic card; substring `ai`/`ии` внутри `pain`/`японии` не должен требовать GitHub evidence.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (+ optional `--site-base`). Флага `--blog-path` нет. Для git-артефактов `memory/blog/llms*.txt` используй пустой `--site-base`.
