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

Флаг `--blog-path` **не существует** у generator — только `--blog-dir` (локальные статьи) и `--out-dir`.
Если `PUBLIC_SITE_URL` в Cloud Secrets попадает в `llms.txt` / `promotion-checklist.md`, добавь `<!-- pragma: allowlist secret -->` на строки с URL перед commit. `schema.jsonld` нельзя комментировать через `//` — publish кладёт raw JSON в WP meta.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
