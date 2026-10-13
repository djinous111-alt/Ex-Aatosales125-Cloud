# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path. Это относится и к `excalibur-blog-geo-qa`, `excalibur-blog-fixer` и остальным ролям: один Task = одна роль.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.
- Cursor Write на gitignored fragment path может вернуть success без файла — пиши через `python3 scripts/excalibur_blog_write_fragment.py` и сразу `test -f`.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research notes gate считает `accessed_at` и как литералы `accessed_at:`, и как ISO-даты в URL-строках `source_table`.
- TECH_MARKERS — word-boundary для коротких токенов (`ai`/`ии`/`api`); auto-import ниша (Encar/растаможка/аккредитив/JP/KR/CN) не требует GitHub×3.
- Wordstat HTTP 500 / `code:13`: retry+backoff, затем fallback (WP gap / zen parent / WebSearch); live impressions = `n/a`, без выдуманных показов.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Cloud install обязан ставить `paramiko` (`.cursor/cloud-agent-install.sh` + doctor check). При nginx **504** на multi-MB bootstrap HTTP trigger — SSH CLI php fallback (`php8.3`…); WebFetch/curl 504 HTML ≠ success (нужен `OK post=`).
- Schema meta: в git — placeholders (`[PUBLIC_SITE_URL]` / `[CATALOG_URL]` / …); publish expand-ит перед upload (`schema_build.py` / `wp_publish.py`).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru` и `min_*` в `article_required_signals` (doctor FAIL без них). Не вычищать при rebrand/sync.
- Инсайт-blockquote: без ярлыков `TL;DR` / `Быстрый инсайт` (пиши «Если коротко:»).
- CTA с публичными URL: `<!-- pragma: allowlist secret -->` на строке; коммит через `bash scripts/excalibur_git.sh`.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Brand CTA host из `CATALOG_URL` / `PUBLIC_SITE_URL` может отвечать 502/503/504 при живом Telegram — link-verify soft-pass с warning `soft brand catalog 5xx` (не меняй домен статьи; origin 503 — ops/human).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Ниша канала: **Авто-Сейлс** (JP/KR/CN import из `memory/brief/site-brief.md`). Запрещены Cursor/n8n/Make/AI-automation темы без явного Director override.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Wordstat 500: не блокируй P0 при WP gap + parent-кластер + WebSearch; пиши `scout_signal: wordstat_unavailable_fallback`.
- Каннибализация: `--check-query` + `--proposed-slug` + `--deny-slugs`; helper смотрит live WP REST / `EXCALIBUR_RECENT_WP_POSTS` / `published-live-*.json`, не только ledger. `published-live-*.json` может быть устаревшим — предпочитай fresh REST/env.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- Перед commit: `bash scripts/excalibur_git.sh commit …` или `eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"` — Cloud иногда кладёт raw URL в `CLOUD_AGENT_INJECTED_SECRET_NAMES`.
