# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20260928-0938-schema-secret-scanner-public-urls
status: open
run_date: 2026-09-28
role: excalibur-blog-schema
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: medium
category: env

### What went wrong
- Pre-commit secret scanner блокирует `schema.jsonld`, потому что `PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL` совпадают с публичными brand URL в BlogPosting/author.sameAs (как в HTML с `<!-- pragma: allowlist secret -->`).
- В `CLOUD_AGENT_INJECTED_SECRET_NAMES` иногда попадает сырой URL вместо имени env-переменной → bash `${!SECRET_NAME}` падает с `invalid variable name` до сканирования.

### How the agent recovered this run
- Отфильтровал невалидные идентификаторы из `CLOUD_AGENT_INJECTED_SECRET_NAMES` перед commit.
- В `schema.jsonld` на строках с публичными URL добавил `"_comment": "pragma: allowlist secret"` (валидный JSON; сканер пропускает строку).

### Durable fix needed before next run
- В skill `schema-excalibur-blog` / pitfalls: публичные site/catalog/Telegram/MAX URL в JSON-LD требуют allowlist pragma на той же строке (аналог HTML).
- В `excalibur_blog_wp_publish.py`: перед записью post meta удалять ключи `"_comment"` из JSON-LD, чтобы не светить pragma в `<script type="application/ld+json">`.
- Не помечать публичные brand URL как commit-blocking secrets, либо завести allowlist доменов для schema/HTML.

### Suggested files to inspect/change
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `skills/schema-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_wp_publish.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260928-0935-writer-utility-pain-markers-missing
status: open
run_date: 2026-09-28
role: excalibur-blog-writer
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: high
category: docs

### What went wrong
- `memory/brief/editorial-policy.json` не содержал `pain_markers_ru` / `outcome_markers_ru`, хотя `excalibur_blog_utility_gate.py` считает их с дефолтом `min_pain_markers=2` / `min_outcome_markers=3`.
- При пустых списках gate всегда даёт BLOCK (`pain_markers=0`, `outcome_markers=0`) даже на уже опубликованных AS08/AS09 и на свежей AS02 с живым human-voice PASS.
- Повтор известного пробела из INC-20260726-2108 (writer AS02 policy CTA gap): маркеры боли/результата снова выпали из policy.

### How the agent recovered this run
- Восстановил `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` (списки согласованы с маркерами `human_voice_gate` + utility-сигналы `чеклист`/`вердикт`).
- Усилил в `article.html` формулировки боли/результата; utility gate AS02 → PASS; human-voice → PASS; html linter → PASS.

### Durable fix needed before next run
- Зафиксировать в pitfalls/utility skill: `editorial-policy.json` обязан держать непустые `pain_markers_ru` и `outcome_markers_ru`.
- В `excalibur_blog_utility_gate.py`: если списки маркеров пусты/отсутствуют – WARNING + skip count, а не ложный BLOCK на всех статьях; либо doctor-check на наличие ключей.
- Не давать редактору/фиксерy удалять эти ключи при чистке policy.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
- pending


## INC-20260928-0920-scout-as-prefix-regex
status: open
run_date: 2026-09-28
role: excalibur-blog-scout
topic_id: AS02
article_dir: n/a
severity: high
category: script

### What went wrong
- `scripts/excalibur_blog_scout_helper.py` и `scripts/excalibur_blog_today.py` матчат topic id только как `B\d+` (карточки в `blog-topics.md`, папки `memory/blog/articles/`, next-id / P0 suggest).
- Для ниши AVTO SALES пул использует `AS##`, поэтому `--suggest-next` печатает `Next ID: B01`, `Total topics in pool: 0`, `Unwritten: []`, а `today.py` отдаёт `EXCALIBUR_TOPIC_SELECTION=needs_scout` даже при живых P0 AS01–AS07.
- `--check-query` тоже не видит AS-карточки, поэтому ложно отвечает `NO CANNIBALIZATION` на exact primary_query вроде `encar на русском` (AS02).

