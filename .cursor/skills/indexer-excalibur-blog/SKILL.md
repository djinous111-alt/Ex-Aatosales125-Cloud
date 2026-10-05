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
  --site-base ${PUBLIC_SITE_URL}

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base ${PUBLIC_SITE_URL} \
  --out-dir memory/blog
```

CLI принимает **`--blog-dir`**, не `--blog-path`. Флага `--blog-path` в argparse нет — не добавляй его.

Перед commit: на строках с live permalink в `llms.txt` / `llms-full.txt` / `promotion-checklist.md` допустим `// pragma: allowlist secret`. Для git commit предпочитай `bash scripts/excalibur_git.sh commit …`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
