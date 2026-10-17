# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **сразу** fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; **не** крутить retry typed Task (в т.ч. `excalibur-blog-geo-qa`).
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
- `paramiko` обязателен для SSH publish: cloud install ставит `requirements.txt`; `--env-check` теперь проверяет `paramiko_importable`.
- HTTP bootstrap trigger / WebFetch wait = **300s** (не 120). Remote bootstrap удаляется только после `OK post=` — при timeout оставляй файл для retry.
- Дата в ledger: `EXCALIBUR_RUN_DATE`, не слепой `date.today()` с отстающих Cloud VM.

## Schema / secret scan

- В `schema.jsonld` URL-поля (`url`, `@id`, `sameAs`), совпадающие с Cloud Secrets (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`), нуждаются в same-line `pragma: allowlist secret` (через `"_a": "pragma: allowlist secret"` рядом с полем).
- Коммиты только через `bash scripts/excalibur_git.sh` — wrapper отфильтровывает public CTA/site names и невалидные токены из `CLOUD_AGENT_INJECTED_SECRET_NAMES`.

## Research / tech gate

- `research_notes_gate` детектит tech-нишу по **word-boundary**, не substring: `ai`/`ии` внутри `reader_pain` / `ожидании` не делают тему технической.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Перед обвинением текста: проверь `memory/brief/editorial-policy.json` — `pain_markers_ru` / `outcome_markers_ru` не пустые. Пустые списки = policy error, не «слабо раскрыта боль».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `excalibur_blog_scout_helper.py --suggest-next` обязан учитывать `memory/topics/live-reserved.json` (`reserved[]` + `next_forced_topic_id`), иначе предложит уже живой B01 после WP publish.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--site-base` + `--out-dir` (флага `--blog-path` нет; doctor проверяет `--blog-dir`).
