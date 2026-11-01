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
  --site-base ""

# Commit-safe llms index (relative /blog/<slug>/ URLs):
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --blog-path memory/blog/articles \
  --relative-urls \
  --out-dir memory/blog

# Optional runtime/live index only (do NOT commit absolute host):
# python3 scripts/excalibur_blog_llms_generator.py \
#   --blog-dir memory/blog/articles \
#   --site-base "$PUBLIC_SITE_URL" \
#   --out-dir /tmp/llms-live
```

Notes:

- `--blog-path` is an alias for `--blog-dir` (doctor checks it).
- Runtime may use `--site-base $PUBLIC_SITE_URL`; **committed** `memory/blog/llms.txt` / `llms-full.txt` must keep relative `/blog/<slug>/` paths (`--relative-urls` or empty site-base; default when `--out-dir` is under `memory/`).
- Clear absolute `site_base` from `interlink-suggestions.json` before commit if the report is tracked.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
