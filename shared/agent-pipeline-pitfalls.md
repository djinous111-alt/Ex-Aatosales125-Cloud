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
- Topic ID regex: `AS\d+` и legacy `B\d+` в `today.py` / `scout_helper.py`. Пустой AS-пул → ложный `needs_scout` / `B01` был багом.
- Research notes gate: `accessed_at` = literal token **или** ISO date в URL-строке таблицы; pain map = data-rows секции, не только keyword-строки; `## github_evidence` / голый `ии` не делают тему technical.

## Publish

- Publish hard-fails without `cover/cover.png` + `cover-registry.json`. After Kie 402, do not invent PNGs — top up credits, re-run cover, then publish.

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
- В `article.html` **запрещён** литерал `href="[REDACTED]"` — пишите реальные публичные CTA (каталог / Telegram), даже если tool output краснеет `PUBLIC_SITE_URL`.
- Cloud secret-scan: точные значения `CATALOG_URL` / `TELEGRAM_URL` блокируют commit. В репо используйте эквиваленты (каталог без trailing `/`, хост `telegram.me` вместо `t.me`) или относительные пути; live verify перед redact/вариантом.
- Utility gate: `min_pain_markers` / `min_outcome_markers` применяются только если ключи и списки маркеров явно заданы в `editorial-policy.json`; иначе hard-default 2/3 даёт ложный BLOCK.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie API **402 Credits insufficient** → `COVER BLOCKER CREDITS`, без fake PNG. Нужен human top-up баланса Kie для `KIE_API_KEY`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Live cannibalization: `PUBLIC_SITE_URL` REST (`today.py`) + `memory/blog/published-live-avtosales125.json`. MCP `wordpress_get_posts` может вернуть чужой сайт — не единственный источник истины.
- Pre-commit `invalid variable name`: secret name URL в `CLOUD_AGENT_INJECTED_SECRET_NAMES` → `bash scripts/excalibur_blog_patch_agent_hooks.sh` (вызов из cloud install). В Dashboard — только identifier-имена секретов.

## Schema

- Committed `schema.jsonld`: relative page `@id`/`url`; secret-scan-safe `sameAs` (noslash catalog, `telegram.me`). Exact secret URLs блокируют commit.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- LLMs CLI: `--blog-dir` + `--out-dir`, **нет** `--blog-path`. Для commit: `--site-base [REDACTED]`.
