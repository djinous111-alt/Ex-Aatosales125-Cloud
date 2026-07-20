---
name: schema-excalibur-blog
description: Excalibur BLOG Schema — BlogPosting + FAQPage JSON-LD, автор из registry.
---

# Excalibur BLOG — Schema

## Вход

- `article.html`, `article.meta.json`, `research-notes.md` / `research-context.json`
- `shared/authors-registry.json`
- `memory/brief/site-brief.md` (site_url) или env `PUBLIC_SITE_URL`

## Задача

1. Собрать `schema.jsonld`: BlogPosting + FAQPage (+ HowTo для режима B).
2. `datePublished` из `research-context.json` (today).
3. Автор строго из `authors-registry.json` по `author_id`.

## Durable helper (обязательно)

Не изобретай one-shot decode+write. Используй:

```bash
python3 scripts/excalibur_blog_schema_write.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Опции:

- `--site-base <url>` — override, если нужно;
- `--dry-run` — посчитать FAQ/HowTo без записи.

Скрипт:

- декодирует Cloud Secret URL с `\uXXXX` через `unicode_escape`;
- читает FAQ из HTML и author из registry;
- пишет `schema.jsonld` в article dir.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Fragment: `.cursor/excalibur-blog-fragments/schema.md`  
Incident queue: `memory/pipeline-fix-queue.md` (не `pipeline-incident-queue.md`).

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
