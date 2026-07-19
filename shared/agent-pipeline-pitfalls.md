# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud/Automation часто **не** принимает `excalibur-blog-*` как typed Task types → это ожидаемый режим, не разовый сбой.
- **Постоянный fallback:** отдельный `Task(generalPurpose)` на каждую роль + пути `.cursor/agents/<role>.md` и `.cursor/skills/<skill>/SKILL.md` (короткий контракт: вход, маркер результата, запреты). Один Task = одна роль.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Если недоступен даже `generalPurpose` → терминальный блокер single-agent pipeline.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Topic IDs: `B\d+` и `AS\d+` — today/scout_helper обязаны матчить `(?:AS|B)\d+`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat: длинный secondary может вернуть пустой/`totalCount`-only → укороти query (cluster-first) и ретрай; пустой ответ не блокирует research.
- Research notes gate: tech markers с word-boundary (`ai`/`ии` не ловят «pain»/«компании»); GitHub ≥3 только для tech-карточек, не для автологистики.

## Pre-commit / secrets scrub

- Cloud `pre-commit.cursor` / `commit-msg.cursor` падают с `invalid variable name`, если в `CLOUD_AGENT_INJECTED_SECRET_NAMES` есть невалидный bash-идентификатор.
- На install/до commit: `bash scripts/excalibur_blog_patch_cursor_precommit.sh` (идемпотентно skip non-identifier names).
- Если patch ещё не применён и hook снова abort — допустим safe `--no-verify` только для артефактов без handoff/секретов; заведи/обнови incident; попроси человека починить Dashboard secret names.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Нужен пакет `paramiko` (Dockerfile + `.cursor/cloud-agent-install.sh`); если import падает — `pip3 install --break-system-packages paramiko`.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- Cloud Secret `SSH_PATH` алиасится в `SSH_ROOT` внутри `load_env`; предпочтительно задать `SSH_ROOT` явно (часто `.`).
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning.
- Ledger (`shared/published-articles.md`): строки topic только **внутри** первой markdown table; prose/blockquote — после таблицы. `research_start` / `upsert_publish_ledger` используют table-aware upsert.
- Publish без обновления ledger → следующий прогон может дублировать slug.

## Writer / utility / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` в editorial-policy должны быть non-empty; пустой список → fallback на те же дефолты, что human_voice_gate (иначе pain/outcome=0 на всех статьях).
- Карточка темы: до append в `blog-topics.md` проверь utility gate — в `h1` или `primary_query` обязателен маркер (`как` / чек-лист / сравнен / …).

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- llms generator CLI: `--blog-dir`, не `--blog-path` (doctor проверяет `--blog-dir`).

## Cover

- Preferred: `python3 scripts/excalibur_blog_kie_gpt_image2_api.py` (ONE gpt-image-2 i2i, max_wait ≥900s). На Kie `failCode=500` скрипт ретраит один create+poll; затем MCP fallback. Не запускай 4 отдельных image jobs.
- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Перед append карточки: `h1`/`primary_query` с utility-маркером; topic_id может быть `AS##` или `B##`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms: только `--blog-dir memory/blog/articles`.
