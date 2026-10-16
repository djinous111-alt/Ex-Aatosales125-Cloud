---
name: scout-excalibur-blog
description: Scout Авто-Сейлс — P0-темы Япония/Корея/Китай, Wordstat, без каннибализации.
---

# Excalibur BLOG — Scout (Авто-Сейлс)

## Когда запускаться

По запросу пользователя или Директора, когда пул тем в `blog-topics.md` исчерпан или нужен свежий P0.

## Канон ниши

Читай **`memory/brief/site-brief.md`** до генерации тем.

- Бренд: Авто-Сейлс / AVTO SALES
- Кластеры: Япония, Корея (Encar), Китай, Владивосток/СВХ, утильсбор/пошлины, доверие/VIN, сравнение стран
- **Запрещено** предлагать темы про Cursor, n8n, Make, ИИ-агентов, «контент-завод», RAG/LLM — это legacy другой ниши

## Архитектура

```text
published-articles.md + blog-topics.md + live WP denylist
              ↓
excalibur_blog_scout_helper.py --suggest-next
              ↓
WebSearch (тренды пригона/растаможки 2026)
              ↓
wordstat_get_top_requests (parent → how-to)
              ↓
excalibur_blog_scout_helper.py --check-query
              ↓
Append Topic Card → blog-topics.md
```

## Алгоритм

### 1 — Аудит и ID

```bash
python3 scripts/excalibur_blog_scout_helper.py --suggest-next
```

Учти AS* статьи и недавние WP post_id из задачи Директора (helper видит в основном B*).

### 2 — WebSearch

Примеры запросов:

- «можно ли привезти гибрид из японии 2026»
- «trust encar carhistory до депозита»
- «утильсбор 2026 изменения чеклист»
- «авто из китая растаможка сроки владивосток»

### 3 — Wordstat (cluster-first)

1. Широкий parent (`авто из японии`, `encar`, `растаможка авто`).
2. Узкий how-to.
3. Если узкий вернул только `totalCount` — low-result, не fatal; semantic tail из parent.
4. Если `wordstat_get_top_requests` отвечает **500 Internal** (или иной server error) после 2–3 попыток с паузой — **не blocker**. Fallback:
   - `wordstat_get_dynamics` с `PERIOD_MONTHLY`, region `225`, `fromDate` = первый день месяца, `toDate` = **последний** день месяца (иначе 400 InvalidArgument);
   - плюс Metrika/zen-topics / WebSearch как вторичный сигнал спроса.
5. В карточке темы зафиксируй источник: `top_requests` или `dynamics fallback`.

### 4 — Cannibalization

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<запрос>"
```

Плюс ручная сверка с `shared/published-articles.md` и live slug/denylist.

### 5 — Карточка (utility-only B)

```markdown
## {ID} — Короткое название

- **priority:** P0 | P1
- **slug:** {kebab-case}
- **h1:** Как / Чек-лист / Можно ли …
- **primary_query:** …
- **secondary_queries:** …
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:** …
- **faq_hints:** …
- **internal_links:** /
- **cover_scene_hint:** сцена с авто/портом/документами, герой Авто-Сейлс
```

Append в конец `memory/topics/blog-topics.md`.

## Блокеры

- `article_mode: A`
- темы вне Авто-Сейлс (AI/automation)
- игнор cannibalization / live WP denylist
- выдуманные цифры спроса без Wordstat
