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

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Перед темой сверь `shared/wp-slug-denylist.json` + live site search + ledger. WordPress MCP не sole source (может вернуть чужой хост).

## Research

- `research_notes_gate.py -o research-notes-gate.json` — **basename only** (или абсолютный / repo-relative multi-part от корня). Repo-relative путь как article-dir-relative создаёт nested `memory/...`.
- `technical_topic` — word-boundary; Japan/auto ниша не должна ложно срабатывать на `ai`/`ии`/`make`.
- `research_start` заменяет host из `PUBLIC_SITE_URL` на `[REDACTED]` в `research-serp.json` перед записью.

## Pre-commit / secrets

- Перед `git commit`: `source scripts/excalibur_blog_filter_secret_names.sh` (comma-separated bash-safe names). URL-shaped tokens в `CLOUD_AGENT_INJECTED_SECRET_NAMES` ломают `${!SECRET_NAME}`.
- Не коммить host из `PUBLIC_SITE_URL` в schema/llms/SERP; root-relative `/…` + absolutize на publish.

## Utility / GEO QA

- `editorial-policy.json` обязан содержать `pain_markers_ru` / `outcome_markers_ru`; иначе utility_gate раньше давал pain=0/outcome=0 BLOCK. Пустые списки теперь skip+warn.
- «Делать/Не делать» ≠ recommendation markers; нужны формы из `recommendation_markers_ru`.
- Link-verify percent-encode IRI (2GIS Cyrillic path) сам; Writer encode — бонус.

## Cover

- Outfit lock: charcoal softshell + cream crewneck, **не** hoodie. Auto quad-manifest не сидит SEO/Wordstat/hoodie stubs.
- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Schema

- Commit-safe: root-relative `@id`/`url`/`image`; публичный `sameAs` only. Publish absolutize для WP meta.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- LLMS CLI: `--blog-dir` (fs) + `--blog-path` (URL prefix, default `/blog`) + commit-safe `--site-base ""`.
