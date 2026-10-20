---
name: scout-excalibur-blog
description: Excalibur BLOG Scout — тренды и Wordstat для ниши Авто-Сейлс, без каннибализации.
---

# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

**Ниша:** только Авто-Сейлс (`memory/brief/site-brief.md`). Не Cursor/AI/Make, пока Director не дал явный override.

---

## Архитектура работы

```text
site-brief.md + published-articles.md + published-live-*.json + blog-topics.md
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next B-id)
              ↓
WebSearch (автоиз Азии / Encar / растаможка / утильсбор 2026)
              ↓
wordstat_get_top_requests (parent cluster → narrow how-to)
              ↓
excalibur_blog_scout_helper.py --check-query (Bxx+ASxx+ledger+live)
              ↓
Append new Topic Card to blog-topics.md
```

---

## Подробный алгоритм действий

### Шаг 1 — Анализ прошлого и получение ID
* Считай ledger `shared/published-articles.md` (Bxx **и** ASxx), live snapshot `memory/blog/published-live-*.json`, пул `memory/topics/blog-topics.md`.
* Вызови helper:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Запомни следующий `topic_id` (B-серия; ASxx не увеличивают B-номер) и denylist/live slug.

### Шаг 2 — Поиск трендов (WebSearch)
2–3 запроса в нише Авто-Сейлс, например:
* «Hyundai Avante комплектации Encar 2026»
* «авто из Кореи ловушки до депозита»
* «утильсбор 2026 что проверить»

### Шаг 3 — Валидация спроса (Yandex Wordstat)
* Сначала **parent-кластер**, затем узкий how-to.
* Узкий ответ только `totalCount` / `{}` = low-result signal → бери semantic tail из parent.
* Микро-спрос без хвоста — отложи тему.

### Шаг 4 — Каннибализация
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Helper сверяет pool Bxx+ASxx, ledger и live WP JSON. При OVERLAP — другая формулировка или тема.

### Шаг 5 — Карточка (Utility-Only)
Шаблон как раньше (`priority`, `slug`, `h1`, `primary_query`, …, `article_mode: B`). Append в конец `memory/topics/blog-topics.md`.

---

## Блокеры скаута
* Создание темы с `article_mode: A`.
* Уход в Cursor/AI/Make без override Director.
* Игнорирование live JSON / ASxx при cannibal-check.
* Выдуманные цифры спроса без Wordstat.
