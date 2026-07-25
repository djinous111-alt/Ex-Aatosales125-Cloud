# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types (в т.ч. `excalibur-blog-geo-qa`) → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path. Repo не контролирует Cloud Task enum.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `today.py` / `scout_helper.py` парсят topic_id `(?:B|AS)\d+` — AS-пул в `blog-topics.md` должен быть видим для suggest/check-query.
- Research `accessed_at`: литералы `accessed_at: YYYY-MM-DD` **или** ISO-даты в строках `source_table` с URL; плейсхолдеры `<today>`/TBD не засчитываются.
- `technical_topic` не должен включаться только из‑за секции `github_evidence` / упоминаний api в evidence.

## Pre-commit / secrets

- `CLOUD_AGENT_INJECTED_SECRET_NAMES` обязан содержать только bash-идентификаторы `^[A-Za-z_][A-Za-z0-9_]*$`. Raw URL в списке → skip (см. live `pre-commit.cursor` + `scripts/excalibur_blog_precommit_secret_name_guard.sh`).
- Публичные marketing URL (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) лучше **не** держать в Cursor Secrets — иначе schema/registry false-positive на commit. Needs-human: Dashboard config.
- Workaround при сломанном имени: `CLOUD_AGENT_INJECTED_SECRET_NAMES="" git commit` только как аварийный путь; durable fix — валидные имена + публичные URL вне Secrets.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Recommendation markers (`сделайте`/`не делайте`/…), ≥3 outcome, ≥2 pain; слово `FAQ` только в H2 «Частые вопросы»; insight без `TL;DR`/`Быстрый инсайт`.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- H2 не должен содержать подстроку `faq` / «частые вопрос» кроме единственного `<h2>Частые вопросы</h2>` (иначе html-linter = duplicate FAQ).
- Insight-блок: не начинать с ярлыков `TL;DR` / `Быстрый инсайт`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` обязаны быть в `memory/brief/editorial-policy.json`; пустой список больше не должен давать ложный BLOCK (скрипт skip), но маркеры должны оставаться в policy.
- Cloud typed Task `excalibur-blog-*` может отсутствовать в enum → `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Primary path: `python3 scripts/excalibur_blog_kie_gpt_image2_api.py` (async). Sync MCP — fallback.
- Kie `code=402` / credits insufficient → **needs-human** top-up `KIE_API_KEY` billing; не фабриковать canvas/cover.
- MCP `NoneType…get` без URL часто = upstream 402/auth; подтверди через Kie script, не делай слепой третий create.
- Cover deps: Pillow + numpy (`requirements.txt` / `.cursor/cloud-agent-install.sh`).

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- AS* и B* карточки оба в пуле; не дублируй AS→B только потому что today.py «не видит» AS (после fix regex).

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-path /blog` (default), не путать с `--blog-dir`. Doctor проверяет наличие флага `--blog-path`.
