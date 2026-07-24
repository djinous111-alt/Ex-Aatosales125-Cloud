# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- **Канон:** typed `excalibur-blog-*` Task types часто нет в Cloud enum (в т.ч. `excalibur-blog-geo-qa`) → сразу `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; не жечь токены на retry typed name.
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
- HTTP trigger / nginx часто отдаёт **504 ~120s**, пока PHP-FPM ещё пишет post: **не** долби concurrent curl (дубли media `-1/-2/-3`). Один trigger → WebFetch/wait → при timeout проверь live WP REST by slug; скрипт умеет SSH-success+HTTP-504 recovery.
- `paramiko` должен быть в Cloud image / `cloud-agent-install.sh` (PEP 668: `--break-system-packages` или venv).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Для human-voice / utility PASS в тексте нужны явные outcome-глаголы: `результат` / `получите` / `проверьте` / … (≥3) и pain-маркеры (≥2).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate требует `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json`; пустые списки больше не должны silently BLOCK (скрипт enforce только при non-empty).
- Human voice: в тексте ≥3 outcome-маркера (`результат`/`получите`/`проверьте`/…) и ≥2 pain; инсайт без ярлыка `TL;DR` / `Быстрый инсайт`.
- Cloud typed Task `excalibur-blog-*` может отсутствовать в enum → `Task(generalPurpose)` + agent/skill paths (канон, не «аварийный» путь).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie **402 Credits insufficient** / MCP opaque NoneType → emergency Cursor `GenerateImage` i2i (§4b cover skill); canonical path остаётся MCP/Kie после top-up credits.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `--suggest-next` floored по max Bxx из topics + ledger + article dirs + live WP slug match + `EXCALIBUR_USED_TOPIC_IDS` / `--used-ids`. Не доверяй suggest-next, если ledger отстаёт от WP.
- `--check-query` сканирует **Bxx и ASxx** карточки в `blog-topics.md`.

## Research

- Wordstat MCP server id = `MCP-KV` (legacy `user-mcp-kv`).
- WebFetch timeout на competitor URL ≠ research blocker: WebSearch extract / один retry.
- Research-notes TECH_MARKERS: короткие `ai`/`ии`/`api` — token match, не substring (`pain`/`России` не делают тему technical).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `excalibur_blog_llms_generator.py` принимает `--blog-dir` (не `--blog-path`); doctor проверяет `--blog-dir`. Не передавай `--blog-path`.
