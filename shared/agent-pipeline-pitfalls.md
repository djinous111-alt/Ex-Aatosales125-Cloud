# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud часто **не** принимает typed Task `excalibur-blog-*` (в т.ч. `excalibur-blog-geo-qa`) → это **канонический fallback**, не инцидент: отдельный `Task(generalPurpose)` на каждую роль + `.cursor/agents/<role>.md` + `.cursor/skills/<skill>/SKILL.md`. Не открывай INC на каждый такой fallback.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research-notes-gate` считает литералы `accessed_at: YYYY-MM-DD` (≥5), не даты только в колонке таблицы.
- WebFetch 504/timeout → не блокер research: зафиксируй URL + WebSearch/альтернативный fetch; не выдумывай факты.

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
- llms generator CLI: только `--blog-dir` (не `--blog-path`); doctor это проверяет.
- `editorial-policy.json` обязан содержать `pain_markers_ru` / `outcome_markers_ru` (как в `human_voice_gate`). Пустые списки → utility gate **пропускает** check с WARN, а не BLOCK нулями.
- Brand catalog CTA: HTTP 5xx при `href == CATALOG_URL` → link-verify **soft-pass** (не content defect). Literal `[REDACTED]` в href → hard-fail.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `wordpress_get_posts` MCP может вернуть **чужой** сайт — не доверяй слепо. При неполном `shared/published-articles.md` после rebrand обязателен denylist slug/post_id из automation memory + live WP list из cron; не republish известные post_id.

## Git / secrets

- Коммиты в Cloud: `bash scripts/excalibur_git.sh …` — нормализует `CLOUD_AGENT_*_SECRET_NAMES` (только bash identifiers) и убирает публичные CTA/site имена из scan (`CATALOG_URL`, `TELEGRAM_URL`, `PUBLIC_SITE_URL`, `MAX_URL`, `WP_*`).
- Не коммить `href="[REDACTED]"` CTA; в article держи живые URL из env.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
