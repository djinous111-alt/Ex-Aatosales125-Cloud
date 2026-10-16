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
- Cloud Secret `SSH_ROOT` **должен быть `.`** (Beget login cwd). Non-dot path перекрывает `memory/site.env.local` → первый SFTP ENOENT; скрипт retry на `.`, но secret всё равно поставь `.` в Dashboard (repo это не меняет).
- `paramiko` обязан ставиться на boot через `.cursor/cloud-agent-install.sh` + `requirements.txt`; doctor WARN → `pip install paramiko`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` и `outcome_markers_ru` (синхрон с `human_voice_gate`). Пустые списки → false BLOCK на любой статье; doctor FAIL + utility_gate fail-fast.
- Recommendation markers — точные формы `сделайте` / `не делайте` (не «Делать/Не делать»); CTA URL из conversion-map, при `[REDACTED]` — из env `CATALOG_URL`/`TELEGRAM_URL`, никогда литерал `[REDACTED]` в href.
- human-voice `exactly_five_lists`: считает только `<ol>` с **ровно** 5 `<li>`; чеклисты 6–10 не false-positive.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Ниша только **Авто-Сейлс** (`memory/brief/site-brief.md`): Япония/Корея/Китай, СВХ, утильсбор, VIN. Не предлагать Cursor/n8n/Make/ИИ-агентов.
- Helper/today видят topic ID **AS*** и **B***.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` (не `--blog-path`); doctor проверяет именно `--blog-dir`.
- Interlinker: `--redact-site-base` → в JSON report `site_base: [REDACTED]`; live HTML links — из `--site-base` / `PUBLIC_SITE_URL`.

## Research

- Gate `accessed_at`: ≥5 дат из литералов `accessed_at: YYYY-MM-DD` **или** pipe-row `source_table` (URL + ISO date). Заголовок колонки сам по себе не считается.
- Шаблоны `github_evidence` / упоминания MCP в notes не включают `technical_topic` сами по себе.
- WebFetch 5xx/timeout на госпортале → soft-fail + вторичные официальные источники (ConsultantPlus/ФНП), без выдуманного UI.

## Git / secrets pre-commit

- Перед `git commit` (в т.ч. schema.jsonld): `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"`.
- Sanitize `CLOUD_AGENT_INJECTED_SECRET_NAMES` должен оставаться **CSV** (`a,b,c`), не space-separated: hook парсит через `IFS=','`.
- Невалидные имена (URL-подобные) ломают `${!SECRET_NAME}` → «invalid variable name».
- Schema: не вырезай sameAs/catalog/telegram URL из JSON-LD ради scanner — сначала filter-скрипт.
