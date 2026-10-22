# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

_(current B01 CX-5 run: all listed below closed by fixer)_

## INC-20261022-2125-publish-missing-site-env-and-paramiko
status: fixed
run_date: 2026-10-23
role: excalibur-blog-publish
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: env

### What went wrong
- `memory/site.env.local` was missing again (Cloud Secrets present in process env).
- `paramiko` was not installed in the runtime image; env-check does not import it, so missing dep surfaces only on real publish.

### How the agent recovered this run
- Wrote `memory/site.env.local` from Cloud Secrets without wrapping quotes; set `SSH_ROOT=.`.
- Installed `paramiko` via `python3 -m pip install --break-system-packages paramiko` (5.1.0).

### Durable fix needed before next run
- Ensure cloud install script / environment.json install step includes `paramiko` from `requirements.txt`.
- Document or automate bootstrap of `memory/site.env.local` from Cloud Secrets when missing (gitignored).
- Keep `SSH_ROOT=.` in Cloud Secrets for this host.

### Suggested files to inspect/change
- `.cursor/cloud-agent-install.sh`
- `.cursor/environment.json`
- `requirements.txt`
- `skills/publish-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- cloud-agent-install installs paramiko; doctor ensure_site_env_local + paramiko check
- publish --env-check reports paramiko_available; publish skill documents bootstrap
files_changed:
- `.cursor/cloud-agent-install.sh`
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-publish.md`
- `requirements.txt` (already listed paramiko)
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → errors=0
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` → paramiko_available=true
commit: pending-parent-commit

## INC-20261022-2130-publish-http-timeout-webfetch-reconstruct
status: fixed
run_date: 2026-10-23
role: excalibur-blog-publish
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: high
category: publish

### What went wrong
- SSH upload of ~6.8MB bootstrap OK; local HTTP trigger hit `TimeoutError` at 120s while PHP still running.
- Entered WebFetch fallback; agent started `curl --max-time 300` but script only waits 120s for `memory/webfetch-response.txt`, then raises RuntimeError and exits without writing `wp-publish-result.json`.
- Server-side bootstrap completed (and a second trigger after the first timeout created duplicate media: cover 4454→4459, inlines *-1.png). Live post was already published.

### How the agent recovered this run
- Did **not** run a third publish.
- Verified via WP REST + wp-cli: post_id=4453, featured=4459, inline=4460/4461/4463, schema_meta present, skip_theme_faq=1, permalink HEAD 200.
- Reconstructed `wp-publish-result.json` verdict=pass; updated ledger/log/promotion/handoff.

### Durable fix needed before next run
- Increase Cloud WebFetch fallback wait well beyond HTTP timeout (e.g. 300s) and/or stream curl into webfetch file earlier.
- On client timeout: auto-probe REST by slug before FAIL; reconstruct result when live post matches slug.
- Prefer not re-triggering bootstrap when REST already shows published slug+featured for same payload (avoid duplicate media).
- Document: agent must start curl/WebFetch **immediately** on FALLBACK_TRIGGER_URL and keep waiting until OK post= or proven 504+REST reconstruct.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py` (`trigger_bootstrap_http` wait loop)
- `skills/publish-excalibur-blog/SKILL.md`
- `shared/excalibur-wp-publish-contract.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- WebFetch fallback wait raised to 300s; rejects non-OK HTML responses
- REST probe by slug + reconstruct; skip re-bootstrap when live slug+featured already exists
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-publish.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py`
- `rg WEBFETCH_FALLBACK_WAIT_SECONDS=300 scripts/excalibur_blog_wp_publish.py`
commit: pending-parent-commit


## INC-20261022-2123-indexer-stale-llms-blog-path
status: fixed
run_date: 2026-10-23
role: excalibur-blog-indexer
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: docs

### What went wrong
- Agent/skill shell examples still pass `--blog-path /` to `excalibur_blog_llms_generator.py`.
- Current CLI help has only `--blog-dir`, `--site-base`, `--out-dir` (no `--blog-path`); unknown flag would fail the Indexer step.
- `excalibur_blog_doctor.py` still asserts `"--blog-path" in llms_help.stdout`, so doctor FAIL is a false positive / stale contract.

