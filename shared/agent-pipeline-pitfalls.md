# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path. Это first-class путь, не «аварийный костыль», пока typed tasks не зарегистрированы (включая geo-qa).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research_notes_gate` technical markers — word-boundary (не substring): `pain` / `японии` не делают auto-тему technical и не требуют ≥3 github.com.
- `accessed_at` считается и из литералов `accessed_at:`, и из дат в source_table с колонкой accessed_at.
- Для non-software ниш (Авто-Сейлс) github.com quota только если topic действительно technical.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Cloud Secrets часто дают `SSH_PATH`, а скрипт читает `SSH_ROOT` — `load_env` мапит `SSH_PATH→SSH_ROOT` (default `.`).
- Fresh Cloud VM: `memory/site.env.local` gitignored → publish/doctor auto-bootstrap из process env (**без кавычек** вокруг values).
- `paramiko` обязателен в image (`requirements.txt`, `.cursor/Dockerfile`, `cloud-agent-install.sh`).

## Writer / Fact Check Box / CTA

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA в committed HTML: `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}` — не вставляй live URL (secret-scan). Publish подставляет значения на деплое.
- `editorial-policy.json` обязан держать `pain_markers_ru` / `outcome_markers_ru` + `_markers_pinned: true`. Rebrand/sync не должен вычищать marker vocabulary. Utility gate падает на human-voice fallback, если списки пусты.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `link_verify` расширяет `${ENV}` из os.environ для HTTP и redact'ит live URLs в JSON; не править HTML ради verify.
- Insight-блок: не начинай с `TL;DR` / `Быстрый инсайт`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным: **не цитируй** `лох`/`лохов` даже в negatives — только generic «no demeaning slang». Prompt builder блокирует banned lemmas + white-hoodie outfit lock.
- Outfit берётся из `scene_hint` / `blog-hero` outfit_rule (softshell/crewneck), не hardcoded white hoodie.
- Cloud cover default: **Kie** `excalibur_blog_kie_gpt_image2_api.py`. Sync MCP `gpt-image-2` — legacy fallback, max 1 attempt; при -32001 не blind-retry.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- LIVE denylist: `python3 scripts/excalibur_blog_scout_helper.py --live-slugs` / `--live-search` / `--check-slug` против `PUBLIC_SITE_URL`. MCP `wordpress_get_posts` может указывать на другой хост — не авторитетен для AVTO SALES.
- Ниша Авто-Сейлс: следуй Director Task + site-brief, не AI/Cursor defaults в scout skill.

## Indexer / Git / Secrets

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` нет).
- Перед `git commit`: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit …` — фильтрует non-identifier tokens в `CLOUD_AGENT_*_SECRET_NAMES` (иначе pre-commit `invalid variable name`).
