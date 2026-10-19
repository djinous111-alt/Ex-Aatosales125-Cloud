# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → **сразу** fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path; **не** крутить retry typed Task (в т.ч. `excalibur-blog-geo-qa`).
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- `research_notes_gate` детектит tech-нишу по **word-boundary**, не substring: `ai`/`ии` внутри `reader_pain` / `ожидании` не делают тему технической. Проверка: `python3 scripts/excalibur_blog_research_notes_gate.py --self-test`.
- `-o research-notes-gate.json` — basename (пишется в `--article-dir`); не передавай repo-relative `memory/blog/articles/.../research-notes-gate.json`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- HTTP bootstrap trigger / WebFetch wait = **300s** (не 120). Fallback принимает файл только с литералом `OK post=` (nginx 504 HTML — не success).
- После 504/false-fail: проверь slug через REST/wp-cli; если пост уже создан — reconstruct artifacts, **не republish** и не трогай чужие post_id.

## Schema / Writer / secret scan

- `CLOUD_AGENT_INJECTED_SECRET_NAMES` иногда содержит non-identifier (URL / `[REDACTED]` token) → bash `${!name}` падает с `invalid variable name`. Workaround: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit -m "..."`. Root fix — Dashboard: только bash-safe имена секретов.
- Public CTA/site names (`CATALOG_URL`, `TELEGRAM_URL`, `PUBLIC_SITE_URL`, `MAX_URL`) часто в secret scan — filter script их выкидывает из scan list (значения остаются в env).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Ярлык **«Материал проверен»** обязателен дословно; soft FIX меняет только вторую строку/источники.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA: живые URL из env / conversion-map; никогда `href="[REDACTED]"` в article.html.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать непустые `pain_markers_ru` / `outcome_markers_ru` (`_markers_pinned`); rebrand/start scripts не должны их затирать — иначе utility gate BLOCK на всех статьях. Doctor проверяет списки.
- Utility `recommendation_markers_ru` считает «сделайте/не делайте/проверьте/…», не «Делать/Не делать»; writer должен попадать в список или расширять policy осознанно.
- Insight-блок: запрещены ярлыки `TL;DR` и `Быстрый инсайт`.
- `link_verify` IRI-encode кириллические URL (2GIS); `python3 scripts/excalibur_blog_link_verify.py --self-test`.

## Cover

- Cloud default: Kie async (`excalibur_blog_kie_gpt_image2_api.py` + `KIE_API_KEY`). Sync MCP `gpt-image-2` — legacy; `-32001` → Kie recovery, не duplicate jobs.
- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `excalibur_blog_scout_helper.py --suggest-next` обязан учитывать `memory/topics/live-reserved.json` и/или `memory/blog/live-reserved.json` (`reserved[]` / `reserved_topic_id` + `next_forced_topic_id`), иначе предложит B01 на пустом pool.
- Ниша сайта — AVTO SALES (Корея/Китай/Япония), не Cursor/Make defaults из старых scout prompts.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- llms generator CLI: `--blog-dir` + `--site-base` + `--out-dir` (флага `--blog-path` нет; doctor проверяет `--blog-dir`).
