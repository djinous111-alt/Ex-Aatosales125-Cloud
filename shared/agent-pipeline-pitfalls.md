# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- В частности typed Task `excalibur-blog-geo-qa` часто отсутствует в Cloud enum → тот же `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md`.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Topics / AS pool

- Topic ID regex: `(?:AS|B)\d+` (Авто-Сейлс = `ASxx`, generic = `Bxx`). `today.py` / `scout_helper.py` обязаны видеть оба пула.
- Пока в `blog-topics.md` есть unpublished AS P0 — **не** запускай Scout за новыми темами; бери следующий AS из пула.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.
- Каноническая очередь инцидентов: `memory/pipeline-fix-queue.md` (не `pipeline-incident-queue.md`).

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research-serp.json`: site host из `PUBLIC_SITE_URL` редактируется скриптом перед записью; не коммить сырой SERP с live host как «секрет»-коллизию.

## Secret-scan vs CTA / schema

- Redaction в tool output / commit hook ≠ литерал `[REDACTED]` в `article.html` href. CTA бери из conversion-map/env.
- Schema/llms/publish artifacts: live URLs для WP, redacted/`allowlist` для git commit.
- `link-verify` FAIL на `href="[REDACTED]"`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA / utility

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: если `pain_markers_ru` / `outcome_markers_ru` пусты — checks skip (не always-BLOCK). Маркеры живут в `memory/brief/editorial-policy.json`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Hero host: catbox/0x0 fail → reuse existing `reference_url_hosted` (site face URL OK).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir`, не `--blog-path`. При drift doctor vs skill — смотри `--help`.
