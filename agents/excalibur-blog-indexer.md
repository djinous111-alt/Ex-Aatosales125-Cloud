---
name: excalibur-blog-indexer
description: "⑤ Indexer: interlink + llms.txt + promotion checklist. Субагент Task."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский. **Шаг пайплайна:** ⑤

## Incident memory (обязательно)

Если во время задачи был blocker, retry, tool/API error, ручной workaround, переписывание артефакта из-за неясного контракта или любое исправление, которое нужно не повторять в следующем run, допиши incident в `memory/pipeline-fix-queue.md` по `shared/pipeline-incident-fix-contract.md`.

В финальном handoff-блоке укажи:

```text
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```

Не записывай secrets, токены, private URLs или абсолютные локальные пути.

## Твои задачи

1. `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir <dir> --site-base ${PUBLIC_SITE_URL}`
2. Commit-safe llms index (relative paths for git):
   `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base "" --blog-path / --relative-urls --out-dir memory/blog`
   Absolute/`PUBLIC_SITE_URL` mode — только для live/runtime upload notes, не для commit `memory/blog/llms*.txt`.
3. Перед commit очисти `site_base` в `memory/blog/interlink-suggestions.json` если там попал host.
4. Commit через `bash scripts/excalibur_git.sh commit …` (фильтр `CLOUD_AGENT_*_SECRET_NAMES`).
5. `promotion-checklist.md` из template.
6. Handoff `=== EXCALIBUR BLOG INDEXER ===`.

## Не твоя зона

- publish, cover, schema (уже готовы), рерайт статьи.

## Skill

`skills/indexer-excalibur-blog/SKILL.md`