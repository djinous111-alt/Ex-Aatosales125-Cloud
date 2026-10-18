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
- `--env-check` обязан `import paramiko` когда SSH сконфигурирован; install script ставит deps из `requirements.txt`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP bootstrap wait для крупных PHP payload: default **300s** (не 120s).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- **Запрещён** литерал `href="[REDACTED]"` в `article.html`. CTA = абсолютные https URL из conversion-map / `PUBLIC_SITE_URL` / prior PASS article. HTML linter + link-verify блокируют redacted placeholders.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` не должны быть пустыми (`_markers_pinned`). Empty list → utility_gate skip+warning; doctor fail если списки отсутствуют/пусты после rebrand.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Никогда не параллелить `Write(quad-manifest.json)` с `excalibur_blog_cover_quad_prompt.py --write-batch`. Сначала сохранить manifest, потом prompt/batch; проверить hook в `quad-mcp-prompt.txt` до Kie.
- Prompt builder берёт prefix/negative/outfit из style JSON + design-code + blog-hero; hardcode Excalibur/SEO/white hoodie запрещён.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Ниша Авто-Сейлс: не дрейфовать в Cursor/Make/n8n/ИИ-агентов; ориентир `memory/brief/site-brief.md`.
- `--suggest-next` читает `memory/topics/live-reserved.json` → `next_forced_topic_id`, если id ещё не в ledger/active dirs. Формат: `{"next_forced_topic_id":"B09", ...}`.

## Research

- `research_notes_gate` помечает technical_topic только по word-boundary маркерам в topic fields; substring `ai`/`ии` внутри `reader_pain`/`комплектации` не должен требовать GitHub.
- Строки `pain_solution_map` считаются как data-rows секции-таблицы, не по substring pain|solution по всему файлу.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (НЕ `--blog-path`). Doctor проверяет актуальные флаги.

## Git / Cloud secrets

- Если pre-commit Secrets Scanner падает с `invalid variable name` на `${!SECRET_NAME}`: в `CLOUD_AGENT_INJECTED_SECRET_NAMES` / `CLOUD_AGENT_ALL_SECRET_NAMES` есть не-identifier (URL-like). Workaround: отфильтровать список до `^[A-Za-z_][A-Za-z0-9_]*$` перед commit; `--no-verify` только как last resort + INC `needs-human` на Cloud Dashboard secret names.
