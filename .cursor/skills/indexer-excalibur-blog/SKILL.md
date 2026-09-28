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
  --site-base "${PUBLIC_SITE_URL:-}"

# Git-safe llms: relative /blog/<slug>/ (default). Do NOT embed raw PUBLIC_SITE_URL.
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --url-mode relative \
  --out-dir memory/blog
```

Перед commit артефактов:

```bash
source scripts/excalibur_blog_sanitize_secret_names.sh
```

Если когда-нибудь нужен absolute URL в llms (не для git): `--url-mode absolute --site-base "$PUBLIC_SITE_URL"` — generator сам добавит `<!-- pragma: allowlist secret -->`.  
`interlink-report.json` хранит `site_base` пустым при absolute env URL (secret-scanner safe).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
  - Live URL / site lines: relative path **или** same-line `<!-- pragma: allowlist secret -->`
