# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

## INC-20260722-2138-cover-kie-402-emergency-generateimage
status: needs-human
run_date: 2026-07-23
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-zakaz-2026
severity: high
category: api

### What went wrong
- Kie API returned 402 Credits insufficient; MCP sync failed; emergency GenerateImage used; canvas was 1536×1024 not 2048×1152.

### How the agent recovered this run
- ONE GenerateImage i2i → resize → split+inject; non-toxic stickers.

### Durable fix needed before next run
- (partial done in repo) Document Kie→MCP→GenerateImage + 402 handling; auto-normalize in split.
- (human) Top up Kie credits so preferred async path works without emergency.

### Suggested files to inspect/change
- Kie dashboard credits (human)
- `skills/cover-excalibur-blog/SKILL.md`
- `shared/kie-gpt-image-api-contract.md`

### Secrets
- none recorded

### Fixer resolution
status: needs-human
reason:
- Kie account still needs credit top-up (HTTP 402); cannot fix balance via git.
- Repo durable path is done: emergency GenerateImage documented; `cover_quad_split.py` auto-normalizes to 2048×1152; `--canvas-local` clarified as nonexistent (use split `--canvas`).
needed_decision_or_secret:
- Top up Kie credits for `KIE_API_KEY` account; confirm next cover run succeeds on Kie async without 402.
files_changed:
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/kie-gpt-image-api-contract.md`
- `shared/blog-cover-quad-canvas-contract.md`
- `scripts/excalibur_blog_cover_quad_split.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_split.py`
- normalize smoke 1536×1024 → 2048×1152 + split PASS

## INC-20260723-2122-bash-unsafe-secret-names
status: needs-human
run_date: 2026-07-23
role: excalibur-blog-fixer
topic_id: n/a
article_dir: n/a
severity: medium
category: env

### What went wrong
- `CLOUD_AGENT_ALL_SECRET_NAMES` содержит URL-shaped токен (не bash identifier: `://`, `/`, `.`, `-`).
- Platform pre-commit, который разворачивает имена секретов в shell, падает с `invalid variable name`.

### How the agent recovered this run
- Перед commit: sanitize `CLOUD_AGENT_INJECTED_SECRET_NAMES` через `scripts/excalibur_blog_check_secret_names.py --print-sanitized-injected`.
- В docs добавлен durable note + advisory checker (не закрывает Dashboard rename).

### Durable fix needed before next run
- В Cursor Dashboard → Cloud Secrets: **удалить или переименовать** секрет, чьё *имя* выглядит как URL (не значение URL в нормальном `*_URL` ключе).
- Имена только `[A-Za-z_][A-Za-z0-9_]*`. Значения URL — в секретах вроде `PUBLIC_SITE_URL` / `CATALOG_URL`, не в имени ключа.

### Suggested files to inspect/change
- Cursor Dashboard Cloud Secrets (human)
- `scripts/excalibur_blog_check_secret_names.py` (advisory already in repo)
- `CURSOR-CLOUD-RUNBOOK.md`

### Secrets
- none recorded (URL-shaped name redacted in logs)

### Fixer resolution
status: needs-human
reason:
- Durable rename/delete of the bad Cloud Secret name must be done in Cursor Dashboard by a human; repo only has advisory check + sanitize recipe.
reconfirmed_at: 2026-07-22
note: advisory script still WARNs; Dashboard rename still required.
needed_decision_or_secret:
- Open Cursor Dashboard → Secrets for this environment → find the secret whose **name** is URL-shaped (not a normal `FOO_URL` key) → delete it or rename to a bash-safe identifier → re-run `python3 scripts/excalibur_blog_check_secret_names.py` until WARN clears.

## Fixed / closed this run

## INC-20260723-2140-indexer-llms-doctor-blog-path
status: fixed
run_date: 2026-07-23
role: excalibur-blog-indexer
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-zakaz-2026
severity: medium
category: script

### What went wrong
- `excalibur_blog_doctor.py` требовал `--blog-path` в help llms generator → false-positive FAIL.
- Реальный CLI принимает только `--blog-dir`; agent/skill examples ещё показывали `--blog-path /`.

### How the agent recovered this run
- Запустил llms generator с `--blog-dir` без `--blog-path`.

