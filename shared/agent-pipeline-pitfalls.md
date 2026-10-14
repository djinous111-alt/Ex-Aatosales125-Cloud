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
- SSH root: Cloud Secret `SSH_ROOT=.` для login-cwd hosts; если unset — env-check WARN, publish может упасть на ENOENT (скрипт ретраит `.`).
- `paramiko` обязателен для SSH publish: ставится в `.cursor/cloud-agent-install.sh` и `requirements.txt`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Committed CTA `href` → `[REDACTED]` если CATALOG/TELEGRAM/PUBLIC_SITE в Cloud Secrets; перед link-verify подставь live URL из env.
- Коммиты артефактов: `bash scripts/excalibur_git.sh` (фильтр `CLOUD_AGENT_INJECTED_SECRET_NAMES`).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `link_verify`: catalog HTTP 5xx и egrul SSL → soft-pass (`catalog_5xx` / `egrul_*`), не ручной rewrite verdict.
- `editorial-policy.json` обязан держать непустые `pain_markers_ru` / `outcome_markers_ru`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- `hero_reference_url.py --force`: сначала hash-compare с hosted URL; не уходи на litterbox.

## Scout

- Ниша = Авто-Сейлс из `site-brief.md` (Япония/Корея/Китай), не Cursor/n8n/Make.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Research

- `technical_topic` в research-notes-gate: word-boundary маркеры + auto-niche override; авто-гайдам не нужен GitHub «для gate».

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` (не `--blog-path`).
