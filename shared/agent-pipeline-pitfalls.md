# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types (в т.ч. **`excalibur-blog-geo-qa`**, research, writer, cover, schema, indexer, publish, fixer) → это **постоянный** enum gap, не one-off. Canonical path: `Task(generalPurpose)` + `.cursor/agents/<role>.md` + `.cursor/skills/<skill>/SKILL.md` на каждую роль отдельно.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Git commit / secrets env

- Перед любым `git commit` в Cloud: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` **в том же shell**, затем `git add` + `git commit`.
- Хелпер оставляет comma-separated `CLOUD_AGENT_*_SECRET_NAMES`, дропает non-identifier junk и public CTA/site URL names (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`, `WP_SITE_URL`, `WP_HOME`).
- Не склеивай имена пробелами — pre-commit hook падает с `invalid variable name`.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research_notes_gate.py -o`: bare filename → в `--article-dir`; путь с `/` → от корня репо. Prefer `-o research-notes-gate.json`.
- TECH_MARKERS в research gate — token/word-boundary match; `ai`∈`reader_pain` / `ии`∈`Японии` и heading `## github_evidence` сами по себе не делают тему technical.

## Writer / editorial markers

- `memory/brief/editorial-policy.json` обязан иметь non-empty `pain_markers_ru` (≥2) и `outcome_markers_ru` (≥3); doctor это проверяет.
- В `article.html` CTA href: раскрывай `CATALOG_URL` / `TELEGRAM_URL` из env; никогда не пиши буквальный `[REDACTED]` в href.

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
- llms generator CLI: `--blog-dir` / `--site-base` / `--out-dir` — **нет** `--blog-path`. Пустой `--site-base ""` даёт относительные `/blog/<slug>/` пути.
