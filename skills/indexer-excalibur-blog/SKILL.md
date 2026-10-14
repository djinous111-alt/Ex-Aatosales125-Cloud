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

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "$PUBLIC_SITE_URL" \
  --out-dir memory/blog
```

CLI: only `--blog-dir` (no `--blog-path`). Generator auto-redacts live `PUBLIC_SITE_URL` to `[REDACTED]` in committed `llms*.txt`. Publish expands placeholders when deploying site-root files.

Commits: use `bash scripts/excalibur_git.sh commit …` (filters invalid `CLOUD_AGENT_*_SECRET_NAMES`).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (commit-safe `[REDACTED]` bases)
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
