# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Особенно часто typed `excalibur-blog-geo-qa` недоступен — сразу `Task(generalPurpose)` с geo-qa agent/skill; это штатный путь, не блокер.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.
- Перед `git commit`, если pre-commit падает на `invalid variable name`: `eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"`. CTA/schema/llms строки с публичными marketing URL — с `pragma: allowlist secret`.

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
- Большой bootstrap HTTP может уйти в timeout, пока PHP ещё работает: скрипт поллит WP REST by slug (soft-success) параллельно с WebFetch wait. **Не** делай второй curl bootstrap.
- `paramiko` обязателен для SSH publish; Cloud install ставит его из `.cursor/cloud-agent-install.sh`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан иметь непустые `pain_markers_ru` / `outcome_markers_ru` (doctor проверяет). Utility gate при пустых списках только WARN, но preflight должен ловить пустоту.
- Internal href: латинские live WP slugs; link-verify percent-encode не-ASCII paths, но topic card не должна гадать кириллицей.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Ниша только Авто-Сейлс (`memory/brief/site-brief.md`): аукционы, Encar, растаможка, СВХ, утиль, JP/KR/CN. Stale Cursor/AI/n8n/Make в старых примерах — игнорировать.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- Каннибализация: local `--check-query` **и** live `--check-live-wp`. Local PASS при live near-duplicate ≠ gap для новой статьи.

## Research

- `technical_topic` / GitHub×3 — только для tech/automation маркеров с word-boundary. Авто-ниша (аукционный лист, Encar, растаможка) GitHub не требует.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (нет `--blog-path`).
