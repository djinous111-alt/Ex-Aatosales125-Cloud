# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

## Ниша (AVTO SALES)

Блог — **Авто-Сейлс / AVTO SALES**: импорт авто из Японии/Кореи/Китая, СВХ Владивосток, растаможка, Encar, утильсбор, документы, аукционы.

**Не брать** темы про Cursor / n8n / Make / AI-агентов / MCP / автопостинг SaaS — это чужая ниша.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md (AS* + B*) + today.py WP recent
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID; parses AS\d+ and B\d+)
              ↓
WebSearch (Cursor native: auto-import / customs / SVH trends)
              ↓
wordstat_get_top_requests (cluster-first; sequential calls preferred)
              ↓
excalibur_blog_scout_helper.py --check-query + manual WP slug reconcile
              ↓
Append new Topic Card to blog-topics.md
```

---

## Подробный алгоритм действий

### Шаг 1 — Анализ прошлого и получение ID
* Считай список опубликованных статей из `shared/published-articles.md` и пул тем из `memory/topics/blog-topics.md` (**и `## AS01…`, и `## B01…`**).
* Запусти дату/WP live list:
  ```bash
  python3 scripts/excalibur_blog_today.py
  ```
  Обязательно сверь кандидатов с `EXCALIBUR_RECENT_WP_POSTS` — live WP slugs могут отсутствовать в ledger.
* Вызови helper-скрипт:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Helper парсит `## AS\\d+` и `## B\\d+`. Запомни следующий `topic_id` (обычно `Bxx`) и Unwritten pool.

### Шаг 2 — Поиск горячих трендов (WebSearch)
Сделай 2–3 запроса через `WebSearch` по нише AVTO SALES, например:
* «СВХ Владивосток стоимость хранения 2026»
* «растаможка авто из Кореи / Японии / Китая»
* «Encar проверка Carhistory до депозита»
* «утильсбор 2026 легковые»

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Для 2–3 кандидатов вызови `wordstat_get_top_requests` (MCP-KV).
* **Cluster-first:** сначала широкий parent-запрос, потом узкий how-to.
* **Последовательные вызовы** предпочтительнее параллельного batch: частичный fail batch (`server/toolName Required`) → retry одиночным вызовом.
* `totalCount`-only на узкий запрос = low-result signal, не fatal — опирайся на broad cluster.

### Шаг 4 — Тест на каннибализацию
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Плюс **ручная** сверка slug/query с `EXCALIBUR_RECENT_WP_POSTS` и карточками AS08/AS09/… даже если ledger пуст.

Если `OVERLAP DETECTED` или пересечение с live WP — измени угол или тему.

### Шаг 5 — Сборка карточки темы (Utility-Only)
```markdown
## {ID} — Короткое название темы

- **priority:** P0 (если высокий спрос) | P1
- **slug:** {kebab-case-slug}
- **h1:** {Заголовок с глаголом действия: Как / Чек-лист / Инструкция}
- **primary_query:** {главный запрос из Вордстата}
- **secondary_queries:** {2-3 сопутствующих запроса из Вордстата}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:**
  1. {Действие 1}
  2. {Действие 2}
  3. {Действие 3}
  4. {Чек-лист/Сравнение}
- **faq_hints:** {2-3 вопроса-подсказки из хвоста Вордстата}
- **internal_links:** /
- **cover_scene_hint:** {порт/таможня/Encar/салон + герой Авто-Сейлс; угол avto-sales125.ru}
```

Допиши (append) карточку в конец `memory/topics/blog-topics.md`.

---

## Блокеры скаута
* Создание темы с `article_mode: A` (новости, разборы) — разрешен только режим **B**.
* Игнорирование проверки на каннибализацию ключей / live WP posts.
* Выдумывание цифр спроса без вызова Wordstat API.
* Тема вне ниши AVTO SALES (Cursor/n8n/Make/AI-агенты).
