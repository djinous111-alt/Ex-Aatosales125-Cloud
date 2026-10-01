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
  --site-base "[REDACTED]"

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base "[REDACTED]" \
  --out-dir memory/blog
```

Предпочтительно `--site-base "[REDACTED]"` для commit-safe артефактов. Если нужен live base URL, генераторы сами добавят `<!-- pragma: allowlist secret -->` / `// pragma: allowlist secret` на строки с site URL. CLI flag — `--blog-dir`, не `--blog-path`.

Перед commit: если `CLOUD_AGENT_INJECTED_SECRET_NAMES` содержит не-identifier (URL-shaped), отфильтруй имена до `^[A-Za-z_][A-Za-z0-9_]*$` (см. `CURSOR-CLOUD-RUNBOOK.md`).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
