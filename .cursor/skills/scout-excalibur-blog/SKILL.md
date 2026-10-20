---
name: scout-excalibur-blog
description: Excalibur BLOG Scout — AVTO SALES темы, Wordstat, denylist WP slug.
---

# Excalibur BLOG — Scout (Авто-Сейлс)

## Когда запускаться

Когда пул `memory/topics/blog-topics.md` пуст/исчерпан или Директор просит новую P0-тему.

## Ниша (канон)

Только **AVTO SALES** по `memory/brief/site-brief.md`:

- Корея / Япония / Китай под заказ
- растаможка, утильсбор, СВХ Владивосток
- Encar / Trust Encar / аукцион / доверие до депозита

**Не ниша:** Cursor, Make, n8n, AI-агенты, автопостинг, «контент-завод» (legacy drift — игнорировать).

Аудитория: покупатель авто под заказ, beginner angle = первый результат до депозита.

---

## Архитектура

```text
published-articles.md + wp-slug-denylist.json + published-live + blog-topics.md
              ↓
excalibur_blog_today.py (EXCALIBUR_RECENT_WP_POSTS)
              ↓
excalibur_blog_scout_helper.py --suggest-next
              ↓
WebSearch (авто-ниша 2026)
              ↓
wordstat_get_top_requests (cluster-first)
              ↓
excalibur_blog_scout_helper.py --check-query  (+ denylist)
              ↓
Append Topic Card → blog-topics.md
```

---

## Алгоритм

### 1) Audit + ID

```bash
python3 scripts/excalibur_blog_today.py
python3 scripts/excalibur_blog_scout_helper.py --suggest-next
```

Обязательно проверь:

- `shared/wp-slug-denylist.json` существует и не пуст
- иначе **blocker**: собери slugs из `EXCALIBUR_RECENT_WP_POSTS` + `memory/blog/published-live-avtosales125.json` + notes, запиши JSON, только потом append

### 2) WebSearch (авто, не AI)

Примеры запросов: «Kia/Hyundai из Кореи комплектации 2026», «растаможка авто из Китая чек-лист», «утильсбор 2026 как считать», «Encar проверка до депозита».

### 3) Wordstat cluster-first

1. Широкий parent (модель/кластер)
2. Узкий how-to
3. `totalCount`-only на узком = low-result signal → опирайся на parent semantic tail

### 4) Cannibalization

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<primary_query>"
```

Helper сверяет pool тем **и** `shared/wp-slug-denylist.json`. CRITICAL overlap → другая тема.

### 5) Карточка (utility-only Mode B)

```markdown
## {ID} — Короткое название

- **priority:** P0 | P1
- **slug:** {kebab-case-slug}
- **h1:** {Как / Чек-лист / …}
- **primary_query:** {Wordstat}
- **secondary_queries:** {2-3}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:**
  1. {Действие}
  2. {Действие}
  3. {Действие}
  4. {Чек-лист/Сравнение}
- **faq_hints:** {2-3}
- **internal_links:** /
- **cover_scene_hint:** {авто-сцена, не SEO/Wordstat}
```

Append в конец `memory/topics/blog-topics.md`.

---

## Блокеры

- Mode A / новости без практики
- Тема вне AVTO SALES (AI/Make/Cursor drift)
- Нет `shared/wp-slug-denylist.json`
- Игнор denylist / recent WP republish
- Выдуманный Wordstat без MCP
