# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Typed `excalibur-blog-*` (включая geo-qa) в Cloud enum обычно недоступны → **нормальный путь** `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill; копируй промпт из `shared/pipeline-task-map.md`.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Перед `git commit`: `source scripts/sanitize_cloud_secret_names.sh` — иначе pre-commit падает на `invalid variable name`, если в `CLOUD_AGENT_*_SECRET_NAMES` попали URL/`[REDACTED]`.

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
- CTA в git: `[CATALOG_URL]` / `[TELEGRAM_URL]`; publish и link-verify резолвят из env. Не коммить живые значения этих secrets.

## Research

- `regulation.gov.ru` часто отдаёт 5xx — это soft failure. Fallback: `publication.pravo.gov.ru` + официальные operator pages + новости с id проекта regulation; не блокируй research на одном 503.

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
- Outfit героя = погода/тема из `scene_hint` + `blog-hero.json` outfit_rule; не hardcode white hoodie. Угол обложки: `avto-sales125.ru`, не Telegram.

## Indexer / doctor

- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` нет). Doctor проверяет актуальные флаги.
- `editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru`; иначе utility gate CONFIG ERROR.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
