# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Особенно часто отсутствует typed Task `excalibur-blog-geo-qa` → **сразу** `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md` + `excalibur-geo-qa` skill; не тратить ретраи на typed enum.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Topic IDs (AS / B)

- Карточки и article dirs: `[A-Z]{1,3}\d+` (`AS01`, `B09`). Скрипты `today.py` / `scout_helper.py` / utility gate обязаны понимать оба префикса.
- `today.py` soft-skip: P0 с utility topic BLOCK пропускается, берётся следующий PASS (`EXCALIBUR_TOPIC_SKIPPED_UTILITY_FAIL`).
- h1/primary_query P0 обязаны содержать маркер из `topic_title_must_match` (как/чек-лист/сравнение/…).

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

## Scout / Research Wordstat

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only / truncated payload без списка фраз = low-result signal, не fatal; sibling phrasing, без выдуманных показов.
- Research gate: ≥5 `accessed_at: YYYY-MM-DD` лейблов; строки `pain_solution_map` с pain|solution|result|боль|решение|результат.

## Writer / CTA / secret-scan

- QA-time HTML: живые `CATALOG_URL`/`TELEGRAM_URL` или относительные пути. **Не** `href="[REDACTED]"` — ломает link-verify.
- Commit: если secret-scan блокирует публичные URL из Cloud Secrets — redact только в staging; working tree для publish снова с live hrefs.

## Utility / pain-outcome

- `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` должны совпадать с константами `human_voice_gate.py`. Utility gate enforce pain/outcome **только если** списки в policy непустые.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- `llms*.txt` / `interlink-suggestions.json` коммить только с `site_base=[REDACTED]` (`--commit-safe` default). Live `PUBLIC_SITE_URL` — только working-tree `--no-commit-safe` перед upload.

## Cover / Kie GPT Image 2

- Preferred path: Cloud Secret / `memory/site.env.local` → `KIE_API_KEY` → `python3 scripts/excalibur_blog_kie_gpt_image2_api.py --article-dir …` then `quad_apply --inject-html`.
- Docs: https://kie.ai/gpt-image-2?model=gpt-image-2-image-to-image
- `createTask` code `402 Credits insufficient` = key valid but balance too low (check `GET https://api.kie.ai/api/v1/chat/credit`). Top up before regenerating covers.
- Do not leave `reference_url_hosted` as `[REDACTED]/…` in `quad-mcp-batch.json`; restore from `memory/cover/blog-hero.json`.

