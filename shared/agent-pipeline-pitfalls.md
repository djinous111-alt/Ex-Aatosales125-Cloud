# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Typed enum часто **без** `excalibur-blog-geo-qa` (и других ролей) на новых Cloud builds → тот же generalPurpose fallback; один Task = одна роль; single-agent pipeline запрещён.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Topic IDs (AS* / B*)

- `excalibur_blog_today.py` и `excalibur_blog_scout_helper.py` обязаны принимать `AS\d+` и `B\d+`. Regex только на `B*` → ложный `needs_scout` при полном AS-пуле.
- Scout `--suggest-next` после Autosales rebrand продолжает серию `AS##`, не сбрасывает на `B01`.

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
- `--env-check` обязан зондировать SSH DNS (`getaddrinfo`), optional `SSH_HOST_IP`, и TCP/22 connect (timeout → `ssh_tcp22`). Не подставляй IP `PUBLIC_SITE_URL` как SSH — HTTP и :22 на Beget часто разные.
- Если Cloud resolver даёт `Temporary failure in name resolution` для Beget `SSH_HOST` и нет `SSH_HOST_IP` → `❌ PUBLISH BLOCKER` (needs-human: DNS/egress или IP secret). Soft-pass catalog DNS в link-verify ≠ LIVE SSH proof.
- DNS OK, но TCP/22 timeout (Errno 110) → тот же PUBLISH BLOCKER / `needs-human`: firewall/allowlist или другой `SSH_HOST_IP` с живым :22. Не invent host/IP вне Cloud Secrets.
- `paramiko` pin в `requirements.txt` + `.cursor/cloud-agent-install.sh`; mid-run `pip install paramiko` — симптом сломанного image.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` / `SSH_PATH` в Cloud Secrets на `.`.
- Pre-commit `invalid variable name` на `${!SECRET_NAME}`: используй `bash scripts/excalibur_git.sh commit …` (фильтрует non-identifier secret names). Не отключай hooks без filter, если в diff нет секретов.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Insight `<blockquote>` не стартует с `TL;DR` / `Быстрый инсайт` — используй «Короткий разбор:» (или живой opener). Secondary query сверяй с local/published primaries до handoff.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` обязаны быть pinned (`_markers_pinned: true`); rebrand wipe → utility gate ломает все статьи. Writer: формы «Сделайте/Не делайте» (или синонимы `делать:` в recommendation markers).
- Catalog host DNS/`Temporary failure` в Cloud → link-verify soft-pass `catalog_dns` / `catalog_5xx` (не вычищать при rebrand).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- MCP-KV down → Kie-first ONE task; auto file-base64 local hero если WP media fetch fails.
- Split без corner brand `avto-sales125.ru` на cover → regression; stamp делает `excalibur_blog_cover_quad_split.py`.

## Research

- MCP-KV / Wordstat OAuth down → `WORDSTAT UNAVAILABLE` + auth-refresh link; **запрещено** выдумывать monthly impressions.
- `research-notes-gate`: считает data-rows под `## pain_solution_map` и `accessed_at:` **или** ISO-даты в URL-строках source table; не требуй English `pain|solution` literals в каждой клетке.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` канонический; `--blog-path` = alias того же пути (не site root `/`).
