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

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен для SSH publish: `requirements.txt` + `.cursor/cloud-agent-install.sh` + Dockerfile. Если `ModuleNotFoundError: paramiko` — `pip install --break-system-packages paramiko` и чини install, не publish без библиотеки.
- `memory/site.env.local` gitignored: publish auto-bootstrap'ит его из Cloud Secrets / process env с `SSH_ROOT=.` если файла нет. `SSH_PASSWORD` → `SSH_PASS`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: в HTML пиши `href="${CATALOG_URL}"` / `${TELEGRAM_URL}` / `${MAX_URL}` (см. `conversion-map.md`). Не выдумывай хосты. Не коммить живые secret URL. Publish expand'ит плейсхолдеры; helper: `scripts/excalibur_blog_cta_hrefs.py --expand|--redact`.
- Pre-commit secret-scan: если `CLOUD_AGENT_INJECTED_SECRET_NAMES` содержит не-идентификатор вроде `[REDACTED]`, отфильтруй имена до `[A-Za-z_][A-Za-z0-9_]*` перед `${!SECRET_NAME}` — иначе hook падает с `invalid variable name`. Используй `scripts/excalibur_git.sh …` вместо голого `git` для commit/push.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru` (как в `human_voice_gate`); utility_gate при пустых списках → skip-warning, не false BLOCK. После rebrand/tip без fixer — восстановить маркеры, не слать writer за «pain=0».
- Инсайт-блок: не начинать с ярлыка `TL;DR` / `Быстрый инсайт`.

## Cover

- Видимый sticker-текст не должен быть токсичным. В **image prompt** (в т.ч. negative) **нельзя цитировать** banned lemmas (`лох`/`лохов`/…): safety filter флажит сам prompt. Пиши «non-toxic / no insults / no humiliating labels» без примеров оскорблений.
- Outfit: только из `blog-hero.json` / `scene_hint` (погода+тема). Запрещён hardcoded `white hoodie` lock.

## Research

- Wordstat: cluster-first. Узкий primary → empty `{}` / «Неожиданный формат» = soft-fail: не выдумывай показы; fallback на parent/secondary; в notes пометь primary как unverified.
- `research_notes_gate` определяет `technical_topic` **только по полям topic card** (h1/slug/queries), не по телу notes: секция `github_evidence` иначе даёт false-positive на авто-howto. Короткие маркеры (`ии`/`ai`) — word-boundary, иначе «японии» ложно technical.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only / empty `{}` на узкий запрос = low-result signal, не fatal.
- LIVE dedup обязателен: `python3 scripts/excalibur_blog_scout_helper.py --live-slugs <slug…>` и `--live-search <модель…>` против WP REST (`PUBLIC_SITE_URL`). `--check-query` видит только B-pool, не LIVE AS/WP посты.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- LLMs generator flags: `--blog-dir` + `--out-dir` (+ `--site-base`). **Нет** `--blog-path`. Для commit-safe артефактов: `--site-base ""` → relative `/blog/<slug>/` (absolute host ловит secret-scan).
