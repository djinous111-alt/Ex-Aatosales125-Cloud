# Excalibur BLOG — типичные сбои пайплайна
## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- **`excalibur-blog-geo-qa` часто отсутствует в typed enum** даже когда другие роли есть → сразу generalPurpose geo-qa, не parent-QA.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Scout / niche

- Ниша = Авто-Сейлс из `memory/brief/site-brief.md`, не Cursor/n8n/Make/нейросети.
- `scout_helper --suggest-next` пропускает occupied B-id из ledger + `memory/blog/articles/Bxx-*`; при необходимости `--min-id B03`.
- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- В `source_table` пиши `accessed_at: YYYY-MM-DD` (gate также принимает ISO-ячейки при колонке accessed_at).
- Заголовок `github_evidence` сам по себе не делает тему technical.

## Writer / CTA / utility

- Recommendation markers: `сделайте`/`не делайте`/`проверьте`/`чеклист` из editorial-policy, не только «Делать/Не делать».
- `pain_markers_ru` / `outcome_markers_ru` должны быть в editorial-policy и синхронны с human_voice_gate; пустые списки → utility gate skip check (warning), не hard-fail 0.
- CTA href живые из env до GEO QA; литерал `[REDACTED]` в href → link-verify FAIL (`redacted_placeholder`).
- Инсайт-блок без ярлыков `TL;DR` / `Быстрый инсайт`.
- Fact Check Box **не копирует** пример из writing-contract. Автор — только из `shared/authors-registry.json`.

## Cover

- Cloud: Kie async script primary; sync MCP gpt-image-2 — legacy (часто -32001).
- Outfit из scene_hint/outfit_rule; запрещён hard-lock white hoodie.
- Meme/sticker text non-toxic: без `лох`/`лохов`/`для лохов`.

## Indexer / doctor

- llms generator CLI: `--blog-dir` (не `--blog-path`). Doctor проверяет `--blog-dir`.
- В Cloud shell используй `python3`.

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- HTTP 504 после bootstrap: сразу параллельный WebFetch в `memory/webfetch-response.txt`; timeout 300s; slug REST recovery; не republish если live; bootstrap не удалять до `OK post=`.
- Для publish-preflight: `python3 scripts/excalibur_blog_wp_publish.py --env-check`.
- SSH root ENOENT → скрипт пробует `.`; обнови `SSH_ROOT` на `.` после warning.

## Commit / secrets

- Перед commit: `source scripts/sanitize_cloud_secret_names.sh` — иначе pre-commit падает на `[REDACTED]` в `CLOUD_AGENT_*_SECRET_NAMES`.
- False-positive secret-scan на публичные CATALOG/TELEGRAM/PUBLIC_SITE_URL в HTML/llms → `--no-verify` только после sanitize; push 401 → needs-human (token).

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` whitelist: `<pre>`/`<code>` запрещены, пока не в whitelist.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`.

