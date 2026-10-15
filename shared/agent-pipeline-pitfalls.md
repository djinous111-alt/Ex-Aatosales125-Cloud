# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path. **Сразу**, без цикла ретраев typed enum.
- **geo-qa:** typed Task `excalibur-blog-geo-qa` часто отсутствует в Cloud enum — сразу `Task(generalPurpose)` (штатный путь, не exception).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat cluster-first: широкий parent → sibling/короткие seeds → длинный how-to. Пустой `{}` / `totalCount`-only без phrase rows = soft-fail (один retry sibling), таблица только из verified counts; не invent numbers. Узкий logistics jargon часто пустой при живом parent cluster.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен для SSH publish: ставится в `.cursor/cloud-agent-install.sh` + `requirements.txt`; doctor проверяет module.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Рекомендации в H2: предпочитай «Сделайте / Не делайте» (utility `recommendation_markers_ru`); «делать / не делать» тоже считается, но императив надёжнее для min_recommendation_markers≥8.
- CTA href = публичные `CATALOG_URL` / `TELEGRAM_URL`: перед commit `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` (исключает эти имена из secret-scan env). Не засоряй HTML pragma-комментариями ради RSS.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` обязан иметь непустые `pain_markers_ru` / `outcome_markers_ru` (utility gate fail-fast + doctor). Пустые списки → ложный BLOCKER на любой статье.

## Cover / Schema / Scout — git commit

- Cloud pre-commit падает с `invalid variable name`, если в `CLOUD_AGENT_*_SECRET_NAMES` есть non-identifier (`[REDACTED]`, raw URL, space-joined blob).
- Перед commit: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `eval "$(bash scripts/excalibur_blog_sanitize_secret_names.sh --export)"`.
- Schema JSON-LD: публичный site URL + registry `sameAs` обязательны; filter env исключает public URL secret names — не редактируй sameAs в `[REDACTED]`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Cloud image gen: **Kie-first** (`excalibur_blog_kie_gpt_image2_api.py`). Sync MCP `gpt-image-2` — max один вызов; после `-32001` без blind retry → Kie.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only / `{}` на узкий запрос = low-result signal, не fatal.
- Перед `git commit` topic card: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` / `--site-base` / `--out-dir` / `--redact-site-base`. Флага `--blog-path` нет (doctor проверяет `--blog-dir` + `--redact-site-base`).
