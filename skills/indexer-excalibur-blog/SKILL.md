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
  --site-base https://avtosales125.ru

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base https://avtosales125.ru \
  --out-dir memory/blog
```

Нет флага `--blog-path` и нет `--redact-site-base` — только `--blog-dir` + `--out-dir` (+ `--site-base`).

Перед `git commit` (llms/checklist содержат абсолютные public URLs):

```bash
EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 source scripts/sanitize_cloud_secret_names.sh
```

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
