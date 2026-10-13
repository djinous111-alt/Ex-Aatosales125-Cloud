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

CLI принимает `--blog-dir` / `--site-base` / `--out-dir`. Флаг `--blog-path` **не существует** — не передавать.
Перед commit: `bash scripts/excalibur_git.sh commit …` или
`export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(bash scripts/excalibur_blog_filter_secret_names.sh)"`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
