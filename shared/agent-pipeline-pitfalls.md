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
- `research_notes_gate`: короткие TECH_MARKERS (`ai`/`ии`/`api`) — только whole-word; авто-темы с `reader_pain`/`комплектации` не требуют GitHub. Non-tech: `github_evidence` = docs/community ок.
- Source table: колонка `accessed_at` с ISO-датами засчитывается gate (не только `accessed_at:`).

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- `paramiko` должен быть в Cloud image (Dockerfile + `cloud-agent-install.sh`); без него SSH publish падает на import.
- SSH root: Cloud Secret `SSH_ROOT=.`. Если unset, publish defaults to `.`; если bootstrap ENOENT на non-dot root — retry `.` + warning.

## Secrets / pre-commit

- Имена Cloud Secrets — только bash-safe: `[A-Za-z_][A-Za-z0-9_]*` (без пробелов, `/`, URL-shaped имён).
- Pre-commit `invalid variable name` = platform hook разворачивает невалидное имя секрета. Проверь staged files; временный `--no-verify` допустим только после проверки diff. Durable: переименуй секреты в Dashboard. Advisory: `python3 scripts/excalibur_blog_check_secret_names.py`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: реальные https URL из conversion-map. **Запрещён** литерал `[REDACTED]` в `href` статьи; redaction — только для логов/handoff.
- Utility/HV маркеры боли/результата/action живут в `memory/brief/editorial-policy.json`; utility_gate имеет built-in fallback, если списки пусты.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Image path: MCP gpt-image-2 → Kie API → emergency `GenerateImage` + resize 2048×1152 + `quad_apply --canvas-local`. HTTP 402 credits → не спамить createTask; top-up `KIE_API_KEY` (human) или emergency fallback.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
