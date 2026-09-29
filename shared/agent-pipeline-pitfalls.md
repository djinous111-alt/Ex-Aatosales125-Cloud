# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path. Это **штатный** путь, пока typed Task catalog недоступен (в т.ч. для `excalibur-blog-geo-qa` и остальных ролей).
- Parent-agent сам пишет статью / `article-qa` вместо отдельной роли → **блокер**, перезапуск нужного Task.
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
- Cloud install обязан ставить `requirements.txt` (нужен `paramiko` для SSH). Если `ModuleNotFoundError: paramiko` — сначала `pip install -r requirements.txt`, затем чинить `.cursor/cloud-agent-install.sh`.

## Git / pre-commit secrets

- Перед любым `git commit` в Cloud: `source scripts/sanitize_cloud_secret_names.sh`.
- Если `pre-commit.cursor` падает с `invalid variable name` — в `CLOUD_AGENT_INJECTED_SECRET_NAMES` есть не-bash identifier (часто URL). Фильтруй имена до `[A-Za-z_][A-Za-z0-9_]*`, **не** используй `--no-verify`.
- В committed артефактах (`llms.txt`, interlink JSON, publish results) не оставляй живой `PUBLIC_SITE_URL`: `[REDACTED]` или `--redact-site-base`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- **Запрещён** литерал `href="[REDACTED]"` в `article.html`. CTA URL бери из `memory/brief/conversion-map.md` / authors registry. Redaction — только для логов/секретов/committed publish artifacts, не для живых ссылок в теле статьи.

## Research / notes gate

- `is_technical_topic` использует word-boundary для коротких маркеров (`ai`/`ии`/`api`); substring `pain`→`ai` или `Японии`→`ии` больше не делает авто-тему technical.
- GitHub ≥3 обязателен только для technical topics; для авто/растаможки достаточно official docs/help URL.
- `accessed_at` засчитывается по литералу или ISO-дате в URL-строке source table; `pain_solution_map` считает data-rows таблицы после заголовка.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- Utility gate: `pain_markers_ru` / `outcome_markers_ru` живут в `memory/brief/editorial-policy.json`. Пустой список маркеров = проверка отключена (не вечный BLOCK). Regression: `python3 scripts/excalibur_blog_utility_gate.py --self-test`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `scout_helper` / `today.py` понимают префиксы `AS\d+` и `B\d+` (и любой `## [A-Z]+\d+`). Unwritten исключает ledger `published|in_progress|draft_ready` и active article dirs. Next ID остаётся в серии `Bxx`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- LLMs CLI: `--blog-dir` + `--out-dir` (не `--blog-path`). Для commit: `--redact-site-base`.
