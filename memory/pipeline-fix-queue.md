# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

_none (2026-07-18 AS04 fixer pass)_

## INC-20260718-1239-cover-mcp-timeout-kie-missing-zimage-fallback
status: fixed
run_date: 2026-07-18
role: excalibur-blog-cover
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: high
category: api

### What went wrong
- Preferred path `KIE_API_KEY` + `scripts/excalibur_blog_kie_gpt_image2_api.py` unavailable: env secret missing, no `memory/site.env.local`.
- Sync MCP-KV `gpt-image-2` i2i 2K timed out with client `-32001`; no late URL/task_id recoverable from logs; no async create/status MCP tools exposed.
- Forced documented fallback: ONE `z-image` 16:9 → Pillow rebuild/confirm 2048×1152 → `quad_split --inject-html`.
- Side effect: z-image is t2i (no `input_urls`), so hero likeness is approximate; Cyrillic on panels is partially garbled (readable hooks/caption still present on cover).

### How the agent recovered this run
- Kept ONE-canvas rule (not 4 separate gens).
- Generated via `z-image`, saved `cover/quad-mcp-result.json`, ensured `canvas-quad.png` 2048×1152, split+inject PASS.
- Cover hook/caption non-toxic; brand corner `avto-sales125.ru`; inline panels without hero face.

### Durable fix needed before next run
- Ensure Cloud Secret `KIE_API_KEY` is set and funded (previous runs hit 402 at ~1.43 credits).
- Prefer async Kie script over sync MCP `gpt-image-2` for 2K i2i.
- Optionally expose async MCP create/status tools so timeout recovery can poll `task_id`.
- Document z-image fallback quality limits (face lock + Cyrillic) in cover skill/pitfalls.

### Suggested files to inspect/change
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
- Cursor Dashboard Secrets (`KIE_API_KEY` only; no values recorded)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- Cover skill/pitfalls: prefer async `excalibur_blog_kie_gpt_image2_api.py` when `KIE_API_KEY` present; sync MCP timeout → ONE z-image fallback with documented face-lock/Cyrillic limits.
- Funding/setting `KIE_API_KEY` remains a Dashboard secret action (not a code blocker; fallback path is durable).
files_changed:
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` for z-image/KIE fallback guidance in cover skill + pitfalls
commit: pending-parent-commit


## INC-20260718-1520-director-topic-id-prefix-as-vs-b
status: fixed
run_date: 2026-07-18
role: excalibur-blog-director
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: high
category: script

### What went wrong
- `scripts/excalibur_blog_today.py` `next_p0_topic()` и `scripts/excalibur_blog_scout_helper.py` парсят только `## B\d+` / `(B\d+)-` article dirs.
- Пул тем Авто-Сейлс использует `AS01`…`AS09`, поэтому today.py вернул `EXCALIBUR_TOPIC_SELECTION=needs_scout` и пустой `SUGGESTED_TOPIC_ID` при наличии ненаписанных P0.
- Scout helper показал `Total topics in pool: 0` при 9 карточках в `blog-topics.md`.

### How the agent recovered this run
- Директор вручную выбрал AS04 (utility PASS, slug свободен на WP, не published в ledger) и запустил `research_start.py --topic-id AS04`.

### Durable fix needed before next run
- Расширить regex topic_id до `(?:AS|B)\d+` (или общего `[A-Z]+\d+`) в `excalibur_blog_today.py`, `excalibur_blog_scout_helper.py` и связанных проверках active article dirs.
- Убедиться, что utility soft-skip для FAIL P0 (AS01/AS03/AS05) работает после фикса префикса.

### Suggested files to inspect/change
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- `today.py` / `scout_helper` topic regex expanded to `(?:AS|B)\d+`.
- `today.py` soft-skips P0 topics that fail utility gate (AS01/AS03/AS05).
- Scout `--suggest-next` reports AS* pool correctly (Next AS10 when AS09 exists).
files_changed:
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_today.py scripts/excalibur_blog_scout_helper.py`
- `python3 scripts/excalibur_blog_today.py` → SUGGESTED=AS02 SELECTION=ready
- `python3 scripts/excalibur_blog_scout_helper.py --suggest-next` → pool=9
commit: pending-parent-commit


## INC-20260718-1521-director-llms-blog-path-cli
status: fixed
run_date: 2026-07-18
role: excalibur-blog-director
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_doctor.py` требует `llms generator supports --blog-path`.
- `excalibur_blog_llms_generator.py --help` показывает только `--blog-dir` (и нет `--blog-path`) → doctor SUMMARY errors=1.

### How the agent recovered this run
- Продолжили пайплайн; indexer/fixer должны выровнять CLI и doctor check.

### Durable fix needed before next run
- Либо добавить alias `--blog-path` в llms generator, либо поменять doctor check на `--blog-dir`, плюс обновить skills/docs indexer.

