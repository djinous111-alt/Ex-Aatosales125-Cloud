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
- Topic IDs: `AS##` (legacy pool) + `B##` (новые Scout-карточки). `today.py` / `scout_helper.py` парсят оба.
- Live WP slug: смотри `EXCALIBUR_RECENT_WP_POSTS` / `EXCALIBUR_SLUG_LIVE_HIT` перед выбором темы; уже живой slug = update, не new post.
- Research notes gate: `technical_topic` только по topic card; auto-niche (аукцион/растаможка/Encar…) не technical; `accessed_at` принимается как label или ISO-дата в source_table; `pain_solution_map` считает data-rows таблицы.

## Git / pre-commit

- Prefer `bash scripts/excalibur_git.sh commit …` — фильтрует `CLOUD_AGENT_*_SECRET_NAMES` до bash-идентификаторов (иначе pre-commit `invalid variable name` на `[REDACTED]`).
- `--no-verify` только как аварийный recovery, не как нормальный путь.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Large payload (~7MB): HTTP timeout/504 при живом PHP — wait **300s**, REST soft-success по slug; **не** второй bootstrap trigger (orphan media `-1`/`-2`).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru`.
- `human_voice_gate.py -o human-voice-report.json` — путь `-o` относительно `--article-dir`.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Cloud default: `python3 scripts/excalibur_blog_kie_gpt_image2_api.py` (async). Sync MCP `gpt-image-2` timeout `-32001` → **не** blind-retry; переходи на Kie.

## Scout

- Ниша канала: **Авто-Сейлс** (JP/KR/CN import). Запрещены Cursor/n8n/Make/AI-automation темы без явного Director override.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
