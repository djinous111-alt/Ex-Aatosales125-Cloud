# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Topic IDs / Scout / today

- Topic ID regex: `(?:AS|B)\d+` в `excalibur_blog_today.py` и `excalibur_blog_scout_helper.py`. Только `B\d+` → ложный `needs_scout` и предложение `B01` при живом AS-пуле.
- Scout `--suggest-next` предпочитает серию AS. Не предлагай cannibalizing AS01–AS07, если live WP уже закрыл эти темы.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research notes gate: `technical_topic` через word-boundary маркеры (`ai`∉`pain`, `ии`∉`сценарии`). Серия AS## не считается software-tech по notes body; github≥3 только для реальных tech-тем.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `cover/cover.png` + registry обязательны: скрипт hard-fail (в т.ч. `--dry-run`). Cascade Cover CREDITS → top-up Kie → Cover resume → Publish; **не** invent cover.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Telegram CTA в git: plaintext `@handle`, без `href` на `TELEGRAM_URL`/`t.me` secret value (pre-commit secret-scan). Не ставь `href="[REDACTED]"`.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: в `editorial-policy.json` обязаны быть non-empty `pain_markers_ru` / `outcome_markers_ru` (+ mins). Rebrand/sync иногда вычищает их → любой article BLOCK; doctor проверяет markers; empty-list skip в `utility_gate.py` — только warning.
- Recommendation markers: «Делать/Не делать» и «чек-лист» (с дефисом) **не** считаются. Нужны phrases из policy: `сделайте`, `не делайте`, `чеклист`, `проверьте`, `ориентир`, …
- Инсайт-блок не начинать с ярлыка `TL;DR` / `Быстрый инсайт`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie **402 Credits insufficient** → `❌ COVER BLOCKER CREDITS` (needs-human top-up). Оставь `quad-mcp-batch.json`, не invent cover. Resume: MCP/kie API → apply `--inject-html`.

## Scout / pre-commit

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `CLOUD_AGENT_INJECTED_SECRET_NAMES` — **comma**-separated. Non-identifier / redacted names skip (иначе `invalid variable name`). Канон hook: `scripts/pre-commit.cursor` (install копирует в agent-hooks).
- Marketing URL secrets (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, …) не сканируются hook’ом — иначе llms.txt/CTA не коммитятся.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` + `--out-dir`, **не** `--blog-path` (флага нет).
