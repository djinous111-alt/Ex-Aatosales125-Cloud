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

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.


## Topic IDs / Scout niche

- После ребренда pool использует `AS*`; `today.py` / `scout_helper.py` обязаны парсить `(?:AS|B)\d+`. Doctor проверяет dual-prefix + `--suggest-next`.
- Scout ниша = **Авто-Сейлс** (авто из Азии, растаможка, СВХ, доставка), не Cursor/n8n leftover.
- `needs_scout` / выбор темы: смотри `EXCALIBUR_RECENT_WP_POSTS` из today.py и полный `shared/published-articles.md`; не опирайся только на короткий локальный ledger.

## Research gates

- `research_notes_gate` определяет technical topic только по полям карточки темы (word-boundary для `ai`/`ии`/…); не сканирует `reader_pain` body на substring.
- `research_start` автоматически редактирует origin `PUBLIC_SITE_URL` в `research-serp.json` → `https://example.invalid` перед записью (secret-scan).

## CTA / secret-scan

- Writer: CTA URL из env через `excalibur_blog_cta_urls.py`; запрещено копировать `[REDACTED]` в href.
- Telegram CTA строка в HTML: `<!-- pragma: allowlist secret -->`.
- `schema.jsonld`: неизвестные ключи `__excalibur_pragma_N` = allowlist; publish strips их перед WP meta.
- Indexer/llms: default `--site-base` пустой → относительные `/blog/<slug>/`; не передавай live `PUBLIC_SITE_URL` в git-артефакты. CLI: `--blog-dir`, не `--blog-path`.

## Cover

- Prefer Kie async `scripts/excalibur_blog_kie_gpt_image2_api.py` (createTask→recordInfo) над долгим sync MCP `gpt-image-2`.
- После MCP `-32001` timeout — **не** blind-retry sync create; переходи на Kie API / async status.
- Outfit: `blog-hero.outfit_rule` / weather сцены, не hardcoded white hoodie.

## Utility gate

- `pain_markers_ru` / `outcome_markers_ru` должны быть в `editorial-policy.json`; если списки пустые — utility_gate **пропускает** pain/outcome check (не BLOCK).

## Publish HTTP

- Bootstrap trigger: urllib 120s → curl `--max-time 300` → WebFetch file wait. Не запускай второй publish параллельно с WebFetch (race).