### How the agent recovered this run
- Вручную посчитал ID: AS01–AS09 в пуле; next new = AS10+; выбрал незакрытую P0 `AS02` без новой карточки.
- Каннибализацию проверил вручную против AS01–AS09 и live WP slugs; utility gate: `python3 scripts/excalibur_blog_utility_gate.py --topic-id AS02` → PASS.

### Durable fix needed before next run
- Расширить regex topic id до `(?:AS|B)\d+` (или конфигурируемый prefix) в scout_helper и today:
  - парсинг `## AS## —` / `## B## —` в `blog-topics.md`;
  - article dirs `AS##-*` / `B##-*`;
  - `--suggest-next` next id по фактическому префиксу пула (для AVTO SALES → AS10+);
  - `--check-query` обязан учитывать AS-карточки.
- Обновить pitfalls/scout skill: не доверять `Total topics in pool: 0` при AS-пуле.

### Suggested files to inspect/change
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_today.py`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260928-0926-research-wordstat-secondary-format
status: open
run_date: 2026-09-28
role: excalibur-blog-research
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: low
category: api

### What went wrong
- `wordstat_get_top_requests` для secondary query `как читать encar` вернул неожиданный формат `{ "totalCount": "7" }` без списка фраз/показов (и с `regions`, и без).
- Primary/соседние фразы (`encar`, `encar на русском`, `проверка авто корея`, `trust encar`, `енкар на русском`, `carhistory`) отработали нормально.
- WebFetch `https://teletype.in/@vezemavto/B2hgUEkytih` дал 502; контент восстановлен из SERP/WebSearch snippet.
- Gate ложно пометил тему Encar как `technical_topic=true` из-за маркера `github` в `github_evidence` / TECH_MARKERS, хотя ниша авто how-to.
- Commit blocked: `research-serp.json` и ledger содержали `PUBLIC_SITE_URL`; Cloud secret scan не даёт коммитить self-site URL. Также `CLOUD_AGENT_INJECTED_SECRET_NAMES` иногда содержит URL вместо имени секрета → pre-commit `invalid variable name`.

### How the agent recovered this run
- В `research-notes.md` зафиксировал Wordstat-таблицу по успешным фразам и явную secondary note без выдуманных показов.
- Для Teletype использовал сниппеты WebSearch + параллельные гайды (chest-import, auto.ru, carto).
- Research-notes gate: PASS (warning про official docs на technical false-positive оставлен).
- Self-site URL в `research-serp.json` заменены на placeholder; в `published-articles.md` URL AS08/AS09 переведены в site-relative paths; secret-names env отфильтрован по `str.isidentifier()` перед commit.

### Durable fix needed before next run
- В MCP/обёртке Wordstat: при ответе только `totalCount` без `topRequests` возвращать понятную ошибку или пустой список, а не "unexpected format" без retry-подсказки.
- В `excalibur_blog_research_notes_gate.py`: не считать тему technical только из наличия секции `github_evidence` / слова github в notes; матчить tech-markers по topic h1/primary_query, не по всему тексту notes.
- Pitfalls: при secondary Wordstat totalCount-only не выдумывать impressions.
- `research_start` / SERP writer: сразу редактировать self-site URL (PUBLIC_SITE_URL) в serp JSON; ledger хранить path-only или env-composed URL.
- Document Cloud secret-scan + invalid SECRET_NAMES workaround in pitfalls.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/excalibur-research/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260616-2015-geo-qa-html-cli-mismatch
status: fixed
run_date: 2026-06-16
role: excalibur-blog-geo-qa
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: qa

### What went wrong
- `article.html` used `<pre><code>` for the llms.txt template, but `excalibur_blog_html_linter.py` forbids those tags and only allows the strict article whitelist.
- `excalibur_blog_research_notes_gate.py` interprets a relative `-o` path inside `article_dir`; passing a repo-relative path as `-o` produced a nested duplicate output before cleanup.
- `.cursor/skills/excalibur-geo-qa/SKILL.md` instructs `excalibur_blog_cannibalization_guard.py --article-dir ...`, while the actual script accepts `--blog-dir`, `--threshold` and `-o/--output`; the documented command exited with argparse error.

