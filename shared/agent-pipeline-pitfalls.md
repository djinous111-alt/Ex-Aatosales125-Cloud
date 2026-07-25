# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types (в т.ч. `excalibur-blog-geo-qa`) → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path. Это канон до восстановления typed enum, не повод стопать пайплайн.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research_notes_gate` technical_topic: word-boundary маркеры; `ai`⊂`pain` / `ии`⊂«Японии» — не tech. Не-tech тема не обязана иметь 3 GitHub URL.

## Scout / topic_id floor

- `--suggest-next` = max(pool Bxx, `memory/blog/articles/Bxx-*`, ledger, `memory/scout-topic-id-floor.json`, env `EXCALIBUR_TOPIC_ID_FLOOR` / `EXCALIBUR_RECENT_WP_TOPIC_IDS`) + 1.
- AS-only pool при live WP на B05+ ≠ начинать с B01. После publish обновляй floor watermark.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен для SSH publish: ставится в `.cursor/Dockerfile` и `.cursor/cloud-agent-install.sh`; doctor WARN/FAIL без модуля.

## Writer / Fact Check Box / CTA

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA URL: `shared/public-cta.json` или conversion-map через python/shell. **Запрещён** литерал `[REDACTED]` в `href` (secret-scrub). `link_verify` падает на scrubbed href.
- Utility gate читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json`. Пустой список = WARN (skip), не вечный BLOCK с 0 hits.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Schema/Writer: URL из registry/site-brief читай python-байтами, не scrubbed Read — иначе `[REDACTED]` в JSON-LD/HTML.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- MCP/Kie 402 Credits → emergency §4b: один `GenerateImage` 16:9 → LANCZOS 2048×1152 → `quad_apply.py --local-canvas`. Top-up Kie — needs-human/ops.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: `--blog-dir` (не `--blog-path`); default `--url-mode relative` для git-safe `/blog/<slug>/`. Absolute + `PUBLIC_SITE_URL` часто ломает secret-scan.
- Pre-commit `invalid variable name`: в Cloud Secrets имя не bash-identifier (URL-as-name) — удалить/переименовать в Dashboard; `--no-verify` только после review staged secrets.
