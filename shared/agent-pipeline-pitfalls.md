# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud часто **не** принимает typed `excalibur-blog-*` (включая `excalibur-blog-geo-qa`) → **default** сразу `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path + короткий контракт (входы, маркер, запреты). Не тратить run на discovery enum.
- Parent-agent сам пишет статью вместо writer Task → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- WebFetch 5xx/504 на конкуренте → soft: WebSearch highlights + ≥2 независимых источника; не блокер notes.
- В notes/serp внутренние URL: relative или `[PUBLIC_SITE_URL]`, не сырой secret.

## Git / secrets scan

- Commits предпочтительно через `bash scripts/excalibur_git.sh …` — фильтрует `CLOUD_AGENT_*_SECRET_NAMES` до валидных bash identifiers (`^[A-Za-z_][A-Za-z0-9_]*$`), CSV через запятую.
- Не коммитить live `PUBLIC_SITE_URL`/`CATALOG_URL`/`TELEGRAM_URL` в schema/llms/interlink/research; пиши `[REDACTED]`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Cloud install обязан ставить `paramiko` (`requirements.txt` + `.cursor/cloud-agent-install.sh` с `--break-system-packages`).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru` (doctor FAIL если пусто). utility_gate при пустых списках — WARN/skip, не ложный BLOCK статьи.
- Catalog CTA HTTP 5xx при `href == CATALOG_URL` → link-verify soft-pass + warning (не fail).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Ниша = Авто-Сейлс из `memory/brief/site-brief.md` (Япония/Корея/Китай, растаможка, СВХ). Не AI/Cursor/Make.
- Topic IDs: `AS*` (legacy pool) и `B*` (новые карточки). today.py / scout_helper принимают оба префикса.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms CLI: только `--blog-dir` (флага `--blog-path` нет). doctor проверяет `--blog-dir` и отсутствие `--blog-path`.
