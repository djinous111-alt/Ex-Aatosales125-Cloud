# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **штатный** fallback: отдельный `Task(generalPurpose)` на каждую роль + `.cursor/agents/<role>.md` + `.cursor/skills/<skill>/SKILL.md` (один Task = одна роль). Включая `geo-qa`, `cover`, `schema`, `indexer`, `publish`, `fixer`.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research-notes gate: short tech markers (`ai`, `ии`, `make`) только с token-boundary; AUTO_NICHE (Корея/Япония/Китай, Encar, СВХ…) не требует GitHub, пока нет strong markers (`docker`, `github`, `mcp`, …). Не выдумывать GitHub под авто-нишу.
- В `source_table` пиши ячейки как `accessed_at: YYYY-MM-DD` (счётчик gate ищет `accessed_at:`), не голую дату.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- `research_start` / publish ledger updater обязаны вставлять row **внутрь** markdown-таблицы (после последней table row), не append после blockquote note.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Cloud WebFetch Fallback: скрипт печатает `FALLBACK_TRIGGER_URL` сразу; агент стартует `curl -fsS --max-time 300 "$URL" > memory/webfetch-response.txt` **сразу** (не ждать истечения local urlopen). Скрипт ждёт файл до **300s**.

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
- Sync MCP `gpt-image-2` → `-32001` без URL/логов: **не** blind retry. Если есть `KIE_API_KEY` → `python3 scripts/excalibur_blog_kie_gpt_image2_api.py --article-dir …` (preferred Cloud recovery). `COVER MCP ASYNC BLOCKER` только если нет async MCP tools **и** нет Kie key.

## Scout / Wordstat

- Ниша = Авто-Сейлс (`memory/brief/site-brief.md`: JP/KR/CN, растаможка, СВХ), не Cursor/Make/AI из устаревших промптов.
- `--check-query` смотрит blog-topics **и** `memory/blog/published-live-*.json` (+ optional denylist). Live slug overlap = OVERLAP.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal / soft-pass, не fatal.

## Indexer / llms / secrets

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms CLI: `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- Committed `memory/blog/llms*.txt`: `--site-base [REDACTED]` или `--redact-site-base`. Live `PUBLIC_SITE_URL` в артефактах ломает secret-scan.
- Перед `git commit`, если pre-commit падает на `invalid variable name`: отфильтруй `CLOUD_AGENT_INJECTED_SECRET_NAMES` до `^[A-Za-z_][A-Za-z0-9_]*$` (`eval "$(bash scripts/excalibur_blog_sanitize_secret_names.sh --export)"`).

## Utility / editorial-policy

- `pain_markers_ru` / `outcome_markers_ru` + `min_*` в `memory/brief/editorial-policy.json` обязательны. Пустые списки → utility gate BLOCK на любой статье. Doctor проверяет наличие маркеров.
- Recommendation markers включают `чеклист`, `чек-лист`, `делать`, `не делать`, `сделайте`, `не делайте`.
