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

## Commit / Cloud secret scan

- BlogPosting/`sameAs` намеренно содержат публичные URL (`PUBLIC_SITE_URL`, catalog/Telegram/MAX).
- Перед `git commit`: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` — пропускает невалидные secret names и публичные marketing URL secrets.
- Не используй `--no-verify`. Если scan всё ещё блокирует — см. `shared/agent-pipeline-pitfalls.md` (Git / Cloud secret scan).
