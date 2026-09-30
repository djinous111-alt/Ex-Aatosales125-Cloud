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
- `paramiko` ставится в `.cursor/cloud-agent-install.sh`.
- HTTP trigger timeout по умолчанию 180s; при timeout сначала SSH CLI (`php8.1`/`php`), затем WebFetch wait. `EXCALIBUR_BLOG_PUBLISH_FORCE_SSH_CLI=yes` пропускает HTTP.
- Перед publish восстанови Telegram/catalog CTA из env; после — снова redact для commit.

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

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `excalibur_blog_llms_generator.py` CLI: `--blog-dir`, `--out-dir`, `--site-base` (флага `--blog-path` нет). Для git commit генерируй с `--commit-safe` / `https://SITE.example`, не с live `PUBLIC_SITE_URL`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `excalibur_blog_scout_helper.py --suggest-next` читает `memory/topics/live-wp-occupied-ids.json` и пропускает occupied_topic_ids; также распознаёт legacy `ASxx` карточки. Перед новой картой: `--check-query "…" --slug "…"`.
- Avoid delivery/avtovoz: смотри `avoid_slug_substrings` / `avoid_query_tokens` в live-wp-occupied-ids.json.

## Research

- `research_notes_gate`: TECH_MARKERS матчятся token-boundary по topic metadata (h1/query/slug), не по именам полей вроде `reader_pain`. Non-tech auto how-to не требует 3 GitHub URL.
- `pain_solution_map`: считаются строки markdown-таблицы в секции; English keywords не обязательны в каждой ячейке.

## CTA / secret-scan / commits

- В git-артефактах (`article.html`, schema sameAs при необходимости, llms.txt) CTA/Telegram/catalog/public site URL → `href="[REDACTED]"` или `https://SITE.example`. Live URL восстанавливай из env только перед publish/link-verify с live checks.
- Перед `git commit` в Cloud: `source scripts/excalibur_blog_filter_injected_secret_names.sh` (фильтрует `CLOUD_AGENT_INJECTED_SECRET_NAMES` до bash identifiers). Не используй `--no-verify` как первый шаг.
- `link_verify`: `[REDACTED]` placeholders пропускаются; non-ASCII URL path IRI-кодируется автоматически.
- Insight label: не `TL;DR` / `Быстрый инсайт` — используй `Коротко по делу`.

## Utility gate

- `pain_markers_ru` / `outcome_markers_ru` должны быть в `memory/brief/editorial-policy.json`. Если списки пустые — utility gate пропускает pain/outcome check (warning), а не BLOCK.
