# Pipeline incident queue

Durable incident memory for Excalibur BLOG. Contract: `shared/pipeline-incident-fix-contract.md`.

## INC-20261021-2105-scout-niche-skill-drift
status: open
run_date: 2026-10-21
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: prompt

### What went wrong
- Scout skill drift toward Cursor/Make niche instead of AVTO SALES (recorded by Scout handoff).

### How the agent recovered this run
- Forced AVTO SALES niche per run contract; selected Mohave B01 card.

### Durable fix needed before next run
- Lock scout skill/prompts to AVTO SALES niche only.

### Suggested files to inspect/change
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-scout.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261021-2106-scout-missing-wp-denylist
status: open
run_date: 2026-10-21
role: excalibur-blog-scout
topic_id: B01
article_dir: n/a
severity: medium
category: docs

### What went wrong
- `shared/wp-slug-denylist.json` missing; Scout had to denylist manually from today.py + ledger.

### How the agent recovered this run
- Manual denylist from recent WP slugs and published-live.

### Durable fix needed before next run
- Restore or generate `shared/wp-slug-denylist.json` in repo/bootstrap.

### Suggested files to inspect/change
- `shared/wp-slug-denylist.json`
- `scripts/excalibur_blog_today.py`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261021-2130-research-wordstat-empty-primary
status: open
run_date: 2026-10-21
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-kia-mohave-iz-korei-komplektatsii-lovushki-2026
severity: low
category: api

### What went wrong
- MCP-KV `wordstat_get_top_requests` for phrase `как выбрать киа мохаве из кореи` returned unexpected empty object `{}` (not HTTP 401). Exact primary impressions unavailable.

### How the agent recovered this run
- Cluster-first: used parent `киа мохаве` (62207), `киа мохаве дизель` (5223), `киа мохаве из кореи` (267), `киа мохаве комплектации` (424); marked primary as n/a without inventing volumes.

### Durable fix needed before next run
- Document in research skill: empty `{}` / totalCount-only responses are non-fatal; require cluster-first fallback and explicit n/a row; do not treat as 401 auth warning.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-research/SKILL.md`
- `skills/excalibur-research/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20261021-2131-research-pain-map-gate-keywords
status: open
run_date: 2026-10-21
role: excalibur-blog-research
topic_id: B01
article_dir: memory/blog/articles/B01-kia-mohave-iz-korei-komplektatsii-lovushki-2026
severity: medium
category: qa

### What went wrong
- First `research-notes-gate` BLOCK: `pain_solution_map too thin: rows=1 < 3` because gate regex counts only rows containing `боль|pain|решение|solution|result|результат`. Header matched once; Russian data rows without those tokens were ignored.

### How the agent recovered this run
- Rewrote each pain_solution_map row with explicit `боль:` / `solution:` / `результат:` prefixes; gate PASS on retry.

### Durable fix needed before next run
- Either document required keywords in research agent/skill template, or relax gate to count non-header table rows under `## pain_solution_map`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_research_notes_gate.py`
- `.cursor/agents/excalibur-blog-research.md`
- `.cursor/skills/excalibur-research/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
- pending
