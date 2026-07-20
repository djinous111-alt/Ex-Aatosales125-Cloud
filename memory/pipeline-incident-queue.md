# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

(none)

## Fixed incidents


## INC-20260720-1337-publish-paramiko-missing
status: fixed
run_date: 2026-07-20
role: excalibur-blog-publish
topic_id: AS10
article_dir: memory/blog/articles/AS10-sbkts-i-epts-vladivostok-2026
severity: medium
category: env
fixed_at: 2026-07-20
fix_summary:
- `paramiko` already in `requirements.txt`; cloud install now installs `-r requirements.txt` with paramiko fallback.
- Doctor checks paramiko (WARN default, FAIL with `--publish`).
- Documented in CURSOR-CLOUD-RUNBOOK / CLOUD-AUTOMATION / publish skills.
files_changed:
- `.cursor/cloud-agent-install.sh`
- `scripts/excalibur_blog_doctor.py`
- `CURSOR-CLOUD-RUNBOOK.md`
- `CLOUD-AUTOMATION.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_doctor.py`
- `python3 scripts/excalibur_blog_doctor.py` → errors=0 (paramiko OK)
commit: 58846fed40661af307e001f1cfea0af31a465af4

### What went wrong
- `scripts/excalibur_blog_wp_publish.py` failed on first publish attempt: `ModuleNotFoundError: No module named 'paramiko'`.

### Fixer resolution
- Durable install + doctor preflight.


## INC-20260720-1329-indexer-llms-blog-path-stale
status: fixed
run_date: 2026-07-20
role: excalibur-blog-indexer
topic_id: AS10
severity: medium
category: docs
fixed_at: 2026-07-20
fix_summary:
- Doctor asserts `--blog-dir` / `--out-dir` (warn if stale `--blog-path` present).
- Indexer agent/skill examples drop `--blog-path`.
- LLMs generator: `--redact-site-base` for commit-safe outputs; publish reinject docs.
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_llms_generator.py`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_doctor.py` → OK blog-dir/out-dir
- `python3 scripts/excalibur_blog_llms_generator.py --help` → blog-dir + redact-site-base
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- CLI/docs aligned; no `--blog-path`.


## INC-20260720-1327-cover-white-hoodie-hardcode
status: fixed
run_date: 2026-07-20
role: excalibur-blog-cover
topic_id: AS10
severity: medium
category: prompt
fixed_at: 2026-07-20
fix_summary:
- Removed Outfit lock white hoodie from `cover_quad_prompt.py`; outfit follows scene_hint + blog-hero outfit_rule.
- Neutralized SEO/Wordstat/white-hoodie defaults in `quad_manifest.py` and `visual_manifest.py`.
- Cover skill documents no-hoodie rule.
files_changed:
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `scripts/excalibur_blog_quad_manifest.py`
- `scripts/excalibur_blog_visual_manifest.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
checks_run:
- `rg 'Outfit lock: thick heavyweight white hoodie' scripts` → absent
- py_compile cover/quad scripts
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- Hardcode removed.


## INC-20260720-1324-schema-secret-scan-and-missing-helper
status: fixed
run_date: 2026-07-20
role: excalibur-blog-schema
topic_id: AS10
severity: medium
category: script
fixed_at: 2026-07-20
fix_summary:
- Added `scripts/excalibur_blog_schema_write.py` (BlogPosting+FAQPage+HowTo mode B, commit-safe redaction).
- Publish `load_article` reinjects CTA/site URLs into HTML + schema.jsonld.
- Schema/publish skills document helper + reinject contract.
files_changed:
- `scripts/excalibur_blog_schema_write.py`
- `scripts/excalibur_blog_cta_urls.py`
- `scripts/excalibur_blog_wp_publish.py`
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
checks_run:
- `python3 scripts/excalibur_blog_schema_write.py --article-dir ...AS10... --dry-run` → graph with FAQ+HowTo, `[REDACTED]/` paths
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- Helper restored; publish reinject wired.


## INC-20260720-1320-geoqa-utility-pain-markers-missing
status: fixed
run_date: 2026-07-20
role: excalibur-blog-geo-qa
topic_id: AS10
severity: high
category: script
fixed_at: 2026-07-20
fix_summary:
- Kept `pain_markers_ru` / `outcome_markers_ru` in `memory/brief/editorial-policy.json`.
- Shared module `excalibur_blog_voice_markers.py` + `resolve_marker_lists` used by utility_gate and human_voice_gate.
files_changed:
- `scripts/excalibur_blog_voice_markers.py`
- `scripts/excalibur_blog_utility_gate.py`
- `scripts/excalibur_blog_human_voice_gate.py`
- `memory/brief/editorial-policy.json` (markers retained)
checks_run:
- utility gate AS10 → PASS
- markers resolve fallback smoke
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- Shared markers + policy lists durable.


## INC-20260720-1321-geoqa-cta-reinject-and-gov-link
status: fixed
run_date: 2026-07-20
role: excalibur-blog-geo-qa
topic_id: AS10
severity: medium
category: env
fixed_at: 2026-07-20
fix_summary:
- Added `scripts/excalibur_blog_cta_urls.py` (--redact/--reinject) with typed placeholders.
- Documented QA reinject + gov.ru soft-fail / plaintext-without-href in geo-qa + pitfalls.
- `link_verify.py` already soft-fails `*.gov.ru` connection-reset (retained).
files_changed:
- `scripts/excalibur_blog_cta_urls.py`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_cta_urls.py --help`
- link_verify soft-fail hosts include gov.ru (rg)
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- CTA contract + gov soft-fail docs.


