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

CLI принимает только `--blog-dir` (корень articles), `--site-base`, `--out-dir`. Флага `--blog-path` нет — не передавай его.

Перед commit llms/URL-строк: `source scripts/sanitize_cloud_secret_names.sh`, на новых URL-строках — `<!-- pragma: allowlist secret -->`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
