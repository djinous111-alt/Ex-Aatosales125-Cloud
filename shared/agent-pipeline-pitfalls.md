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

## Indexer / llms

- `excalibur_blog_llms_generator.py` принимает `--blog-dir` и `--out-dir`, **не** `--blog-path`. Doctor проверяет актуальные флаги.

## Scout / denylist

- Перед выбором темы: `shared/wp-slug-denylist.json` + live `PUBLIC_SITE_URL` REST. WordPress MCP без сверки live URL — не источник denylist.

## Research gate

- Нужны литералы `accessed_at:` (≥5) и pain/solution/result в data-rows `pain_solution_map`.
- Не путать URL-значения с именами в `CLOUD_AGENT_INJECTED_SECRET_NAMES` (только bash identifiers).

## Writer / utility

- `editorial-policy.json` обязан иметь непустые `pain_markers_ru` / `outcome_markers_ru` до сдачи HTML.
- Не коммитить placeholder `href="[REDACTED]"` в `article.html`; CTA только из conversion-map. `link_verify` валит placeholder tokens.

## Cover

- Image flow: Kie async script first; sync MCP — fallback.
- `reference_url_hosted` только https (litterbox после catbox/0x0).
- Outfit из weather/topic; **NO hoodie** hardcode.
- Corner brand `avto-sales125.ru` штампуется split-скриптом, если модель не отрисовала.

## Publish

- `memory/site.env.local` auto-write из env; `SSH_ROOT=.`; нужен `paramiko` в runtime/install.
- Ledger-строки держать внутри markdown table (не после note-блока).
- HTTP trigger timeout → сразу curl/WebFetch `FALLBACK_TRIGGER_URL` в `memory/webfetch-response.txt`; скрипт ждёт **300s**. При отсутствии `OK post=` — REST by slug + reconstruct, **без** повторного bootstrap.

## Schema / pre-commit

- Absolute site/catalog/telegram URLs в `schema.jsonld` → commit-safe `[REDACTED]` / `schema.jsonld.runtime`; hydrate at publish from env. Same-line `pragma: allowlist secret` только если scanner allows.
- Перед `git commit` в Cloud: `eval "$(bash scripts/excalibur_blog_filter_secret_names.sh | sed …)"` или `scripts/excalibur_git.sh commit …` — отфильтровать невалидные имена из `CLOUD_AGENT_INJECTED_SECRET_NAMES`.