### How the agent recovered this run
- Replaced the template block with whitelist-safe `<blockquote><p><br>` markup without changing the article's practical meaning.
- Removed the unintended nested duplicate `research-notes-gate.json` and kept the canonical file in the article directory.
- Re-ran the cannibalization guard with `--blog-dir memory/blog/articles -o memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta/cannibalization-report.json`; verdict PASS.

### Durable fix needed before next run
- Update Writer/QA contracts to avoid `<pre><code>` in `article.html` unless the linter whitelist is intentionally expanded.
- Update `.cursor/skills/excalibur-geo-qa/SKILL.md` to use the actual cannibalization guard CLI or update the script to support `--article-dir`.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_cannibalization_guard.py`
- `scripts/excalibur_blog_html_linter.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Writer/article writing contracts now forbid `<pre>`/`<code>` in `article.html` until the HTML linter whitelist is intentionally expanded, and document whitelist-safe blockquote/table/list alternatives.
- GEO QA skill now documents the actual cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`.
- GEO QA note clarifies that `research_notes_gate.py -o research-notes-gate.json` is relative to `--article-dir`.
files_changed:
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_cannibalization_guard.py --help`
- `rg` check for old Writer `<pre><code>` instruction strings
- `rg` check for old cannibalization `--article-dir` command in source docs
commit: pending-parent-commit

## INC-20260616-2018-cover-toxic-sticker
status: fixed
run_date: 2026-06-16
role: excalibur-blog-cover
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: prompt

### What went wrong
- The one-shot Kie image-to-image quad generation succeeded, but the cover panel included an insulting Russian sticker phrase even though the style preset asks for a non-toxic tone.
- Geometry, white background, hero face, typography and inline utility passed; the issue was limited to one generated sticker text on the top-left cover panel.

### How the agent recovered this run
- Did not launch a second image job.
- Retouched only the offending sticker layer in `cover/cover.png` and the matching top-left area of `cover/canvas-quad.png`, replacing it with a neutral `SEO-МИФ / БЕЗ МАГИИ` sticker.

### Durable fix needed before next run
- Add explicit negative prompt wording for cover/inline generated text: no insults, no toxic labels, no words like `лох`, `лохов`, `для лохов`.
- Consider adding a lightweight post-generation OCR/text QA note to the cover skill when generated Russian sticker text is visible.

### Suggested files to inspect/change
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `memory/cover/cover-design-code.json`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Cover style JSON, design code, prompt builder, agent contracts and skill QA now explicitly forbid toxic/insulting generated sticker text while preserving the meme/sticker/collage style.
- Visible text QA now treats words such as `лох`, `лохов`, `для лохов` and similar humiliating labels as a cover blocker.
files_changed:
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `memory/cover/cover-design-code.json`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_prompt.py`
- JSON parse for `memory/cover/quad-style-digital-meme-collage-ru.json`
- JSON parse for `memory/cover/cover-design-code.json`
commit: pending-parent-commit

## INC-20260616-1950-scout-wordstat-format
status: fixed
run_date: 2026-06-16
role: excalibur-blog-scout
topic_id: B09
article_dir: n/a
severity: low
category: api

### What went wrong
- `wordstat_get_top_requests` for the narrow phrase `как создать llms txt` returned an unexpected payload shape with only `totalCount`, so the tool wrapper could not print top phrases.

### How the agent recovered this run
- Used the successful broader Wordstat result for `llms.txt`, which included the full semantic tail and showed related actionable phrases such as `создать llms txt`.

### Durable fix needed before next run
- Make the Wordstat MCP wrapper handle low-result responses that include only `totalCount`, or document that Scout should query the broader cluster first.

### Suggested files to inspect/change
- `shared/pipeline-incident-fix-contract.md`
- `agents/excalibur-blog-scout.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Scout agent and skill now require Wordstat cluster-first validation: broad parent query before narrow how-to query.
- `totalCount`-only responses are documented as low-result signals, not fatal tool/API failures; Scout should broaden the query and use the broad cluster for semantic tail.
files_changed:
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` check for Wordstat cluster-first/totalCount guidance in Scout source docs
commit: pending-parent-commit

## INC-20260616-2031-indexer-python-missing
status: fixed
run_date: 2026-06-16
role: excalibur-blog-indexer
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: env

### What went wrong
- The Indexer contract requested `python scripts/excalibur_blog_interlinker.py ...`, but the Cloud shell has no `python` executable.
- The first interlinker command failed with `python: command not found`, forcing a retry.

### How the agent recovered this run
- Re-ran the same interlinker command with `python3`, then used `python3` for the llms generator.
- Both scripts completed successfully after the retry.

### Durable fix needed before next run
- Standardize Indexer shell examples on `python3` or provide a `python` alias in the Cloud environment.

### Suggested files to inspect/change
- `agents/excalibur-blog-indexer.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/environment.json`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Indexer agent and skill shell examples now use `python3` for interlinker and llms generator.
- Publish post-publish interlinker example also uses `python3`.
files_changed:
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` check for old `python scripts/excalibur_blog_interlinker.py` and `python scripts/excalibur_blog_llms_generator.py` in source docs
commit: pending-parent-commit


