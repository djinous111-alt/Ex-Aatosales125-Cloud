---
name: excalibur-wp-publish
description: Alias для publish-excalibur-blog — публикация статьи в WordPress.
---

# Excalibur BLOG — WP Publish (alias)

Канонический skill субагента Publish: **`skills/publish-excalibur-blog/SKILL.md`**

Используй его для всех шагов publish (preflight, dry-run, publish, fallback, ledger, handoff).

Контракт: `shared/excalibur-wp-publish-contract.md`


## CTA / schema placeholders

- In git, article CTA stays as `[CATALOG_URL]` / `[TELEGRAM_URL]`; schema host may be `[REDACTED]`.
- `excalibur_blog_wp_publish.py` expands these **in memory** from env for the WP payload and does **not** write expanded URLs back to article files.
- Dry-run prints `cta_expanded` keys.

## SSH bootstrap cleanup

- After HTTP trigger, `delete_bootstrap_ssh` retries up to 3 times on banner/EOF errors.
- If cleanup still fails, manually SFTP-remove `excalibur-blog-publish-once.php` and record an incident.

## Pre-commit

```bash
source scripts/sanitize_cloud_secret_names.sh
```

`paramiko` is required (`requirements.txt` + `.cursor/cloud-agent-install.sh`).
