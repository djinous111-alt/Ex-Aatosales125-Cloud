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

## URL / commit

- В `schema.jsonld` нужны **live** own-site/CTA URL (валидный JSON-LD для publish). HTML pragma (`<!-- pragma: allowlist secret -->`) в JSON-LD **запрещён**.
- После registry sameAs URL check коммить через:
  `eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"` или `bash scripts/excalibur_git.sh commit ...`.
- Если secret-names hook всё ещё broken — `--no-verify` допустим только для staged `schema.jsonld` без секретов в других файлах.
