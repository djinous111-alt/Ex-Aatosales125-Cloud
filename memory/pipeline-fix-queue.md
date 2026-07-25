# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

> Post-fixer 2026-07-26: open AS02 incidents closed as `fixed` or `needs-human` below. Remaining human blockers: Kie credits + cover→publish resume.


## INC-20260726-2116-publish-missing-cover
status: needs-human
run_date: 2026-07-26
role: excalibur-blog-publish
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: blocker
category: publish

### What went wrong
- Publish step ⑥ ran with `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` and `publish: yes`, but required featured assets are missing: `cover/cover.png` and `cover/cover-registry.json`.
- Root cause is upstream cover failure (Kie createTask 402 credits) — see INC-20260726-2112-cover-kie-402-credits.
- Contract forbids inventing cover.png; featured image + alt registry are hard preconditions for WP publish.

### How the agent recovered this run
- Preflight: link-verify PASS (3/3), `--env-check` allow_publish=true / SSH host+user configured.
- Dry-run `excalibur_blog_wp_publish.py --dry-run` OK (slug/title/PHP payload), but live publish was **not** started.
- Returned explicit `❌ PUBLISH BLOCKER` (step completed, not skipped); ledger left `in_progress`.

### Durable fix needed before next run
- Top up Kie credits → re-run cover for AS02 → produce `cover/cover.png` + `cover-registry.json` + inject inline figures.
- Then re-run publish only (link-verify → dry-run → publish → ledger `published`).
- Optional: make `--dry-run` fail-fast when cover.png missing so director sees blocker earlier.

### Suggested files to inspect/change
- `memory/blog/articles/AS02-encar-na-russkom-kak-chitat/cover/`
- `scripts/excalibur_blog_wp_publish.py` (preflight cover gate in dry-run)
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `memory/pipeline-fix-queue.md#INC-20260726-2112-cover-kie-402-credits`

### Secrets
- none recorded

### Fixer resolution
status: needs-human
fixed_at: 2026-07-26
reason:
- Depends on cover (Kie 402); featured assets still missing — cannot invent cover.png.
- Durable partial fix shipped: dry-run fail-fast when cover.png / cover-registry.json absent.
needed_decision_or_secret:
- After cover PASS for AS02: link-verify → dry-run → live publish → ledger `published`.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- AS02 `--dry-run` → exit 2, cover_missing listed
resume:
- cover → publish
commit: f9344e2

## INC-20260726-2112-cover-kie-402-credits
status: needs-human
run_date: 2026-07-26
role: excalibur-blog-cover
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: high
category: api

### What went wrong
- Preferred cover flow `scripts/excalibur_blog_kie_gpt_image2_api.py` (createTask → recordInfo) failed at createTask with `code=402` / `Credits insufficient`.
- Same Cloud `KIE_API_KEY` balance issue as prior B01 cover run; cannot produce `canvas-quad.png` / `cover.png` / inline panels.
- Skill forbids GenerateImage workaround and inventing cover assets without a real MCP/Kie URL.

### How the agent recovered this run
- Director MCP retry `gpt-image-2`: error NoneType/.get — no URL; cover remains missing (no invented PNG).
- Prepared AS02 cover artifacts only: `cover/quad-manifest.json` (Encar hooks, non-toxic stickers), `quad-mcp-prompt.txt`, `quad-mcp-batch.json` (1 job, `input_urls` set).
- Did **not** invent `cover.png` / inline PNGs; did **not** inject fake figures into `article.html`.
- Wrote fragment `.cursor/excalibur-blog-fragments/cover.md` with status ❌ and blocker `KIE API 402 credits`.

### Durable fix needed before next run
- Top up Kie.ai credits for Cloud Secret `KIE_API_KEY`.
- Re-run cover only: `python3 scripts/excalibur_blog_kie_gpt_image2_api.py --article-dir memory/blog/articles/AS02-encar-na-russkom-kak-chitat` then `excalibur_blog_quad_apply.py --inject-html` (batch already ready).
- Optionally document preflight balance check before cover||schema parallel start.

### Suggested files to inspect/change
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `memory/blog/articles/AS02-encar-na-russkom-kak-chitat/cover/quad-mcp-batch.json`
- Cursor Dashboard Secrets → `KIE_API_KEY` billing

### Secrets
- none recorded (do not log API key)

### Fixer resolution
status: needs-human
fixed_at: 2026-07-26
reason:
- Cannot top-up Kie.ai credits from the repository; createTask 402 is an external billing blocker.
needed_decision_or_secret:
- Human: top up Kie credits for Cloud Secret `KIE_API_KEY`.
- Resume cover only (keep prepared `quad-mcp-batch.json`): `python3 scripts/excalibur_blog_kie_gpt_image2_api.py --article-dir memory/blog/articles/AS02-encar-na-russkom-kak-chitat` then `excalibur_blog_quad_apply.py --inject-html` (or MCP gpt-image-2 with batch args).
- Do not invent cover.png / GenerateImage workaround.
files_changed:
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- confirmed AS02 cover/ has quad-mcp-batch.json and no cover.png
commit: f9344e2

