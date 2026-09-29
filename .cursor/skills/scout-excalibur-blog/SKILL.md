---
name: scout-excalibur-blog
description: Excalibur BLOG Scout — тренды автоимпорта, Wordstat, новые utility-темы без каннибализации.
---

# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

Ниша: читай `memory/brief/site-brief.md` (AVTO SALES — авто из Японии/Кореи/Китая). Не используй AI/Cursor/Make шаблон запросов.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md + live-wp-occupied-ids.json
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID)
              ↓
WebSearch (тренды автоимпорта 2026)
              ↓
wordstat_get_top_requests (Yandex Wordstat API demand verify)
              ↓
excalibur_blog_scout_helper.py --check-query (Cannibalization Guard)
              ↓
Append new Topic Card to blog-topics.md
```

---

## Подробный алгоритм действий

### Шаг 1 — Анализ прошлого и получение ID
* Считай `shared/published-articles.md`, пул `memory/topics/blog-topics.md` (AS* и B*), `memory/topics/live-wp-occupied-ids.json`.
* Вызови helper:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Helper пропускает ledger + article dirs + live-WP occupied. Запомни следующий свободный `topic_id` (например `B04`).

### Шаг 2 — Поиск трендов (WebSearch)
2–3 запроса по нише site-brief:
* «авто из японии под ключ 2026», «растаможка авто корея владивосток», «утильсбор 2026 легковые», «encar проверка до депозита», «свх владивосток сроки».
* Найди практические боли, по которым мало качественных гайдов.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
* **Cluster-first:** широкий parent → узкий how-to.
* Если узкий запрос вернул только `totalCount` — это low-result signal, не fatal; бери semantic tail из parent-кластера.
* Фильтр: микро-спрос (<10 показов) без смежных тем — отложи.

### Шаг 4 — Каннибализация
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
При `OVERLAP DETECTED` — переформулируй или смени тему.

### Шаг 5 — Карточка темы (Utility-Only)
```markdown
## {ID} — Короткое название темы

- **priority:** P0 | P1
- **slug:** {kebab-case-slug}
- **h1:** {Как / Чек-лист / …}
- **primary_query:** {из Wordstat}
- **secondary_queries:** {2-3}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:**
  1. {Действие 1}
  2. {Действие 2}
  3. {Действие 3}
  4. {Чек-лист/Сравнение}
- **faq_hints:** {2-3}
- **internal_links:** /
- **cover_scene_hint:** {порт / авто / герой Авто-Сейлс}
```

Append в конец `memory/topics/blog-topics.md`.

---

## Блокеры скаута

- Нет свободного topic_id после occupied/ledger → обнови `live-wp-occupied-ids.json` или уточни у оператора.
- Wordstat auth 401 → экспертная оценка + явный warning в карточке/отчёте.
