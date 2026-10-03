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

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --relative-urls \
  --out-dir memory/blog
```

Relative `/blog/<slug>/` URLs are git-safe (Cursor secret-scan blocks absolute `PUBLIC_SITE_URL`).
Publish may regenerate absolute URLs on disk for deploy; do not rely on git HEAD for live llms if scanner blocked absolute forms.

## Pre-commit

```bash
source scripts/sanitize_cloud_secret_names.sh
```

Before `git commit` when Cloud injects non-identifier secret names.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (relative URLs for git)
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
