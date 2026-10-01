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
- Research-notes gate: `accessed_at:` ≥5; строки `pain_solution_map` с pain/solution/result; `technical_topic` — word-boundary, не substring `ai`/`ии` в `reader_pain`.
- `research_start` редактирует host из `PUBLIC_SITE_URL` в `research-serp.json` → `[REDACTED]` перед записью.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен в `.cursor/cloud-agent-install.sh` / `requirements.txt`; без него SSH publish падает на import.
- HTTP trigger default timeout **300s**; при timeout скрипт пробует SSH CLI (`php8.3` → `php8.1` → `php`) до WebFetch wait (180s). Host bare `php` может быть 5.6.
- После cleanup bootstrap — один SSH-php retry, без слепого третьего republish.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` должны быть заполнены; пустые списки не должны false-BLOCK (мин. применяются только при non-empty lists).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Outfit из `cover.scene_hint` / `blog-hero` outfit_rule — не hardcode white hoodie. Предпочитай Kie async перед sync MCP (`-32001`).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Пустой local B-pool ≠ `B01` свободен. Смотри `memory/topics/live-wp-occupied-ids.json` + `scout_helper --suggest-next` (mapped live WP ids/slugs).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` / `--out-dir` / `--site-base` — **нет** `--blog-path`. Для memory/blog коммитов `--site-base '[REDACTED]'`.

## Git / secret-scan

- Перед commit: `eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export --empty-ok)"` (фильтрует invalid `${!SECRET_NAME}`).
- Для `schema.jsonld` с public brand URLs: `EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1` + sanitize (или `--exclude-public-url-secrets`).
