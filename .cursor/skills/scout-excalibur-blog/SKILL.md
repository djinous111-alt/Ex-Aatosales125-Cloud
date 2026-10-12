# Excalibur BLOG — Scout (Скаут-разведчик новых тем)

## Когда запускаться

Запускается по запросу пользователя для расширения пула тем или перед началом нового цикла написания статьи, когда старые темы в `blog-topics.md` исчерпаны.

## Ниша (обязательно)

Только **Авто-Сейлс** из `memory/brief/site-brief.md`:

- авто под заказ из Японии / Кореи / Китая;
- аукционы и аукционный лист, Encar / Trust / Carhistory;
- растаможка, утильсбор, СВХ Владивосток, доставка по РФ;
- доверие: VIN, ДТП, перекупы; сравнение стран под бюджет.

**Запрещено** подменять нишу на Cursor AI, n8n, Make.com, «ИИ-агенты / нейросети» — это stale examples из старых прогонов, не текущий сайт.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID)
              ↓
WebSearch (тренды ниши Авто-Сейлс, 2026)
              ↓
wordstat_get_top_requests (cluster-first → narrow how-to)
              ↓
excalibur_blog_scout_helper.py --check-query (local pool)
              ↓
excalibur_blog_scout_helper.py --check-live-wp (live WP REST)
              ↓
Append new Topic Card to blog-topics.md
```

---

## Подробный алгоритм действий

### Шаг 1 — Анализ прошлого и получение ID
* Считай `shared/published-articles.md` и `memory/topics/blog-topics.md`.
* Вызови:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
* Учти `EXCALIBUR_RECENT_WP_POSTS` из `python3 scripts/excalibur_blog_today.py` — live уже может закрывать «gap».

### Шаг 2 — Поиск горячих трендов (WebSearch)
2–3 запроса по нише, например:
* «как читать аукционный лист Япония 2026»
* «проверка авто Encar Trust Carhistory чек-лист»
* «растаможка авто Владивосток утильсбор 2026»
* «СВХ Владивосток что проверить до выдачи»

Найди практические боли, по которым мало качественных гайдов **на live-сайте**.

### Шаг 3 — Валидация спроса (Yandex Wordstat)
* Сначала широкий parent-кластер, потом узкий how-to.
* `totalCount`-only на узком = low-result signal; бери semantic tail из широкого ответа.
* Микро-спрос (&lt;10 показов) без хвоста — отложи тему.

### Шаг 4 — Каннибализация: local + live WP
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
python3 scripts/excalibur_blog_scout_helper.py --check-live-wp "<выбранный_запрос>"
```
* Local `OVERLAP DETECTED` → переформулируй или другая тема.
* Live near-duplicate (похожий title/slug на PUBLIC_SITE) → **не** пиши «на сайте нет гайда»; либо refresh существующего URL, либо другая тема.
* Не полагайся только на local `memory/blog/articles` и ledger — они могут отставать от WP.

### Шаг 5 — Сборка карточки темы (Utility-Only)
```markdown
## {ID} — Короткое название темы

- **priority:** P0 (если высокий спрос) | P1
- **slug:** {kebab-case-latin-slug}
- **h1:** {Заголовок с глаголом: Как / Чек-лист / Инструкция}
- **primary_query:** {главный запрос из Вордстата}
- **secondary_queries:** {2-3 сопутствующих}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:**
  1. {Действие 1}
  2. {Действие 2}
  3. {Действие 3}
  4. {Чек-лист/Сравнение}
- **faq_hints:** {2-3 вопроса из хвоста Вордстата}
- **internal_links:** {латинские dated paths с live WP, не кириллица}
- **cover_scene_hint:** {сцена для героя Авто-Сейлс + плашка}
```

`internal_links`: только ASCII/latin permalink paths из WP REST (пример: `/2026/10/04/prohodnye-avto-iz-yaponii-2026-chek-list-do-stavki/`). Кириллические path-догадки ломают link-verify и 404 на live.

Допиши (append) карточку в конец `memory/topics/blog-topics.md`.

---

## Блокеры скаута
* Создание темы с `article_mode: A` — разрешён только **B**.
* Игнорирование local или live cannibalization.
* Выдуманный спрос без Wordstat.
* Stale Cursor/AI/n8n/Make ниша вместо Авто-Сейлс.
