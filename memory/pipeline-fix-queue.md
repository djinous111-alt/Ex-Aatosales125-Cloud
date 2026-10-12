# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

(none)

## Fixed incidents

## INC-20261012-1326-geo-qa-utility-pain-outcome-policy
status: fixed
run_date: 2026-10-12
role: excalibur-blog-geo-qa
topic_id: B01
article_dir: memory/blog/articles/B01-levyj-rul-iz-korei-kak-vybrat-2026
severity: blocker
category: script
fixed_at: 2026-10-12

### What went wrong
- `excalibur_blog_utility_gate.py` always counts `pain_markers_ru` / `outcome_markers_ru` from `memory/brief/editorial-policy.json` and defaults `min_pain_markers=2`, `min_outcome_markers=3`.
- Current policy file has neither key → marker lists are empty → every article gets `pain_markers=0` and `outcome_markers=0` → permanent `UTILITY ARTICLE BLOCKER`, even when human-voice gate already finds pain/outcome hits via its hardcoded lists.
- B01 additionally has a real content gap: `action_markers=6 < 8` (writer used «Делать/Не делать», while gate counts «сделайте/не делайте» and peers).

### How the agent recovered this run
- Did not edit `article.html` (GEO QA contract: FIX → writer).
- Wrote `article-qa.md` verdict FAIL + writer FIX for action markers.
- Recorded this incident for Fixer; cover||schema not started.

### Durable fix needed before next run
- Add `pain_markers_ru` and `outcome_markers_ru` to `memory/brief/editorial-policy.json` (align with `PAIN_MARKERS` / `OUTCOME_MARKERS` in `scripts/excalibur_blog_human_voice_gate.py`, or document a single shared list).
- Add `min_pain_markers` / `min_outcome_markers` explicitly under `article_required_signals`.
- Document in writer skill/contract that recommendation markers must use exact substrings from `recommendation_markers_ru` («сделайте», not only «Делать»).
- Optionally: if policy lists missing, utility gate should warn/skip pain-outcome checks instead of hard-blocking with zeros.

### Fixer resolution
status: fixed
fixed_at: 2026-10-12
fix_summary:
- Added `pain_markers_ru` / `outcome_markers_ru` aligned with human-voice gate PAIN_MARKERS / OUTCOME_MARKERS.
- Set explicit `min_pain_markers: 2` and `min_outcome_markers: 3` in `article_required_signals`.
- Utility gate now warns/skips pain-outcome checks when policy lists are missing (no hard-block with zeros).
- Writer/contract/editorial docs require exact `recommendation_markers_ru` substrings.
files_changed:
- `memory/brief/editorial-policy.json`
- `scripts/excalibur_blog_utility_gate.py`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `shared/editorial-utility-only.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m json.tool memory/brief/editorial-policy.json`
- `python3 scripts/excalibur_blog_utility_gate.py --article-dir memory/blog/articles/B01-levyj-rul-iz-korei-kak-vybrat-2026 --output …` → PASS (pain=3, outcome=6, action=17)
commit: pending-parent-commit

## INC-20261012-1310-doctor-llms-blog-path
status: fixed
run_date: 2026-10-12
role: excalibur-blog-director
topic_id: B01
article_dir: memory/blog/articles/B01-levyj-rul-iz-korei-kak-vybrat-2026
severity: low
category: script
fixed_at: 2026-10-12

### What went wrong
- `scripts/excalibur_blog_doctor.py` still checks that `excalibur_blog_llms_generator.py --help` contains `--blog-path`.
- Current generator CLI only exposes `--blog-dir`.

### Fixer resolution
status: fixed
fixed_at: 2026-10-12
fix_summary:
- Doctor assertion updated to `--blog-dir`.
files_changed:
- `scripts/excalibur_blog_doctor.py`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → SUMMARY errors=0 warnings=0
- `rg` confirms no `--blog-path` in doctor
commit: pending-parent-commit

## INC-20261012-1305-scout-as-topics-blind-check
status: fixed
run_date: 2026-10-12
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: script
fixed_at: 2026-10-12

### What went wrong
- Scout helper parsed only `## B\d+` cards, so `--check-query` ignored all `AS*` primary queries.

