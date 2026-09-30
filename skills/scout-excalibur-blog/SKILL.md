# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

Канон ниши: `memory/brief/site-brief.md` (Авто-Сейлс / AVTO SALES). Не генерировать темы про Cursor/AI/n8n/Make/автопостинг.

---

## Архитектура работы

```text
site-brief.md + published-articles.md + blog-topics.md (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID)
              ↓
WebSearch (Cursor native: auto-import / customs / Asia cars 2026)
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
* Считай `memory/brief/site-brief.md`, `shared/published-articles.md`, live WP avoid-list из handoff/today и пул тем из `memory/topics/blog-topics.md`.
* Вызови helper-скрипт:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Запомни следующий `topic_id` (например, `B02`) и список невыполненных тем.

### Шаг 2 — Поиск горячих трендов в реальном времени (WebSearch)
Сделай 2-3 поисковых запроса через инструмент `WebSearch` Курсора по нише Авто-Сейлс:
* Примеры: *«растаможка авто из японии 2026 чек-лист»*, *«как проверить авто на encar trust»*, *«утильсбор ввезённый авто 2026»*, *«постановка на учет авто из китая гиbdd»*, *«свх владивосток документы после таможни»*, *«корея или япония авто под бюджет»*.
* Найди свежие практические боли частника, по которым не хватает качественных гайдов и которые не пересекаются с уже опубликованными WP-статьями.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Для 2-3 отобранных вариантов тем вызови `wordstat_get_top_requests` сервера `user-mcp-kv`.
* **Cluster-first:** сначала широкий parent (например, `растаможка авто из японии`, `постановка на учет авто`), затем узкий how-to.
* Если узкий запрос вернул только `totalCount` без top phrases — это low-result signal, не fatal; используй parent для semantic tail / FAQ / secondary.
* Выбери primary query с живым спросом и 3–5 связанных вопросов для FAQ.

### Шаг 4 — Тест на каннибализацию ключевых слов
Перед созданием темы запусти:
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Если `OVERLAP DETECTED` или пересечение с live WP avoid-list — измени формулировку или возьми другую тему.

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
- **cover_scene_hint:** {Краткое ТЗ для картинки — авто/порт/документы, без токсичных стикеров}
```

Допиши (append) карточку в конец `memory/topics/blog-topics.md`.

---

## Блокеры скаута
* Тема вне ниши Авто-Сейлс (Cursor/AI/n8n/Make/автопостинг/нейросети).
* Создание темы с `article_mode: A` (новости, разборы) — разрешен только режим **B**.
* Игнорирование проверки на каннибализацию ключей / live WP avoid-list.
* Выдумывание цифр спроса без вызова Wordstat API.
* Статичные цены/калькуляторы пошлин в outline.
