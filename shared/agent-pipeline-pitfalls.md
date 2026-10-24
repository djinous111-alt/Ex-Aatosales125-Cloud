# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Часто отсутствует именно typed `excalibur-blog-geo-qa` в enum → сразу `Task(generalPurpose)` с agent+skill GEO QA, без ретраев typed Task.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Cloud Secrets: имена только `[A-Za-z_][A-Za-z0-9_]*`. Иначе pre-commit падает на `${!SECRET_NAME}` (`invalid variable name`). Перед commit: `source scripts/excalibur_blog_filter_secret_names.sh`.

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
- `paramiko` обязателен для SSH publish: ставится в `.cursor/cloud-agent-install.sh` / Dockerfile; doctor `--publish` FAIL если модуль отсутствует.
- `memory/site.env.local` gitignored — на старте publish материализуй из Cloud Secrets (`SSH_PASS` ← `SSH_PASSWORD`, `SSH_ROOT=.`), не печатай значения.
- В git `schema.jsonld` / link-verify держи `env:PUBLIC_SITE_URL` (и др.); publish расширяет плейсхолдеры перед WP meta. Абсолютный host из secrets в staged files → COMMIT BLOCKED.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP trigger timeout для большого bootstrap (~6MB) — 300s. При timeout/nginx **504** сначала REST reconstruct по slug; **не** второй overlapping trigger (дубли media `*-1.png`). 504 HTML в `webfetch-response.txt` ≠ success.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `excalibur_blog_utility_gate.py` читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json`. Пустой список → warning + skip check (не hard BLOCK). Держи списки синхронными с `human_voice_gate` PAIN/OUTCOME_MARKERS.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- MCP-KV / sync `gpt-image-2` `namespaceStatus: error` → сразу `excalibur_blog_kie_gpt_image2_api.py` (async Kie), не только при `-32001`.
- После split `excalibur_blog_cover_quad_split.py` по умолчанию PIL-штампует угол `avto-sales125.ru` на `cover.png`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- MCP-KV `namespaceStatus: error` / Wordstat unavailable → non-blocking: LIVE denylist + Autostat/WebSearch; impressions `n/a`; допиши incident (не выдумывай объёмы).
- До выбора slug обязателен `shared/wp-slug-denylist.json` (doctor FAIL если нет). Restore: `python3 scripts/excalibur_blog_wp_slug_denylist.py --rebuild`.

## Research

- `research_notes_gate` technical_topic: короткие маркеры `ии`/`ai` матчятся как токены (word-boundary). Подстрока «Японии»/«комплектации» больше не делает авто-тему technical.
- Wordstat MCP error path = тот же non-blocking fallback, что у Scout (`⚠️ WORDSTAT AUTH WARNING` + incident).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: флаги `--blog-dir` / `--out-dir` / `--site-base` (не `--blog-path`). Для git-артефактов `--site-base ""` → relative `/blog/<slug>/`.
