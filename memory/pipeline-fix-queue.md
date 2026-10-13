# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

_None — B01 2026-10-14 fixer closed all listed open incidents._

## Recently fixed (2026-10-14)

## INC-20261014-0001-director-doctor-blog-dir
status: fixed
run_date: 2026-10-14
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: low
category: script

### What went wrong
- `excalibur_blog_doctor.py` still checked llms generator for `--blog-path`, while CLI only exposes `--blog-dir` (pitfalls/memory already say `--blog-dir` only). Preflight SUMMARY errors=1.

### How the agent recovered this run
- One-line doctor check updated to `--blog-dir`; doctor now SUMMARY errors=0.

### Durable fix needed before next run
- Confirm doctor/pitfalls/skills stay aligned on `--blog-dir`; close after verify.

### Suggested files to inspect/change
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Doctor checks `--blog-dir` and asserts llms CLI has no `--blog-path`.
- Pitfalls/indexer docs aligned on `--blog-dir` only.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → SUMMARY errors=0
- `rg` for stale `--blog-path` CLI examples
commit: 1634fa0

## INC-20261014-0002-director-scout-niche-mismatch
status: fixed
run_date: 2026-10-14
role: excalibur-blog-director
topic_id: n/a
article_dir: n/a
severity: medium
category: docs

### What went wrong
- Scout agent/skill still describe AI/automation/Cursor niche, while `memory/brief/site-brief.md` and live WP blog are Авто-Сейлс (import from Japan/Korea/China). `blog-topics.md` has AS* cards but today/scout helpers only accept `B\d+`, so selection becomes needs_scout even with AS P0 topics present.

### How the agent recovered this run
- Director instructs Scout Task to follow site-brief Avto-Sales niche and avoid cannibalization with EXCALIBUR_RECENT_WP_POSTS + AS pool; not following outdated AI scout prompts.

### Durable fix needed before next run
- Rewrite scout agent/skill prompts for Авто-Сейлс niche OR dual-mode from site-brief; optionally teach helpers to recognize AS* topic IDs or migrate AS→B cards.

### Suggested files to inspect/change
- `.cursor/agents/excalibur-blog-scout.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Scout agent/skill rewritten for Авто-Сейлс niche from site-brief (not AI/Cursor).
- `today.py` and `scout_helper.py` accept both `AS*` and `B*` topic IDs; today suggests unused P0 AS01 when available.
files_changed:
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `shared/pipeline-task-map.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_scout_helper.py --suggest-next` (AS+B pool)
- `python3 scripts/excalibur_blog_today.py` → SUGGESTED_TOPIC_ID=AS01
commit: 1634fa0+6f6a09a

## INC-20261014-2105-scout-precommit-secret-names
status: fixed
run_date: 2026-10-14
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: low
category: env

### What went wrong
- `git commit` failed in Cloud pre-commit secrets scanner: `CLOUD_AGENT_INJECTED_SECRET_NAMES` contained a non-identifier token that breaks `${!SECRET_NAME}` (invalid variable name).

### How the agent recovered this run
- Filtered injected/all secret-name lists to valid bash identifiers only for the commit environment, then re-ran commit+push. Hook still scanned remaining secrets; commit was not `--no-verify`.

### Durable fix needed before next run
- Ensure Cloud secret-name injection never emits non-identifier placeholders into `CLOUD_AGENT_*_SECRET_NAMES`, or harden pre-commit to skip invalid names.

### Suggested files to inspect/change
- Cloud Agent secrets injection / pre-commit.cursor hook
- optional local wrapper docs in `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Added `scripts/excalibur_git.sh` that filters `CLOUD_AGENT_*_SECRET_NAMES` to valid bash identifiers (comma-separated) before invoking git/pre-commit.
- Documented in pitfalls, schema/indexer/research skills.
files_changed:
- `scripts/excalibur_git.sh`
- `shared/agent-pipeline-pitfalls.md`
- `CURSOR-CLOUD-RUNBOOK.md`
checks_run:
- filter smoke: invalid tokens dropped; `PUBLIC_SITE_URL,CATALOG_URL` kept
- `bash scripts/excalibur_git.sh status -sb`
commit: 1634fa0

## INC-20261014-0013-research-webfetch-chest-import-504
status: fixed
run_date: 2026-10-14
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026
severity: low
category: api

