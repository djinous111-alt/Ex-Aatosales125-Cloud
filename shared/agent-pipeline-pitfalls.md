# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Особенно часто недоступен typed Task `excalibur-blog-geo-qa` → сразу `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md` (не тратить ретраи на typed type).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Перед `git commit` в Cloud: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit …`. `CLOUD_AGENT_*_SECRET_NAMES` иногда содержит non-identifier (`[REDACTED]` / URL) → `${!NAME}` ломает pre-commit.

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
- Крупный bootstrap (~7–9MB): HTTP может дать `RemoteDisconnected`/504 после SSH OK. Скрипт сначала REST-reconstruct by slug (`OK post=`), иначе печатает `FALLBACK_TRIGGER_URL` — открывай WebFetch **сразу параллельно**. Не делай second-trigger, если slug уже LIVE (дубли `*-1.png`). Timeout: `EXCALIBUR_PUBLISH_HTTP_TIMEOUT` (default 300s).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Не хардкодить `white hoodie` / outfit lock в prompt builder: одежда из `blog-hero.json` `outfit_rule` + `scene_hint` (погода/тема). Sanitize batch — только временный workaround.

## Research / Writer gates

- `TECH_MARKERS` в research-notes-gate — word-boundary для коротких токенов (`ии`/`ai`); «комплектации» ≠ technical topic, GitHub ≥3 не требовать для авто how-to.
- В source table пиши `accessed_at: YYYY-MM-DD` (≥5). В `pain_solution_map` строки должны содержать боль|pain|решение|solution|result|результат.
- `memory/brief/editorial-policy.json` обязан держать `_markers_pinned`, `pain_markers_ru`, `outcome_markers_ru` и min counts; utility-gate имеет default fallback, doctor падает если списки пусты.

## Scout / today

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `{}` / `totalCount`-only / пустой top на узкий how-to = low-result signal, не fatal; бери parent/mid volumes.
- `excalibur_blog_today.py` / `excalibur_blog_scout_helper.py` матчат topic_id `((?:AS|B)\d+)`. Только `B\d+` → false `needs_scout` при пустом B-пуле, даже если AS* P0 есть.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Канонические относительные URL: `--site-base "" --blog-path /` → `/{slug}/` (не хардкод `/blog/{slug}/`). Legacy: `--blog-path /blog/`.
- Rebrand/sync **не должен** выкидывать `--blog-path` из llms/interlinker; doctor падает если флага нет. Never drop `outfit_lock_from_hero` / `_markers_pinned` / `excalibur_git.sh` either.
