# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Boot/sanitizer может стереть durable pins (editorial markers, link soft-pass, llms `--blog-path`, `excalibur_git.sh`, denylist). Перед Scout/Writer: `python3 scripts/excalibur_blog_doctor.py` — errors must be 0; восстанавливай pins из git tip, не invent ad hoc.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- MCP-KV Wordstat unavailable → `## wordstat` UNAVAILABLE + warning, WebSearch-only, **zero invented shows**, incident в queue.
- Research-notes tech heuristic: short markers (`ai`/`ии`) — word-boundary only; ignore `## github_evidence` when classifying. Auto-import AS## how-to ≠ forced GitHub≥3.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Preflight: `python3 scripts/excalibur_blog_wp_publish.py --env-check` (не ad-hoc import без `scripts/` в `sys.path`).
- `ssh.dns.resolved=true` ≠ TCP/22 OK. При `ssh_tcp22_timeout` — **не** LIVE write, ledger `publish_blocked`, Fixer → `needs-human` (restore egress or verified `SSH_HOST_IP`). Не маскировать как fixed без реального TCP.
- SSH root может быть login cwd: ENOENT на root → retry `.`; после warning обнови `SSH_ROOT` Cloud Secret.
- `load_article`: только module-level `re` (локальный `import re` после schema `re.sub` → UnboundLocalError).
- Denylist LIVE posts (не перезаписывать foreign): см. `shared/wp-slug-denylist.json`; doctor fail-closed если файл missing/empty.

## Writer / Fact Check Box

- Catalog CTA host must match `PUBLIC_SITE_URL` (`avtosales125.ru`). Do not copy hyphenated `avto-sales125.ru` from stale conversion-map; Telegram `t.me/avtosales125`. Cover corner visual may still say `avto-sales125.ru`.
- Utility tokens: exact policy markers + aliases (`не делайте`/`не делать`, `чеклист`/`чек-лист`).
- Outcome-before-FAQ H2: avoid Latin `FAQ` substring until/unless linter uses strict FAQ-title match.
- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- link-verify: catalog/site SSL/timeout soft-pass (`catalog_ssl` / `site_ssl`) — warning, not hard FAIL.
- utility: skip `min_pain`/`min_outcome` only when marker lists empty; lists must stay pinned (`_markers_pinned`).
- MCP URLs в production article.html → fix перед publish.
- `article.html` whitelist: `<pre>`/`<code>` запрещены, пока не в whitelist; код/шаблоны — blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style OK, but visible text non-toxic: no `лох` / `лохов` / `для лохов`.
- MCP-KV `gpt-image-2` down → first-class Kie fallback (`hero_reference_url.py --force --provider kie` + `excalibur_blog_kie_gpt_image2_api.py`); one job; WP media hero often dead — prefer Kie tempfile when HEAD fails.

## Scout

- Autosalas IDs: `AS##` (helper `AS|B`). Ignoring helper that returns `B01` on empty B-pool when AS cards exist = bug (fixed: AS|B regex).
- Wordstat cluster-first; `totalCount`-only = low-result, not fatal. UNAVAILABLE = WebSearch-only + incident, never fabricate shows.
- `shared/wp-slug-denylist.json` must exist before append; rebuild from git + ledger + known LIVE if wiped.

## Indexer

- Cloud shell: `python3` for interlinker/llms (no bare `python`).
- Commit-safe llms: `--site-base "" --blog-path / --relative-urls` → `/blog/<slug>/`. Absolute `PUBLIC_SITE_URL` only for live/runtime notes, not git `memory/blog/llms*.txt`.
- Clear `site_base` host from `interlink-suggestions.json` before commit.

## Git / pre-commit

- Cursor secret scanner: `CLOUD_AGENT_*_SECRET_NAMES` must be comma-separated bash identifiers. Non-ids (URLs/placeholders) → `invalid variable name`.
- Always: `bash scripts/excalibur_git.sh commit …` or `source scripts/excalibur_blog_filter_commit_secret_env.sh` before commit.
