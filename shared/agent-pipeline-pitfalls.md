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

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Cloud boot обязан ставить `paramiko` (`.cursor/cloud-agent-install.sh` + `requirements.txt`). Если `ModuleNotFoundError: paramiko` — это install drift, не «опциональная» зависимость.
- `memory/site.env.local` для bash `source`: значения со спецсимволами в **одинарных кавычках**. Publish/doctor читают process env (Cloud Secrets) приоритетнее файла и снимают кавычки в Python.

## Git / Cloud secret scan

- Перед `git commit`: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` — отфильтрует невалидные bash-идентификаторы и публичные marketing URL secrets (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`, …).
- Не коммить live host в `memory/blog/interlink-suggestions.json` / `llms.txt`: interlinker redacts absolute `http(s)` `site_base`; llms generator — `--site-base ""` для relative `/blog/<slug>/`.
- В `article.html` / `schema.jsonld` публичные CTA/sameAs URL допустимы; при ложном secret-scan блоке используй filter-скрипт выше (не `--no-verify`).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` обязан иметь непустые `pain_markers_ru` / `outcome_markers_ru` (doctor + utility gate fail-fast). Не коммить `href="[REDACTED]"` в `article.html` до link-verify.

## Research

- `source_table`: колонка `accessed_at` может быть ISO-датой в строке с URL **или** токеном `accessed_at: YYYY-MM-DD` — gate считает оба стиля.
- `technical_topic` не срабатывает на подстроку «ии» внутри обычных RU слов; auto-niche (Япония/Корея/Китай) не требует GitHub evidence.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms CLI: `--blog-dir` / `--site-base` / `--out-dir` — **нет** `--blog-path`.
