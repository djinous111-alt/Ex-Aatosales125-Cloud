# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- В т.ч. `excalibur-blog-geo-qa`: если typed Task отсутствует — сразу generalPurpose с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md` (штатный fallback, не ad-hoc).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research-serp.json` не должен содержать абсолютный `PUBLIC_SITE_URL` (скрипт redacts → `[PUBLIC_SITE_URL]`).
- `technical_topic` gate: короткие маркеры `ai`/`ии` только word-boundary; поля `reader_pain` сами по себе не делают тему technical.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- Нужен `paramiko` (install: `.cursor/cloud-agent-install.sh` / Dockerfile / `requirements.txt`). Doctor проверяет модуль.
- Если Cloud Secrets только в process env — перед publish создай gitignored `memory/site.env.local` с unquoted `KEY=value` (не bash-source пароли с metacharacters). `SSH_ROOT=.` предпочтителен.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Schema/llms в git — placeholders (`[PUBLIC_SITE_URL]`…); publish expand-ит schema meta перед upload.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным.
- В generation prompt запрещай insults без перечисления banned tokens (`лох` и т.п. в prompt рискует отрисовкой моделью). QA картинки может отдельно блокировать эти слова на финальном PNG.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `--suggest-next` обязан учитывать ledger reserved + active dirs + LIVE snapshot (`memory/blog/published-live-*.json`). Перед новой карточкой: `--check-slug`.

## Indexer / git commits

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` (не `--blog-path`; alias deprecated).
- Коммиты: `bash scripts/excalibur_git.sh commit …` — sanitize non-identifier secret names и skip `PUBLIC_SITE_URL`/`WP_*` false positives.
- Cloud Secrets names must be bash identifiers (`A-Za-z_[A-Za-z0-9_]*`); URL-as-name ломает pre-commit `${!name}`.
