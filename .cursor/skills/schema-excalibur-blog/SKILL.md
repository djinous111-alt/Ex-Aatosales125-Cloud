---
name: schema-excalibur-blog
description: Excalibur BLOG Schema — BlogPosting + FAQPage JSON-LD, автор из registry.
---

# Excalibur BLOG — Schema

## Вход

- `article.html`, `article.meta.json`, `research-notes.md`
- `shared/authors-registry.json`
- `memory/brief/site-brief.md` (site_url)
- `shared/public-cta.json` (публичные sameAs / catalog fallback)

## Secret-scrub (критично)

- Read/Grep и печать env маскируют `site_url`, `sameAs`, `avatar_url`, `PUBLIC_SITE_URL` как литерал `[REDACTED]`.
- **Не собирай** `schema.jsonld` из scrubbed Read-output.
- Читай URL через python/shell (байты файла / hex / base64), либо из `shared/public-cta.json` + authors-registry через `json.load`.
- Self-check: в `schema.jsonld` литерал `[REDACTED]` = **0**. Иначе BLOCKER.

```bash
python3 -c "import json,pathlib; p=pathlib.Path('memory/blog/articles/<id>/schema.jsonld'); t=p.read_text(encoding='utf-8'); assert '[REDACTED]' not in t, 'scrub leak'; print('schema OK')"
```

## Задача

1. BlogPosting: headline, datePublished (today из research-context), author Person + sameAs.
2. FAQPage из FAQ секции статьи.
3. HowTo / Review — только если архетип требует.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
