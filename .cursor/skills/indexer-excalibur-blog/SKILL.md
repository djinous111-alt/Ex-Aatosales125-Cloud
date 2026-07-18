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
  --blog-path / \
  --out-dir memory/blog
```


## Commit-safe site base

- По умолчанию оба скрипта пишут `site_base=[REDACTED]` (`--commit-safe`, default on): иначе Cursor secret-scan блокирует commit `llms*.txt` / `interlink-suggestions.json`, если в артефакт попал `PUBLIC_SITE_URL`.
- Не передавай live `PUBLIC_SITE_URL` в `--site-base` для файлов, которые уйдут в git.
- Для publish-deploy live-копии: `python3 scripts/excalibur_blog_llms_generator.py ... --no-commit-safe --site-base "$PUBLIC_SITE_URL"` **только в working tree**, без commit.
- Applied interlinks в HTML всегда относительные `/blog/.../`.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
