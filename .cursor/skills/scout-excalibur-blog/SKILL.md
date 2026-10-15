# Excalibur BLOG — Scout (Скаут тем Авто-Сейлс)

## Когда запускаться

По запросу пользователя или перед новым циклом, когда пул P0 в `blog-topics.md` исчерпан.

Канон ниши: `memory/brief/site-brief.md` (Авто-Сейлс: Япония/Корея/Китай, СВХ, утиль, логистика Владивосток). **Не** предлагать Cursor/Make/n8n/AI-темы.

---

## Архитектура работы

```text
site-brief + published-articles.md + blog-topics.md (AS* и B*)
              ↓
excalibur_blog_scout_helper.py --suggest-next
              ↓
WebSearch (автологистика / таможня / проверка 2026)
              ↓
wordstat_get_top_requests (cluster-first; 1 retry on fetch failed)
              ↓
helper --check-query + Director denylist + ledger
              ↓
Append Topic Card → blog-topics.md
```

---

## Подробный алгоритм

### Шаг 1 — Аудит и ID

```bash
python3 scripts/excalibur_blog_scout_helper.py --suggest-next
```

Helper парсит `(AS|B)\d+` и учитывает slug из ledger. Запомни next `Bxx` и список AS*/B*.

### Шаг 2 — WebSearch (ниша Авто-Сейлс)

Примеры запросов:

- «доставка авто из Владивостока жд или автовоз 2026»
- «растаможка авто из Кореи пошагово»
- «СВХ Владивосток что проверить до оплаты»
- «утильсбор 2026 авто из Японии»
- «Trust Encar Carhistory до депозита»

### Шаг 3 — Wordstat

1. Сначала широкий parent (`доставка авто из владивостока`, `растаможка авто из кореи`).
2. Затем узкий how-to.
3. При `HTTP MCP ... fetch failed` — **ровно один retry** той же фразы; не burst параллельно без нужды.
4. `totalCount`-only / low-result на узком = signal → опирайся на parent-хвост; не fatal.
5. Не выдумывать показы.

### Шаг 4 — Каннибализация

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<primary_query>"
```

Дополнительно:

- live denylist Директора и `shared/published-articles.md` — **первичны**;
- WordPress MCP (`wordpress_get_posts` / `wordpress_search_posts`) использовать **только** если permalink host совпадает с хостом `PUBLIC_SITE_URL` / Авто-Сейлс. Чужой хост (например другой блог в тех же MCP credentials) — игнорировать для блокировки темы.

### Шаг 5 — Карточка (utility-only B)

```markdown
## {ID} — Короткое название темы

- **priority:** P0 | P1
- **slug:** {kebab-case-slug}
- **h1:** {Как / Чек-лист / Сравнение …}
- **primary_query:** {из Wordstat}
- **secondary_queries:** {2-3}
- **search_intent:** how_to | checklist | comparison | troubleshooting | workflow | parent_guide
- **article_mode:** B
- **h2_outline:** …
- **faq_hints:** …
- **internal_links:** /
- **cover_scene_hint:** …
```

Append в конец `memory/topics/blog-topics.md`.

### Commits (memory markdown)

Перед `git commit` schema/URL-тяжёлых файлов:

```bash
eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
```

Если pre-commit падает на `[REDACTED]: invalid variable name` на **non-secret** markdown (`blog-topics.md`, queue) — допустим `--no-verify` только для таких файлов; secrets/credentials не коммитить.

---

## Блокеры

* `article_mode: A`
* Игнор каннибализации / denylist
* Темы вне site-brief (AI/Cursor/Make) без явного override
* Выдуманные цифры Wordstat
