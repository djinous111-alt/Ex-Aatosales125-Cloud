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

CLI: `--blog-dir` (articles root) + `--out-dir`. Do **not** pass `--blog-path` (removed / never existed on generator).

## Commit note

If Cursor pre-commit secret-scrub dies with `invalid variable name` on public site URLs in `llms.txt`, retry with `git commit --no-verify` and log incident (do not strip live public URLs). Install patch: `scripts/excalibur_blog_patch_cursor_secret_scrub.sh` (also via cloud-agent-install).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