### Durable fix needed before next run
- (done) doctor `--blog-dir`/`--out-dir`; sync indexer agent/skill; pitfalls note.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-22
fix_summary:
- Doctor checks `--blog-dir` and `--out-dir` (not `--blog-path`).
- Indexer agent/skill examples use `--blog-dir` + `--out-dir` only; note about secret-scan redact on llms/promotion.
- Pitfalls Indexer section updated.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_doctor.py`
- `python3 scripts/excalibur_blog_doctor.py` → OK llms `--blog-dir`/`--out-dir`
- `rg` no erroneous `--blog-path /` shell examples in durable indexer sources
commit: 7168a9d

## INC-20260722-2146-publish-paramiko-missing-from-cloud-install
status: fixed
run_date: 2026-07-22
role: excalibur-blog-publish
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-zakaz-2026
severity: high
category: env

### What went wrong
- `ModuleNotFoundError: paramiko` on first SSH publish; install.sh/Dockerfile omitted paramiko despite `requirements.txt`.

### How the agent recovered this run
- Manual `pip3 install paramiko`; publish PASS (WP 3625).

### Durable fix needed before next run
- (done) install path + Dockerfile + doctor import check.

### Suggested files to inspect/change
- `.cursor/cloud-agent-install.sh`
- `.cursor/Dockerfile`
- `scripts/excalibur_blog_doctor.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-22
fix_summary:
- `cloud-agent-install.sh` installs from `requirements.txt` and ensures `paramiko`.
- Dockerfile pins numpy + paramiko with other deps.
- Doctor checks `import paramiko` (warn default; error with `--publish`).
- Pitfalls + CURSOR-CLOUD-RUNBOOK note.
files_changed:
- `.cursor/cloud-agent-install.sh`
- `.cursor/Dockerfile`
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`
- `CURSOR-CLOUD-RUNBOOK.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_doctor.py`
- `python3 scripts/excalibur_blog_doctor.py` → OK paramiko
- `import paramiko` OK in env
commit: 7168a9d


## INC-20260723-2120-utility-gate-empty-pain-outcome
status: fixed
run_date: 2026-07-23
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-zakaz-2026
severity: high
category: script

### What went wrong
- `excalibur_blog_utility_gate.py` требует `min_pain_markers` default 2 и `min_outcome_markers` default 3.
- В `memory/brief/editorial-policy.json` нет ключей `pain_markers_ru` / `outcome_markers_ru` (пустые списки) → counts всегда 0 → article utility gate **всегда BLOCK**, даже при сильном pain/outcome в тексте.
- Дополнительно `recommendation_markers_ru` не знает `чек-лист` / `делать:` / `не делать:` — статья с естественными «Делать/Не делать» и «чек-лист» набирает только 5/8 (`проверьте`+`ориентир`).

### How the agent recovered this run
- GEO QA не правил `article.html` (контракт: FIX-лист Writer). Зафиксировал FAIL + FIX; эскалация на Fixer для policy/script до повторного PASS.

### Durable fix needed before next run
- Добавить в `editorial-policy.json` осмысленные `pain_markers_ru` и `outcome_markers_ru` (и при желании `min_pain_markers` / `min_outcome_markers` в `article_required_signals`).
- В `excalibur_blog_utility_gate.py`: если список маркеров пуст — не применять default min (считать min=0) либо fail-fast с явной ошибкой конфигурации.
- Расширить `recommendation_markers_ru`: `чек-лист`, `делать:`, `не делать:` (и/или документация Writer: exact literals).
- Проверить, что предыдущий Fixer-fix «utility DEFAULT markers» действительно попал в ветку (сейчас на диске списки отсутствуют).

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/editorial-utility-only.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-23
fix_summary:
- Restored `pain_markers_ru` / `outcome_markers_ru` + mins in `editorial-policy.json` (regression after rebrand).
- Expanded `recommendation_markers_ru` with `делать:`, `не делать:`, `чек-лист`.
- `utility_gate.py` again has built-in DEFAULT lists + warning when policy lists are empty.
- Writer/editorial docs document exact recommendation literals.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/editorial-utility-only.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_utility_gate.py`
- JSON parse `memory/brief/editorial-policy.json`
- `utility_gate --article-dir B01` → PASS (pain=6, outcome=5, action=27)
commit: 3d871ab

## INC-20260723-2121-cloud-typed-geo-qa-missing
status: fixed
run_date: 2026-07-23
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-zakaz-2026
severity: medium
category: tool

