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
  --site-base ""

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "" \
  --out-dir memory/blog
```

**Важно:**

- CLI llms generator: `--blog-dir` + `--out-dir` (нет `--blog-path`).
- Для git-commit артефактов всегда `--site-base ""` → relative `/blog/<slug>/`.
- Не подставляй `${PUBLIC_SITE_URL}` в llms/interlink JSON: Cursor secret-scan блокирует commit.
- Absolute `site_base` только для live deploy вне git.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
