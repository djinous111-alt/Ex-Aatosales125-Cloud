# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud часто **не** принимает `excalibur-blog-*` как typed Task types (в т.ч. `excalibur-blog-geo-qa`) → канон: `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; один Task = одна роль.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата / темы

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Topic IDs: **AS\d+** (канон) и legacy **B\d+**. `today.py` / `scout_helper` обязаны видеть оба; иначе pool=`needs_scout` при живых AS-карточках.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat: cluster-first. Ответ `totalCount`-only / `{}` → broaden once, иначе `N/A` (не выдумывать показы, не retry-spam).
- Research gate: предпочтительно `accessed_at: YYYY-MM-DD` (≥5); `## github_evidence` не должен сам по себе включать technical-topic heuristics.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Нет `memory/site.env.local` → `python3 scripts/excalibur_blog_site_env_bootstrap.py` (из Cloud Secrets; не коммитить; не печатать значения).
- Нужен `paramiko` (`requirements.txt` + `.cursor/cloud-agent-install.sh`).
- Schema `${ENV}` / `${A|B}` гидрируется **in-memory** в `excalibur_blog_wp_publish.py`; не мутировать committed `schema.jsonld`.
- Ledger / wp-publish-result: URL как `${PUBLIC_SITE_URL}/…`, не абсолютный host (secret-scan).
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA / utility markers

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан иметь `_markers_pinned=true` и non-empty `pain_markers_ru` / `outcome_markers_ru`. Пустые списки после rebrand = CONFIG error utility gate, не «плохая статья». Doctor/smoke ловят wipe.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- MCP `gpt-image-2` `-32001` timeout без URL → сразу Kie async fallback (`excalibur_blog_kie_gpt_image2_api.py`), не пустой polling.
- Outfit: `scene_hint` / `blog-hero.outfit_rule`, **не** hardcoded white hoodie.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: канон `--blog-dir`; `--blog-path` — alias. Для commit: `--site-base ""` → relative `/blog/<slug>/`. Не коммитить абсолютный PUBLIC host в llms/interlink JSON.
