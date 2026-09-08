# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

---

## Ниша (обязательно)

Читай `memory/brief/site-brief.md` **до** поиска трендов.

Текущий канон: **Авто-Сейлс** — авто под заказ из Японии/Кореи/Китая, растаможка, СВХ Владивосток, доставка, утильсбор/пошлины, проверка лотов (Encar, аукционы, VIN).

Серия ID: **`AS##`**. Helper `excalibur_blog_scout_helper.py` / `excalibur_blog_today.py` парсят `(?:AS|B)\d+`; при живом AS-пуле `--suggest-next` должен вернуть следующий `AS##`, не `B01`.

**Запрещено** скаутить legacy AI/Cursor/n8n/Make-темы, пока site-brief задаёт авто-вертикаль.

Перед новым Scout сверь `shared/published-articles.md` с живыми WP-постами (site-relative `/YYYY/MM/DD/slug/`), чтобы не предложить уже опубликованный кластер.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next AS## ID)
              ↓
WebSearch (тренды Авто-Сейлс 2026)
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
* Считай список опубликованных статей из `shared/published-articles.md` и пул тем из `memory/topics/blog-topics.md`.
* Вызови helper-скрипт:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Запомни следующий `topic_id` (например, `AS17`) и список невыполненных тем.

### Шаг 2 — Поиск горячих трендов (WebSearch)
Сделай 2-3 поисковых запроса через `WebSearch` по нише Авто-Сейлс:
* Примеры: *«утильсбор 2026 как проверить мощность»*, *«encar проверка авто до покупки»*, *«растаможка авто Владивосток чек-лист»*, *«доставка авто из Владивостока 2026»*.
* Найди практические боли покупателя до депозита/оплаты, по которым не хватает utility-гайдов.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Для 2-3 отобранных вариантов тем вызови `wordstat_get_top_requests` сервера `user-mcp-kv`.
* **Cluster-first:** широкий parent (`утильсбор`, `encar`, `растаможка`) → узкий how-to.
* Если узкий запрос возвращает только `totalCount` — это low-result signal, не fatal; бери хвост из широкого кластера.
* Фильтр: микро-спрос без смежных тем — отложи.

### Шаг 4 — Тест на каннибализацию ключевых слов
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Если `OVERLAP DETECTED` — измени формулировку или выбери другую тему.

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

Допиши (append) карточку в конец `memory/topics/blog-topics.md` с id `AS##`.

---

## Блокеры скаута
* Создание темы с `article_mode: A` (новости, разборы) — разрешен только режим **B**.
* Игнорирование проверки на каннибализацию ключей.
* Выдумывание цифр спроса без вызова Wordstat API.
* Уход в чужую нишу (AI/Cursor/n8n), пока site-brief = Авто-Сейлс.
