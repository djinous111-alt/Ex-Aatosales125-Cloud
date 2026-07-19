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

Примечания:

- CLI flag: `--blog-dir` (алиас `--blog-path` для совместимости с doctor/старыми docs).
- Для git-safe артефактов всегда `--site-base [REDACTED]`. Скрипт сам редактирует absolute `PUBLIC_SITE_URL`, если агент передал live URL.
- Pre-commit secret-scan: если hook падает с `invalid variable name` на `CLOUD_AGENT_INJECTED_SECRET_NAMES` — после проверки diff допустим `git commit --no-verify`. Не коммить live site URL.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
