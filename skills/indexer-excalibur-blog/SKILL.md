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

`--blog-path` — **алиас** `--blog-dir` (директория статей на диске), не URL-путь WordPress.
Никогда не передавай `--blog-path /` или `/blog`: это filesystem-root / URL path, не `memory/blog/articles`. Скрипт игнорирует такие значения с WARNING (если задан `--blog-dir`), но агент обязан передавать только `--blog-dir memory/blog/articles`.
Если нужен алиас явно: `--blog-path memory/blog/articles` (эквивалент `--blog-dir`).
Для commit-safe вывода при `PUBLIC_SITE_URL` в Cloud Secrets используй relative `/blog/{slug}/` или pragma allowlist — не коммить абсолютный public URL.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
