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
- Publish HTTP gateway 504 on large cover+inline PHP (~7MB): script falls back to SSH CLI `/usr/local/bin/php8.1` (Beget default `php` is 5.6 and cannot boot modern WP). Override with `EXCALIBUR_BLOG_PHP_BIN`; force CLI with `EXCALIBUR_BLOG_PUBLISH_FORCE_SSH_CLI=yes`.

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
- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` больше нет).

## Research notes gate

- `technical_topic` определяется по полям topic card (h1/query/slug), не по телу notes: голый substring `ai`/`ии` давал false positive на `reader_pain` / «декларации».
- Строки `pain_solution_map` должны содержать `боль|pain|решение|solution|результат|result`, иначе row counter = 0.
- GitHub evidence (≥3 URL) обязателен только для technical topics; auto/import и прочие non-tech ниши — community/official docs достаточно.

## Utility / editorial policy

- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` и `outcome_markers_ru` (+ mins в `article_required_signals`). Doctor это проверяет.

## Cloud pre-commit / secrets

- Перед commit: `source scripts/sanitize_cloud_secret_names.sh`. Для schema/llms: `EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 source …`.
- Public CTA в HTML: `<!-- pragma: allowlist secret -->` на строке с href.
- Secret names только bash identifiers; не инжектить raw URL как имя.

## Publish deps / gateway

- `paramiko` обязателен для SSH publish; ставится через `.cursor/cloud-agent-install.sh` / `requirements.txt`.
- HTTP gateway 504 на большом PHP payload → SSH CLI php fallback (`EXCALIBUR_BLOG_PUBLISH_FORCE_SSH_CLI=yes`).
