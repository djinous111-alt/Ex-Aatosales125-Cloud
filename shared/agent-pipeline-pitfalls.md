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
- `--check-query` обязан сверять ещё и live WP (`EXCALIBUR_RECENT_WP_POSTS` / `PUBLIC_SITE_URL`), не только `blog-topics.md`.
- Пул тем: карточки **AS*** и **B***; today/scout helper обязаны видеть оба префикса. Next B-id не переиспользует номера с live WP/ledger.
- Не доверяй одному устаревшему `published-live-*.json` без live REST.

## Research

- Wordstat empty/`totalCount`-only: parent-кластер + явная пометка в notes; не выдумывай показы.
- Official customs.gov.ru / DVTU 504 → Alta-Soft / пресс-релизы / gazette mirrors.
- `research_notes_gate` tech markers = whole-word; `reader_pain` / русские слова с «ии» не делают тему technical.

## Writer / Git hygiene

- Action markers: «сделайте/не делайте» и «делать/не делать» оба валидны (`recommendation_markers_ru`).
- Публичные CTA (`t.me/...`, каталог): на строке `href` — `<!-- pragma: allowlist secret -->`, если URL совпадает с Cloud Secret value.
- Dashboard Secrets: имена = bash identifiers; **не** класть публичные URL как secret names/values для scanner.

## Doctor / Indexer CLI

- llms generator CLI = `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
