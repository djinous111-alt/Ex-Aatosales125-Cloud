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
  --site-base ""
```

Флаги: `--blog-dir` + `--out-dir` (не `--blog-path`). Для commit: `--site-base ""` (relative URLs).

Перед `git commit` при Cloud secret-scan `invalid variable name`:  
`source scripts/excalibur_blog_filter_secret_names.sh`

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
