---
name: schema-excalibur-blog
description: Excalibur BLOG Schema — BlogPosting + FAQPage JSON-LD, автор из registry.
---

# Excalibur BLOG — Schema

## Вход

- `article.html`, `article.meta.json`, `research-notes.md`
- `shared/authors-registry.json`
- `memory/brief/site-brief.md` (site_url)

## Задача

1. BlogPosting: headline, datePublished (today из research-context), author Person + sameAs.
2. FAQPage из FAQ секции статьи.
3. HowTo / Review — только если архетип требует.

## Commit hygiene (Cloud)

В committed `schema.jsonld` используй плейсхолдеры, не live URL:

- `[PUBLIC_SITE_URL]` / `[REDACTED]`
- `[CATALOG_URL]` / `[TELEGRAM_URL]` / `[MAX_URL]`

Перед `git commit`:

```bash
source scripts/sanitize_cloud_secret_names.sh
# или:
bash scripts/excalibur_git.sh commit -m "schema: ..."
# preflight:
python3 scripts/excalibur_blog_sanitize_secret_names.py --check
```

`CLOUD_AGENT_INJECTED_SECRET_NAMES` должен быть **comma-separated** bash-идентификаторами; URL-токен в списке → `invalid variable name` в pre-commit.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
