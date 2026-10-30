# Excalibur BLOG — Writer

## Вход

- `research-notes.md` с **utility_verdict: PASS**
- `shared/excalibur-article-writing-contract.md`
- `shared/editorial-utility-only.md`
- `memory/brief/site-brief.md`, `conversion-map.md`
- `memory/brief/editorial-policy.json` — до письма проверь `_markers_pinned`, `pain_markers_ru`, `outcome_markers_ru` и min counts; если списки стёрты template-reset’ом — восстанови из defaults utility-gate / pitfalls, иначе gate даст pain/outcome=0 BLOCK

## Задача

1. **Только режим B** — инструкция/гайд/чеклист/comparison. Режим A запрещён.
2. Outline H2 = подзадачи с **действием** (не «вообще про тему»).
3. **ПРОСТОЙ ЧЕЛОВЕЧЕСКИЙ ЯЗЫК (ГЛАВНОЕ ПРАВИЛО):** Пиши максимально понятно и доступно для простого человека (предпринимателя, новичка, не-программиста). Исключай сложный технический снобизм. Любой используемый термин (API, RAG, Self-hosted, Docker) **обязан** иметь моментальную расшифровку и объяснение «на пальцах» (на простых аналогиях).
4. **ОФОРМЛЕНИЕ ТЕКСТА (БЕЗ ДЛИННЫХ ТИРЕ И ЁЛОЧЕК):** Запрещено использовать длинные тире («—») и кавычки-ёлочки (««», «»»). Всегда используй среднее тире («–») или обычный дефис («-»), а вместо кавычек-ёлочек — стандартные прямые двойные кавычки («"`»).
5. Hook 350–500 символов: боль → ответ → **что сделает читатель**.
6.  Минимум **5** нумерованных шагов `<ol>` + workflow (`→`) или таблица.
7. Каждый H2: рекомендация «делать / не делать».
8. Body 8 500–9 500 знаков, FAQ 5–7 пар — **ответы-действия**, **один** блок `<h2>Частые вопросы</h2>` (без второго FAQ).
9. `article.meta.json`: `article_mode: B`, `char_count`, `meta_ab` с A/B/AEO оптимизацией:
   - `title_seo`: 35–75 симв, точный `primary_query` в начале + триггер.
   - `title_ctr`: 40–100 симв, кликабельный крючок, обязательно эмодзи (например 💻, 🚀) или знаки ?, !
   - `title_aeo`: 35–90 симв, сформулирован как вопрос ИИ-поисковику (начинается с "Как", "Что", "Почему" или содержит "?").
   - `description_seo`: 100–180 симв.
10. Подзаголовки H2 должны начинаться с **глаголов действия** (создайте, настройте, проверьте) или содержать **маркеры действия** (как, чеклист, сравнение, выбор, пошагово). Минимум 3 H2 должны быть активными.
11. **RSS И ДЗЕН-СОВМЕСТИМОСТЬ (КРИТИЧЕСКИ):** Тело статьи `article.html` должно быть чистым, семантическим HTML без JS-кнопок, инлайновых стилей `style="..."` или кастомных тегов. Инсайт-выжимку оборачивай в `<blockquote>` (Дзен нативно стилизует цитаты). Код/JSON — whitelist-safe (`<blockquote><p>…<br>…</p></blockquote>` / table / list); `<pre>`/`<code>` запрещены HTML-линтером.
12. **СТРУКТУРНЫЕ ЭЛЕМЕНТЫ (инсайт, EEAT — без оглавления):**
    - Сразу после Lead-абзаца вставляй `<blockquote>` с тематическим ярлыком (**не** `TL;DR`, **не** `Быстрый инсайт`; пример: `Инсайт до депозита:`).
    - **ЗАПРЕЩЕНО:** интерактивное оглавление — `<ol>`/`<ul>` с `<a href="#...">` на H2 сразу после инсайта. После blockquote идёт контекстный `<p>`, затем первый `<h2>`.
    - Атрибут `id` у `<h2>` — только для внешней перелинковки; не создавай оглавление в теле.
    - В конце (перед FAQ) — **Fact Check Box** через `<blockquote>` от редакции Авто-Сейлс. **Не** упоминай Wordstat и Метрику в тексте.
13. **CTA URL / Cloud secret-scan:** живые `CATALOG_URL` / `TELEGRAM_URL` в `href` часто ломают pre-commit. На строке с CTA добавь HTML-комментарий `<!-- // pragma: allowlist secret -->`. Перед `git commit`: `eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"` или `bash scripts/excalibur_git.sh commit …`. Не подставляй `[REDACTED]` в живые `href`.

## Выход

```text
memory/blog/articles/<topic_id>-<slug>/article.html
memory/blog/articles/<topic_id>-<slug>/article.meta.json
```

## Blockers

- нет research-notes.md
- utility-only нарушен (вода, нет шагов)
- объём вне диапазона после 1 правки

References: `article-archetypes.md` (§ B only), `geo-writing-checklist.md`, `ai-slop-blocklist.md`
