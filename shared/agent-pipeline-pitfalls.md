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
- `research_notes_gate` technical_topic: маркеры `ai`/`ии` должны матчиться по границам слова. Substring ломает авто-темы («японии», `reader_pain`) и требует ложный GitHub evidence – см. INC-20261021-0915.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Utility gate: в `editorial-policy.json` обязательны `pain_markers_ru` и `outcome_markers_ru`; пустые списки раньше давали вечный BLOCK (см. INC-20261021-0914).
- GEO QA перед link-verify hydrates CTA `[REDACTED]` из `PUBLIC_SITE_URL` и `TELEGRAM_URL`.
- Инсайт-блок не должен начинаться с `TL;DR` или `Быстрый инсайт`.

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie i2i: `reference_url_hosted` / `input_urls` только **https** (http → risk `failCode=500`); hero script и kie API делают upgrade + один retry.
- Outfit lock: charcoal softshell + cream crewneck; hoodie defaults запрещены (`validate_outfit_lock`).
- `quad_manifest --merge` / visual_manifest не должны оставлять SEO-stub (`SEO-текст`, `Wordstat + ноутбук`, худи) на авто-темах.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Канон denylist: `shared/wp-slug-denylist.json` + `EXCALIBUR_RECENT_WP_POSTS`; helper: `--check-slug` / `--suggest-next`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator flags: `--blog-dir` + `--out-dir` (не `--blog-path`). Для commit: `--site-base ""` (relative URLs).

## Publish 504

- nginx edge ~120s может 504 на bootstrap PHP; после `FALLBACK_TRIGGER_URL` сразу WebFetch/curl → `memory/webfetch-response.txt`.
- Скрипт REST-probe по slug и reconstruct result/ledger без republish, если live OK.
- Publish hydrates `[REDACTED]` CTA/schema из env перед SSH.

## Pre-commit secret names

- Если `CLOUD_AGENT_INJECTED_SECRET_NAMES` содержит literal `[REDACTED]` → `invalid variable name`.
- Перед commit: `source scripts/excalibur_blog_filter_secret_names.sh` (comma-separated identifiers only).
