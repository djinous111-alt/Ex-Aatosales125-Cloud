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


## Cloud commit: public URLs in JSON-LD

`schema.jsonld` обязан содержать абсолютные `sameAs` / site URL из registry + `PUBLIC_SITE_URL`.
Cloud secret scanner может блокировать commit этих строк. На объектах/строках с URL добавь:

```json
"excaliburCommitPragma": "pragma: allowlist secret"
```

Перед commit при ошибке `invalid variable name` в pre-commit:

```bash
eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"
```