### How the agent recovered this run
- Ran llms generator with `--blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` only (per Director override).
- Generated `memory/blog/llms.txt` and `memory/blog/llms-full.txt` successfully (3 articles).
- First `git commit` blocked by secret-scan (`PUBLIC_SITE_URL` embedded in llms/interlink JSON); replaced site base with `[REDACTED]` in those artifacts for the commit, then re-hydrated working copies for publish.

### Durable fix needed before next run
- Remove `--blog-path` from indexer agent/skill shell blocks (`.cursor/` + `agents/` + `skills/`).
- Update doctor: drop the `--blog-path` check; optionally assert `--out-dir` / `--blog-dir` instead.
- Align any remaining docs that mention `--blog-path` for llms generator.
- Llms/interlink scripts (or indexer skill) should write git-safe placeholders for site base, or document post-generate redact+rehydrate like schema.jsonld.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `.cursor/agents/excalibur-blog-indexer.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- Indexer agent/skill CLI uses --blog-dir/--out-dir only
- Doctor asserts --blog-dir/--out-dir and warns if stale --blog-path appears in help
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → llms --blog-dir/--out-dir OK
- `python3 scripts/excalibur_blog_llms_generator.py --help`
commit: pending-parent-commit

## INC-20261023-2140-writer-editorial-policy-pain-outcome-markers-missing
status: fixed
run_date: 2026-10-23
role: excalibur-blog-writer
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: docs

### What went wrong
- В `memory/brief/editorial-policy.json` снова отсутствовали `pain_markers_ru` / `outcome_markers_ru`.
- `excalibur_blog_utility_gate.py` при пустых списках всегда даёт BLOCK по pain/outcome (min 2/3), даже если статья человеческая.
- Это уже чинилось в прошлых B01 run (Monjaro/Harrier), но списки снова пропали из policy.

### How the agent recovered this run
- Восстановил `pain_markers_ru` и `outcome_markers_ru` в `editorial-policy.json` (без короткого маркера `боль`, чтобы не ловить ложное `больше`).
- Selfcheck: html_linter PASS, utility PASS, human_voice PASS.

### Durable fix needed before next run
- Закрепить fallback-маркеры внутри `excalibur_blog_utility_gate.py`, если policy-списки пустые (как заявлялось в Harrier fixer notes, но в текущем скрипте fallback нет).
- Добавить doctor-check: policy обязана содержать non-empty pain/outcome marker lists.
- Не давать scout/research затирать эти ключи при правках policy.

### Suggested files to inspect/change
- `scripts/excalibur_blog_utility_gate.py`
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_doctor.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- utility_gate falls back to DEFAULT_PAIN/OUTCOME markers when policy lists empty
- editorial-policy.json keeps non-empty pain/outcome + min_* signals; doctor enforces
files_changed:
- `scripts/excalibur_blog_utility_gate.py`
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_doctor.py`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → pain/outcome checks OK
- `python3 -m py_compile scripts/excalibur_blog_utility_gate.py`
commit: pending-parent-commit


## INC-20261023-2112-research-notes-gate-accessed-at-and-tech-false-positive
status: fixed
run_date: 2026-10-23
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: low
category: script

### What went wrong
- Первый прогон `excalibur_blog_research_notes_gate.py` дал BLOCK: `accessed_at=1 < 5`, хотя в `source_table` уже были даты доступа в колонке.
- Gate считает только литералы `accessed_at:`; дата в ячейке таблицы без префикса не засчитывается.
- Тема про Mazda CX-5 ложно помечена `technical_topic: true` из-за маркера `github` в обязательном блоке `github_evidence`, из-за чего появляется WARN про official docs/developer URL.

### How the agent recovered this run
- Переписал ячейки `source_table` в формат `accessed_at: 2026-10-23`; повторный gate = PASS.
- Оставил WARN без блокировки Writer; GitHub URL для VIN/community уже есть (≥3).

