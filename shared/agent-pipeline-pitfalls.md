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
- `research_notes_gate` определяет tech-тему по **целым токенам** (`ai`, `ии`, …), не substring: поле `reader_pain` и слова вроде «объявлении» не делают тему technical. GitHub ≥3 URL обязателен только при `technical_topic: true` (не для таможенно-правовых/авто utility-тем без tech-маркеров в topic card).

## Topic IDs / ledger

- `today.py` / `scout_helper.py` парсят `(?:AS|B)\d+`. Регресс на только `B\d+` → ложный `needs_scout` / `B01` при живом пуле `AS##`.
- Перед Scout сверь `shared/published-articles.md` с WP (site-relative URL). Неполный ledger → повторный выбор уже опубликованных тем.
- Doctor проверяет AS|B regex в scripts и наличие `pain_markers_ru` / `outcome_markers_ru` в editorial-policy.

## Publish

- Cloud install (`.cursor/cloud-agent-install.sh`) обязан ставить `requirements.txt` (включая `paramiko`) в тот же `python3`, что запускает publish. Если `ModuleNotFoundError: paramiko` — `pip3 install --break-system-packages paramiko` и починить install-скрипт/snapshot.
- Large SSH bootstrap (~7MB): `trigger_bootstrap_http` = urllib 120s → curl `--max-time 300` → WebFetch wait 180s; do not race writers on `memory/webfetch-response.txt`. Регресс «urllib-only» = blocker на больших bootstrap.
- `shared/published-articles.md` URLs must stay site-relative (`/YYYY/MM/DD/slug/`); `site_relative_permalink()` в publish script; не коммитить absolute `PUBLIC_SITE_URL` в ledger.
- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: `python3 scripts/cta_urls.py` → живые href из env. При secret-scan на commit — `<!-- pragma: allowlist secret -->` сразу после CTA-абзаца; **не** писать литерал `[REDACTED]` в body HTML.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru`; `utility_gate` пропускает pain/outcome check только если списки пустые. Writer: маркеры «сделайте/не делайте/проверьте», не только «Делать/Не делать».
- Инсайт-блок: не начинать с ярлыка `TL;DR` / `Быстрый инсайт`.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Ниша = `memory/brief/site-brief.md` (Авто-Сейлс / авто-логистика). Не скаутить legacy AI/Cursor/n8n, пока brief задаёт авто-вертикаль. Серия ID: `AS##`.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: только `--blog-dir` (нет `--blog-path`). Для артефактов без absolute URL предпочитай `--site-base ""`.

## Incident memory

- Канон очереди: `memory/pipeline-fix-queue.md` (не путать с устаревшим/дублирующим `memory/pipeline-incident-queue.md`).
