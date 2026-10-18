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
- Utility gate читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json`; без списков count=0 → ложный BLOCK. Держи паритет с human-voice `PAIN_MARKERS`/`OUTCOME_MARKERS`.
- Literal `href="[REDACTED]"` в `article.html` = link-verify blocker (`PUBLIC_SITE_URL/[REDACTED]` → 404). CTA URL — живые HTTPS из brief/env; `[REDACTED]` только в отчётах.
- `edata.customs.ru` / `customs.gov.ru` SSL handshake timeout → soft external failure в link-verify (warning, не publish blocker); URL официального ЛК оставляй.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Research

- `customs.gov.ru` / `edata.customs.ru` 5xx/504: surrogate official (ConsultantPlus / отраслевые гайды с цитатой приказа) + note в source_table; не блокируй research.
- Research-notes tech detection — word-boundary; авто/таможня не tech → не требуй ≥3 github.com URL.
- В source_table: `accessed_at: YYYY-MM-DD`; в pain_solution_map — слова `боль`/`решение`/`результат`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- WP MCP может смотреть на чужой хост: denylist live slugs бери из `memory/topics/live-reserved.json` + `site:<live-host>`, не только из MCP.
- `excalibur_blog_scout_helper.py --suggest-next` читает `live-reserved.json` (`reserved_topic_ids`, `next_forced_topic_id`).

## Git / Secrets Scanner

- Если `pre-commit.cursor` Secrets Scanner падает с `invalid variable name` / `SECRET_NAME` (невалидный bash-идентификатор в env) — допустим одноразовый `git commit --no-verify` после ручной проверки staged-файлов на сырые токены + incident в queue. Durable fix имён секретов — в Cloud Dashboard (human).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (не `--blog-path`).
