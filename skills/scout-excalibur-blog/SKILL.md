# Excalibur BLOG — Scout (Авто-Сейлс JP/KR/CN)

## Когда запускаться

По запросу пользователя для расширения пула тем или когда P0-темы в `blog-topics.md` исчерпаны / заняты на live WP.

---

## Архитектура работы

```text
published-articles.md + blog-topics.md + EXCALIBUR_RECENT_WP_POSTS (Audit)
              ↓
excalibur_blog_scout_helper.py --suggest-next (Get next ID + live slug sample)
              ↓
WebSearch (импорт авто JP/KR/CN, растаможка, проверка до депозита)
              ↓
wordstat_get_top_requests (Yandex Wordstat, cluster-first)
              ↓
excalibur_blog_scout_helper.py --check-query + wordpress_search_posts
              ↓
Append new Topic Card to blog-topics.md
```

Ниша: `memory/brief/site-brief.md`. **Запрещены** темы Cursor / ИИ / Make / n8n / «нейросети для бизнеса».

---

## Подробный алгоритм действий

### Шаг 1 — Анализ прошлого и получение ID
* Прочитай ledger, активные `memory/blog/articles/*`, пул тем.
* Запусти `python3 scripts/excalibur_blog_today.py` и сохрани `EXCALIBUR_RECENT_WP_POSTS`.
* Helper:
  ```bash
  python3 scripts/excalibur_blog_scout_helper.py --suggest-next
  ```
* Ledger может быть неполным: slug на live WP = тема занята, даже если ID свободен в пуле.

### Шаг 2 — WebSearch по нише Авто-Сейлс
Примеры запросов:
* «полная стоимость авто из Японии под ключ 2026»
* «Trust Encar vs Carhistory до депозита»
* «растаможка авто из Кореи Владивосток чеклист»
* «как проверить аукционный лист Япония»

### Шаг 3 — Wordstat
* Сначала широкий parent (`авто из японии`, `авто из кореи`), затем узкий how-to.
* `totalCount`-only на узком запросе = low-result signal, не fatal: бери semantic tail из parent.
* Микроспрос (<10) без хвоста — отложи тему.

### Шаг 4 — Каннибализация
```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<выбранный_запрос>"
```
Дополнительно: `wordpress_search_posts` по slug/фразам. Не дублируй live статьи.

### Шаг 5 — Карточка utility-only
```markdown
## {ID} — Короткое название темы

- **priority:** P0 | P1
- **slug:** {kebab-case-slug}
- **h1:** {Как / Чек-лист / Сравнение …}
- **primary_query:** {из Wordstat}
- **secondary_queries:** {2-3}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:**
  1. {Действие 1}
  2. {Действие 2}
  3. {Действие 3}
  4. {Чек-лист/Сравнение}
- **faq_hints:** {2-3}
- **internal_links:** /
- **cover_scene_hint:** {порт/аукцион/Encar/таможня — DIY collage, без Wordstat на картинке}
```

Append в конец `memory/topics/blog-topics.md`. Без статичных сумм пошлин в карточке.

---

## Блокеры скаута
* `article_mode: A` или новости без инструкции.
* Темы вне Авто-Сейлс (Cursor/ИИ/автоматизация агентов).
* Игнор live WP / каннибализации.
* Выдуманные цифры спроса без Wordstat.
