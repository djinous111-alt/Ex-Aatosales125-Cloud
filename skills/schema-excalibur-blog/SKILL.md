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

## Commit / secret scan

`schema.jsonld` обязан содержать live absolute public URLs (site + author `sameAs` из registry) для publish meta — **не** стрипай их под scanner и **не** используй `--no-verify`.

Перед `git commit` schema:

```bash
bash scripts/excalibur_git.sh add memory/blog/articles/<dir>/schema.jsonld
bash scripts/excalibur_git.sh commit -m "schema(...): ..."
```

Wrapper фильтрует невалидные bash-имена в `CLOUD_AGENT_*_SECRET_NAMES` и исключает public CTA/site names (`PUBLIC_SITE_URL`, `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`, …) из scan-списка. Корневой Dashboard rename non-bash secret names — needs-human (см. pitfalls).
