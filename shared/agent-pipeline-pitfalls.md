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
- Large bootstrap (~7MB): HTTP timeout/WebFetch wait = 300s; SSH `banner_timeout=60`. После timeout — **один** trigger (WebFetch **или** curl), не оба. REST soft-success by slug — ок, если post уже published.

## Pre-commit / secret names

- Перед любым `git commit` в Cloud: `source scripts/sanitize_cloud_secret_names.sh` (фильтрует non-identifier токены в `CLOUD_AGENT_*_SECRET_NAMES`, иначе hook `invalid variable name`).
- Live marketing/site URLs в `article.html` CTA, `schema.jsonld`, `llms.txt`, `promotion-checklist.md` коммить с `pragma: allowlist secret` на тех же строках; не заменяй CTA на `[REDACTED]`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Utility gate требует `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json` (пустые списки = warning+skip, не hard BLOCK).

## Research

- `research_notes_gate` считает `accessed_at` и как литералы `accessed_at:`, и как ISO-даты в markdown table rows с URL (≥5).
- Слово `github` в секции `github_evidence` само по себе не делает `technical_topic` для авто/legal ниш.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `link-verify.json` с сырыми secret URL не коммитить — redacted report или pragma.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Hero rehost: catbox 412 / 0x0 503 при `--force` = soft-fail, если уже есть валидный `reference_url_hosted` (WP/CDN).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Cannibalization: `scout_helper --check-query` + `--check-slug` читает `memory/blog/published-live-*.json`; при пустом ledger live slug audit обязателен.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- Live URL строки в llms/promotion — с `pragma: allowlist secret`; generator добавляет pragma при live `--site-base`.
