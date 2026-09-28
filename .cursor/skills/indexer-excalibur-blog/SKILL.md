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

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --url-mode relative \
  --out-dir memory/blog
```

CLI notes:

- llms generator accepts `--blog-dir`, `--out-dir`, `--url-mode {relative,absolute}` — **нет** `--blog-path`.
- Prefer `--url-mode relative` (default) → `/blog/<slug>/` so commits avoid Cloud secret-scanner hits on `PUBLIC_SITE_URL`.
- Absolute mode: `--url-mode absolute --site-base "$PUBLIC_SITE_URL"` (only for runtime deploy copies, not for git).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