### What went wrong
- Cloud API не принимает typed Task `excalibur-blog-geo-qa` → роль запущена через fallback `Task(generalPurpose)` + пути `.cursor/agents/excalibur-blog-geo-qa.md` и `.cursor/skills/excalibur-geo-qa/SKILL.md`.

### How the agent recovered this run
- Выполнен полный GEO QA контракт в generalPurpose Task; cover/schema/publish не запускались.

### Durable fix needed before next run
- Зафиксировать в `AGENTS.md` / `CLOUD-AUTOMATION.md` / `.cursor/rules/excalibur-blog-orchestrator.mdc` durable fallback: при отсутствии typed enum — один `Task(generalPurpose)` на роль с agent+skill paths (уже частично есть; проверить, что GEO QA явно в списке и Director всегда использует fallback без попытки typed-only).

### Suggested files to inspect/change
- `AGENTS.md`
- `CLOUD-AUTOMATION.md`
- `.cursor/rules/excalibur-blog-orchestrator.mdc`
- `.cursor/agents/excalibur-blog-director.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-23
fix_summary:
- Documented immediate generalPurpose fallback when typed `excalibur-blog-geo-qa` (and other roles) are missing; no typed-only retry loop.
- Explicit GEO QA agent+skill paths in AGENTS.md / director / CLOUD-AUTOMATION / orchestrator rules / pitfalls.
files_changed:
- `AGENTS.md`
- `CLOUD-AUTOMATION.md`
- `rules/excalibur-blog-orchestrator.mdc`
- `.cursor/rules/excalibur-blog-orchestrator.mdc`
- `agents/excalibur-blog-director.md`
- `.cursor/agents/excalibur-blog-director.md`
- `skills/director-excalibur-blog/SKILL.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` for geo-qa generalPurpose fallback in AGENTS.md / CLOUD-AUTOMATION.md / orchestrator
commit: 3d871ab

## INC-20260723-2106-research-notes-gate-format-quirks
status: fixed
run_date: 2026-07-23
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-avto-iz-korei-pod-zakaz-2026
severity: medium
category: script

### What went wrong
- Первый прогон `excalibur_blog_research_notes_gate.py` дал BLOCK: `accessed_at` в таблице источников как дата `2026-07-23` не считался — gate ищет литерал `accessed_at:` (`\baccessed_at\b\s*:`).
- Строки `pain_solution_map` без слов pain/solution/result/боль/решение/результат не засчитывались (header + 1 случайное совпадение = 2 < 3).
- `search_intent: workflow` попадает в TECH_MARKERS (`workflow`), тема авто-импорта помечается `technical_topic=true` и требует ≥3 GitHub URL + docs URL — лишний шум для не-IT статьи.

### How the agent recovered this run
- Переписал ячейки даты в `accessed_at: 2026-07-23`, префиксы pain/solution/результат в строках карты, добавил GitHub/docs evidence; gate PASS со второго прогона.

### Durable fix needed before next run
- Документировать в research skill/agent контракт gate: в source_table дата должна быть `accessed_at: YYYY-MM-DD`; в pain_solution_map — ключевые слова pain/solution/result (или RU-эквиваленты) в каждой data-row.
- Убрать `workflow` из TECH_MARKERS или не сканировать `search_intent` на tech-маркеры (иначе любой workflow-гайд = «technical»).
- Опционально: считать колонку `accessed_at` в markdown-таблице без требования двоеточия в ячейке.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/skills/excalibur-research/SKILL.md`
- `.cursor/agents/excalibur-blog-research.md`
- `shared/editorial-utility-only.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-23
fix_summary:
- Removed `workflow` from TECH_MARKERS; `search_intent` no longer scanned for tech.
- Short TECH_MARKERS are whole-word; `count_accessed_at` accepts ISO dates in accessed_at column; `count_pain_solution_map_rows` counts section table rows.
- Research agent/skill + editorial docs document gate contract; `--self-test` covers workflow false-positive.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `agents/excalibur-blog-research.md`
- `.cursor/agents/excalibur-blog-research.md`
- `shared/editorial-utility-only.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_research_notes_gate.py`
- `python3 scripts/excalibur_blog_research_notes_gate.py --self-test` → PASS
- research-notes-gate B01 → PASS (`technical_topic=false`)
commit: 3d871ab

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

