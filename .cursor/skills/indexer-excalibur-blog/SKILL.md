---
name: indexer-excalibur-blog
description: Excalibur BLOG Indexer — interlink между статьями + llms.txt для AI crawlers.
---

# Excalibur BLOG — Indexer

После cover + schema.

## Shell

```bash
python3 scripts/excalibur_blog_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base [REDACTED]

# Commit-safe llms (default site-base is [REDACTED]; use --redact-site-base if you passed a live URL)
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base [REDACTED] \
  --redact-site-base \
  --out-dir memory/blog
```

**CLI notes:**

- Flag is `--blog-dir`, **not** `--blog-path`.
- If you generated with live `--site-base "$PUBLIC_SITE_URL"` for local preview, re-run with `--redact-site-base` (or sed live base → `[REDACTED]`) before `git commit` — secret-scan treats `PUBLIC_SITE_URL` as secret.
- Same for `interlink-suggestions.json` `site_base` field if present.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (URLs with `[REDACTED]` in committed copies)
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
