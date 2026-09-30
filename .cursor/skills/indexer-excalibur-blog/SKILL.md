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
  --site-base '[REDACTED]'

# CLI: --blog-dir only (no --blog-path). Commit-safe site-base for memory/blog artifacts:
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base '[REDACTED]' \
  --out-dir memory/blog
```

Live `PUBLIC_SITE_URL` — только на publish; не пиши боевой URL в commit-tracked `memory/blog/llms*.txt`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