## INC-20260616-2042-publish-ssh-root-dot
status: fixed
run_date: 2026-06-16
role: excalibur-blog-publish
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: publish

### What went wrong
- A safe env-preflight wrapper initially imported `excalibur_blog_wp_publish.py` without adding `scripts/` to `sys.path`, causing `ModuleNotFoundError: asset_download`; the check was re-run with the correct `sys.path`.
- The first real publish attempt connected over SSH but failed before upload with `FileNotFoundError/ENOENT` because the configured publish root path does not exist inside the SSH account cwd.
- Commit was blocked by Cursor secret-scan because `PUBLIC_SITE_URL`/`WP_SITE_URL` are configured as secrets and appeared in staged publish artifacts; committed copies were redacted to `[REDACTED]` to match repository policy.

### How the agent recovered this run
- Re-ran the env check with `scripts/` on `sys.path`; allow flag, public URL and SSH settings were confirmed without printing secret values.
- Retried publish with `SSH_ROOT=.` so the bootstrap was written to the SSH login cwd; WordPress post, featured image, 3 inline images and schema meta published successfully.
- Replaced public site base in committed artifacts with `[REDACTED]`; live permalink remains available in local runtime handoff and WordPress result before redaction.

### Durable fix needed before next run
- Update Cloud publish root secret to `.` (or remove invalid panel path) for this SSH account, or make `excalibur_blog_wp_publish.py` auto-probe `.` when configured root returns ENOENT before bootstrap upload.
- Document that direct import of publish helpers in ad-hoc checks needs `scripts/` on `sys.path`, or expose a tiny env-check CLI in the script.
- Decide whether `PUBLIC_SITE_URL` should remain a secret-scanned value; if yes, keep committed examples/results redacted by contract.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `CURSOR-CLOUD-RUNBOOK.md`
- Cursor Dashboard Cloud Secrets (`SSH_ROOT` only; no secret values recorded here)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- `excalibur_blog_wp_publish.py` now has `--env-check` for safe publish env validation without ad-hoc imports or secret output.
- SSH bootstrap upload now retries once at `.` when a configured non-dot root returns ENOENT, and cleanup deletes the actual uploaded remote path.
- Publish skill/runbook document the env-check CLI, `scripts/` sys.path guidance for ad-hoc imports, and the optional Cloud Secret root update to `.` if fallback warning appears.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `CURSOR-CLOUD-RUNBOOK.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py`
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` (JSON output validated; non-publish env may return exit 1)
- `python3 -m json.tool /tmp/excalibur_publish_env_check.json`
commit: pending-parent-commit

## Fixed incidents

Handled above; commit is pending Director review.
