# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **сразу** fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (особенно geo-qa: не ретрай typed).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Git / pre-commit secrets

- `pre-commit.cursor` падает с `invalid variable name`, если в `CLOUD_AGENT_INJECTED_SECRET_NAMES` есть имя не из `[A-Za-z_][A-Za-z0-9_]*`.
- Перед commit: `source scripts/excalibur_blog_filter_commit_secret_env.sh` или `scripts/excalibur_git.sh commit ...` (не `--no-verify`).
- Корневой fix: переименовать Dashboard secret в bash-safe идентификатор (needs-human).

## Doctor / Indexer CLI

- llms generator: `--blog-dir` + `--out-dir` (+ `--site-base`). Флаг `--blog-path` устарел; doctor проверяет актуальные флаги.

## Research / TECH_MARKERS

- `research_notes_gate` матчит tech-маркеры по word-boundary, не substring (`reader_pain` / `объявлении` ≠ tech).
- Регрессия: `python3 scripts/excalibur_blog_research_notes_gate.py --self-test`.

## Editorial markers

- `memory/brief/editorial-policy.json` обязан иметь непустые `pain_markers_ru` / `outcome_markers_ru` и `_markers_pinned: true`.
- Doctor и utility gate → POLICY BLOCK при wipe; не списывать на «слабую статью».

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
- Human-voice soft metric `exactly_five_lists` считает только `<ol>` с ровно 5 `<li>` (не ≥5).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
