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
  --site-base [REDACTED] \
  --out-dir memory/blog
```

Только `--blog-dir` (не `--blog-path` — такого флага нет).

## Commit / secret-scan

- `PUBLIC_SITE_URL` часто в Cloud Secrets: llms generator сам дописывает `# pragma: allowlist secret` на URL-строки.
- В `promotion-checklist.md` на строках Live URL добавляй `<!-- pragma: allowlist secret -->`.
- Не коммить живые URL без pragma, если значение секрета совпадает с site base.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
