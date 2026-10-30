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

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).

## Cloud secret-scan / commit

Публичные marketing/site URL (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`) в `schema.jsonld` часто режет Cloud secret-scan.

- На строках с URL добавляй EOL JSONC-комментарий: `// pragma: allowlist secret`.
- `excalibur_blog_wp_publish.py` **снимает** эти комментарии перед записью WP meta (валидный JSON-LD).
- Перед commit: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit …` (фильтрует non-identifier имена в `CLOUD_AGENT_*_SECRET_NAMES`).
