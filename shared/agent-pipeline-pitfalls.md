# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- **geo-qa:** typed Task `excalibur-blog-geo-qa` часто отсутствует в Cloud enum — сразу `Task(generalPurpose)` (штатный путь, не exception).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat cluster-first: широкий parent → sibling/короткие seeds → длинный how-to. `totalCount`-only / truncated без топа = partial (один retry), таблица из parent/sibling; не invent primary breakdown.
- Research notes gate: `technical_topic` использует token-match; поле `reader_pain` / слово «японии» сами по себе **не** делают тему technical и не требуют 3 GitHub URL.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен для SSH publish: ставится в `.cursor/cloud-agent-install.sh` + `requirements.txt`; doctor проверяет module. Cold boot без paramiko → pip install + incident.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA href = `CATALOG_URL` / `TELEGRAM_URL`: на той же строке `<!-- pragma: allowlist secret -->`, иначе Cloud secret-scan блокирует commit.
- Если host `CATALOG_URL` стабильно 503, а `PUBLIC_SITE_URL` 200 — CTA на рабочий публичный host; secret values не печатать; incident.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` обязан иметь непустые `pain_markers_ru` / `outcome_markers_ru` (utility gate fail-fast + doctor). Пустые списки → ложный BLOCKER на любой статье.

## Cover / Schema / Scout — git commit

- Cloud pre-commit может упасть с `invalid variable name`, если в `CLOUD_AGENT_*_SECRET_NAMES` есть non-identifier placeholder.
- Перед commit: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` (фильтр identifier + skip public marketing URL secrets).
- Boot install (`.cursor/cloud-agent-install.sh`) также патчит `pre-commit.cursor` маркером `EXCALIBUR_SECRET_SCAN_HARDENED`.
- Schema JSON-LD: нет HTML pragma — только filter env; не редактируй sameAs в `[REDACTED]`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` / `--site-base` / `--out-dir`. Флага `--blog-path` нет (doctor проверяет `--blog-dir`).
