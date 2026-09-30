---
name: indexer-excalibur-blog
description: Excalibur BLOG Indexer — interlink между статьями + llms.txt для AI crawlers.
---

# Excalibur BLOG — Indexer

После cover + schema.

## Commit-safe site-base (обязательно)

В Cloud sandbox **не** передавай `${PUBLIC_SITE_URL}` в interlinker / llms generator: абсолютный host попадает в `memory/blog/llms*.txt` и `interlink-suggestions.json`, и pre-commit secret-scan блокирует commit.

- Для repo-артефактов всегда: `--site-base '[REDACTED]'`
- Live URL — только на publish / post-publish promotion
- `excalibur_blog_llms_generator.py` сам переписывает absolute own-site URL → `[REDACTED]` с WARN (safety net)

## Shell

```bash
python3 scripts/excalibur_blog_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base '[REDACTED]'

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base '[REDACTED]' \
  --out-dir memory/blog
```

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
