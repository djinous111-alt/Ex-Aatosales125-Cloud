# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

---

## Ниша (обязательно)

Канон: `memory/brief/site-brief.md` → `niche`.

- **Разрешено:** Авто-Сейлс — авто из Японии/Кореи/Китая, растаможка, СВХ Владивосток, проверка до депозита, ЭПТС/СБКТС, доставка по РФ.
- **Запрещено:** Cursor AI, n8n, Make.com, ИИ-агенты, RAG, DevOps, «автоматизация бизнеса» вне авто-ниши.

Если WebSearch/Wordstat уводит в AI-automation — смени запрос, не пиши карточку.

---

## Архитектура работы

```text
site-brief.md niche + published-articles.md + blog-topics.md (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID)
              ↓
WebSearch (Авто-Сейлс JP/KR/CN trends 2026)
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
* Считай список опубликованных статей из `shared/published-articles.md` и пул тем из `memory/topics/blog-topics.md`. Учти LIVE WP / `EXCALIBUR_RECENT_WP_POSTS`.
* Вызови helper-скрипт:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
  Helper сидирует next B## из **max(pool, ledger, article dirs, wp-publish-log, LIVE slug hints)** (`memory/topics/slug-topic-hints.json`). **Не** переиспользуй topic_id, если ID/slug ещё жив на LIVE, даже при пустом pool.
  Запомни следующий `topic_id` (например, `B02`) и список невыполненных тем.
* Git commit после правок тем: `bash scripts/excalibur_git.sh commit -m "…"` (sanitize `CLOUD_AGENT_*_SECRET_NAMES`; иначе pre-commit падает на `[REDACTED]`).
* После publish нового slug — допиши пару slug→topic_id в `memory/topics/slug-topic-hints.json`.

### Шаг 2 — Поиск горячих трендов в реальном времени (WebSearch)
Сделай 2-3 поисковых запроса через инструмент `WebSearch` Курсора по нише Авто-Сейлс:
* Примеры: *«растаможка авто из китая 2026 чек-лист»*, *«проверка encar carhistory до депозита»*, *«ЭПТС СБКТС Владивосток инструкция»*, *«утильсбор авто из японии корей 2026»*.
* Найди свежие практические боли новичков, по которым не хватает качественных гайдов.
* **Не** ищи Cursor/n8n/Make/ИИ-агентов.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Для 2-3 отобранных вариантов тем вызови инструмент `wordstat_get_top_requests` сервера `user-mcp-kv`.
* **Cluster-first:** сначала широкий parent (`растаможка авто`, `авто из китая`), затем узкий how-to.
* Если узкий запрос возвращает только `totalCount` — это low-result signal, не fatal; используй широкий кластер для semantic tail.
* **Фильтр:** Если тема имеет микро-спрос (меньше 10 показов в месяц) и нет смежных тем — отложи её и возьми другую.

### Шаг 4 — Тест на каннибализацию ключевых слов
Перед созданием темы запусти:
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
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
* Тема вне ниши Авто-Сейлс JP/KR/CN (Cursor/n8n/Make и т.п.).
* Создание темы с `article_mode: A` (новости, разборы) — разрешен только режим **B**.
* Игнорирование проверки на каннибализацию ключей.
* Выдумывание цифр спроса без вызова Wordstat API.
