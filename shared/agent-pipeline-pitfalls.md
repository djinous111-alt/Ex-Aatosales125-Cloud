# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud **часто не принимает** typed `excalibur-blog-*` (в т.ч. `excalibur-blog-geo-qa`) как Task types → **поддерживаемый путь**: отдельный `Task(generalPurpose)` на каждую роль + `.cursor/agents/<role>.md` + `.cursor/skills/<skill>/SKILL.md`. Это не workaround, а штатный Cloud fallback (см. `AGENTS.md`, `shared/pipeline-task-map.md`).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Git / SECRET_NAMES

- Коммиты через `bash scripts/excalibur_git.sh …`: скрипт чистит `CLOUD_AGENT_INJECTED_SECRET_NAMES` (только bash identifiers) и исключает public URL names (`PUBLIC_SITE_URL`, `WP_*`, `CATALOG_URL`, `TELEGRAM_URL`) из secret-scan.
- Plain `git commit` без фильтра падает на URL-shaped «именах» (`invalid variable name`) или переписывает CTA в literal `[REDACTED]`.
- Никогда не коммитить `href="[REDACTED]"` в `article.html` — восстанавливай live `CATALOG_URL`/`TELEGRAM_URL`.

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
- Cloud install ставит `paramiko` и при отсутствии `memory/site.env.local` бутстрапит его из env (`SSH_ROOT=.` по умолчанию). Файл gitignored — не коммитить.
- Brand catalog CTA: если `href == CATALOG_URL` и host отвечает HTTP 5xx/egress flake — `link_verify` soft-pass (не content defect). Literal `[REDACTED]` — hard FAIL.

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

## Scout / Research — Wordstat

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- HTTP 500 (`code:13 Internal`) от Yandex Search API — **не fatal**. Retry 1–2× с backoff; при устойчивом 500: historical/scout fallback с явной меткой non-live + WebSearch SERP; пиши `⚠️ WORDSTAT API WARNING` (не выдумывай live-показы). 401 → `⚠️ WORDSTAT AUTH WARNING`.

## Writer / utility gate

- `excalibur_blog_utility_gate.py` требует `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json`. Если массивы отсутствуют — WARN (не вечный BLOCK с нулями); восстанови списки из human_voice_gate markers.

## Indexer / doctor

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `excalibur_blog_llms_generator.py` принимает только `--blog-dir` (флага `--blog-path` нет). Doctor проверяет `--blog-dir`.
