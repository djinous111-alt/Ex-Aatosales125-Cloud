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
- `SSH_ROOT` по умолчанию `.`; legacy `SSH_PATH` → `SSH_ROOT`. Нужен пакет `paramiko` (cloud-agent-install / doctor).
- Рекомендуемый Cloud Secret: `SSH_ROOT=.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `editorial-policy.json` обязан содержать `pain_markers_ru` / `outcome_markers_ru`; пустые списки без defaults → ложный BLOCK для любой статьи. Script defaults: `resolve_marker_lists()` в `excalibur_blog_utility_gate.py`.
- Инсайт-блок: не начинать с ярлыка `TL;DR` или `Быстрый инсайт`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Cover prompt: **не** hardcode white hoodie. Outfit из `scene_hint` + `blog-hero.json` `outfit_rule`; всегда NO cap / NO hood (hoodie только если scene_hint явно просит).

## Scout

- Topic ID: `(?:AS|B)\d+`. Для Авто-Сейлс helper/`today.py` предлагают `ASxx`, не `B01`.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- WP MCP (`wordpress_get_posts`) может указывать на **чужой** сайт. Для каннибализации опирайся на `blog-topics.md` + `published-live-avtosales125.json` + `today.py` recent posts; не доверяй MCP без сверки site identity.
- Cloud Secrets names должны быть валидными bash identifiers; иначе `pre-commit.cursor` → `invalid variable name`. Workaround: ручной scan + временный empty `CLOUD_AGENT_INJECTED_SECRET_NAMES`; durable — переименовать secrets в Dashboard.

## Research

- `research_notes_gate` technical markers — word-boundary; префикс `AS*` = non-tech niche (не требовать github≥3 из-за «Японии»/поля `reader_pain`).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir`, не `--blog-path`.

## Schema

- Пиши schema через `python3 scripts/excalibur_blog_schema_write.py --article-dir …` (unicode_escape для Cloud Secret URL).
