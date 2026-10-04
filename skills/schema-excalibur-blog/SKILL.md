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

## Secret-scan / commit

`schema.jsonld` почти всегда содержит `PUBLIC_SITE_URL`, author `sameAs`, avatar URL — Cloud pre-commit secrets scanner блокирует commit без allowlist.

После сборки JSON-LD **до** `git commit`:

1. На каждой строке с site/CTA/avatar/sameAs URL добавь суффикс ` // pragma: allowlist secret` (JSONC-стиль, как в успешных B01 commits).
2. Валидация: `python3 -c "import json,re,pathlib; t=pathlib.Path('schema.jsonld').read_text(); print(json.loads(re.sub(r'// pragma: allowlist secret','',t)))"`.
3. Commit через `scripts/excalibur_git.sh commit …` (фильтр invalid `CLOUD_AGENT_*_SECRET_NAMES`).

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).
