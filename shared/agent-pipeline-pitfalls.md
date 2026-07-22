# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата / topic_id

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Topic IDs: **AS**\* (Avto-Sales) и legacy **B**\* — общий модуль `scripts/excalibur_topic_ids.py` (не матчить только `B\\d+`).
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Research-notes gate: short tech markers (`ai`, `ии`, `api`…) — whole-word; «Hyundai»/«комплектации» ≠ technical.
- В `source_table` нужен литерал `accessed_at: YYYY-MM-DD`; в pain_map data-строках — токены pain/solution/result.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH publish требует **paramiko** (`requirements.txt` + `.cursor/cloud-agent-install.sh` / Dockerfile). Doctor WARN/FAIL если нет модуля при allow_publish.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box / CTA

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: живые catalog/Telegram href + `<!-- pragma: allowlist secret -->` на той же строке/абзаце; не `[REDACTED]` в article.html (ломает link-verify).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate считает pain/outcome markers из editorial-policy (fallback human-voice). Пустые списки без fallback больше не false-BLOCK.
- `link_verify.py` редактирует secret URL values в отчёте → `[REDACTED]` для commit-safe GEO QA.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Перед createTask: `kie_gpt_image2_api.py --credits-only --min-credits 2.0`. При 402/insufficient → emergency GenerateImage → 2048×1152 → split; top-up Kie = needs-human.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator: только `--blog-dir` (флага `--blog-path` нет).
- URL-строки в llms/promotion при Cloud Secret `PUBLIC_SITE_URL` — с `pragma: allowlist secret`.

## Cloud Secrets / pre-commit

- Имена секретов должны быть bash-идентификаторами (`^[A-Za-z_][A-Za-z0-9_]*$`). URL-shaped secret *names* ломают `${!SECRET_NAME}` в pre-commit → `scripts/excalibur_blog_patch_precommit_secret_scan.sh` (вызывается из install).
- Предпочтительно переименовать такие secrets в Dashboard (например `PUBLIC_SITE_URL` вместо URL-as-name) — это needs-human.
