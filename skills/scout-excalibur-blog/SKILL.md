---
name: scout-excalibur-blog
description: Excalibur BLOG Scout — новые topic cards, Wordstat, cannibalization guard.
---

# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md + live-wp-occupied-ids.json
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID; AS*|B*)
              ↓
WebSearch (Cursor native trend scouting for 2026)
              ↓
wordstat_get_top_requests (Yandex Wordstat API demand verify)
              ↓
excalibur_blog_scout_helper.py --check-query (Cannibalization Guard + occupied slugs)
              ↓
Append new Topic Card to blog-topics.md
```

---

## Подробный алгоритм действий

### Шаг 1 — Анализ прошлого и получение ID
* Считай `shared/published-articles.md`, `memory/topics/blog-topics.md` (**AS\d+ и B\d+**) и `memory/topics/live-wp-occupied-ids.json`.
* Live dedupe для Авто-Сейлс (обязательно, если helper JSON устарел):
  `PUBLIC_SITE_URL/wp-json/wp/v2/posts?per_page=30&_fields=id,slug,title,date`
* Вызови helper:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Helper учитывает `occupied_topic_ids` / `next_suggested_topic_id` и не предлагает уже занятые ID.

### Шаг 2 — Поиск трендов (WebSearch) в нише Авто-Сейлс
Запросы про импорт авто / растаможку / Encar / правый руль / утильсбор / Владивосток — не AI/n8n/Make.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Cluster-first: широкий parent → узкий how-to. `totalCount`-only на узкий запрос = low-result, не fatal.

### Шаг 4 — Тест на каннибализацию
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Не допускай пересечения с ledger, pool, live occupied slugs.

Перед любым `git commit` в Cloud:
```bash
source scripts/sanitize_cloud_secret_names.sh
```

### Шаг 5 — Карточка темы (Utility-Only)
Формат `## {ID} — …` с `AS` или `B` префиксом; `article_mode: B` only. Append в `memory/topics/blog-topics.md`. После publish/new WP post обновляй `live-wp-occupied-ids.json`.

---

## Блокеры скаута
* `article_mode: A`
* Игнорирование cannibalization / live WP occupied
* Цифры спроса без Wordstat
