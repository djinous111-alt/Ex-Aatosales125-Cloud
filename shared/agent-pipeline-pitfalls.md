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
- В `source_table` колонка `accessed_at`: канон **`accessed_at: YYYY-MM-DD`** (с двоеточием). Gate также принимает голый ISO в этой колонке, но префикс — предпочтителен.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен для SSH publish: bake в `.cursor/Dockerfile` + `.cursor/cloud-agent-install.sh`; doctor проверяет `paramiko available`. Не ставить вручную каждый run.
- Cloud Secret `SSH_ROOT=.` предпочтителен, чтобы `--env-check` не показывал `root: unset`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## Writer / utility markers

- Utility gate считает `recommendation_markers_ru` буквально: `не делайте`, `чеклист` (без дефиса), `сделайте`, `проверьте`… Заголовки «Делать/Не делать» и «чек-лист» сами по себе **не** набирают `min_recommendation_markers`.
- `pain_markers_ru` / `outcome_markers_ru` должны быть в `memory/brief/editorial-policy.json` (выровнены с human-voice). Пустые списки → utility_gate пропускает pain/outcome check с warning, не BLOCK на count=0.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Doctor/llms: generator CLI flag is `--blog-dir`, not `--blog-path`.

## Git / pre-commit

- Cursor Cloud hook `pre-commit.cursor` may fail with `invalid variable name` on `${!SECRET_NAME}` when `CLOUD_AGENT_INJECTED_SECRET_NAMES` has empty/invalid entries. Env-side fix needed. Workaround: after reviewing staged files for secrets, `git commit --no-verify` is allowed for that exact error only.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Kie/MCP **402 Credits**: не retry-loop. Emergency **§4b** (`skills/cover-excalibur-blog/SKILL.md`): ONE GenerateImage 16:9 → LANCZOS 2048×1152 → `cover_quad_split --inject-html`. Top-up Kie — human/env; пайплайн продолжать через §4b.
- На canvas не рисовать фейковые суммы пошлины / `%` / `₽`, если редакция запрещает статический прайс.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: только `--blog-dir` (не `--blog-path`; argparse отклоняет).
