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
  --site-base "${PUBLIC_SITE_URL}"

# WP root permalinks (site-brief blog_path: /): empty site-base → relative /{slug}/
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "" \
  --blog-path / \
  --out-dir memory/blog
```

**Не** ставь live host в default `--site-base` скрипта (secret-scan). Перед commit: `bash scripts/excalibur_git.sh commit …` если pre-commit ругается на `invalid variable name`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
