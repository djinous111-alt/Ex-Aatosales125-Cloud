# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- То же для `excalibur-blog-geo-qa`: если typed Task недоступен — `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md` (не пропускать QA).
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
- `memory/site.env.local` часто отсутствует на fresh Cloud pod: publish bootstrap’ит его из process env (`SSH_PATH`→`SSH_ROOT`, default `.`).
- `paramiko` обязателен для SSH publish (requirements.txt + cloud-agent-install + Dockerfile).
- Перед PHP payload publish гидратит `${CATALOG_URL}` / `env:PUBLIC_SITE_URL` in-memory; в git остаются placeholders.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Инсайт-blockquote: **не** начинай с `TL;DR` / `Быстрый инсайт` — тематический ярлык («Инсайт до депозита»).
- CTA в git: только `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}`; live URL — только expand для link-verify/publish.
- `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` обязаны быть non-empty; utility gate имеет human-voice fallback, doctor падает если списки пусты.

## Research

- `is_technical_topic()` смотрит topic card + word-boundary для коротких маркеров (`ai`/`ии`); не сканирует весь `research-notes.md` (иначе `reader_pain` / `комплектации` дают false-positive и требуют github_urls≥3).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `-o` для human-voice / research-notes gate: basename → article_dir; путь `memory/...` → repo root (иначе nested duplicate tree).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Outfit: погода/тема из `blog-hero.json` / scene_hint — **не** hardcode white hoodie в prompt builder.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Git commit в Cloud: `bash scripts/excalibur_git.sh commit ...` — фильтрует non-identifier имена из `CLOUD_AGENT_INJECTED_SECRET_NAMES` (иначе pre-commit `${!NAME}` падает).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` + `--out-dir` (+ optional `--site-base ""` для relative `/blog/<slug>/`). Флага `--blog-path` **нет**.

## Schema

- В committed `schema.jsonld` пиши `env:PUBLIC_SITE_URL` (и related), не live hosts; publish гидратит перед upload.
