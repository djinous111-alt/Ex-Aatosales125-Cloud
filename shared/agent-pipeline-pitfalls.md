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
- Cloud Secrets часто дают `SSH_PATH`, не `SSH_ROOT`: `load_env()` мапит `SSH_PATH`→`SSH_ROOT` если ROOT пуст. Предпочтительно держать `SSH_ROOT=.`.
- `paramiko` обязателен для SSH publish — ставится из `requirements.txt` / `.cursor/cloud-agent-install.sh`.
- `schema.jsonld` коммить только с `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}`; publish гидратит placeholders в payload.

## Git / pre-commit secrets

- Перед `git commit` фильтруй `CLOUD_AGENT_INJECTED_SECRET_NAMES` / `CLOUD_AGENT_ALL_SECRET_NAMES` до bash-идентификаторов: `bash scripts/excalibur_git.sh commit …` или `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"`.
- Иначе pre-commit.cursor падает на `${!SECRET_NAME}` с `invalid variable name`, если в списке URL/пустой токен.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate считает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json` (должны совпадать с human-voice). Если списки пусты — gate падает обратно на константы `human_voice_gate`. Инсайт-блок не начинать с `TL;DR` / `Быстрый инсайт`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Outfit: не хардкодить white hoodie; `excalibur_blog_cover_quad_prompt.py` берёт `outfit_rule` из `memory/cover/blog-hero.json` + scene_hint.
- Corner brand `avto-sales125.ru`: после split `excalibur_blog_cover_quad_split.py` ставит navy pill stamp из `cover_corner_brand.text`.

## Research

- `research_notes_gate` technical markers — word-boundary; «комплектации» / `reader_pain` не делают AVTO SALES тему technical.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Topic IDs: `(?:AS|B)\d+` в `scout_helper` / `today.py`. На AVTO SALES pool `--suggest-next` должен вернуть `AS##`, не фейковый `B01`. Всегда сверяй LIVE REST + AS cards.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `excalibur_blog_llms_generator.py --blog-path /` (из site-brief): URLs как `/{slug}/`, не `/blog/{slug}/`.
