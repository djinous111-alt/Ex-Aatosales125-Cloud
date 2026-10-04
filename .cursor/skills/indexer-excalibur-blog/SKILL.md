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

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`

## Redact-for-git / restore-for-publish

- В `llms.txt` / `llms-full.txt` / `interlink-suggestions.json` / `promotion-checklist.md` для git заменяй live site base на `[REDACTED]` (secret-scan ловит `PUBLIC_SITE_URL`).
- Перед publish/deploy восстанови runtime URL из env (или положись на expand в publish path).
- Перед commit: `source scripts/sanitize_cloud_secret_names.sh` или `bash scripts/excalibur_git.sh commit ...`.
