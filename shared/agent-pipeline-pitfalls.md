# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types (в т.ч. `excalibur-blog-geo-qa`) → сразу fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; не ретраить typed launch.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `technical_topic` в research-notes-gate смотрит **только topic card** (h1/query/slug/intent), не body notes: иначе `## github_evidence` / «агентская смета» ложно требуют GitHub quota.
- В source table пиши `accessed_at: YYYY-MM-DD` (или ISO-дату в URL-строке таблицы) — gate считает эти формы.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Читай Secrets через Python (`load_env`), не `source` password-bearing `site.env.local` в bash.
- `paramiko` обязателен для SSH publish — ставится в `.cursor/cloud-agent-install.sh`; doctor WARN если нет.
- В git: `schema.jsonld` / CTA с `env:NAME` и `${NAME}`; publish гидратирует in-memory. Сырые site/CTA URL в schema → Cloud secret-scan fail.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Инсайт-блок: тематический ярлык; **не** `TL;DR` / `Быстрый инсайт` (GEO QA + html-linter warning).
- tip/rebrand sync **не должен** вычищать `pain_markers_ru` / `outcome_markers_ru` / mins из `memory/brief/editorial-policy.json`; utility-gate имеет fallback на human-voice markers, doctor проверяет ключи.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `link_verify` IRI-encode non-ASCII path/query; 2GIS search URL лучше сразу percent-encode; CTA в git как `${CATALOG_URL}` / `${TELEGRAM_URL}`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным: demeaning slang запрещён; prompt builder **не** цитирует `лох/лохов` даже в negatives и **не** lock'ает white hoodie — outfit из `scene_hint`.
- Primary image path: Kie async (`excalibur_blog_kie_gpt_image2_api.py`) при `KIE_API_KEY`. Sync MCP `-32001` → ONE Kie recovery same batch, не dead-end `COVER MCP RECOVERY NEEDED` и не второй sync create.

## Scout / git

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Cloud `git commit` через `scripts/excalibur_git.sh` — фильтрует non-identifier имена в `CLOUD_AGENT_INJECTED_SECRET_NAMES` (URL-as-secret-name ломает `${!SECRET_NAME}` в pre-commit hook). Dashboard: URL values не должны быть secret *names*.

## Indexer / doctor

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: только `--blog-dir` (флага `--blog-path` нет). Doctor assert'ит `--blog-dir` и отсутствие `--blog-path`.
- Commit-safe llms: `--site-base ""` → relative `/blog/<slug>/`; не коммить absolute `PUBLIC_SITE_URL` в llms.txt.
