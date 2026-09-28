# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud часто не принимает `excalibur-blog-*` как typed Task → сразу `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; **не трать шаг на retry typed** (в т.ч. `excalibur-blog-geo-qa`).
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
- Utility action-маркеры: `сделайте` / `не делайте` / `чеклист` (без дефиса). Формулировки «Делать/Не делать» и `чек-лист` **не** считаются.
- При FIX после GEO QA **не** делай полный `Write` HTML из буфера `Read`: слой отображения может подменить CTA `href` на `[REDACTED]`. Правь тело через `StrReplace`; URL бери из `conversion-map.md` / git HEAD.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json` (синхрон с human-voice). Пустые списки больше не BLOCK; но списки обязательны в policy.
- Doctor проверяет llms CLI как `--blog-dir` (не устаревший `--blog-path`).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Topic IDs dual-prefix: `AS##` и `B##`. Scout helper / today видят оба; next ID остаётся в серии `B##`. `--check-query` обязан ловить overlap с AS-пулом.

## Research

- `pain_solution_map` gate считает **только** строки таблицы внутри секции `## pain_solution_map` (≥3 data-rows после header). Пример строки: `| боль: … | решение: … | результат: … |`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Для git-committed `llms.txt` / `llms-full.txt` используй `--url-mode relative` (default) → `/blog/<slug>/`. Absolute `PUBLIC_SITE_URL` в артефактах ломает Cloud secret scanner.
- Если всё же пишешь absolute/redacted URL-строки: same-line `<!-- pragma: allowlist secret -->` (llms generator делает это при `--secret-pragma`, default on).
- `interlink-report.json`: `site_base` должен быть пустым/relative; скрипт больше не пишет absolute PUBLIC_SITE_URL в report.

## Cover / hero host

- `excalibur_blog_hero_reference_url.py` пробует hosts: catbox → 0x0 → litterbox → tmpfiles → uguu.
- При `--force` upload fail: сначала sha256-сравни существующий `reference_url_hosted` с локальным PNG; match = не blocker, reuse URL.

## Git / Cloud secret scanner

- Перед `git commit` в Cloud: `source scripts/excalibur_blog_sanitize_secret_names.sh` — фильтрует `CLOUD_AGENT_INJECTED_SECRET_NAMES` до bash identifiers.
- Ошибка `invalid variable name` на pre-commit = в списке секретов попал raw URL; sanitize, **не** `--no-verify`.
- `PUBLIC_SITE_URL` как Cloud Secret → не коммить absolute site URL без pragma / relative path / `[REDACTED]`.

## Publish / env bake

- `paramiko` обязателен для SSH publish. Bake: `requirements.txt` + `.cursor/Dockerfile` + `.cursor/cloud-agent-install.sh`.
- Preflight: `python3 scripts/excalibur_blog_doctor.py --publish` → FAIL если paramiko отсутствует (без `--publish` = WARN).
- Не ставь `pip install paramiko` как норму каждого run — это симптом сломанного environment build.