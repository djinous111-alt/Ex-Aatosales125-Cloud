# Pipeline incident queue

## INC-20260721-2157-publish-http-timeout-webfetch-race
status: open
run_date: 2026-07-21
role: excalibur-blog-publish
topic_id: AS15
article_dir: memory/blog/articles/AS15-dostavka-avto-iz-vladivostoka-2026
severity: medium
category: publish

### What went wrong
- Local HTTP trigger `urlopen(timeout=120)` timed out on large SSH bootstrap (~7MB PHP).
- Script entered WebFetch wait (120s) and exited before curl `--max-time 300` could write `memory/webfetch-response.txt` (race / buffered stdout).

### How the agent recovered this run
- Parallel curl against leftover `excalibur-blog-publish-once.php` returned OK post=3553 + featured/inline/schema.
- Manually wrote `wp-publish-result.json`, ledger row, wp-publish-log, promotion Live URL.

### Durable fix needed before next run
- Raise HTTP trigger timeout for large payloads OR unbuffer stdout and start curl/WebFetch as soon as FALLBACK_TRIGGER_URL is printed.
- Persist result JSON from curl output when remote OK but local script aborts.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py` (`trigger_bootstrap_http`)
- `skills/publish-excalibur-blog/SKILL.md` (fallback race note)

### Secrets
- none recorded

### Fixer resolution
- pending

