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
  --out-dir memory/blog \
  --commit-safe
```

CLI принимает только `--blog-dir` / `--out-dir` / `--site-base` / `--commit-safe`. Флага `--blog-path` **нет**.
Для commit в git всегда `--commit-safe` (site base → `[REDACTED]` / relative `/blog/...`), иначе secret-scan блокирует `PUBLIC_SITE_URL`.
Absolute URLs раскрывай только при upload на сервер.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
