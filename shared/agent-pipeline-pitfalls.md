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
- `technical_topic` — word-boundary для коротких маркеров (`ai`, `ии`, `api`); поле `reader_pain` не должно давать false positive. Авто-how-to без tech не требует `github_urls >= 3`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Cloud install обязан ставить `paramiko` (`requirements.txt` / `.cursor/cloud-agent-install.sh`). `--env-check` проверяет `import paramiko`.

## Writer / Fact Check Box / CTA / utility

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA `href` только из env `CATALOG_URL` / `TELEGRAM_URL` / `MAX_URL`. Литерал `[REDACTED]` из brief в HTML запрещён (html-linter FAIL).
- Utility recommendation markers — точные строки policy: `сделайте`, `не делайте`, `чеклист` (не «Делать», не «чек-лист»).
- `editorial-policy.json` обязан иметь non-empty `pain_markers_ru` / `outcome_markers_ru` и `_markers_pinned: true`; иначе utility gate = POLICY BLOCK.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Cursor Cloud default: `python3 scripts/excalibur_blog_kie_gpt_image2_api.py` (async createTask→poll). Sync MCP `gpt-image-2` — legacy fallback; после `-32001` без URL/task_id не делай второй sync create.
- После split `excalibur_blog_cover_quad_split.py` по умолчанию PIL-штампует угол `avto-sales125.ru` на cover (+ TL canvas).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Перед выбором slug: `python3 scripts/excalibur_blog_scout_helper.py --check-query … --check-slug …` против `shared/wp-slug-denylist.json`. Нет файла → REST rebuild + incident.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: только `--blog-dir` + `--out-dir`; empty `--site-base ""` для relative `/blog/<slug>/` в git. Флаг `--blog-path` удалён — не использовать.

## Git / secrets scan

- Cloud commits: `bash scripts/excalibur_git.sh commit …` или `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` перед `git commit`. Иначе pre-commit падает на non-identifier secret names / публичных CTA URL.
