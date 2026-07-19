# Excalibur BLOG — Scout (новые темы Авто-Сейлс)

## Когда запускаться

Когда пул P0 в `blog-topics.md` исчерпан или пользователь просит расширить темы. Ниша: **Авто-Сейлс** (`memory/brief/site-brief.md`), id серии **`AS##`**.

---

## Архитектура работы

```text
published-articles.md + WP recent posts + blog-topics.md
              ↓
excalibur_blog_scout_helper.py --suggest-next  → AS##
              ↓
WebSearch (аукционы / Encar / растаможка / СВХ / утильсбор)
              ↓
wordstat_get_top_requests (cluster-first)
              ↓
excalibur_blog_scout_helper.py --check-query
              ↓
Append Topic Card (AS##) to blog-topics.md
```

---

## Подробный алгоритм

### Шаг 1 — Audit + next ID

```bash
python3 scripts/excalibur_blog_today.py
python3 scripts/excalibur_blog_scout_helper.py --suggest-next
```

Сверь `shared/published-articles.md` с `EXCALIBUR_RECENT_WP_POSTS`. Topic id — `AS##`, не legacy `B##`.

### Шаг 2 — Тренды (WebSearch)

Примеры запросов: «аукционный лист японского авто как читать 2026», «растаможка авто из Кореи 2026», «СВХ Владивосток сроки», «Trust Encar проверка до депозита», «утильсбор 2026 как считают».

Не искать темы про Cursor/AI/агентов/n8n.

### Шаг 3 — Wordstat

Сначала широкий parent (`аукционный лист`, `растаможка авто из японии`, `encar`), затем узкий how-to. `totalCount`-only на узком = low-result signal, не fatal.

### Шаг 4 — Каннибализация

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<запрос>"
```

### Шаг 5 — Карточка

```markdown
## AS11 — Короткое название

- **priority:** P0 | P1
- **slug:** {kebab-case}
- **h1:** {Как / Чек-лист / …}
- **primary_query:** …
- **secondary_queries:** …
- **search_intent:** how_to | checklist | comparison | troubleshooting
- **article_mode:** B
- **h2_outline:** …
- **faq_hints:** …
- **internal_links:** /
- **cover_scene_hint:** …
```

Append в конец `memory/topics/blog-topics.md`.

---

## Блокеры

* `article_mode: A`
* Игнор каннибализации / Wordstat
* Темы вне ниши Авто-Сейлс (AI/MCP/Cursor)
* Предложение уже опубликованного slug из WP/ledger