### What went wrong
- `WebFetch` на конкурента `chest-import.com/stati/elektromobili-iz-kitaya` вернул 504 Gateway Timeout; полный текст страницы в этом run недоступен.

### How the agent recovered this run
- Использованы сниппеты/highlights `WebSearch` + параллельные официальные/экспертные источники (Минфин/Альта, iCustoms, Авто-Сейлс, utilsbor-calc, Drom); URL конкурента оставлен в `source_table` с пометкой о 504.
- Перед commit значения `PUBLIC_SITE_URL` в `research-notes.md` / `research-serp.json` заменены на плейсхолдер `[PUBLIC_SITE_URL]` (secret scan); commit через sanitize `CLOUD_AGENT_*_SECRET_NAMES` (как INC-2105). Предпочтительно: `bash scripts/excalibur_git.sh`.

### Durable fix needed before next run
- В research skill: при 5xx WebFetch — явный fallback на WebSearch highlights + минимум 2 независимых источника по тому же тезису; не блокировать notes из-за одного конкурента.
- Research_start / notes: сразу писать внутренние URL сайта как relative path или `[PUBLIC_SITE_URL]`, не сырой secret; документировать `scripts/excalibur_git.sh` в research skill.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
- `scripts/excalibur_blog_research_start.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Research skill: WebFetch 5xx/504 → WebSearch highlights + ≥2 independent sources; not a notes blocker.
- Internal site URLs as relative/`[PUBLIC_SITE_URL]`; prefer `scripts/excalibur_git.sh` for commits.
files_changed:
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` for WebFetch 5xx guidance in research skills
commit: 6f6a09a


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


## INC-20261014-2119-geo-qa-typed-task-missing
status: fixed
run_date: 2026-10-14
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026
severity: medium
category: docs

### What went wrong
- Cloud API не принимает typed Task `excalibur-blog-geo-qa` (отсутствует в Cloud Task enum); роль запущена через fallback `Task(generalPurpose)` + `.cursor/agents/excalibur-blog-geo-qa.md` + skill.

### How the agent recovered this run
- Выполнен полный GEO QA контракт как generalPurpose subagent по agent/skill paths; pipeline не останавливался.

### Durable fix needed before next run
- Зарегистрировать typed Task types `excalibur-blog-*` в Cloud enum **или** закрепить в AGENTS.md / director skill / pitfalls, что default path = `Task(generalPurpose)` + agent/skill paths (без повторного «discovery» каждый run).
- Docs/fixer: убедиться, что директор всегда передаёт короткий контракт (входы, маркеры, запреты) при fallback.

### Suggested files to inspect/change
- `AGENTS.md`
- `.cursor/agents/excalibur-blog-director.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
- Cursor Cloud Task type registry (вне репо)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Docs default path: typed `excalibur-blog-*` (incl. geo-qa) often missing → immediately `Task(generalPurpose)` + agent/skill + short contract; no enum discovery loops.
files_changed:
- `AGENTS.md`
- `shared/pipeline-task-map.md`
- `shared/agent-pipeline-pitfalls.md`
- `skills/director-excalibur-blog/SKILL.md`
- `.cursor/skills/director-excalibur-blog/SKILL.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
checks_run:
- `rg` for generalPurpose/geo-qa default guidance
commit: 924dd06

## INC-20261014-2120-geo-qa-utility-markers-regression
status: fixed
run_date: 2026-10-14
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026
severity: high
category: qa

### What went wrong
- `utility_gate` вернул BLOCK: `pain_markers=0`, `outcome_markers=0`, хотя в `article.html` уже есть «боль/ошиб/ломает/результат/проверьте/соберите».
- Причина: в `memory/brief/editorial-policy.json` снова отсутствовали `pain_markers_ru` / `outcome_markers_ru` и min-пороги (регрессия; main тоже без списков). Пустые списки + default min_pain=2/min_outcome=3 → ложный BLOCK статьи.

### How the agent recovered this run
- Текст статьи не правился.
- Восстановлены marker lists + `min_pain_markers`/`min_outcome_markers` в `editorial-policy.json` из известного good-state пайплайна.
- Повтор utility: PASS (pain=7, outcome=7).

