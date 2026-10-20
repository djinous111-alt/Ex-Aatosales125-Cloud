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

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.

## Indexer / llms

- `excalibur_blog_llms_generator.py` принимает `--blog-dir` / `--out-dir` / `--site-base`. Флага `--blog-path` нет; doctor проверяет `--blog-dir`.
- Для git commit llms часто `--site-base ""` (относительные пути), иначе secret-scan может редactить абсолютный PUBLIC_SITE_URL.

## Research / Wordstat / gates

- Wordstat: cluster-first (parent → how-to). Пустой `{}` / totalCount-only на how-to = low-result, не fatal; пиши WORDSTAT NOTE, не выдумывай показы.
- `research_notes_gate`: TECH_MARKERS матчятся по word-boundary; бренд `kia` не должен форсить GitHub evidence. Auto how-to/checklist в авто-нише — не technical.
- Pre-commit: перед `${!SECRET_NAME}` фильтруй `CLOUD_AGENT_INJECTED_SECRET_NAMES` до bash-safe идентификаторов (`source scripts/excalibur_blog_filter_injected_secrets.sh` или install.sh).

## Writer / utility

- `pain_markers_ru` / `outcome_markers_ru` должны жить в `memory/brief/editorial-policy.json`. Пустые списки → utility gate **skip** pain/outcome (WARN), не hard-BLOCK всех статей.

## GEO QA / TL;DR

- Ярлык `TL;DR / Быстрый инсайт:` в insight `<blockquote>` разрешён (writing-contract блок 2). GEO QA не валит за этот ярлык.

## Cover

- Outfit lock: softshell/crewneck, **NO hoodie**. `quad_manifest --merge` не тащит legacy SEO/Wordstat/hoodie сцены.
- Генерация: default Kie async API; sync MCP gpt-image-2 legacy; после `-32001` не blind-retry.

## Schema / publish

- Commit schema с `[REDACTED]`/`${PUBLIC_SITE_URL}` при secret-scan; publish гидратирует URL из env.
- Cloud install обязан ставить `paramiko`; `SSH_ROOT=.` в site.env / Secrets.

## Scout

- `--check-query` мержит `published-live-*.json` + `memory/blog/wp-slug-denylist.json`. Stale live JSON → denylist + ledger authoritative.