### Suggested files to inspect/change
- `scripts/excalibur_blog_llms_generator.py`
- `scripts/excalibur_blog_doctor.py`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- Added `--blog-path` as argparse alias of `--blog-dir` in llms generator.
- Indexer skill cleaned (removed bogus `--blog-path /`); documents alias.
files_changed:
- `scripts/excalibur_blog_llms_generator.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
checks_run:
- `python3 scripts/excalibur_blog_llms_generator.py --help` shows `--blog-path`
- `python3 scripts/excalibur_blog_doctor.py` → OK blog-path; SUMMARY errors=0
commit: pending-parent-commit


## INC-20260718-1525-research-wordstat-compound-phrase-totalcount
status: fixed
run_date: 2026-07-18
role: excalibur-blog-research
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: low
category: api

### What went wrong
- `wordstat_get_top_requests` для составной фразы «утильсбор корея китай япония» вернул нестандартный ответ `{"totalCount":"17"}` без топа фраз (аналог known scout pitfall).

### How the agent recovered this run
- Повторил запросы по отдельным кластерам: «утильсбор корея», «утильсбор япония», «утильсбор китай»; цифры в research-notes только из успешных ответов.

### Durable fix needed before next run
- В skill research: при secondary из 3+ стран/слов — сразу бить Wordstat по частям; `totalCount`-only = low-result, не fatal.
- Опционально: soft-retry wrapper в MCP/docs.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- Research skill + pitfalls: compound secondary (3+ words/countries) → Wordstat by parts; totalCount-only = low-result, not fatal.
files_changed:
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` for totalCount/compound Wordstat guidance
commit: pending-parent-commit


## INC-20260718-1526-research-notes-gate-tech-marker-ii-false-positive
status: fixed
run_date: 2026-07-18
role: excalibur-blog-research
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_research_notes_gate.py` `TECH_MARKERS` содержал короткие подстроки `ai` / `ии` без границ слова.
- H1 с «Японии» давал `technical_topic=true` → требование `github_urls>=3` для нетехнической авто-темы → BLOCK.

### How the agent recovered this run
- Добавлен `_marker_matches()` с word-boundary для маркеров длиной ≤3; gate PASS без фейковых GitHub URL.
- Также выровнены форматы `accessed_at:` в source_table и keywords pain/solution/result в pain_solution_map (gate regex).

### Durable fix needed before next run
- Закрепить word-boundary для коротких TECH_MARKERS в gate; добавить unit/smoke-тест на тему с «Японии»/«России».
- Документировать контракт pain_solution_map rows (нужны слова pain|solution|result|боль|…) и `accessed_at:` ≥5.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- Kept `_marker_matches()` word-boundary for short TECH_MARKERS; added `--self-test` smoke (Японии/России not technical; ИИ/MCP are).
- Research skill documents pain_solution_map markers + accessed_at ≥5.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_research_notes_gate.py --self-test` → PASS
commit: pending-parent-commit


## INC-20260718-1250-publish-paramiko-missing
status: fixed
run_date: 2026-07-18
role: excalibur-blog-publish
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: high
category: env

### What went wrong
- `paramiko` missing in Cloud image; publish SSH import failed until ad-hoc pip install.

### How the agent recovered this run
- `pip3 install --break-system-packages paramiko` for this run.

### Durable fix needed before next run
- Add paramiko to cloud-agent-install and document preflight import.

### Suggested files to inspect/change
- `.cursor/cloud-agent-install.sh`
- `skills/publish-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- `.cursor/cloud-agent-install.sh` installs + verifies `paramiko`.
- Publish skill notes preflight `python3 -c "import paramiko"`.
files_changed:
- `.cursor/cloud-agent-install.sh`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -c "import paramiko"`
commit: pending-parent-commit

## INC-20260718-1255-publish-http-gateway-504-ssh-php-exec
status: fixed
run_date: 2026-07-18
role: excalibur-blog-publish
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: publish

### What went wrong
- Local HTTP bootstrap trigger hit timeout/Gateway 504; agent recovered via manual SSH PHP exec.

### How the agent recovered this run
- SSH exec `/usr/local/bin/php8.2` on uploaded bootstrap → PASS.

### Durable fix needed before next run
- Automate HTTP → SSH PHP exec → WebFetch fallback chain in publish script + docs.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- `publish_via_ssh` now tries SSH PHP exec (`SSH_PHP_BIN`, default php8.2) before WebFetch wait when HTTP fails.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py`
commit: pending-parent-commit

## INC-20260718-1245-indexer-interlink-suggestions-live-site-base
status: fixed
run_date: 2026-07-18
role: excalibur-blog-indexer
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: low
category: script

### What went wrong
- Interlinker JSON report could embed live `PUBLIC_SITE_URL` when passed as `--site-base` (commit/secret-scan risk).

### How the agent recovered this run
- Regenerated llms/interlink artifacts with `[REDACTED]` site-base.

### Durable fix needed before next run
- Redact live URLs in interlink report; default `--site-base [REDACTED]`; keep relative href inject.

### Suggested files to inspect/change
- `scripts/excalibur_blog_interlinker.py`
- `skills/indexer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- `commit_safe_site_base()` redacts live URLs in JSON report; default site-base `[REDACTED]`; indexer skill updated.
files_changed:
- `scripts/excalibur_blog_interlinker.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- unit assert `commit_safe_site_base('https://example.com') == '[REDACTED]'`
commit: pending-parent-commit


## INC-20260718-1536-geo-qa-utility-empty-pain-outcome-markers
status: fixed
run_date: 2026-07-18
role: excalibur-blog-geo-qa
topic_id: AS04
article_dir: memory/blog/articles/AS04-utilsbor-na-avto-2026
severity: medium
category: qa

### What went wrong
- Utility article gate treated empty `pain_markers_ru` / `outcome_markers_ru` as hard fail (counts vs defaults) when lists were missing from editorial-policy.json.

### How the agent recovered this run
- Policy lists filled; gate now skips pain/outcome checks when marker lists are empty.

### Durable fix needed before next run
- Populate policy marker lists; skip enforcement when lists empty.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-18
fix_summary:
- Added pain/outcome marker lists to editorial-policy.json.
- Utility gate enforces min_pain/min_outcome only when marker lists are non-empty.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_utility_gate.py`
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
