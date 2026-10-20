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
- llms generator: `--blog-dir` + `--out-dir` (не `--blog-path`).


## Indexer / doctor CLI

- llms generator: только `--blog-dir` + `--out-dir` (+ `--site-base`). Флаг `--blog-path` удалён; doctor и skill examples не должны его требовать.

## Cover

- Не запускай `cover_quad_prompt.py` в том же parallel tool-batch, что и ручной rewrite `quad-manifest.json`.
- Outfit lock Cloud: softshell + crewneck, **не** hoodie. SEO/Wordstat stub в cover_hook/scene_hint → discard, не Kie.
- `quad_manifest.py` / `validate_outfit_lock()` блокируют stub до createTask.

## CTA / secret-scan

- QA: hydrate CTA из env; commit может `[REDACTED]`; publish hydrates.
- `CLOUD_AGENT_INJECTED_SECRET_NAMES` может содержать не-идентификаторы (`[REDACTED]`, URL) → filter `^[A-Za-z_][A-Za-z0-9_]*$` (pre-commit.cursor + `scripts/excalibur_blog_filter_secret_names.sh`).

## Scout

- Ниша только AVTO SALES (`site-brief.md`). Cursor/Make skill drift — игнорировать.
- Без `shared/wp-slug-denylist.json` — blocker; helper `--check-query` читает denylist.

## Writer / utility

- Держи `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json`; пустые списки в gate = skip, не false-BLOCK.
- Recommendation = глаголы из `recommendation_markers_ru`, не только «Делать:».
