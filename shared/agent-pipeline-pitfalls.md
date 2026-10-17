# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types (в т.ч. `excalibur-blog-geo-qa`) → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; это нормальный путь, не blocker.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Git commit в Cloud: всегда `bash scripts/excalibur_git.sh …` — фильтрует non-identifier и public CTA/site names из `CLOUD_AGENT_INJECTED_SECRET_NAMES`.

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
- Жёсткий якорь: в Fact Check blockquote обязана быть фраза **«Материал проверен»**. Варьировать можно только источники/даты; «Проверка редакции» вместо якоря → BLOCK.
- Utility markers: `чеклист` (без дефиса) + императивы `сделайте`/`не делайте`/`проверьте`/`избегайте`/`используйте` из `recommendation_markers_ru`. «Делать/Не делать» и «чек-лист» не засчитываются.
- CTA href = live `CATALOG_URL`/`TELEGRAM_URL`/`MAX_URL` до GEO QA; коммит через `excalibur_git.sh`.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Gate `-o` для research-notes / human-voice: передавай **filename** (`research-notes-gate.json`), не repo-relative path (иначе nested duplicate под article_dir).

## Cover

- Default image path: `scripts/excalibur_blog_kie_gpt_image2_api.py` (async). Sync MCP `gpt-image-2` — legacy fallback (часто `-32001`).
- После split **всегда** `--inject-html`, если Registry имеет inline slots. Publish preflight: если HTML без `<figure class="inline-quad">` → `cover_quad_split.py --inject-html`.
- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным; prompt builder не должен перечислять оскорбительные слова в negative line (generic «no insulting slang»).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `--suggest-next` читает `memory/topics/live-reserved.json` (live B* + denylist + `next_forced_topic_id`). Перед append: `--check-slug`.

## Research

- Tech topic: `ai` внутри `reader_pain` ≠ technical; short ASCII markers требуют word boundary. Smoke: `python3 scripts/test_research_notes_gate_tech.py`.

## Schema

- Public marketing URLs в `schema.jsonld` / `sameAs`: либо per-line `pragma: allowlist secret`, либо commit через `excalibur_git.sh`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` + `--site-base` + `--out-dir` (не `--blog-path`). Doctor asserts `--blog-dir`.
