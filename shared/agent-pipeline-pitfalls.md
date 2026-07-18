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
- Topic ID pool: `AS##` (Авто-Сейлс) и legacy `B##`. `today.py` / `scout_helper` парсят `(?:AS|B)\d+`; P0 с utility FAIL soft-skip.
- Wordstat: составные secondary (3+ слов/стран) бей по частям; `totalCount`-only = low-result, не fatal.
- Research-notes gate: короткие TECH_MARKERS (`ai`/`ии`) — word-boundary; «Японии» ≠ technical. Smoke: `python3 scripts/excalibur_blog_research_notes_gate.py --self-test`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен для SSH publish (ставится в `.cursor/cloud-agent-install.sh`). Preflight: `python3 -c "import paramiko"`.
- HTTP trigger timeout/504 → SSH PHP exec (`SSH_PHP_BIN`, default `php8.2`) → затем WebFetch wait.

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
- Предпочтительный путь cover: `KIE_API_KEY` + `excalibur_blog_kie_gpt_image2_api.py` (async). Sync MCP `gpt-image-2` 2K может таймаутить без `task_id`.
- Fallback `z-image`: только ONE canvas 16:9; t2i без face-lock; кириллица на панелях может быть искажена.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-path` = alias `--blog-dir` (doctor check).
- Interlinker: для коммита передавай `--site-base [REDACTED]`; live URL в JSON-отчёте автоматически редactится; HTML links остаются относительными `/blog/<slug>/`.
