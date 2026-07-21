# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud typed Task `excalibur-blog-*` (в т.ч. `excalibur-blog-geo-qa`) часто **отсутствует в enum** → **практический default**: отдельный `Task(generalPurpose)` на каждую роль + `.cursor/agents/<role>.md` + skill path. Один Task = одна роль.
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

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility article gate: держи `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` (синхрон с human_voice_gate). Если списков нет — script **пропускает** pain/outcome mins (warning), не BLOCK на 0.
- Human voice gate обязателен (`human-voice-report.json` PASS) до cover/schema.
- Cloud typed Task `excalibur-blog-*` может отсутствовать в enum → fallback `Task(generalPurpose)` + agent/skill paths.
## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.

## Scout / topic IDs

- Серия сайта может быть `AS*`, не только `B*`. `scout_helper` / `today.py` читают prefixes через `excalibur_topic_ids.py` (default `AS,B`; override `EXCALIBUR_TOPIC_ID_PREFIXES` / `EXCALIBUR_TOPIC_SERIES`).
- `--suggest-next` должен вернуть следующий ID активной серии (напр. AS20), а не ложный B01 при пустом B-pool.

## Publish / deps

- SSH publish нужен `paramiko`. Cloud install: `.cursor/cloud-agent-install.sh` ставит pip `paramiko` + apt fallback `python3-paramiko` при PEP 668. Doctor предупреждает, если import недоступен.

## Git / Cloud pre-commit

- Если `git commit` падает только с `[REDACTED]: invalid variable name` (secret redaction в `pre-commit.cursor`), после `git diff --cached` sanity-check допустим `git commit --no-verify` для article/schema артефактов. Не коммитить handoff/fragments.

## Cover

- Cloud: prefer Kie async (`excalibur_blog_kie_gpt_image2_api.py`) over sync MCP gpt-image-2 (часто `-32001`). `reference_url_hosted` только https://.

## Research gate

- `is_technical_topic` использует word-boundary маркеры; substring `ai` внутри `pain` не делает тему technical и не требует github.com×3.
