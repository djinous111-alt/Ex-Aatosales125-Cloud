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

## Secret-scan / commit hygiene

- `excalibur_blog_llms_generator.py` автоматически добавляет `// pragma: allowlist secret` на строки с абсолютными `http(s)://` URL (когда `PUBLIC_SITE_URL` = Cloud Secret).
- В `promotion-checklist.md` на строках с live/public URL добавляй HTML-комментарий `<!-- // pragma: allowlist secret -->`.
- В `interlink-suggestions.json` (не деплоится) предпочитай redact `site_base` → `${PUBLIC_SITE_URL}` / `[REDACTED]`, а не live origin.
- Не коммить live `PUBLIC_SITE_URL` в `shared/published-articles.md` без redaction/`[REDACTED]`.
