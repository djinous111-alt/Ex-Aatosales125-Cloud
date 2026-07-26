# Pipeline incident queue — Excalibur BLOG

Durable memory for fixer loop. Do not put secrets here.

## INC-20260726-1319-cover-kie-402-credits
status: open
run_date: 2026-07-26
role: excalibur-blog-cover
topic_id: AS10
article_dir: memory/blog/articles/AS10-postanovka-na-uchet-avto-posle-epts-2026
severity: blocker
category: api

### What went wrong
- Cover pipeline stopped: MCP gpt-image-2 failed (`NoneType.get`); preferred Kie createTask returned 402 Credits insufficient.
- No canvas URL; `cover/cover.png`, inline images, and `cover-registry.json` were not created. Images were not invented.

### How the agent recovered this run
- Explicit COVER BLOCKER; prepared `cover/quad-manifest.json`, `quad-mcp-batch.json`, `quad-mcp-prompt.txt` for retry after credits.

### Durable fix needed before next run
- Ensure Kie credits / billing before cover step; document Cloud fallback when MCP image tool returns None.
- Publish must remain blocked until real cover exists (no silent publish without featured image).

### Suggested files to inspect/change
- `skills/cover-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `shared/excalibur-wp-publish-contract.md` (cover precondition)

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260726-1323-publish-missing-cover
status: open
run_date: 2026-07-26
role: excalibur-blog-publish
topic_id: AS10
article_dir: memory/blog/articles/AS10-postanovka-na-uchet-avto-posle-epts-2026
severity: blocker
category: publish

### What went wrong
- Publish step ran after Indexer with `publish: yes`, but preflight found `cover/cover.png` and `cover-registry.json` missing (root cause: Kie 402 / cover blocker).
- Skill/contract require cover before WP publish. Cover was not invented. Step completed as explicit PUBLISH BLOCKER (not silent skip).

### How the agent recovered this run
- Re-ran link-verify → pass; dry-run payload OK; did **not** call live publish.
- Wrote `wp-publish-result.json` verdict=fail (blocker); updated handoff `=== EXCALIBUR BLOG PUBLISH ===`; left ledger `in_progress`.

### Durable fix needed before next run
- Director/gate: do not launch publish until cover PASS, or publish agent always hard-stops on missing cover (already done this run).
- Unblock: top up Kie → re-run cover → re-run publish.

### Suggested files to inspect/change
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-director.md` (gate cover before publish)
- `scripts/excalibur_blog_wp_publish.py` (optional: hard-fail when cover_b64 empty)

### Secrets
- none recorded

### Fixer resolution
- pending

## NOTE — queue file recovery
- Runtime ghost/missing `memory/pipeline-incident-queue.md` observed during publish (listdir/stat mismatch). File recreated with cover+publish incidents from handoff/automation memory. Other AS10 incidents referenced in handoff (scout/research/writer/geo-qa/schema/indexer) may need re-append by fixer from PR/fragments if still open.
