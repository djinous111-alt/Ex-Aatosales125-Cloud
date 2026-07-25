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
- Dry-run fail-fast без `cover/cover.png` + `cover-registry.json` (exit 2); resume: cover → publish.

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
- Kie createTask `402 Credits insufficient` → needs-human top-up `KIE_API_KEY`; сохраняй quad-mcp-batch, не выдумывай cover.png.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Research

- Wordstat `{"totalCount":"..."}` без phrase list → `WORDSTAT PARTIAL`: retry без regions / шире формулировка; не выдумывай impressions.
- `research_notes_gate.py -o research-notes-gate.json` — путь относителен к `--article-dir`, не к корню репо.

## Writer / CTA

- CTA href из env (`CATALOG_URL` / `TELEGRAM_URL`) + `<!-- pragma: allowlist secret -->`; не коммить `shared/public-cta.json` с живыми URL при Cloud Secrets.
- Recommendation markers = императив (`Сделайте` / `Не делайте`); `Делать:` / `Не делать:` utility gate не засчитывает.
- Пустые `pain_markers_ru` / `outcome_markers_ru` / `recommendation_markers_ru` в editorial-policy → utility gate fail-fast на policy.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `--blog-path` = алиас `--blog-dir` (filesystem). Никогда `--blog-path /` — это не WP URL path; перезапишет llms пустым индексом. Используй `--blog-dir memory/blog/articles`.

## Topic IDs / Cloud image

- today/scout helper принимают topic_id `(?:B|AS)\d+`.
- Doctor требует numpy: `python3-numpy` в Dockerfile + pip fallback в `cloud-agent-install.sh`.

