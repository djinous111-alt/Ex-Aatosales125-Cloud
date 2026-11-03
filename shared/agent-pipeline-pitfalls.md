# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата / Wordstat

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `today.py` / `scout_helper.py` обязаны понимать **AS## и B##**; `needs_scout` только при пустом P0-пуле.
- MCP-KV discovery `error` / empty tools = Wordstat UNAVAILABLE (как 401): пиши warning + `н/д`, не выдумывай показы.
- `research_notes_gate`: short TECH_MARKERS (`ai`) — token-boundary; `## github_evidence` сам по себе не делает тему technical.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- **config PASS ≠ DNS/TCP PASS:** смотри `ssh.dns` и `ssh.tcp22`; при `ssh_tcp22_timeout` — `publish_blocked`, не LIVE. `SSH_HOST_IP` только после ручной проверки (не invent).
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / markers / git

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- `memory/brief/editorial-policy.json` обязан иметь `_markers_pinned` + непустые `pain_markers_ru` / `outcome_markers_ru` (+ `min_*`). Utility gate fail-soft, если списки пусты; doctor падает, если pin снят.
- Коммиты агентов: `bash scripts/excalibur_git.sh commit …` (фильтрует `CLOUD_AGENT_*_SECRET_NAMES` → valid bash identifiers; чинит `invalid variable name` в pre-commit.cursor).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- Typed Task `excalibur-blog-geo-qa` может отсутствовать → `Task(generalPurpose)` + agent/skill paths.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `link_verify`: soft-pass `catalog_dns` / `catalog_5xx` / `catalog_ssl` / `site_ssl` + URL redact `${ENV}` — pin в doctor; Cloud egress часто timeout/SSL. Soft-pass смотрит `checked_url` для relative internals.
- Инсайт-блок: не ярлыки `TL;DR` / `Быстрый инсайт` (human-voice BLOCK); writing-contract → `Короткий разбор:`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- **Kie-first** когда MCP-KV down; WP hero timeout → `hero_reference_url.py --provider kie` / `excalibur_blog_kie_file_base64_upload.py`; `tempfile.redpandaai.co` allowed в `cover_quad_prompt`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-path` = alias `--blog-dir` (doctor проверяет оба).
