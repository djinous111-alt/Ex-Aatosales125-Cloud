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

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.


## Publish HTTP timeout

- После SSH upload большой payload часто превышает HTTP wait. Скрипт: REST soft-success по slug **до** второго HTTP/curl.
- Параллельный curl во время первого PHP run → orphan media (`cover-2`) и local `cover/inline-*.png` srcs в контенте. Запрещено.

## Indexer / llms

- `excalibur_blog_llms_generator.py` принимает `--blog-dir`, не `--blog-path`.
- В `llms*.txt` / interlink report пиши `[PUBLIC_SITE_URL]`, не live secret URL (scripts rewrite http(s) bases).

## Cover image flow

- Default: Kie async (`excalibur_blog_kie_gpt_image2_api.py`). Sync MCP `gpt-image-2` — legacy (часто `-32001`).
- Prompt builder: без toxic example tokens и без hardcoded hoodie outfit; outfit из `scene_hint` + design code.
- Auto manifest hooks — из `primary_query`/H1 ниши, не SEO demo strings.

## Writer CTA / utility

- CTA из env `CATALOG_URL`/`TELEGRAM_URL` или unredacted conversion-map; запрещён `href="[REDACTED]"`.
- `pain_markers_ru` / `outcome_markers_ru` в editorial-policy обязательны для utility gate.

## Link-verify gov egress

- Soft-fail для FSA/elpts/gosuslugi/customs flake; канонический ЭПТС entrypoint из Cloud: `https://elpts.ru/`.

## Research gates

- `TECH_MARKERS` — token match по topic card; ultra-short `ai`/`ии` убраны (false-positive на «pain»/«аккредитации»).
- Wordstat: cluster-first; `totalCount`-only = low-result signal (как у Scout).

## Cloud Task enum

- Typed `excalibur-blog-*` часто нет в enum → `Task(generalPurpose)` per role = supported path.
