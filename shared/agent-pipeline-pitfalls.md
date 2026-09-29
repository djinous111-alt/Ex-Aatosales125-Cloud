# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Typed Task `excalibur-blog-geo-qa` часто отсутствует в Cloud enum → сразу `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md`; plugin agents/ уже регистрирует роль, но enum API может отставать.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Cloud secret-scan / pre-commit

- `CLOUD_AGENT_INJECTED_SECRET_NAMES` должен содержать только валидные bash-идентификаторы. Литералы вроде `[REDACTED]` или сырые URL как «имена» ломают `${!SECRET_NAME}` — перед commit отфильтруй: только `^[A-Za-z_][A-Za-z0-9_]*$`.
- Публичные URL сайта (`PUBLIC_SITE_URL`, Telegram/MAX/catalog) намеренно попадают в `schema.jsonld` (sameAs / mainEntityOfPage). Для commit schema/llms артефактов исключи эти public URL keys из injected secret names или пометь строку `<!-- pragma: allowlist secret -->`.
- `research-serp.json`: `research_start` редактирует host `PUBLIC_SITE_URL` в path-only/`[REDACTED]`. Ledger permalinks — path-only (`/2026/.../`), без host.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- WebFetch 5xx/timeout на конкуренте → сразу WebSearch + ≥2 альтернативных URL; не блокируй notes.
- Автоимпорт: официальные домены publication.pravo.gov.ru, garant.ru, consultant.ru, eec.eaeunion.org, tks.ru — допустимый fallback вместо customs.gov.ru при слабом SERP.
- `research_notes_gate`: `accessed_at` считается и как `accessed_at:`, и как ISO-даты в markdown table rows с URL. TECH_MARKERS — token-boundary; «японии» ≠ technical topic.

## Writer / utility markers

- Канон маркеров боли/результата: `memory/brief/editorial-policy.json` → `pain_markers_ru` / `outcome_markers_ru` (общий для utility gate и human-voice gate).
- Пустые списки маркеров → warning и skip hard min, не ложный BLOCK. Не возвращать жёсткий min без непустого списка в policy.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- Publish нужен `paramiko` (SSH). Он в `.cursor/cloud-agent-install.sh` и `requirements.txt`. На PEP 668 Cloud image: `pip3 install --break-system-packages paramiko`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `--suggest-next` учитывает AS*+B* в `blog-topics.md`, ledger, article dirs и `memory/topics/live-wp-occupied-ids.json` (B01/B02 и др. live WP). Не предлагай ID из occupied.
- Ниша AVTO SALES: читай `memory/brief/site-brief.md` (автоимпорт Япония/Корея/Китай), не дефолтный AI/Cursor шаблон.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--out-dir` (флага `--blog-path` нет).
