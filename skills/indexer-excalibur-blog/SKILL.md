---
name: indexer-excalibur-blog
description: Excalibur BLOG Indexer — interlink между статьями + llms.txt для AI crawlers.
---

# Excalibur BLOG — Indexer

После cover + schema.

## Shell

Для **commit-safe** артефактов всегда передавай пустой `--site-base` (relative `/blog/<slug>/`).
Абсолютный `$PUBLIC_SITE_URL` в `llms.txt` / `llms-full.txt` / `interlink-report.json` ломает pre-commit secret scanner.

```bash
python3 scripts/excalibur_blog_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base ""

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "" \
  --out-dir memory/blog
```

Флаг CLI — **`--blog-dir`**, не `--blog-path`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