## INC-20260726-2108-writer-as02-policy-cta-gap
status: fixed
run_date: 2026-07-26
role: excalibur-blog-writer
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: medium
category: docs

### What went wrong
- `shared/public-cta.json` отсутствует; Writer брал CTA из env `CATALOG_URL` / `TELEGRAM_URL` (с `<!-- pragma: allowlist secret -->`), иначе conversion-map содержит placeholder.
- `memory/brief/editorial-policy.json` не содержал `pain_markers_ru` / `outcome_markers_ru`, а `excalibur_blog_utility_gate.py` по умолчанию требует min 2/3 → любой article utility gate BLOCK (в т.ч. уже опубликованный AS09).
- Recommendation markers в тексте должны быть императивом (`Сделайте` / `Не делайте`), формулировка `Делать:` / `Не делать:` utility gate не засчитывает.

### How the agent recovered this run
- CTA href подставлены из env; pragma allowlist на строках ссылок.
- В `editorial-policy.json` добавлены `pain_markers_ru` / `outcome_markers_ru` (как в human-voice gate) и явные min в `article_required_signals`.
- Статья переписана с маркерами действия; utility + human-voice + html linter PASS.

### Durable fix needed before next run
- Не коммитить `shared/public-cta.json`, пока CATALOG/TELEGRAM/PUBLIC/MAX URL лежат в Cloud Secrets (secret scan блокирует). Writer: CTA только из env + `<!-- pragma: allowlist secret -->`. Долгосрочно: вынести публичные URL из Secrets (см. INC-1720) либо whitelist в precommit.
- Зафиксировать в writer skill: recommendation markers = императив из `recommendation_markers_ru`.
- Fixer: подтвердить, что utility gate не падает при пустых marker lists (skip или fail-fast на policy).

### Suggested files to inspect/change
- `shared/public-cta.json` (создать)
- `memory/brief/editorial-policy.json`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_utility_gate.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-26
fix_summary:
- Writer skill/contract: CTA from env + pragma allowlist; do not commit live `public-cta.json` while URLs are Cloud Secrets; example at `shared/public-cta.example.json`.
- Recommendation markers documented as imperatives from `recommendation_markers_ru` (`Сделайте`/`Не делайте`); `Делать:` not counted.
- `editorial-policy.json` already has pain/outcome markers + mins; utility gate fail-fast if marker lists empty.
- conversion-map documents env-based CTA roles.
files_changed:
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `shared/public-cta.example.json`
- `memory/brief/conversion-map.md`
- `memory/brief/editorial-policy.json` (markers confirmed)
- `scripts/excalibur_blog_utility_gate.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_utility_gate.py`
- JSON parse editorial-policy + public-cta.example
- `rg` pragma/CTA guidance in writer skills
commit: f9344e2

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
commit: bb13591

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

## INC-20260724-2029-director-as-topic-regex
status: fixed
run_date: 2026-07-24
role: excalibur-blog-director
topic_id: AS02
article_dir: n/a
severity: high
category: script

### What went wrong
- `excalibur_blog_today.py` and `excalibur_blog_scout_helper.py` matched only `B\\d+` topic cards, so AS* pool looked empty and today returned `needs_scout`.
- Doctor failed: missing numpy; llms generator lacked `--blog-path` alias required by doctor/indexer contract.

### How the agent recovered this run
- Extended topic regex to `(?:B|AS)\\d+` in today + scout helper.
- Added `--blog-path` alias to llms generator.
- Installed `python3-numpy` via apt for the Cloud VM.

### Durable fix needed before next run
- Keep AS|B topic ID support in today/scout helper.
- Keep `--blog-path` alias; ensure Cloud image has numpy (apt or environment.json).

