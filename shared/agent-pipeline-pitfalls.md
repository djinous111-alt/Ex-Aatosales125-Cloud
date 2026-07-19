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
- Topic ids: `(?:AS|B)\d+`. Пул Авто-Сейлс = `AS##`; `today`/`scout_helper` не должны предлагать `B01` при живом AS-пуле.
- Директор перед выбором темы сверяет `shared/published-articles.md` с `EXCALIBUR_RECENT_WP_POSTS` (ledger sync).
- Research gate: TECH_MARKERS — token match; «ии» внутри «Японии» и поле `reader_pain` не делают topic technical. AS* auto niche не требует 3 GitHub URL; допустим `github_evidence: n/a` с причиной.
- `accessed_at`: считаются и `accessed_at: YYYY-MM-DD`, и ISO-даты в URL-строках source table.
- `research-serp.json` при записи redact'ит Cloud Secret URLs (`PUBLIC_SITE_URL` и др.).

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root: нужен `SSH_ROOT` (часто `.`). Legacy `SSH_PATH` мапится в `SSH_ROOT` в `load_env`. Если bootstrap ENOENT — скрипт пробует `.` и пишет warning.
- `paramiko` обязателен для SSH publish; Cloud install ставит `requirements.txt`. Fallback: `pip3 install --break-system-packages paramiko`.
- Literal `[REDACTED]` в `href` статьи = FAIL (`link_verify`); восстанови CTA из env до QA/publish.

## Writer / Fact Check Box / CTA secret-scan

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: живые https из `CATALOG_URL`/`TELEGRAM_URL`; на CTA-строке `<!-- pragma: allowlist secret -->`; запрет literal `href="[REDACTED]"`.
- Schema JSON-LD: перед commit `python3 scripts/excalibur_blog_schema_write.py --article-dir … --in-place` (unicode-escape secrets; HTML pragma в JSON нельзя).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: в `memory/brief/editorial-policy.json` обязаны быть `pain_markers_ru` / `outcome_markers_ru`; скрипт не должен BLOCK при пустых списках (регрессия после rebrand — см. AS02/AS10).
- Utility action-маркеры: «сделайте/не делайте», не «Делать/Не делать»; `чеклист` без дефиса.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- При наличии `KIE_API_KEY` стартуй сразу Kie async (`excalibur_blog_kie_gpt_image2_api.py`); sync MCP `gpt-image-2` — fallback. `-32001` ≠ final blocker; не apply без URL; не второй sync create вслепую.

## Scout

- Ниша: Авто-Сейлс (Япония/Корея/Китай, растаможка, Encar, СВХ) — не AI/Cursor/MCP.
- Wordstat: cluster-first (широкий parent → узкий how-to). `totalCount`-only на узком = low-result, не fatal.
- Next id: `AS##` через `scout_helper --suggest-next`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` / `--site-base` / `--out-dir` — **не** `--blog-path`.
- Перед commit redact `PUBLIC_SITE_URL` → `[REDACTED]` в llms/checklist; Publish регенерирует llms с живым site-base перед upload.
