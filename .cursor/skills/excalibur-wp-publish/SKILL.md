---
name: excalibur-wp-publish
description: Alias для publish-excalibur-blog — публикация статьи в WordPress.
---

# Excalibur BLOG — WP Publish (alias)

Канонический skill субагента Publish: **`skills/publish-excalibur-blog/SKILL.md`**

Используй его для всех шагов publish (preflight, dry-run, publish, fallback, ledger, handoff).

Контракт: `shared/excalibur-wp-publish-contract.md`

## CTA/schema hydrate + nginx 504

- Before SSH publish the script hydrates committed `[REDACTED]` placeholders from `PUBLIC_SITE_URL` / `TELEGRAM_URL`.
- If local HTTP trigger returns nginx **504**, script prints `FALLBACK_TRIGGER_URL` immediately — WebFetch/curl that URL into `memory/webfetch-response.txt` without waiting for another local attempt.
- On 504 the script also probes WP REST `posts?slug=` and reconstructs `wp-publish-result.json` + ledger when the live post is already OK (**no republish**).
- After success, slug is appended to `shared/wp-slug-denylist.json`.
- Before `git commit` of publish artifacts: `source scripts/excalibur_blog_filter_secret_names.sh`.
