# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- **Канон Cloud orchestration:** `Task(generalPurpose)` + `.cursor/agents/<role>.md` + `.cursor/skills/<skill>/SKILL.md` на каждую роль. Typed Task enum `excalibur-blog-*` в Cursor Cloud **не зарегистрирован** (platform limitation) — не блокируй пайплайн ожиданием typed types.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research notes: в `source_table` достаточно ISO-дат `YYYY-MM-DD` в ячейках (gate считает их как access dates); в `pain_solution_map` — обычные `|`-rows таблицы (не обязательно слова pain/solution в каждой клетке).
- `technical_topic` в research-notes-gate смотрит только h1/slug/intent темы — секция `github_evidence` / упоминание MCP Wordstat сами по себе tech-флаг не включают.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- **`SSH_ROOT=.`** — канон для этого WP SSH account (login cwd). Если unset, publish-скрипт теперь сам трактует root как `.`; всё равно задай Cloud Secret `SSH_ROOT=.`.
- Нужен **paramiko** (`pip`/`requirements.txt` или `python3-paramiko` через apt). Doctor WARN/FAIL без модуля; cloud install ставит paramiko.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` обязательны (fail-fast в doctor + utility_gate). Recommendation markers — **точные** формы из policy (`сделайте` / `не делайте`, не «делать»).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Link-verify: при HEAD 502/503/504 скрипт делает GET-fallback (CDN вроде kolesa.kz часто ломает только HEAD).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie `402 Credits insufficient` → **не ретраи** createTask; cover skill **§4b emergency**: GenerateImage + reference → LANCZOS 2048×1152 → quad split/inject. Top-up Kie credits = human.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `--suggest-next` / today.py учитывают **ledger + article dirs + live WP + AS*/B* pool**. Не бери B01/B02 без сверки с WP, если на сайте уже есть контент эпохи AS*/B*. При пустом B* и живом WP — `EXCALIBUR_TOPIC_ID_FLOOR=B0N` или ручной ID.
- `--check-query` сверяет overlap и с live WP slugs/titles.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` / `--site-base` / `--out-dir`. Флага `--blog-path` нет — сверяй `--help`, не копируй устаревший shell из skill дословно.
- Doctor preflight проверяет `--blog-dir` (не `--blog-path`).