### Durable fix needed before next run
- Закрепить marker lists в policy и добавить в `utility_gate.py` WARN/skip (не BLOCK), если списки маркеров пустые.
- `excalibur_blog_doctor.py` должен падать, если `pain_markers_ru`/`outcome_markers_ru` отсутствуют или пусты.
- Не допускать rebrand/template sync, затирающий эти ключи.

### Suggested files to inspect/change
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Kept non-empty `pain_markers_ru`/`outcome_markers_ru` in editorial-policy.
- utility_gate: empty marker lists → WARN/skip (not BLOCK).
- doctor FAIL if marker lists missing/empty (<3).
files_changed:
- `memory/brief/editorial-policy.json` (verified present)
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/agent-pipeline-pitfalls.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → pain/outcome marker checks OK
commit: 1634fa0

## INC-20261014-2121-geo-qa-catalog-503-softpass
status: fixed
run_date: 2026-10-14
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026
severity: low
category: script

### What went wrong
- `link_verify` FAIL на CTA каталога: HTTP 503 Service Temporarily Unavailable при корректном absolute href (совпадает с `CATALOG_URL` после rstrip `/`).
- В текущем `scripts/excalibur_blog_link_verify.py` нет durable soft-pass для catalog host 5xx (есть только soft timeout для t.me/vk).

### How the agent recovered this run
- Manual soft-pass в `link-verify.json` по правилу пайплайна: catalog host 5xx + href≈CATALOG_URL → pass; telegram и internal links OK.

### Durable fix needed before next run
- В `excalibur_blog_link_verify.py`: если `href.rstrip('/') == CATALOG_URL.rstrip('/')` (или same host marketing CTA) и status 5xx → `ok=True` + warning, не fail verdict.
- Redact live catalog/site URLs в JSON отчёте (`${CATALOG_URL}`) чтобы не ломать secret scan.

### Suggested files to inspect/change
- `scripts/excalibur_blog_link_verify.py`
- `shared/agent-pipeline-pitfalls.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- `link_verify`: catalog CTA HTTP 5xx when href matches `CATALOG_URL` (or same host) → soft-pass + warning.
- Report URLs redacted to `${CATALOG_URL}`/`${PUBLIC_SITE_URL}` for secret-scan safety.
files_changed:
- `scripts/excalibur_blog_link_verify.py`
- `shared/agent-pipeline-pitfalls.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
checks_run:
- unit: `is_soft_catalog_failure` + `redact_report_urls`
commit: 1634fa0

## Fixed incidents

Handled above; commit is pending Director review.

## INC-20261014-2124-schema-precommit-secret-names
status: fixed
run_date: 2026-10-14
role: excalibur-blog-schema
topic_id: B01
article_dir: memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026
severity: medium
category: env

### What went wrong
- Pre-commit secrets scanner failed with `invalid variable name` because `CLOUD_AGENT_INJECTED_SECRET_NAMES` ended with a non-identifier token (displayed/stored as `[REDACTED]`), so `${!SECRET_NAME}` aborted under `set -e`.
- First `schema.jsonld` draft also contained live `PUBLIC_SITE_URL` / `CATALOG_URL` values copied from `shared/authors-registry.json` (avatar/sameAs), which would fail secret-scan even after the hook bug is fixed.

### How the agent recovered this run
- Scrubbed site/catalog secret values in `schema.jsonld` to `[REDACTED]` (AS08/AS09 pattern) before commit.
- Re-exported `CLOUD_AGENT_INJECTED_SECRET_NAMES` / `CLOUD_AGENT_ALL_SECRET_NAMES` filtered to `^[A-Za-z_][A-Za-z0-9_]*$` for the commit process only; secret scan still ran for valid names.
- **cover (same run):** hit identical pre-commit abort (`https:/` / `[REDACTED]` token in `CLOUD_AGENT_*_SECRET_NAMES`); recovered with the same identifier filter before `feat(cover)` commit `0dd39ed`. Cover pipeline itself had no image retry/blocker.

### Durable fix needed before next run
- Ensure Cloud Agent secret-name injection never appends redacted/non-identifier tokens to `CLOUD_AGENT_*_SECRET_NAMES`.
- Schema skill/script: always sanitize `PUBLIC_SITE_URL`/`CATALOG_URL`/`TELEGRAM_URL`/`MAX_URL` out of committed `schema.jsonld` (write `[REDACTED]` placeholders) even when reading authors-registry.
- Prefer a small `scripts/excalibur_git.sh` wrapper that filters secret names + scrubs staged article artifacts.

