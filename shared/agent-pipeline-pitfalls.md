# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (в т.ч. `excalibur-blog-geo-qa`).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research gate: `-o research-notes-gate.json` (basename). Non-tech (СВХ/авто) → `github_evidence: N/A`, не gist-заглушки.
- Tech markers в gate — word-boundary; «ai»/«ии»/«rag» внутри обычных слов не делают тему technical.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root: рекомендуй `SSH_ROOT=.`; скрипт пробует `.` при ENOENT. Нужен **paramiko**.
- HTTP trigger timeout=300s. При timeout **не** жди webfetch 120s в том же процессе: `--recover-from-rest` (если пост есть) или WebFetch + `--resume-from-webfetch`. Не второй bootstrap.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: `shared/public-cta.json` / env `CATALOG_URL`/`TELEGRAM_URL`; запрет literal `[REDACTED]` в href.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` должны быть в editorial-policy; пустые списки → fail-open warning.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie `402` credits / MCP fail → Cursor `GenerateImage` + `quad_apply --local-canvas` (ONE canvas). Credits top-up — human.
- Outfit из scene_hint/blog-hero, не hardcode white hoodie.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Helper парсит `## AS\\d+` и `## B\\d+`. Сверяй `EXCALIBUR_RECENT_WP_POSTS` из today.py даже при пустом ledger.
- Ниша AVTO SALES — не Cursor/n8n/Make.
- Wordstat: последовательные вызовы надёжнее batch.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` (не `--blog-path`); опционально `--url-mode relative|absolute`.
