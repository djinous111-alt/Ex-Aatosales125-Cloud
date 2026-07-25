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
  --site-base "${PUBLIC_SITE_URL}"

# Default --url-mode relative → git-safe /blog/<slug>/ (не коммить absolute PUBLIC_SITE_URL в llms*.txt)
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --url-mode relative \
  --out-dir memory/blog
```

Для локального preview с абсолютными URL (не для commit, если `PUBLIC_SITE_URL` в secret-scan):

```bash
python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --url-mode absolute \
  --site-base "${PUBLIC_SITE_URL}" \
  --out-dir memory/blog
```

**Нет флага `--blog-path`.** Только `--blog-dir`.

## Secret-scan

- `PUBLIC_SITE_URL` в Cloud Secrets часто ловится pre-commit secret-scan при absolute URLs в `llms.txt`.
- Канон для git: `--url-mode relative`.
- В `interlink-suggestions.json` можно оставить placeholder `${PUBLIC_SITE_URL}` вместо литерала origin.
- Если pre-commit падает с `invalid variable name` — в `CLOUD_AGENT_INJECTED_SECRET_NAMES` есть не-bash identifier (часто URL-as-name); это needs-human в Dashboard Secrets, не чинится `--no-verify` навсегда.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
