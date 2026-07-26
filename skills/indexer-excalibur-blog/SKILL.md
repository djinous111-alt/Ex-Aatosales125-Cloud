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
  --site-base https://avtosales125.ru

# --blog-dir = filesystem path to article folders.
# --blog-path is ONLY an alias of --blog-dir (NOT site-brief blog_path "/", NOT URL prefix).
# Public site URL goes in --site-base only.
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "${PUBLIC_SITE_URL}" \
  --out-dir memory/blog
```

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
