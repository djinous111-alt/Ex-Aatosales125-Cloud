# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

---

## Ниша (обязательно)

Читай `memory/brief/site-brief.md`. Канон: **Авто-Сейлс** — авто из Японии/Кореи/Китая, растаможка, СВХ Владивосток.  
Не генерируй темы про Cursor AI / Make.com / n8n / нейросети, даже если старый agent prompt это упоминал.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md + published-live-*.json (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID)
              ↓
WebSearch (тренд ниши Авто-Сейлс 2026)
              ↓
wordstat_get_top_requests (Yandex Wordstat API demand verify)
              ↓
excalibur_blog_scout_helper.py --check-query [--slug] (pool + live + denylist)
              ↓
Append new Topic Card to blog-topics.md
```

---

## Подробный алгоритм действий

### Шаг 1 — Анализ прошлого и получение ID

* Считай ledger, пул тем **и** live mirror `memory/blog/published-live-*.json`.
* Вызови:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```

### Шаг 2 — Поиск трендов (WebSearch)

Запросы в нише авто-импорта: растаможка Кореи, Encar, под ключ, СВХ, сравнение JP/KR/CN.

### Шаг 3 — Валидация спроса (Yandex Wordstat)

Cluster-first: широкий parent → узкий how-to. `totalCount`-only на узкий = soft-pass, не fatal.

### Шаг 4 — Тест на каннибализацию

```bash
python3 scripts/excalibur_blog_scout_helper.py \
  --check-query "<выбранный_запрос>" \
  --slug "<proposed-kebab-slug>"
```

Helper флагит OVERLAP по:

* B*-карточкам в `blog-topics.md`
* live WP slugs/titles из `published-live-*.json`
* optional `memory/blog/scout-denylist.json`

Если OVERLAP — другая формулировка/тема. Не дублируй live статьи (даже если их нет в B*-пуле).

### Шаг 5 — Карточка (Utility-Only)

Append карточку в `memory/topics/blog-topics.md` (режим B, how_to/checklist/comparison).

---

## Блокеры скаута

* Нет живого Wordstat-спроса и нет смежного кластера
* OVERLAP с live/denylist/pool
* Тема вне ниши Авто-Сейлс
