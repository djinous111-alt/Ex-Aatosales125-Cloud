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
  --site-base '[PUBLIC_SITE_URL]'

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base '[PUBLIC_SITE_URL]' \
  --out-dir memory/blog
```

Notes:

- CLI flag is `--blog-dir` only (not `--blog-path`).
- Pass placeholder `[PUBLIC_SITE_URL]` (scripts also rewrite a live http(s) base) so `memory/blog/llms*.txt` / `interlink-suggestions.json` stay secret-scan safe.
- Before `git commit`, filter invalid names like literal `[REDACTED]` out of `CLOUD_AGENT_INJECTED_SECRET_NAMES` if the platform injects them (breaks `${!SECRET_NAME}`).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