## INC-20260720-1305-scout-as-topic-id-regex
status: fixed
run_date: 2026-07-20
role: excalibur-blog-scout
topic_id: AS10
severity: high
category: script
fixed_at: 2026-07-20
fix_summary:
- Unified `(?:AS|B)\d+` + dash variants `—/–/-` in scout_helper, today.py, utility_gate topic parser.
- `--suggest-next` continues dominant prefix (AS11 after AS10 pool).
files_changed:
- `scripts/excalibur_blog_scout_helper.py`
- `scripts/excalibur_blog_today.py`
- `scripts/excalibur_blog_utility_gate.py`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `scout_helper --suggest-next` → AS11, pool=10
- `today.py` → EXCALIBUR_SUGGESTED_TOPIC_ID=AS01 (next unused P0)
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- AS* topic IDs recognized.


## INC-20260720-1312-research-gate-output-path
status: fixed
run_date: 2026-07-20
role: excalibur-blog-research
topic_id: AS10
severity: low
category: script
fixed_at: 2026-07-20
fix_summary:
- `-o` bare filename → article_dir; multi-part/absolute → as-is (no nesting).
- Removed false technical_topic from notes/github_evidence; AS* never requires GitHub.
- Research skill documents `-o research-notes-gate.json`.
files_changed:
- `scripts/excalibur_blog_research_notes_gate.py`
- `skills/excalibur-research/SKILL.md`
- `.cursor/skills/excalibur-research/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- research gate AS10 → PASS, technical_topic=False
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- Output path + AS github false-positive fixed.


## INC-20260720-1315-writer-cta-url-secret-scan
status: fixed
run_date: 2026-07-20
role: excalibur-blog-writer
topic_id: AS10
severity: medium
category: env
fixed_at: 2026-07-20
fix_summary:
- Writing contract + writer/publish skills: never commit live CTA/site URLs; use `[REDACTED]` / typed placeholders; reinject via cta_urls / wp_publish.
files_changed:
- `shared/excalibur-article-writing-contract.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_cta_urls.py`
- `scripts/excalibur_blog_wp_publish.py`
checks_run:
- docs contain excalibur_blog_cta_urls.py
- wp_publish load_article reinject present (rg)
commit: 58846fed40661af307e001f1cfea0af31a465af4

### Fixer resolution
- Writer/publish CTA secret-scan contract durable.


(Previous queue content was not readable in this workspace snapshot; prior fixed incidents may live only in git history on other branches.)
