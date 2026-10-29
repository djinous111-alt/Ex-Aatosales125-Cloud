# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **сразу** `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (не трать токены на retry typed Task). GEO QA / writer / cover / schema / indexer / publish / fixer — тот же first-class fallback.
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
- `schema.jsonld` коммить с `${PUBLIC_SITE_URL}` / `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}`; publish `expand_env_placeholders` поднимает значения in-memory перед WP upload (файл на диске не переписывать).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Не стирай `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` (`_markers_pinned: true`). Doctor + utility-gate fallback ловят пустые списки.

## Research

- `TECH_MARKERS` — только целые токены; bare `ai`/`ии` ломают auto/China how-to через `reader_pain` / «комплектации».
- В `research-notes.md` нужно ≥5 литералов `accessed_at:`; строки `pain_solution_map` — с `боль`/`решение`/`результат` (или pain/solution/result).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Outfit героя — только `blog-hero.json` outfit_rule + `scene_hint`; **запрещён** hard-lock white hoodie / «белое плотное худи».

## Scout / Git secrets

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Перед `git commit` в Cloud: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit …`. `CLOUD_AGENT_INJECTED_SECRET_NAMES` иногда содержит URL как «имя» → bash `${!SECRET_NAME}` падает с `invalid variable name`. Dashboard: только identifier-имена (`CATALOG_URL`), URL — в value.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- WP root permalinks: `python3 scripts/excalibur_blog_llms_generator.py … --site-base "" --blog-path / --out-dir memory/blog` (пустой site-base → relative `/{slug}/`). Не клади live `PUBLIC_SITE_URL` в default argparse.
