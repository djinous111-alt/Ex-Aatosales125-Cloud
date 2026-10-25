# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **штатный** fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path. Это **не** incident на каждый run (пока generalPurpose работает).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Перед `git commit` в Cloud: `source scripts/excalibur_blog_sanitize_secret_names.sh` — иначе pre-commit может упасть на литерале `[REDACTED]` в `CLOUD_AGENT_*_SECRET_NAMES` (`${!SECRET_NAME}` → invalid variable name). Фильтруй до `^[A-Za-z_][A-Za-z0-9_]*$`, сохраняй comma-list.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research_notes_gate`: ≥5 `accessed_at:`; pain_solution_map rows с pain/solution/result; `technical_topic` смотрит только h1/slug/intent (не body notes с github/mcp/api).

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`. `--env-check` обязан иметь `paramiko_available: true` (install: `requirements.txt` / cloud-agent-install.sh).
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP trigger timeout/504 HTML ≠ fail если пост уже в WP: скрипт поллит REST по slug и reconstruct; **не republish** (orphan media).
- `schema.jsonld` с site/CTA URL: same-line `"x-excalibur-pragma": "pragma: allowlist secret"`.

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
- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` нет).

## Writer / utility markers

- `memory/brief/editorial-policy.json` должен держать `_markers_pinned: true` и non-empty `pain_markers_ru` / `outcome_markers_ru`. Utility gate при пустых списках использует built-in defaults + warning.
