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
4. **Cloud secret scanner:** site NAP URLs (`PUBLIC_SITE_URL`, `TELEGRAM_URL`, `CATALOG_URL`, `MAX_URL`) в `@id` / `sameAs` / `publisher.url` — ожидаемы. Перед commit прогони:

```bash
python3 scripts/excalibur_blog_write_schema.py --annotate \
  memory/blog/articles/<topic_id>-<slug>/schema.jsonld
```

Хелпер идемпотентно добавляет на ту же строку `"x-excalibur-allowlist": "pragma: allowlist secret"`.
Проверка: `python3 scripts/excalibur_blog_write_schema.py --annotate <path> --check`.

5. Перед любым `git commit` в Cloud:

```bash
source scripts/excalibur_blog_sanitize_secret_names.sh
```

Это отфильтровывает не-идентификаторы/URL из `CLOUD_AGENT_INJECTED_SECRET_NAMES` (иначе pre-commit падает на `${!SECRET_NAME}`).

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
