# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Typed `excalibur-blog-*` Task types (в т.ч. geo-qa) часто недоступны в Cloud API; **постоянный путь** — `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill. Enum из repo не регистрируется.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Topic IDs / preflight

- Topic IDs: `B\d+` и `AS\d+` (и вообще `[A-Z]+\d+`). `today.py` / `scout_helper` читают оба префикса; false `needs_scout` при AS-пуле = старый код.
- Doctor: llms generator flag = `--blog-dir` (не `--blog-path`).
- `editorial-policy.json`: `pain_markers_ru` / `outcome_markers_ru` length ≥ 3; пустые списки → utility gate всегда BLOCK. Doctor это проверяет.

## Commit / secrets

- Перед commit: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"`.
- `CLOUD_AGENT_INJECTED_SECRET_NAMES` — только bash identifiers, без URL-значений.
- Public CTA URL names (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, `CATALOG_URL`, `MAX_URL`, …) опускаются из scan: они легитимны в `schema.jsonld`.
- `link-verify.py` по умолчанию redact’ит site/CTA URLs в JSON.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat `wordstat_get_dynamics` + `PERIOD_MONTHLY`: `toDate` = последний день полного месяца, не mid-month `today_iso`.
- research-notes-gate: ≥5 `accessed_at` (YAML `accessed_at:` или ISO-даты в таблице с колонкой accessed_at); ≥3 строки `pain_solution_map`.

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
- llms generator для git: `--site-base ""` или `--relative` (URLs `/blog/<slug>/` без host). Не `--blog-path`.
- interlinker: `--redact-site-base` чтобы в JSON report не попал live host.
