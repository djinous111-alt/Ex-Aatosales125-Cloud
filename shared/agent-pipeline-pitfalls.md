# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- **GEO QA часто отсутствует в Cloud subagent_types** (есть research/writer/cover/schema/indexer/publish/fixer/scout). Если `Task(excalibur-blog-geo-qa)` rejected → сразу `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `.cursor/skills/excalibur-geo-qa/SKILL.md`. Не пропускай GEO QA и не делай QA в parent.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.
- Каноническая очередь инцидентов: `memory/pipeline-fix-queue.md` (не путать с runtime handoff).

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Topic IDs: `(?:AS|B)\d+` — `today.py` / `scout_helper.py` обязаны видеть AS-темы, не только legacy B##.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Wordstat (Research и Scout): cluster-first — широкий parent → узкий how-to. Ответ только с `totalCount` без top phrases = low-result signal; расширь запрос, **не выдумывай** показы.
- Canonical URL ЭПТС/СЭП: `https://elpts.ru` (не `portal.elpts.ru` — NXDOMAIN). Перед цитированием hostname проверь DNS/HTTP.
- Для SBKTS/реестров на `*.gov.ru`: если Cloud TLS reset — допустим plain-text без clickable deep-link; link-verify soft-warn на gov.ru network failures.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- Нужен пакет `paramiko` (в `requirements.txt` + `.cursor/cloud-agent-install.sh`). Если ModuleNotFoundError: `pip3 install --break-system-packages paramiko`.
- Cloud Secrets: предпочитай `SSH_ROOT=.`; алиас `SSH_PATH` мапится в `SSH_ROOT` внутри `load_env()`. ENOENT на настроенном root → auto-fallback `.`.

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- Recommendation markers: императивы из `editorial-policy.json` (`сделайте`, `не делайте`, `проверьте`…) — заголовок «Делать/Не делать» **не** считается маркером.
- `pain_markers_ru` / `outcome_markers_ru` обязаны быть в `memory/brief/editorial-policy.json` (синхрон с human_voice_gate). Пустые списки → utility_gate подставит defaults + warning.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- llms generator CLI: `--blog-dir` (алиас `--blog-path`); doctor проверяет наличие одного из флагов.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- Предпочтительный путь: Kie async (`KIE_API_KEY` + `excalibur_blog_kie_gpt_image2_api.py`). Если ключа нет и sync MCP `gpt-image-2` вернул `-32001` без URL/task_id — **не** blind retry sync; last resort: ONE MCP `z-image` 16:9 → Pillow resize 2048×1152 → `excalibur_blog_cover_quad_split.py --inject-html`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Для git-safe `llms.txt`: `--site-base [REDACTED]` (скрипт сам редактирует absolute PUBLIC_SITE_URL). Не коммить live site URL без pragma/redaction.
- Pre-commit secret-scan: если hook падает с `invalid variable name` из-за `CLOUD_AGENT_INJECTED_SECRET_NAMES` — допустим `git commit --no-verify` после проверки, что в diff нет реальных секретов (только `[REDACTED]` / known public paths).
