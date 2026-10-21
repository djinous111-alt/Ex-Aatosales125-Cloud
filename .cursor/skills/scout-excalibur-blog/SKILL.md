# Excalibur BLOG — Scout (AVTO SALES)

## Когда запускаться

Расширение пула тем или перед циклом статьи, когда `blog-topics.md` исчерпан. Ниша только **Авто-Сейлс**: Япония / Корея / Китай, таможня, Владивосток — см. `memory/brief/site-brief.md`.

---

## Архитектура

```text
published-articles.md + wp-slug-denylist.json + blog-topics.md
              ↓
excalibur_blog_scout_helper.py --suggest-next
              ↓
WebSearch (auto-import / customs / Encar trends 2026)
              ↓
wordstat_get_top_requests (parent cluster → narrow how-to)
              ↓
--check-slug + --check-query
              ↓
Append Topic Card → blog-topics.md
```

---

## Алгоритм

### 1 — Audit + ID
```bash
python3 scripts/excalibur_blog_today.py
python3 scripts/excalibur_blog_scout_helper.py --suggest-next
```
Запомни next `topic_id`, recent WP slugs и `do_not_rewrite_post_ids`.

### 1b — Denylist (обязательно)
Канон: `shared/wp-slug-denylist.json` (Sorento/Alphard/Mohave/K3/Avante/Santa Fe/Tucson/utilzbor/rastamozhka/Seltos/Sportage/K5/AS08/AS09 + live).

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-slug "<candidate-slug>"
python3 scripts/excalibur_blog_scout_helper.py --check-query "<primary_query>"
```

Если denylist отсутствует — blocker + incident; не полагайся только на ledger.

### 2 — WebSearch (ниша AVTO SALES)
Примеры запросов: *«киа … из кореи комплектации 2026»*, *«как растаможить авто из японии чек-лист»*, *«утильсбор на авто 2026»*, *«encar carhistory до депозита»*, *«hyundai … из кореи ловушки»*.  
Не искать Cursor/n8n/Make/AI-агентов.

### 3 — Wordstat
Parent-кластер модели/страны → узкий how-to. Микроспрос без хвоста — отложить тему.

### 4 — Карточка (utility-only B)
```markdown
## {ID} — Короткое название темы

- **priority:** P0 | P1
- **slug:** {kebab-case-slug}
- **h1:** {Как / Чек-лист / …}
- **primary_query:** {из Wordstat}
- **secondary_queries:** {2-3}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:**
  1. {Действие до депозита/ставки}
  2. …
- **faq_hints:** {из хвоста Wordstat}
- **internal_links:** /
- **cover_scene_hint:** {Владивосток / Encar / аукцион / таможня — без Wordstat UI}
```

Append в конец `memory/topics/blog-topics.md`.

---

## Блокеры
* `article_mode: A`
* Нет `--check-slug` / denylist missing
* Каннибализация / clone живого WP slug
* Цифры спроса без Wordstat
* Тема вне AVTO SALES (AI/automation template)
