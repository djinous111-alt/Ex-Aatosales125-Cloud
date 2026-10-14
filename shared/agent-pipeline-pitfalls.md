# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Особенно часто отсутствует typed `excalibur-blog-geo-qa` — Director сразу запускает `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md` (не тратить шаг на typed enum).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Commits: `bash scripts/excalibur_git.sh` — фильтрует невалидные имена в `CLOUD_AGENT_*_SECRET_NAMES` (иначе pre-commit падает).

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research gate: ≥5 `accessed_at:` labels и/или ISO-даты в URL-строках `source_table`; одного заголовка колонки `accessed_at` недостаточно. Рекомендуется `## source_access_log`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Schema/llms commit = `[REDACTED]` для secret URL bases; publish `expand_schema_redacted` перед WP meta / deploy.
- HTTP timeout на ~7MB bootstrap: REST soft-success by slug, не второй curl; bootstrap не удалять до `OK post=`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru` (doctor FAIL если пусто). Не вырезать маркеры при rebrand/sync.
- Link-verify: catalog CTA 5xx при `href == CATALOG_URL` и SSL timeout на egrul/kad.arbitr — soft-pass (не переписывать статью).

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Hero reference: не `--force` reupload, если уже есть WP media URL; catbox/0x0 часто 412/503, prompt требует stable WP host.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms CLI: только `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- Generator redacts live site-base → `[REDACTED]` в committed llms*.txt.
