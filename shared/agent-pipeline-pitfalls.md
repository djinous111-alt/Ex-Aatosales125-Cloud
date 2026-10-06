# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Typed `excalibur-blog-*` (включая geo-qa) часто недоступны в Cloud API → сразу `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; это ожидаемый путь, не ошибка.
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
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен для SSH publish: ставится в `.cursor/cloud-agent-install.sh` / `requirements.txt`. Если `import paramiko` падает — `pip3 install --break-system-packages paramiko`, затем чини install script.
- Перед commit с публичными URL в schema/artifacts: `source scripts/sanitize_cloud_secret_names.sh` или `scripts/excalibur_git.sh commit` (фильтрует не-bash «имена» секретов). В JSON-LD — `"x-excalibur-scan": "pragma: allowlist secret"` на node с публичным URL.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- CTA `href="[REDACTED]"` запрещён: html-linter BLOCK; бери `CATALOG_URL` / `TELEGRAM_URL` из env/conversion map.
- Utility gate читает `pain_markers_ru` / `outcome_markers_ru` из `memory/brief/editorial-policy.json`; human-voice использует тот же policy (fallback defaults в скрипте). Пустые списки = warning/skip, не silent 0 hits. Doctor проверяет non-empty.

## Research

- `research_notes_gate` не считает короткий маркер `ии` substring-ом (false positive в «...ции»). Для non-tech тем GitHub не обязателен.
- В source_table пиши `accessed_at: YYYY-MM-DD` в ячейке, не только голую дату.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- `cover-prompts.json` topics.<id> применяется только при совпадении `slug` с текущей статьёй; иначе — meta/H2. Не оставляй stale SEO B01 (`primer-seo-stati`) после смены темы.
- `quad_manifest.py --merge` игнорирует preserve с другим slug и не подмешивает Wordstat SEO defaults в auto/ГИБДД нишу.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `scout_helper --check-query` учитывает ledger + blog-topics (AS*/B*) + `memory/blog/published-live*.json`. AS* в pool ≠ свободно, если slug/title пересекается с live WP.
- Перед needs_scout обновляй live-snapshot, если ledger неполный.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
