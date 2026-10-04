# Excalibur BLOG — типичные сбои пайплайна

## Cloud / Task

- Cloud не принимает `excalibur-blog-*` как Task types → fallback `Task(generalPurpose)` + `.cursor/agents/<role>.md` + skill path.
- Особенно часто отсутствует typed `excalibur-blog-geo-qa` в Cloud Task enum → сразу `Task(generalPurpose)` с `.cursor/agents/excalibur-blog-geo-qa.md`.
- Parent-agent сам пишет статью вместо `excalibur-blog-writer` → **блокер**, перезапуск writer Task.
- Объединение cover+schema в один Task → запрещено; только параллельные отдельные Task.

## Handoff / fragments

- Параллельные `cover` и `schema` пишут в `.cursor/excalibur-blog-fragments/cover.md` и `schema.md`, директор переносит в handoff.
- Не коммитить `.cursor/excalibur-blog-handoff.md` и fragments.

## Research / дата

- Перед пайплайном: `python3 scripts/excalibur_blog_today.py` и `python3 scripts/excalibur_blog_research_start.py --topic-id …`.
- Если `EXCALIBUR_RUN_DATE` нет в выводе today.py — старая ветка/код, **блокер**.
- Editorial `search_intent` со словом `workflow` ≠ technical topic: gate не требует GitHub только из-за intent.
- `accessed_at` засчитывается и из колонки ISO-дат в source_table (не только `accessed_at:` литералы).
- `research_start` редактирует URL, совпадающие с `PUBLIC_SITE_URL`/catalog secrets, до записи `research-serp.json`.

## Preflight / doctor / CLI

- Doctor проверяет реальные флаги: llms generator → `--blog-dir` / `--out-dir` (не `--blog-path`).
- Indexer llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --relative-urls --out-dir memory/blog`.

## Git / secrets / pre-commit

- Перед `git commit` в Cloud: `source scripts/sanitize_cloud_secret_names.sh` — иначе `${!SECRET_NAME}` падает на non-identifier именах.
- Dashboard secret names должны быть bash identifiers: `A-Za-z_[A-Za-z0-9_]*` (не URL).
- `llms.txt` коммить с relative `/blog/<slug>/` URLs; absolute `PUBLIC_SITE_URL` часто блокируется secret-scan.
- Brand/CTA URL в `schema.jsonld` / `article.html`: `"_excalibur_scan": "pragma: allowlist secret"` или `<!-- pragma: allowlist secret -->` на строке с URL, если значение в Cloud Secrets.
- Перед commit GEO QA: редактируй живые CTA URL в `link-verify.json` (как research-serp).

## Publish

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` только в Cloud Secrets, не в git.
- Publish без обновления `shared/published-articles.md` → следующий прогон может дублировать slug.
- Для publish-preflight используй `python3 scripts/excalibur_blog_wp_publish.py --env-check`, не ad-hoc import без `scripts/` в `sys.path`.
- SSH root может быть login cwd: если bootstrap upload получает ENOENT на настроенном root, publish-скрипт пробует `.` и пишет warning; после warning обнови `SSH_ROOT` в Cloud Secrets на `.`.
- `paramiko` обязателен: `.cursor/cloud-agent-install.sh` ставит его; если нет — `pip3 install --break-system-packages paramiko`.
- HTTP 504 на bootstrap часто значит PHP уже создал пост: скрипт поллит WP REST по slug до WebFetch wait; агент при wait обязан WebFetch URL **параллельно**.
- CTA в git: `[CATALOG_URL]` / `[TELEGRAM_URL]`; publish/link-verify раскрывают из `CATALOG_URL`/`TELEGRAM_URL` env (`site.env.local`).

## Writer / Fact Check Box

- Fact Check Box **не копирует** пример из `shared/excalibur-article-writing-contract.md`. Автор — только из `shared/authors-registry.json` по `author_id` в `article.meta.json`.
- Запрещены legacy-имена вне реестра (в т.ч. «Елена Ковалева»). Human voice gate блокирует несовпадение автора и generic-шаблон «все статистические показатели…».
- CTA href: либо финальные URL из conversion-map (если можно коммитить), либо токены `[CATALOG_URL]`/`[TELEGRAM_URL]` — не оставляй битые relative вроде `CATALOG_URL` без скобок.

## QA

- Шаг cover||schema **только после** GEO QA PASS.
- MCP URLs в production article.html → fix перед publish.
- `article.html` должен проходить whitelist HTML-линтера: `<pre>`/`<code>` запрещены, пока не добавлены в whitelist; код/шаблоны оформляй через blockquote/table/list.
- Cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`, не `--article-dir`.
- `memory/brief/editorial-policy.json` обязан содержать `pain_markers_ru` / `outcome_markers_ru` (+ mins); пустые списки → utility gate warning, не silent 0/0 PASS без маркеров.

## Cover

- Meme/sticker style можно сохранять, но видимый текст не должен быть токсичным или оскорбительным: `лох`, `лохов`, `для лохов` и похожие ярлыки запрещены.
- `excalibur_blog_quad_manifest.py --merge` больше не сидит SEO/B01 defaults (`15k ключей`, Wordstat). Агент **обязан** заполнить `cover_hook` / `meme_caption_ru` / topic scene_hint руками.
- Hero rehost: `excalibur_blog_hero_reference_url.py` = catbox → 0x0 → SSH/WP uploads; stale winter-cars filenames → rehost to `blog-hero-reference.png`.

## Scout

- Wordstat проверяй cluster-first: широкий parent-запрос → узкий how-to. `totalCount`-only ответ на узкий запрос = low-result signal, не fatal.
- `shared/known-wp-slugs.md` — защита от reuse slug после ledger reset; helper `--suggest-next` / `--check-query` / `--check-slug` читают его.
- Перед commit: `source scripts/sanitize_cloud_secret_names.sh`.

## Indexer

- В Cloud shell используй `python3` для interlinker/llms generator; `python` может отсутствовать.
- Не используй `--blog-path` (флага нет). Для git: `--relative-urls`.
