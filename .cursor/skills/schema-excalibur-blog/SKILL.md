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


## Git / Cloud pre-commit

- Public site / Telegram / catalog URLs in `schema.jsonld` are **not** secrets; they belong in schema.
- If Cloud `pre-commit.cursor` / `commit-msg.cursor` aborts with `invalid variable name`, run:
  `bash scripts/excalibur_blog_patch_precommit_secret_scanner.sh`
  (also invoked from `.cursor/cloud-agent-install.sh`). The patch skips non-identifier
  entries in `CLOUD_AGENT_INJECTED_SECRET_NAMES` (e.g. raw URLs mistaken for env names).
- Do **not** `git reset HEAD~1` to probe the hook. Avoid `--no-verify` unless the hook
  is confirmed broken after the patch and the staged files contain no secret values.
