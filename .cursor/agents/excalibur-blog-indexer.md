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
2. Для commit-safe llms (рекомендуется в Cloud):
   `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --out-dir memory/blog --commit-safe`
   (CLI: `--blog-dir` / `--out-dir` / `--site-base`; флага `--blog-path` нет. Не коммить live `PUBLIC_SITE_URL` в llms*.txt.)
3. `promotion-checklist.md` из template.
4. Handoff `=== EXCALIBUR BLOG INDEXER ===`.
5. Перед git commit: `source scripts/excalibur_blog_filter_injected_secret_names.sh`.

## Не твоя зона

- publish, cover, schema (уже готовы), рерайт статьи.

## Skill

`skills/indexer-excalibur-blog/SKILL.md`