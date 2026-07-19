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

CLI llms generator принимает только `--blog-dir` (не `--blog-path`).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`

## Commit note

Перед commit: `bash scripts/excalibur_blog_patch_cursor_precommit.sh`.
Если pre-commit.cursor всё ещё abort с `invalid variable name` — safe `--no-verify` только для indexer-артефактов без handoff/секретов + incident.
