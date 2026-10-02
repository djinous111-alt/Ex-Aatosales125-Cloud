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
- Tech markers в `research_notes_gate` — word-boundary для коротких токенов (`ии`/`ai`/`api`); «японии» ≠ technical topic.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root: пустой/`ENOENT` → login cwd `.`; держи `SSH_ROOT=.` в Cloud Secrets для этого хоста.
- `paramiko` должен быть в `.cursor/cloud-agent-install.sh` и `requirements.txt`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA в git: `href="[REDACTED]"`. Перед link-verify/publish: `python3 scripts/excalibur_blog_cta_expand.py --article-dir <dir> --mode expand`, после — `--mode redact`. Альтернатива для commit live URL: `source scripts/sanitize_cloud_secret_names.sh` + same-line `<!-- pragma: allowlist secret -->`.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- Typed Task `excalibur-blog-geo-qa` может отсутствовать в Cloud enum → сразу `Task(generalPurpose)` + `.cursor/agents/excalibur-blog-geo-qa.md` + skill (не тратить retry на typed name).
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- После sync/rebrand: non-empty `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` (doctor FAIL если пусто). Utility gate skip-when-empty (`--self-test`).
- CTA `[REDACTED]` — не writer corruption: expand → link-verify → re-redact.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Нет default white hoodie: outfit = weather + topic из scene_hint / blog-hero; Kie async i2i first (один quad job).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Helper парсит `## AS\d+` и `## B\d+`; `--suggest-next` читает `memory/topics/live-wp-occupied-ids.json` и не предлагает `occupied_topic_ids` / live slugs.
- Для Авто-Сейлс перед новой темой сверь live WP: `PUBLIC_SITE_URL/wp-json/wp/v2/posts?per_page=30&_fields=id,slug,title,date`.

## Commit / Cloud secrets

- Перед каждым `git commit`: `source scripts/sanitize_cloud_secret_names.sh` (иначе `[REDACTED]: invalid variable name` в pre-commit).
- `CLOUD_AGENT_*_SECRET_NAMES` должны содержать только shell identifiers; raw URL / `[REDACTED]` в списке имён — баг Dashboard Secrets (нужен human cleanup).
- Schema JSON-LD / llms: для git либо `[REDACTED]` site-base, либо same-line pragma allowlist (`"_scan": "pragma: allowlist secret"` / `<!-- pragma: allowlist secret -->`).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- Commit pattern: generate with real `--site-base` for runtime → redact/`[REDACTED]` для git → restore before publish.
