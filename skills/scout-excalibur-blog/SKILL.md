# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID)
              ↓
WebSearch (Cursor native trend scouting for 2026)
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
* Считай список опубликованных статей из `shared/published-articles.md` и пул тем из `memory/topics/blog-topics.md` (**и `B\d+`, и `AS\d+`**).
* Вызови helper-скрипт:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Запомни следующий `topic_id` (например, `B03`) и список невыполненных тем.
* Helper считает next B ID как `max(B in topics+ledger+article dirs)+1` и учитывает AS-пул / live WP slug overlap при `PUBLIC_SITE_URL`.
* После AS→B миграции / ledger reset: **никогда** не начинай снова с B01, если live WP или ledger уже заняли B-серию. Если helper ошибочно предлагает занятый ID — возьми `max(B)+1` вручную и допиши incident.
* Предпочитай сначала закрыть unwritten P0 из AS-пула (`today.py` тоже предлагает AS*), затем новые B-карточки.

### Шаг 2 — Поиск горячих трендов в реальном времени (WebSearch)
Сделай 2-3 поисковых запроса через инструмент `WebSearch` Курсора по вашей нише:
* Поисковые запросы: *«новые ИИ инструменты автоматизации 2026»*, *«how to automate business Claude Cursor»*, *«лучшие сценарии n8n Make автоматизация»*, *«как настроить ИИ-агента инструкция»*.
* Найди свежие, практические боли пользователей, по которым не хватает качественных гайдов.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Для 2-3 отобранных вариантов тем вызови инструмент `wordstat_get_top_requests` сервера `user-mcp-kv`.
* **Цель:** Найти ключевой запрос (primary query) с живым спросом в Яндексе и выписать 3–5 связанных поисковых вопросов для FAQ и secondary queries.
* **Фильтр:** Если тема имеет микро-спрос (меньше 10 показов в месяц) и нет смежных тем — отложи её и возьми другую, более востребованную.

### Шаг 4 — Тест на каннибализацию ключевых слов
Перед созданием темы запусти:
```bash
python scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Если возвращается `OVERLAP DETECTED` — измени формулировку запроса или выбери другую тему. Не допускай семантического пересечения с опубликованными или запланированными статьями!

### Шаг 5 — Сборка карточки темы (Utility-Only)
Сформируй карточку темы по шаблону:
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
- **cover_scene_hint:** {Краткое ТЗ для картинки - обстановка, элементы DIY-коллажа}
```

Допиши (append) карточку в конец `memory/topics/blog-topics.md`.

---

## Блокеры скаута
* Создание темы с `article_mode: A` (новости, разборы) — разрешен только режим **B**.
* Игнорирование проверки на каннибализацию ключей.
* Выдумывание цифр спроса без вызова Wordstat API.
