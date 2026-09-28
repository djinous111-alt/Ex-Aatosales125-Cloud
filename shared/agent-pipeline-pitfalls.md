# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **канонический** fallback: сразу `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path (не тратить шаги на retry typed Task). Особенно часто отсутствует typed `excalibur-blog-geo-qa`.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Перед `git commit` в Cloud: `source scripts/sanitize_cloud_secret_names.sh` — host pre-commit падает на `${!SECRET_NAME}`, если в `CLOUD_AGENT_INJECTED_SECRET_NAMES` после redact попали невалидные bash-идентификаторы.

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
- `paramiko` обязателен для SSH publish: должен быть в `.cursor/Dockerfile` / `cloud-agent-install.sh`. Если `ModuleNotFoundError` — `pip3 install --break-system-packages paramiko`, затем зафиксировать в image install.
- `SSH_ROOT` unset → скрипт использует `.` (login cwd) как default (`root: default-dot` в `--env-check`). Если bootstrap ENOENT на непустом root — retry на `.` + warning; обнови Cloud Secret на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` / `recommendation_markers_ru` должны жить в `memory/brief/editorial-policy.json`; если списки пустые — скрипт берёт defaults (синхрон с human-voice). Regression: `python3 scripts/excalibur_blog_utility_gate.py --self-test`.
- Research notes gate: `technical_topic` использует word-boundary для коротких маркеров (`ai`/`api`/`rag`); обязательные поля вроде `reader_pain` / `github_evidence` не должны сами по себе включать tech-режим.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `excalibur_blog_scout_helper.py` парсит карточки `## B\\d+` и `## AS\\d+` (любые `[A-Za-z]+\\d+`). `--check-query` обязан видеть AS-пул; `--suggest-next` предлагает следующий **B**-id, но печатает AS pool IDs.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` нет). Doctor проверяет `--blog-dir`/`--out-dir`.
