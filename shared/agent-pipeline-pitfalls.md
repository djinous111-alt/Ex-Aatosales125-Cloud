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
- Wordstat `top_requests` 500/server error ≠ research/scout blocker: fallback `wordstat_get_dynamics` (`PERIOD_MONTHLY`, region 225, даты = первый/последний день месяца) + zen-topics/WebSearch.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- Cloud Secret `SSH_ROOT` **должен быть `.`** (Beget login cwd). Non-dot path перекрывает `memory/site.env.local` → первый SFTP ENOENT; скрипт retry на `.`, но secret всё равно поставь `.` в Dashboard (repo это не меняет).
- `paramiko` обязан ставиться на boot через `.cursor/cloud-agent-install.sh` + `requirements.txt`; doctor WARN → `pip install paramiko`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA URL из conversion-map; при `[REDACTED]` — из env `CATALOG_URL`/`TELEGRAM_URL`, никогда литерал `[REDACTED]` в href.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` и `outcome_markers_ru` (синхрон с `human_voice_gate`). Пустые списки → false BLOCK на любой статье (utility score 0); это **config bug**, не writer FIX. doctor FAIL + utility_gate fail-fast.
- Recommendation markers — точные формы `сделайте` / `не делайте` (не «Делать/Не делать»).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Ниша только **Авто-Сейлс** (`memory/brief/site-brief.md`): Япония/Корея/Китай, СВХ, утильсбор, VIN. Не предлагать Cursor/n8n/Make/ИИ-агентов.
- Helper/today видят topic ID **AS*** и **B***.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `top_requests` 500 → dynamics + zen-topics — accepted demand signal, не fatal blocker. Dynamics dates: first/last day of month.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` (не `--blog-path`); doctor проверяет именно `--blog-dir`.
- Interlinker: `--redact-site-base` → в JSON report `site_base: [REDACTED]`; live HTML links — из `--site-base` / `PUBLIC_SITE_URL` (HTML apply уже relative `/blog/{slug}/`).

## Git / secrets pre-commit

- Перед `git commit` (writer/schema/scout/publish): `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"`.
- Sanitize `CLOUD_AGENT_INJECTED_SECRET_NAMES` должен оставаться **CSV** (`a,b,c`), не space-separated: hook парсит через `IFS=','`.
- Невалидные имена (`[REDACTED]`, URL-подобные) ломают `${!SECRET_NAME}` → «invalid variable name»; filter-скрипт их отбрасывает.
- Schema/writer: не вырезай sameAs/catalog/telegram URL из артефактов ради scanner — сначала filter-скрипт (omit `PUBLIC_SITE_URL`/`CATALOG_URL`/`TELEGRAM_URL`/`MAX_URL`).
