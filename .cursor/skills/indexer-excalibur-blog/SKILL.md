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
  --site-base "$PUBLIC_SITE_URL"

# Commit-safe llms (secret-scan): do NOT pass live PUBLIC_SITE_URL into git artifacts.
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --out-dir memory/blog \
  --commit-safe

# Optional live regenerate for deploy only (do not git-add):
# python3 scripts/excalibur_blog_llms_generator.py \
#   --blog-dir memory/blog/articles \
#   --out-dir memory/blog \
#   --site-base "$PUBLIC_SITE_URL"

source scripts/excalibur_blog_filter_injected_secret_names.sh
```

CLI flags: `--blog-dir`, `--out-dir`, `--site-base`, `--commit-safe`. There is **no** `--blog-path`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (site-base `https://SITE.example` in git)
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
