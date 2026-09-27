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

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only / `{}` / пустой список на узкий запрос = low-result signal, не fatal; fallback на parent, без выдуманных impressions.
- Topic ID для Авто-Сейлс — префикс `AS##`. `scout_helper.py --suggest-next` и `today.py` парсят `AS##`/`B##` (не только `B\\d+`).

## Research gate

- `accessed_at:` нужен как литерал в source_table (`accessed_at: YYYY-MM-DD`), не только дата в ячейке.
- `pain_solution_map` строки с маркерами pain/solution/result (или боль/решение/результат).
- Секция `## github_evidence` сама по себе не делает тему technical; GitHub≥3 требуется по topic card markers.

## Writer / Schema / secret-scan

- CTA: реальные URL + `<!-- pragma: allowlist secret -->` на той же строке; не `href="[REDACTED]"`.
- Перед commit: `export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(bash scripts/excalibur_blog_filter_secret_names.sh)"`.
- `schema.jsonld` в repo — relative `@id` / secret-scan-safe sameAs; publish может абсолютизировать.
- Utility markers: «Сделайте/Не делайте», «чеклист»; insight без ярлыка TL;DR; policy keys `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms CLI: `--blog-dir` / `--site-base` / `--out-dir` (**нет** `--blog-path`). Для commit-safe файлов: `--site-base ""` (relative `/blog/<slug>/`).
- Doctor check должен совпадать с `script --help`; не копируй устаревшие флаги из agent.md вслепую.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Нужен `paramiko` (`python3 -c "import paramiko"`); ставится через `.cursor/cloud-agent-install.sh` / Dockerfile.
- Committed publish artifacts: host → `[PUBLIC_SITE_URL]` (`sanitize_publish_artifacts.py` / publish script). Абсолютный permalink только в stdout/handoff.
