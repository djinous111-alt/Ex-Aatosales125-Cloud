---
name: indexer-excalibur-blog
description: Excalibur BLOG Indexer — interlink между статьями + llms.txt для AI crawlers.
---

# Excalibur BLOG — Indexer

После cover + schema.

## Shell

```bash
# Default --site-base empty → relative /blog/<slug>/ (secret-scan safe for git).
# Do NOT pass live $PUBLIC_SITE_URL into committed llms/interlink artifacts.
python3 scripts/excalibur_blog_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug>

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --out-dir memory/blog
```

CLI: `--blog-dir` (не `--blog-path`). Absolute site URLs — только при upload на сервер, не в git.

## Secret-scan

Если когда-либо нужны абсолютные URL в committed файле: HTML `<!-- pragma: allowlist secret -->` на строке;
в JSON — `"site_base": "${PUBLIC_SITE_URL}"` или `__excalibur_pragma_N` keys (как schema). Предпочтительнее относительные пути.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