### Fixer resolution
status: fixed
fixed_at: 2026-10-12
fix_summary:
- `load_existing_topics` parses any PREFIX+digits cards (AS*, B*, …) for cannibalization.
- `--suggest-next` still computes next id from B* only; unwritten list is B*-scoped.
- Restored `scripts/excalibur_blog_filter_secret_names.py` for pre-commit secret-name sanitization.
- Scout skill documents AS* overlap + python3 CLI.
files_changed:
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_filter_secret_names.py`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `--check-query "авто из кореи или японии"` → CRITICAL exact match AS03
- `--suggest-next` → Next B02; B* pool=1; total pool=10
- filter_secret_names smoke on mixed URL/valid names
commit: pending-parent-commit

## INC-20261012-1320-research-gate-ai-false-technical
status: fixed
run_date: 2026-10-12
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-levyj-rul-iz-korei-kak-vybrat-2026
severity: medium
category: script
fixed_at: 2026-10-12

### What went wrong
- Bare substring `ai` in TECH_MARKERS matched `reader_pain` → false `technical_topic` + GitHub×3.

### Fixer resolution
status: fixed
fixed_at: 2026-10-12
fix_summary:
- Short TECH_MARKERS (`ai`, `ии`, `api`, `rag`, `mcp`, `make`) use word-boundary matching.
- Auto-import niche (Encar, растаможка, левый руль, JP/KR/CN, …) forces `technical_topic=false` (no GitHub×3).
- Research skill documents auto-niche GitHub N/A path.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- research-notes gate on B01 → PASS, `technical_topic=False`
commit: pending-parent-commit

## INC-20261012-1321-research-webfetch-timeouts
status: fixed
run_date: 2026-10-12
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-levyj-rul-iz-korei-kak-vybrat-2026
severity: low
category: api
fixed_at: 2026-10-12

### What went wrong
- WebFetch 504 / anti-bot stubs forced ad-hoc recovery without skill guidance.

### Fixer resolution
status: fixed
fixed_at: 2026-10-12
fix_summary:
- Research skill: on 504/anti-bot require ≥2 alternate primaries + `notes_on_fetch_errors` section; not fatal.
files_changed:
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` / skill text review for WebFetch 504 guidance
commit: pending-parent-commit

## INC-20261012-1345-writer-cta-pragma-allowlist
status: fixed
run_date: 2026-10-12
role: excalibur-blog-writer
topic_id: B01
article_dir: memory/blog/articles/B01-levyj-rul-iz-korei-kak-vybrat-2026
severity: medium
category: env
fixed_at: 2026-10-12

### What went wrong
- Pre-commit secrets scanner treats public marketing URLs as secrets; injected secret names may be space-separated / URL-shaped.

### Fixer resolution
status: fixed
fixed_at: 2026-10-12
fix_summary:
- Writer skill + writing contract document same-line `<!-- pragma: allowlist secret -->` for CTA URLs from Cloud Secrets.
- Added `scripts/excalibur_blog_filter_secret_names.py` (filter to valid bash identifiers, comma-join, `--export`).
files_changed:
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `shared/editorial-utility-only.md`
- `scripts/excalibur_blog_filter_secret_names.py`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_filter_secret_names.py`
- filter_secret_names smoke test
commit: pending-parent-commit

## INC-20260616-2015-geo-qa-html-cli-mismatch
status: fixed
run_date: 2026-06-16
role: excalibur-blog-geo-qa
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: qa

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
severity: low
category: prompt
fixed_at: 2026-06-16
fix_summary: Cover toxic sticker text forbidden in style/prompt/QA.
commit: pending-parent-commit

## INC-20260616-1950-scout-wordstat-format
status: fixed
run_date: 2026-06-16
role: excalibur-blog-scout
severity: low
category: api
fixed_at: 2026-06-16
fix_summary: Scout Wordstat cluster-first / totalCount-only documented.
commit: pending-parent-commit

## INC-20260616-2031-indexer-python-missing
status: fixed
run_date: 2026-06-16
role: excalibur-blog-indexer
severity: low
category: env
fixed_at: 2026-06-16
fix_summary: Indexer examples use python3.
commit: pending-parent-commit

## INC-20260616-2042-publish-ssh-root-dot
status: fixed
run_date: 2026-06-16
role: excalibur-blog-publish
severity: low
category: publish
fixed_at: 2026-06-16
fix_summary: Publish --env-check + SSH root ENOENT fallback to `.`.
commit: pending-parent-commit
