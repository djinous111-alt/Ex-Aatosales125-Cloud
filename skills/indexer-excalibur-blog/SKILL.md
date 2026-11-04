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

# Commit-safe llms index: relative /blog/<slug>/ paths (no absolute host in git).
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "" \
  --blog-path / \
  --relative-urls \
  --out-dir memory/blog
```

Optional live/runtime absolute index (do **not** commit these hosts into `memory/blog/llms*.txt`):

```bash
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "${PUBLIC_SITE_URL}" \
  --blog-path / \
  --out-dir /tmp/excalibur-llms-live
```

Before `git commit`: clear `site_base` host from `memory/blog/interlink-suggestions.json` if present.
Commits: `bash scripts/excalibur_git.sh commit -m "…"`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt` with **relative** `/blog/<slug>/` URLs
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
