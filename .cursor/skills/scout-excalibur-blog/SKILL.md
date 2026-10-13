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
* Считай `shared/published-articles.md`, `memory/blog/articles/Bxx-*` и пул `memory/topics/blog-topics.md`.
* Ниша только из `memory/brief/site-brief.md` (Авто-Сейлс). Не предлагай Cursor/n8n/Make/нейросети.
* Вызови helper:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  # при необходимости: --min-id B03
  ```
  Helper пропускает занятые B-id из ledger + article dirs. Запомни `Next available topic ID`.

### Шаг 2 — Поиск горячих трендов (WebSearch)
2–3 запроса `WebSearch` по авто-нише:
* *«аукционный лист япония как читать 2026»*, *«encar проверка авто корея»*, *«растаможка авто владивосток утильсбор»*, *«авто из китая документы»*, *«корея vs япония авто под заказ»*.
* Ищи практические боли новичка импорта без готового гайда.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
Для 2-3 отобранных вариантов тем вызови инструмент `wordstat_get_top_requests` сервера `user-mcp-kv` (cluster-first: широкий parent → узкий how-to).
* **Цель:** Найти ключевой запрос (primary query) с живым спросом в Яндексе и выписать 3–5 связанных поисковых вопросов для FAQ и secondary queries.
* **Фильтр:** Если тема имеет микро-спрос (меньше 10 показов в месяц) и нет смежных тем — отложи её и возьми другую, более востребованную.
* **Retry:** при HTTP 500 / `code:13 Internal` — 2–4 retry с backoff и другой phrasing/device; не крутить бесконечно.
* **Fallback (не блокер P0):** если live Wordstat topRequests недоступен, но есть (a) live WP REST gap по уникальному токену, (b) parent-кластер из `memory/topics/zen-topics-from-metrika.json` / cached Wordstat, (c) WebSearch 2026 подтверждающий боль — зафиксируй `scout_signal: wordstat_unavailable_fallback` в карточке, live impressions = `n/a`, **не выдумывай** показы.

### Шаг 4 — Тест на каннибализацию (ledger + live WP + deny-list)
Перед созданием темы сверь primary_query/h1/slug с:
1. `shared/published-articles.md` + pool (делает helper);
2. live WP: `PUBLIC_SITE_URL` REST или `EXCALIBUR_RECENT_WP_POSTS` из `today.py` (helper подтягивает сам; `published-live-*.json` может быть устаревшим);
3. явный deny-list свежих WP slug’ов от Director.

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>" \
  --proposed-slug "<kebab-slug>" \
  --deny-slugs "slug-a,slug-b"
# или файл: --deny-slugs memory/blog/deny-slugs.txt
```

Если `OVERLAP DETECTED` / WP source=`unavailable` без env — не append карточку. Не полагайся только на ledger.

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
* Выдумывание цифр спроса без вызова Wordstat API (или без явного `scout_signal: wordstat_unavailable_fallback` + WP/WebSearch evidence).
* Темы вне ниши Авто-Сейлс (Cursor/n8n/Make/AI) без явного Director override.