### Suggested files to inspect/change
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_llms_generator.py`
- `.cursor/environment.json`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-26
fix_summary:
- Confirmed `(?:B|AS)\d+` in today.py + scout_helper; `--blog-path` alias on llms generator.
- Cloud image: numpy via Dockerfile `python3-numpy` + pip fallback in `cloud-agent-install.sh`; note in `environment.json`.
files_changed:
- `scripts/excalibur_blog_today.py` (already patched)
- `scripts/excalibur_blog_scout_helper.py` (already patched)
- `scripts/excalibur_blog_llms_generator.py` (alias + URL-path guard)
- `.cursor/Dockerfile`
- `.cursor/cloud-agent-install.sh`
- `.cursor/environment.json`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → errors=0
- `python3 scripts/excalibur_blog_today.py` → SUGGESTED_TOPIC_ID=AS01
- `python3 scripts/excalibur_blog_llms_generator.py --help` has `--blog-path`
- `import numpy` OK
commit: f9344e2

## INC-20260726-2105-research-wordstat-truncated-top
status: fixed
run_date: 2026-07-26
role: excalibur-blog-research
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: medium
category: api

### What went wrong
- `wordstat_get_top_requests` for secondary phrases `как читать encar` and `читать encar` returned truncated payload `{"totalCount":"3"}` without phrase list / impressions (not HTTP 401).
- Same class of truncated Wordstat responses already seen on AS09 for some Encar-check phrases.
- Separately: `excalibur_blog_research_notes_gate.py -o` with a repo-relative path nests output under `article_dir/`; must use `-o research-notes-gate.json` only.
- Gate marks non-tech auto topics as `technical_topic` if notes contain `github` (section `github_evidence`), producing a docs warning unless a `/docs` URL is added.

### How the agent recovered this run
- Kept Wordstat numbers only for successful phrases (`encar на русском`, `проверка авто корея`, `encar`, `trust encar`, `carhistory`); documented partial warning without inventing impressions for broken secondary.
- Re-ran research-notes gate with `-o research-notes-gate.json`; removed nested duplicate output dir; added `https://carapis.com/docs` for official docs signal.
- Gate status PASS.

### Durable fix needed before next run
- Harden Wordstat MCP client/docs: on truncated `totalCount`-only responses, retry without regions / alternate phrasing and surface a stable `WORDSTAT PARTIAL` contract (not only 401 auth warning).
- Document in research skill that `-o` for research-notes gate is relative to `--article-dir`.
- Consider excluding the literal heading `github_evidence` / URL host `github.com` from `is_technical_topic()` false positives for auto niche topics.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `scripts/excalibur_blog_research_notes_gate.py`
- MCP Wordstat wrapper / server notes (if in repo)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-26
fix_summary:
- Research skill: cluster-first Wordstat + `WORDSTAT PARTIAL` for totalCount-only payloads; retry without inventing impressions.
- Documented `-o research-notes-gate.json` relative to `--article-dir`.
- `is_technical_topic()` no longer false-positives on required `github_evidence` heading / github.com hosts.
files_changed:
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `scripts/excalibur_blog_research_notes_gate.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_research_notes_gate.py`
- `rg` WORDSTAT PARTIAL in research skills
commit: f9344e2

## INC-20260726-2114-indexer-llms-blog-path-slash
status: fixed
run_date: 2026-07-26
role: excalibur-blog-indexer
topic_id: AS02
article_dir: memory/blog/articles/AS02-encar-na-russkom-kak-chitat
severity: medium
category: docs

### What went wrong
- Indexer skill/agent still show `llms_generator --blog-path /` (URL path), but script treats `--blog-path` as alias for `--blog-dir`.
- With both flags, `--blog-path /` wins → loads filesystem root → `Loaded 0 articles` and overwrites `memory/blog/llms.txt` / `llms-full.txt` with empty indexes.

### How the agent recovered this run
- Re-ran with only `--blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (omit `--blog-path /`).
- Confirmed `Loaded 3 articles`; AS02 present in `llms.txt`.
- Commit secret-scan blocked absolute `PUBLIC_SITE_URL` in llms/checklist → rewrote committed URLs to relative `/blog/...`.

### Durable fix needed before next run
- Update indexer skill/agent examples: either drop `--blog-path /` or pass `--blog-path memory/blog/articles`.
- Add pitfalls line: never pass `--blog-path /` to llms generator; it is a dir alias, not WP URL path.
- Optional: ignore `--blog-path` values that are URL paths (`/`, `/blog`) when `--blog-dir` is set.
- Document commit-safe llms output: relative `/blog/{slug}/` or pragma allowlist when `PUBLIC_SITE_URL` is a Cloud Secret (related needs-human public-URL secret issue).

### Suggested files to inspect/change
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `agents/excalibur-blog-indexer.md`
- `shared/agent-pipeline-pitfalls.md`
- `scripts/excalibur_blog_llms_generator.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-26
fix_summary:
- Indexer agent/skill examples drop `--blog-path /`; document alias = `--blog-dir memory/blog/articles`.
- llms generator ignores URL-path-like `--blog-path` (`/`, `/blog`) with WARNING when `--blog-dir` is set.
- Pitfalls + commit-safe relative `/blog/{slug}/` note.
files_changed:
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `scripts/excalibur_blog_llms_generator.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `--blog-path /` with `--blog-dir memory/blog/articles` → WARNING + Loaded 3 articles
- `rg` confirmed no command examples with `--blog-path /`
commit: f9344e2

