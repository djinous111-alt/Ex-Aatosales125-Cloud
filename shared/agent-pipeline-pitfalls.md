# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- `excalibur-blog-geo-qa` часто отсутствует в Cloud Task enum → сразу `Task(generalPurpose)` с geo-qa agent/skill (не blocker).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- `git commit` падает с `invalid variable name` на pre-commit secret scan → `bash scripts/excalibur_git.sh commit` (фильтрует невалидные `CLOUD_AGENT_*_SECRET_NAMES`).

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- DuckDuckGo HTML SERP часто SSL-timeout на Cloud egress → research_start fast-fail/circuit breaker; context всё равно пишется. Research собирает source_table через WebSearch/WebFetch (опция `--skip-serp`).
- `research_notes_gate` не считает тему technical только из‑за слова `github` в notes (`## github_evidence` обязателен); technical = маркеры в topic card.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `SSH_PATH` (Cloud) → `SSH_ROOT`; missing `site.env.local` bootstraps from process env.
- Нужен `paramiko` в runtime (`pip install --break-system-packages paramiko` при PEP 668).
- HTTP bootstrap timeout = 300s; при TimeoutError сначала REST-reconstruct by slug — **не** второй FALLBACK trigger если post уже LIVE.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA `href` только из `memory/brief/conversion-map.md` — **запрещён** литерал `href="[REDACTED]"` (link-verify FAIL).
- Recommendation markers: императив (`Сделайте` / `Не делайте` / `Проверьте`), не мягкие ярлыки `Делать:`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` в editorial-policy; пустые списки → checks skip (не false BLOCKER).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Sync MCP `gpt-image-2` `-32001` → сразу Kie API script (`excalibur_blog_kie_gpt_image2_api.py`), не retry loop.
- Outfit героя из `scene_hint` / `outfit_rule`, не hardcoded white hoodie.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- После reset ledger: LIVE denylist через `excalibur_blog_scout_helper.py --live-slugs` / `--live-search` + `PUBLIC_SITE_URL`, не только ledger.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` нет).
