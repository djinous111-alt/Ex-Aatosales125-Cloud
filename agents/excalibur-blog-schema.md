---
name: excalibur-blog-schema
description: "④b Schema: BlogPosting + FAQPage JSON-LD. Субагент Task. Параллель с cover."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский. **Шаг пайплайна:** ④b (параллель с cover)

## Incident memory (обязательно)

Если во время задачи был blocker, retry, tool/API error, ручной workaround, переписывание артефакта из-за неясного контракта или любое исправление, которое нужно не повторять в следующем run, допиши incident в `memory/pipeline-fix-queue.md` по `shared/pipeline-incident-fix-contract.md`.

В fragment `.cursor/excalibur-blog-fragments/schema.md` укажи:

```text
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```

Не записывай secrets, токены, private URLs или абсолютные локальные пути.

## Твои задачи

1. Прочитать article.html, article.meta.json, research-notes, authors-registry.
2. Собрать `schema.jsonld` через durable helper:
   `python3 scripts/excalibur_blog_schema_write.py --article-dir <article_dir>`
   (декод PUBLIC_SITE_URL / unicode_escape, FAQ, author registry, HowTo для mode B).
3. datePublished из research-context (today) — helper берёт сам.
4. Fragment `.cursor/excalibur-blog-fragments/schema.md`:

```text
=== EXCALIBUR BLOG SCHEMA ===
topic_id:
verdict: PASS | BLOCKER
```

Incident memory: только `memory/pipeline-fix-queue.md`.
## Не твоя зона

- cover MCP, правка longread, publish.

## Skill

`skills/schema-excalibur-blog/SKILL.md`

## Выход

`schema.jsonld`
