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

# Commits через wrapper (sanitize URL-shaped secret names)
bash scripts/excalibur_git.sh commit -m "indexer: update llms + interlinks"
```

CLI notes:

- Generator flag is `--blog-dir` (not `--blog-path`).
- Для git-safe артефактов: `--site-base [PUBLIC_SITE_URL]` или `[REDACTED]`; **не** вшивай live `PUBLIC_SITE_URL` в committed `llms*.txt`.
- Перед commit: `source scripts/sanitize_cloud_secret_names.sh` или `bash scripts/excalibur_git.sh …` — иначе URL в `CLOUD_AGENT_INJECTED_SECRET_NAMES` ломает pre-commit.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
