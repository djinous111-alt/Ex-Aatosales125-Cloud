# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **сразу** fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; не ретраить typed name.
- Typed `excalibur-blog-geo-qa` часто отсутствует → generalPurpose с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md` — канонический путь.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- WebFetch 403/504/timeout на FSA/NAMI/ELPTS/Drive2 → WebSearch + зеркала; не блокируй research-notes.
- `source_table`: в ячейках буквально `accessed_at: YYYY-MM-DD`.
- `technical_topic` в research-notes gate — только по topic card (word-boundary маркеры); non-tech → `github_evidence: N/A` ок.

## Topic IDs (Scout / today)

- Парсер topic_id: `[A-Z]+\d+` (AS\* и B\*). Не игнорировать AS01–ASxx в пуле.
- Перед commit: `source scripts/sanitize_cloud_secret_names.sh`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `git push` Invalid username/token → stop retry spam; incident needs-human (Dashboard GitHub token). Local commits ок.

## Writer / Fact Check Box / CTA

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: никогда placeholder href. Если env scrubbed — собери URL из `catalog_host` / `telegram_handle` в site-brief.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` обязан содержать `pain_markers_ru` / `outcome_markers_ru` (согласованы с human-voice gate); иначе utility gate ложно BLOCK.
- Link-verify: soft-fail для social timeouts и official hosts elpts/fsa/nami (403/SSL timeout) — не выкидывать URL из статьи.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Ниша Avto-Sales (авто из Азии), не AI/n8n примеры из старых промптов.

## Indexer / Doctor

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (не `--blog-path`). Doctor проверяет эти флаги.