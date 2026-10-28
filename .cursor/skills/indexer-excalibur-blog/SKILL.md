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
  --site-base "${PUBLIC_SITE_URL}"

# Commit-safe llms: relative /blog/<slug>/ (no absolute host → secret-scan OK).
# Flags are --blog-dir + --out-dir. There is NO --blog-path.
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --out-dir memory/blog \
  --site-base ""
```

Для live/publish-time копии с абсолютным base (не коммитить host, если он в secret-scan):

```bash
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --out-dir memory/blog \
  --site-base "${PUBLIC_SITE_URL}"
```

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
