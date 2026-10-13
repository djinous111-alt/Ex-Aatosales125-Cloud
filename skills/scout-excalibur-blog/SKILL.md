---
name: scout-excalibur-blog
description: Excalibur BLOG Scout — темы Авто-Сейлс, Wordstat, AS*/B* без каннибализации.
---

# Excalibur BLOG — Scout (темы Авто-Сейлс)

## Когда запускаться

Когда today.py вернул `EXCALIBUR_TOPIC_SELECTION=needs_scout` или пользователь просит расширить пул тем.

Ниша всегда из `memory/brief/site-brief.md` (Авто-Сейлс). **Не** генерировать темы про AI/Cursor/Make.

---

## Архитектура работы

```text
site-brief.md + published-articles.md + blog-topics.md (AS* и B*)
              ↓
excalibur_blog_scout_helper.py --suggest-next
              ↓
Prefer unused P0 from pool (AS* or B*)
              ↓
WebSearch (авто-импорт / растаможка / СВХ / Encar 2026)
              ↓
wordstat_get_top_requests (cluster-first)
              ↓
excalibur_blog_scout_helper.py --check-query + live WP denylist
              ↓
Append Topic Card (Bxx) to blog-topics.md  OR  select existing P0
```

---

## Подробный алгоритм действий

### Шаг 1 — Анализ и ID
* Прочитай `shared/published-articles.md`, `memory/topics/blog-topics.md`, `EXCALIBUR_RECENT_WP_POSTS`.
* Вызови:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
* Helper учитывает **и AS*, и B***. Новые карточки — серия `Bxx`.

### Шаг 2 — Сначала незанятый P0 из пула
Если в `blog-topics.md` уже есть `AS*`/`B*` с `priority: P0` и статус не published/in_progress — **выбери его**, не плоди дубль. today.py тоже читает оба префикса.

### Шаг 3 — WebSearch (ниша авто)
Примеры запросов:
* «растаможка авто из Кореи 2026 чек-лист»
* «как проверить авто на Encar»
* «электромобиль из Китая документы»
* «СВХ Владивосток сроки»
* «утильсбор 2026 легковые»

### Шаг 4 — Wordstat (cluster-first)
1. Широкий parent (`авто из кореи`, `растаможка авто`, `электромобиль из китая`).
2. Узкий how-to.
3. `totalCount`-only на узком = low-result signal → бери semantic tail из широкого кластера.

### Шаг 5 — Каннибализация
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Плюс сверка со live WP titles/slugs. При OVERLAP — другая формулировка или другая тема.

### Шаг 6 — Карточка (если нужна новая)
```markdown
## {ID} — Короткое название темы

- **priority:** P0 | P1
- **slug:** {kebab-case-slug}
- **h1:** {Как / Чек-лист / Инструкция …}
- **primary_query:** {из Wordstat}
- **secondary_queries:** {2-3}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:**
  1. …
  2. …
- **faq_hints:** …
- **internal_links:** /
- **cover_scene_hint:** {авто / порт / документы / Владивосток — без AI-стилистики}
```

Append в конец `memory/topics/blog-topics.md`. Commits: `bash scripts/excalibur_git.sh …`.

---

## Блокеры скаута
* Темы про AI/Cursor/n8n/Make вместо Авто-Сейлс.
* `article_mode: A` (новости) — только **B**.
* Игнор каннибализации / live WP denylist.
* Цифры спроса без Wordstat (или без явного auth warning).
