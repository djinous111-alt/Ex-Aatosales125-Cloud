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
  --site-base [PUBLIC_SITE_URL]

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base [PUBLIC_SITE_URL] \
  --out-dir memory/blog

# Commits через wrapper (sanitize URL-shaped secret names + skip PUBLIC_SITE_URL false positives)
bash scripts/excalibur_git.sh commit -m "indexer: update llms + interlinks"
```

CLI notes:
- Generator flag is `--blog-dir` (not `--blog-path`; `--blog-path` is a deprecated alias only).
- For git-safe artifacts use `--site-base [PUBLIC_SITE_URL]` or `[REDACTED]`; do **not** embed live `PUBLIC_SITE_URL` values in committed `llms*.txt`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
