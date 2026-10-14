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
- llms generator CLI: только `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- Commit-safe llms/schema: `--site-base '[REDACTED]'` или пост-редакция live URL → `[REDACTED]`; publish расширяет schema placeholders из env.

## Link verify / Publish

- `CATALOG_URL` + HTTP 5xx при точном совпадении href → soft-pass (warning), не blocker.
- Не-ASCII в path (2GIS и т.п.): `excalibur_blog_link_verify.py` percent-encode IRI перед запросом; writer лучше сразу писать percent-encoded href.
- SSH publish требует `paramiko` в cloud install (`.cursor/cloud-agent-install.sh` / Dockerfile).
- Committed `schema.jsonld` с `[REDACTED]` — норма; `expand_schema_redacted()` в publish подставляет live URL только в WP meta.

## Research

- Пустой `research-serp.json` (DuckDuckGo/HTML = 0) — soft-fail `research_start` + `empty_serp_fallback=true`. Research обязан идти в Cursor WebSearch/WebFetch.
- `research_notes_gate`: tech-topic только по полям topic card; `github_evidence` URL в notes не делает тему technical.

## Writer / Utility

- `editorial-policy.json` обязан держать непустые `pain_markers_ru` / `outcome_markers_ru` (doctor FAIL если пусто). Utility gate при пустых списках — WARN, не universal BLOCK.
- Recommendation markers точные: `чеклист` без дефиса; `чек-лист` не считается.

## Cover

- После `quad_manifest --merge` всегда перезаписывай defaults из `cover_scene_hint` темы + H2; `cover-prompts.json` должен совпадать с текущим slug topic_id.
- Hero rehost: при fail catbox/0x0 сохраняется existing `reference_url_hosted`; fallback `BLOG_HERO_REFERENCE_URL`.

## Secrets / Git

- `CLOUD_AGENT_INJECTED_SECRET_NAMES` — только valid bash identifiers (имена env), не URL.
- Коммиты: `bash scripts/excalibur_git.sh …`.

## GEO QA

- Ярлык `<b>TL;DR / Быстрый инсайт:</b>` в blockquote — разрешён writing contract; не FAIL.
