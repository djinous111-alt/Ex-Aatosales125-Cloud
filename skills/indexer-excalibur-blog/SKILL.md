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
  --site-base "${PUBLIC_SITE_URL}" \
  --redact-site-base

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "" \
  --out-dir memory/blog
```

- Interlinker: `--site-base` для live HTML href; `--redact-site-base` пишет `[REDACTED]` в `interlink-suggestions.json` (не коммить реальный site URL).
- llms generator: только `--blog-dir` (не `--blog-path`).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
