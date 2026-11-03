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
- `--env-check` обязан зондировать SSH DNS (`getaddrinfo`), TCP/22 и уважать optional `SSH_HOST_IP`. Не подставляй IP `PUBLIC_SITE_URL` как SSH — HTTP и :22 на Beget часто разные.
- DNS OK + TCP/22 timeout на hostname/A/`SSH_HOST_IP` → `❌ PUBLISH BLOCKER` (needs-human: Beget SSH listener/firewall или verified `SSH_HOST_IP`). Это не чинится LIVE publish из Cloud.
- Если Cloud resolver даёт `Temporary failure in name resolution` для Beget `SSH_HOST` и нет `SSH_HOST_IP` → `❌ PUBLISH BLOCKER` (needs-human: DNS/egress или IP secret). Soft-pass catalog DNS в link-verify ≠ LIVE SSH proof.
- WP REST / `PUBLIC_SITE_URL` SSL handshake timeout из Cloud egress: ledger может отставать от LIVE. Scout/Director обязаны сверять denylist + automation memory + `EXCALIBUR_RECENT_WP_POSTS` (если доступны), не доверять только `shared/published-articles.md`.
- `paramiko` pin в `requirements.txt` + `.cursor/cloud-agent-install.sh`; mid-run `pip install paramiko` — симптом сломанного image.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` / `SSH_PATH` в Cloud Secrets на `.`.
- Pre-commit `invalid variable name` на `${!SECRET_NAME}`: `CLOUD_AGENT_*_SECRET_NAMES` должны быть **comma**-joined bash identifiers (`[A-Za-z_][A-Za-z0-9_]*`). URL/value в списке имён ломает hook. Используй `bash scripts/excalibur_git.sh commit …` (фильтрует non-identifier names).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` обязаны быть pinned (`_markers_pinned: true`); rebrand wipe → utility gate ломает все статьи. Writer: формы «Сделайте/Не делайте» (или синонимы `делать:` в recommendation markers).
- Catalog/site SSL или DNS fail из Cloud egress → link-verify soft-pass `catalog_ssl` / `site_ssl` / `catalog_dns` / `catalog_5xx` (doctor + smoke pin; не вычищать sanitizer-ом).
- Insight label: запрещены шаблонные `TL;DR` / `Быстрый инсайт`; human-voice gate + writing contract требуют тематический ярлык (`Инсайт до депозита:` и т.п.).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- MCP-KV down → Kie-first ONE task; auto file-base64 local hero если WP media fetch fails; `cover_quad_prompt` принимает Kie tempfile hosts (`tempfile.redpandaai.co` / `redpandaai.co`) как fallback к WP media.
- Outfit lock берётся из `blog-hero.outfit_rule` / scene weather — **не** hardcode white hoodie.
- Split без corner brand `avto-sales125.ru` на cover → regression; stamp делает `excalibur_blog_cover_quad_split.py`.

## Research

- MCP-KV / Wordstat OAuth down → `WORDSTAT UNAVAILABLE` + auth-refresh link; **запрещено** выдумывать monthly impressions.
- `research-notes-gate`: считает data-rows под `## pain_solution_map` и `accessed_at:` **или** ISO-даты в URL-строках source table; не требуй English `pain|solution` literals в каждой клетке.

## Scout

- Ниша только **Авто-Сейлс** (JP/KR/CN import, таможня, Владивосток). Legacy drift в Cursor/Make/n8n/AI-агенты — запрещён.
- Wordstat cluster-first: широкий parent → узкий how-to. `totalCount`-only = low-result, не fatal.
- MCP-KV `namespaceStatus:error` / missing `wordstat_*` → WebSearch-only + явный `wordstat_status: unavailable_mcp_kv` на карточке; без выдуманных shows.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `excalibur_blog_llms_generator.py` обязан принимать `--blog-path` (URL prefix; site-brief `/` → `/blog`). Sanitizer иногда вытирает флаг — doctor check `llms generator supports --blog-path` + smoke.

## Topic selection

- `excalibur_blog_today.py` treats ledger statuses `published|in_progress|draft_ready|publish_blocked` as used.
- Topic cards with `status_note` containing `published` / `live` / `do not republish` are skipped even if missing from a stale ledger.
- After publish TCP/22 blocker, keep `publish_blocked` in ledger so the next run does not re-pick the same slug blindly.
