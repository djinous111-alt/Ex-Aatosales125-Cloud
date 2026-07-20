# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID: AS* or B*)
              ↓
WebSearch (Cursor native trend scouting for current year)
              ↓
wordstat_get_top_requests (Yandex Wordstat API demand verify)
              ↓
excalibur_blog_scout_helper.py --check-query (topics + live WP dump)
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
  Topic ID series: **`(?:AS|B)\d+`**. Для ниши Авто-Сейлс helper предлагает следующий свободный **`ASxx`** (не `B01`).
  Запомни `Next available topic ID` и список unwritten тем.

### Шаг 2 — Поиск горячих трендов в реальном времени (WebSearch)
Сделай 2-3 поисковых запроса через `WebSearch` по нише из `memory/brief/site-brief.md` (авто из JP/KR/CN, растаможка, СВХ, Encar, утильсбор и т.п.):
* Пример: *«таможенная пошлина на авто 2026»*, *«растаможка авто Владивосток сроки»*, *«Encar проверка авто»*.
* Найди практические боли, по которым ещё нет карточки в `blog-topics.md`.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Для 2-3 вариантов вызови `wordstat_get_top_requests` (MCP-KV).
* **Cluster-first:** сначала широкий parent-запрос, потом узкий how-to.
* Ответ только с `totalCount` (без списка фраз) = low-result signal, не fatal — расширь запрос и опирайся на parent-кластер.
* **Фильтр:** микро-спрос (<10) без смежного хвоста — отложи тему.

### Шаг 4 — Тест на каннибализацию
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Helper сравнивает с карточками `AS*`/`B*` **и** со slug dump `memory/blog/published-live-avtosales125.json` (если файл есть).

#### WordPress MCP vs live dump (обязательно)
* `wordpress_get_posts` на MCP-KV может быть привязан к **другому** сайту (чужие slug вроде СБКТС/ЭПТС-импорт).
* Перед использованием MCP WP для анти-каннибализации сверь `PUBLIC_SITE_URL` / site identity.
* Если MCP отдаёт чужой сайт → **не** используй его как live inventory; опирайся на:
  1. `memory/topics/blog-topics.md`
  2. `shared/published-articles.md`
  3. `memory/blog/published-live-avtosales125.json`
  4. `EXCALIBUR_RECENT_WP_POSTS` из `python3 scripts/excalibur_blog_today.py` (через `PUBLIC_SITE_URL`)
* Durable fix credentials — в Cursor Dashboard / MCP WordPress env (без записи значений в git).

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
- **cover_scene_hint:** {Краткое ТЗ для картинки}
```

Допиши (append) карточку в конец `memory/topics/blog-topics.md`.

### Pre-commit / Cloud Secrets (workaround)
Если `pre-commit.cursor` падает с `invalid variable name` на `CLOUD_AGENT_INJECTED_SECRET_NAMES`:
* Имена Cloud Secrets должны быть **валидными bash identifiers** (`[A-Za-z_][A-Za-z0-9_]*`) — без пробелов, дефисов, точек.
* Workaround на один commit: временно очистить `CLOUD_AGENT_INJECTED_SECRET_NAMES` в сессии **только** после ручной проверки staged diff на секреты; затем вернуть env.
* Durable: переименовать невалидные Secret names в Cursor Dashboard (needs-human).

---

## Блокеры скаута
* Создание темы с `article_mode: A` (новости, разборы) — разрешен только режим **B**.
* Игнорирование проверки на каннибализацию ключей.
* Выдумывание цифр спроса без вызова Wordstat API.
* Доверие к WP MCP без проверки, что это сайт Авто-Сейлс.