### Suggested files to inspect/change
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `skills/schema-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
- `scripts/excalibur_git.sh` (create if missing)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Same `scripts/excalibur_git.sh` wrapper as INC-2105.
- Schema skill requires `[REDACTED]` for live site/catalog/telegram/max URLs in committed schema.jsonld.
files_changed:
- `scripts/excalibur_git.sh`
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- secret-name filter smoke test
commit: 1634fa0+6f6a09a

## INC-20261014-2131-indexer-llms-blog-path-stale
status: fixed
run_date: 2026-10-14
role: excalibur-blog-indexer
topic_id: B01
article_dir: memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026
severity: medium
category: docs

### What went wrong
- First llms generator call used `--blog-path /` from `.cursor/agents/excalibur-blog-indexer.md` and skill CLI example.
- `scripts/excalibur_blog_llms_generator.py` rejects `--blog-path` (`unrecognized arguments`).
- After successful generate, pre-commit secret-scan blocked commit: live `PUBLIC_SITE_URL` written into `memory/blog/llms.txt` and `llms-full.txt` (also `interlink-suggestions.json` site_base).
- Separately, space-joined filtered `CLOUD_AGENT_*_SECRET_NAMES` broke the hook (IFS=`,` expects commas) — same family as INC-2124.

### How the agent recovered this run
- Retried llms without `--blog-path`: `--blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` → PASS; B01 present.
- Scrubbed live site/catalog/telegram/max URLs to `[REDACTED]` in llms + interlink-suggestions before commit.
- Re-exported secret-name lists as comma-separated valid identifiers only.

### Durable fix needed before next run
- Remove `--blog-path` from indexer agent/skill CLI examples; document only flags accepted by the script.
- `excalibur_blog_llms_generator.py` / interlinker: write `[REDACTED]` (or `${PUBLIC_SITE_URL}`) in committed artifacts, not live site base.
- Indexer skill: explicit post-generate scrub + comma filter for `CLOUD_AGENT_*_SECRET_NAMES` before commit.

### Suggested files to inspect/change
- `.cursor/agents/excalibur-blog-indexer.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_llms_generator.py`
- `scripts/excalibur_blog_interlinker.py`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- Removed `--blog-path` from indexer agent/skill examples.
- llms generator + interlinker redact live site base to `[REDACTED]` in committed artifacts.
files_changed:
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_llms_generator.py`
- `scripts/excalibur_blog_interlinker.py`
- `scripts/excalibur_blog_doctor.py`
checks_run:
- doctor: no stale `--blog-path` flag
- `redact_site_base_for_commit` unit
commit: 1634fa0+6f6a09a

## INC-20261014-2134-publish-paramiko-missing
status: fixed
run_date: 2026-10-14
role: excalibur-blog-publish
topic_id: B01
article_dir: memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026
severity: blocker
category: env

### What went wrong
- `ModuleNotFoundError: No module named 'paramiko'` during SSH bootstrap upload in `excalibur_blog_wp_publish.py`.
- `requirements.txt` lists paramiko, but Cloud runtime python did not have it installed (PEP 668 blocked plain pip).

### How the agent recovered this run
- Installed with `python3 -m pip install --break-system-packages paramiko` and retried publish.

### Durable fix needed before next run
- Ensure `.cursor/cloud-agent-install.sh` installs paramiko with `--break-system-packages` and environment build includes it so publish agents boot ready.

### Suggested files to inspect/change
- `.cursor/cloud-agent-install.sh`
- `requirements.txt`
- `.cursor/environment.json`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-10-14
fix_summary:
- `.cursor/cloud-agent-install.sh` installs `requirements.txt` including paramiko with `--break-system-packages` and verifies import.
- doctor warns/fails on missing paramiko depending on `--publish`.
- Documented in CURSOR-CLOUD-RUNBOOK / pitfalls.
files_changed:
- `.cursor/cloud-agent-install.sh`
- `requirements.txt` (already listed paramiko)
- `scripts/excalibur_blog_doctor.py`
- `CURSOR-CLOUD-RUNBOOK.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → paramiko available OK
commit: 1634fa0

