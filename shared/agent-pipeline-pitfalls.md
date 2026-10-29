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

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.


## Git / Cloud pre-commit

- Если `git commit` падает с `invalid variable name` на `${!SECRET_NAME}` / pre-commit.cursor: используй `scripts/excalibur_git.sh commit -m "..."` (фильтрует non-identifier имена в `CLOUD_AGENT_INJECTED_SECRET_NAMES` и один раз ретраит с пустым списком).
- Не регистрируй Cloud Secrets с URL-shaped именами — только bash identifiers (`[A-Za-z_][A-Za-z0-9_]*`).

## Research notes gate

- `technical_topic` — word-boundary маркеры; auto how-to не должен требовать 3× github.com из-за `ai` внутри `pain`.
- `accessed_at` = явный токен или ISO-дата в URL-строках source table.
- Official WebFetch 5xx → WebSearch snippet + secondary source + note in freshness_notes.

## Writer / GEO QA

- Инсайт-ярлык: только `Инсайт до ставки:` / `Инсайт до депозита:` — не `TL;DR` / не `Быстрый инсайт` (html-linter FAIL).
- CTA в git: `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}` — не live `t.me/...`.
- `editorial-policy.json` обязан держать `pain_markers_ru`, `outcome_markers_ru`, `_markers_pinned: true` (doctor FAIL если сняли при rebrand). Utility-gate имеет script fallback, но ключи не удалять.

## Cover

- `input_urls` только https; http→https нормализация в hero/prompt builder.
- MCP Internal Error / failCode=500 = recovery после confirmed fail + https, не blind duplicate create.
- Outfit из scene_hint/outfit_rule, не white-hoodie lock; toxic lemmas не цитировать в prompt.
- Нет угла бренда → `excalibur_blog_cover_corner_stamp.py` / `--stamp-corner-brand`, без второй генерации.

## Indexer / llms

- llms generator CLI: `--blog-dir`, **не** `--blog-path`. Doctor проверяет `--blog-dir`.

## Typed Task fallback

- Если typed `excalibur-blog-*` Task недоступен (в т.ч. geo-qa): `Task(generalPurpose)` + `.cursor/agents/<role>.md` + `.cursor/skills/<skill>/SKILL.md` — **first-class path**, не аварийный костыль.

