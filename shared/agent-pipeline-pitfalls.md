# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Особенно часто отсутствует typed `excalibur-blog-geo-qa` (и другие роли): Директор **сразу** запускает `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md`, не ретрая typed name.
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
- `--env-check` / doctor требуют `paramiko`; install: `pip install -r requirements.txt` (cloud-agent-install.sh + Dockerfile).
- Если `memory/site.env.local` отсутствует, publish-скрипт создаёт gitignored файл из process env / Cloud Secrets; `SSH_ROOT` по умолчанию `.`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP trigger / WebFetch poll: `HTTP_TRIGGER_TIMEOUT_SEC` / `FALLBACK_POLL_SEC` (default **300**). После timeout — REST reconstruct by slug; **не** второй bootstrap trigger, пока slug LIVE.
- WebFetch fallback нужен **параллельный** watcher, пишущий `memory/webfetch-response.txt`; иначе REST reconstruct.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA `href` только из `$CATALOG_URL` / `$TELEGRAM_URL` (+ conversion-map). Литерал `[REDACTED]` в href запрещён; при secret-scan — `<!-- pragma: allowlist secret -->` на строке CTA.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` (align human-voice). Пустые списки → fallback markers, не вечный BLOCK.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Cloud default image flow: Kie async (`excalibur_blog_kie_gpt_image2_api.py`) при наличии `KIE_API_KEY`. Sync MCP `-32001` → один Kie async recovery, без слепого второго sync create.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- LIVE dedup: `python3 scripts/excalibur_blog_scout_helper.py --live-slugs` через `PUBLIC_SITE_URL` REST. MCP-KV `wordpress_*` не авторитетен.

## Research

- `technical_topic` в research-notes-gate: TECH markers матчятся token/stem-границей, не substring (`ai` ≠ `reader_pain`, `ии` ≠ `гарантии`).
- Wordstat empty `{}` на primary (не 401) = low-volume quirk: secondary/broad phrases + `n/a` row; не invent impressions.
- Пустой `research-serp.json` → WebSearch/WebFetch как реальный SERP (soft-fail dump).
- Gate: `accessed_at: YYYY-MM-DD` label в source_table; pain_solution_map rows с `боль:`/`решение:`/`результат:`.

## Git / secrets

- Перед commit в Cloud: `bash scripts/excalibur_git.sh commit …` или `eval "$(bash scripts/excalibur_git.sh print-filter)"` — отфильтровать invalid names в `CLOUD_AGENT_*_SECRET_NAMES` (иначе pre-commit.cursor → `invalid variable name`).
- `--no-verify` только если hook всё ещё падает после filter и staged paths проверены на отсутствие private keys/tokens.
- Публичные marketing URL (`PUBLIC_SITE_URL`, catalog/Telegram) лучше не держать как Cloud Secrets. В `schema.jsonld` **не** подставляй `[REDACTED]` — коммить абсолютные публичные URL через `excalibur_git.sh` (или `--no-verify` после проверки).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (+ `--site-base`). Флага `--blog-path` нет; doctor проверяет `--blog-dir`/`--out-dir`.
