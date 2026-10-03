# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Особенно часто отсутствует typed `excalibur-blog-geo-qa` в Cloud Task enum → сразу `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md` (не ретраить typed enum).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research_start.py` redact'ит live `PUBLIC_SITE_URL` в `research-serp.json` → `[PUBLIC_SITE_URL]` (secret-scan).
- `TECH_MARKERS` в research-notes-gate **без** bare `github`; technical_topic смотрит только topic card (не notes body / github_evidence).

## Preflight / doctor / CLI

- Doctor проверяет реальные флаги: llms generator → `--blog-dir` / `--out-dir` / `--relative-urls` (не `--blog-path`).
- Indexer llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --relative-urls --out-dir memory/blog`.

## Git / secrets / pre-commit

- Перед `git commit` в Cloud: `source scripts/sanitize_cloud_secret_names.sh` — иначе `${!SECRET_NAME}` падает на non-identifier именах (URL / `[REDACTED]`).
- Dashboard secret names должны быть bash identifiers: `A-Za-z_[A-Za-z0-9_]*` (не URL).
- `llms.txt` коммить с relative `/blog/<slug>/` URLs; absolute `PUBLIC_SITE_URL` часто блокируется secret-scan.
- Secret redaction token `[REDACTED]` — для commit artifacts / conversion-map, **не** для live CTA `href` в `article.html`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root: если unset — publish defaults to `.`; в Cloud Secrets для этого хоста держи `SSH_ROOT=.`.
- `paramiko` обязателен: `.cursor/cloud-agent-install.sh` ставит его; если нет — `pip3 install --break-system-packages paramiko`.

## Writer / Fact Check Box / CTA

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA href: никогда literal `[REDACTED]`; если conversion-map redacted — `CATALOG_URL`/`TELEGRAM_URL` из env или токены `[CATALOG_URL]`/`[TELEGRAM_URL]`.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать `pain_markers_ru` / `outcome_markers_ru`; пустые списки → utility gate warning, не false BLOCKER на 0 маркеров.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Cloud cover: prefer `scripts/excalibur_blog_kie_gpt_image2_api.py` (после первого sync MCP `-32001` или сразу); не multi-retry sync.
- Outfit из `blog-hero.json` (погода/тема), не hardcoded white hoodie.
- Face host fallback: catbox → 0x0 → litterbox (temporary).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms: `--blog-dir` + `--relative-urls` (не `--blog-path`).