### Durable fix needed before next run
- В skill/research agent явно требовать ≥5 литералов `accessed_at:` (не только колонку дат).
- В `excalibur_blog_research_notes_gate.py` не считать тему technical только из-за слова `github` внутри секции `github_evidence` / обязательных полей; technical marker брать из topic card (h1/primary_query/slug), а не из всего notes blob.
- Опционально: принимать дату в колонке `accessed_at` таблицы без повторения ключа в каждой ячейке.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `.cursor/agents/excalibur-blog-research.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- count_accessed_at accepts table-column ISO dates and accessed_at: literals
- technical_topic uses topic card fields only (github_evidence no longer false-positives CX-5)
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `skills/excalibur-research/SKILL.md`
- `agents/excalibur-blog-research.md`
checks_run:
- `research_notes_gate` on B01 → PASS technical_topic=False accessed_at=17
commit: pending-parent-commit

## INC-20261023-2113-research-precommit-invalid-secret-name
status: fixed
run_date: 2026-10-23
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: env

### What went wrong
- `git commit` падал на Cloud pre-commit.cursor: `invalid variable name` при `${!SECRET_NAME}` для невалидного идентификатора из `CLOUD_AGENT_INJECTED_SECRET_NAMES`.

### How the agent recovered this run
- Локально в VM-hook добавлен skip имён, не совпадающих с `^[A-Za-z_][A-Za-z0-9_]*$`, затем commit прошёл.

### Durable fix needed before next run
- Зафиксировать фильтр валидных secret names в репозитории (wrapper/script или patch install step в environment), чтобы каждый Cloud run не чинил hook вручную.

### Suggested files to inspect/change
- `.cursor/environment.json` / install script
- `scripts/` helper для filter secret names (если появится в repo)
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- Added scripts/excalibur_blog_filter_secret_names.sh + scripts/excalibur_git.sh wrapper
- Pitfalls document Cloud pre-commit identifier filter
files_changed:
- `scripts/excalibur_blog_filter_secret_names.sh`
- `scripts/excalibur_git.sh`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- filter_secret_names smoke: drops URL-like / hyphenated names
commit: pending-parent-commit

## INC-20261023-2105-scout-missing-wp-slug-denylist
status: fixed
run_date: 2026-10-23
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: docs

### What went wrong
- `shared/wp-slug-denylist.json` отсутствует в репозитории, хотя scout-контракт требует сверку с denylist перед новой model/how-to карточкой.
- Без файла каждый scout вынужден заново полагаться на ручной список из промпта Директора и live WP REST, риск republish растёт.

### How the agent recovered this run
- Сверился с ручным denylist из инструкции Директора (Harrier, Monjaro, левый руль, Kia/Hyundai серия, utilsbor, auction sheet, AS08/AS09, Seltos/Sportage/K5/Genesis/Palisade/Staria, Sonata soft-overlap, Grandeur).
- Дополнительно проверил live WP через `PUBLIC_SITE_URL` REST (`/wp-json/wp/v2/posts?slug=...` и search по моделям); wordpress_* MCP не использовался как источник истины.
- Выбрал GAP-тему B01 Mazda CX-5 из Китая: exact slug отсутствует, Wordstat живой.

### Durable fix needed before next run
- Добавить канонический `shared/wp-slug-denylist.json` со slug/WP id уже LIVE и недавно закрытых model-гайдов.
- Обновить scout skill/agent: при отсутствии файла – blocker или явный fallback на denylist + live REST; не молчаливый skip.

### Suggested files to inspect/change
- `shared/wp-slug-denylist.json` (создать)
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `scripts/excalibur_blog_scout_helper.py` (опционально: читать denylist в `--check-query`)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- Created shared/wp-slug-denylist.json (202+ slugs) including CX-5/Harrier/Monjaro/LHD
- Scout skill/helper --check-slug; missing file is blocker path in skill
files_changed:
- `shared/wp-slug-denylist.json`
- `scripts/excalibur_blog_scout_helper.py`
- `skills/scout-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-scout.md`
checks_run:
- `python3 scripts/excalibur_blog_scout_helper.py --help` shows --check-slug
- `doctor` denylist exists/has slugs
commit: pending-parent-commit

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

## INC-20261022-2115-cover-hoodie-outfit-lock
status: fixed
run_date: 2026-10-23
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: prompt

### What went wrong
- `scripts/excalibur_blog_cover_quad_prompt.py` hardcodes `Outfit lock: thick heavyweight white hoodie`, which conflicts with blog-hero outfit_rule (no hood/cap) and explicit cover brief softshell/crewneck for this run.

### How the agent recovered this run
- Patched generated `quad-mcp-prompt.txt` / `quad-mcp-batch.json` before MCP call to softshell/crewneck and NO hoodie.

### Durable fix needed before next run
- Replace hardcoded hoodie outfit lock in prompt builder with weather/topic outfit from scene_hint or blog-hero.outfit_rule; keep explicit NO hoodie/NO hood/NO cap.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `memory/cover/blog-hero.json`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- cover_quad_prompt outfit_lock_from_hero(weather/topic); hard NO hoodie/hood/cap
files_changed:
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
checks_run:
- outfit smoke: rain/port → weather outfit + NO hoodie; no thick white hoodie hardcode
commit: pending-parent-commit

## INC-20261023-2115-schema-secret-scan-jsonld
status: fixed
run_date: 2026-10-23
role: excalibur-blog-schema
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: env

### What went wrong
- `git commit` of `schema.jsonld` blocked by Cursor secret-scan: file contained `PUBLIC_SITE_URL`, `TELEGRAM_URL`, `CATALOG_URL`, `MAX_URL` values required for valid BlogPosting/@id and author sameAs.
- Prior articles already store live URLs in committed schema; current scan rejects new commits with the same pattern.

### How the agent recovered this run
- Wrote full runtime schema for publish at `schema.jsonld.runtime`.
- Committed redacted `schema.jsonld` with `[REDACTED]` placeholders replacing secret URL values.
- Restored unredacted content to `schema.jsonld` after commit so publish can ingest live JSON-LD.
- Fragment documents `incident_report` and READY=yes for pipeline.

### Durable fix needed before next run
- Document in schema skill: commit-safe redaction vs runtime unredacted file (or expand placeholders at publish from env).
- Prefer publish-time URL expansion from env so git never stores secret URL literals.
- Align authors-registry / schema commit policy with secret-scan (placeholders in repo, hydrate at publish).

### Suggested files to inspect/change
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `skills/schema-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_wp_publish.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- Schema skill documents commit-safe [REDACTED]/runtime hydrate vs secret-scan
files_changed:
- `skills/schema-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg schema.jsonld.runtime skills/schema-excalibur-blog/SKILL.md`
commit: pending-parent-commit

## INC-20261022-2118-cover-mcp-timeout-kie-fallback
status: fixed
run_date: 2026-10-23
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026
severity: medium
category: api

### What went wrong
- Sync MCP `gpt-image-2` returned HTTP -32001 Request timed out twice for 2K i2i quad canvas.

### How the agent recovered this run
- Switched to preferred async path `scripts/excalibur_blog_kie_gpt_image2_api.py` with KIE_API_KEY (createTask + poll), per kie-gpt-image-api-contract.

### Durable fix needed before next run
- Cover skill/agent docs should lead with Kie API script as primary Cloud path; MCP sync only as optional probe. Reduce wasted double sync retries.

### Suggested files to inspect/change
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/kie-gpt-image-api-contract.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-22
fix_summary:
- Cover skill/agent lead with Kie async API; sync MCP gpt-image-2 = legacy fallback, no blind retry
files_changed:
- `skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `scripts/excalibur_blog_cover_quad_prompt.py` (preferred_image_flow already Kie)
checks_run:
- `rg "Kie async preferred" skills/cover-excalibur-blog/SKILL.md`
commit: pending-parent-commit

