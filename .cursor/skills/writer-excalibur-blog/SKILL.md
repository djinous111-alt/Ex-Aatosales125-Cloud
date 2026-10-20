# Excalibur BLOG — Writer

## Вход

- `research-notes.md` с **utility_verdict: PASS**
- `shared/excalibur-article-writing-contract.md`
- `shared/editorial-utility-only.md`
- `memory/brief/site-brief.md`, `conversion-map.md`

## Задача

1. **Только режим B** — инструкция/гайд/чеклист/comparison. Режим A запрещён.
2. Outline H2 = подзадачи с **действием** (не «вообще про тему»).
3. **ПРОСТОЙ ЧЕЛОВЕЧЕСКИЙ ЯЗЫК (ГЛАВНОЕ ПРАВИЛО):** Пиши максимально понятно и доступно для покупателя авто под заказ (не дилер и не таможенный брокер). Любой термин (Encar, ЕЛС, СБКТС, утильсбор, ЭПТС) **обязан** иметь моментальную расшифровку и объяснение «на пальцах» (на простых аналогиях).
4. **ОФОРМЛЕНИЕ ТЕКСТА (БЕЗ ДЛИННЫХ ТИРЕ И ЁЛОЧЕК):** Запрещено использовать длинные тире («—») и кавычки-ёлочки (««», «»»). Всегда используй среднее тире («–») или обычный дефис («-»), а вместо кавычек-ёлочек — стандартные прямые двойные кавычки («"`»).
5. Hook 350–500 символов: боль → ответ → **что сделает читатель**.
6.  Минимум **5** нумерованных шагов `<ol>` + workflow (`→`) или таблица.
7. Каждый H2: рекомендация глаголами из `recommendation_markers_ru` (сделайте/не делайте/проверьте/чеклист), не только ярлык «Делать:».
8. Body 8 500–9 500 знаков, FAQ 5–7 пар — **ответы-действия**, **один** блок `<h2>Частые вопросы</h2>` (без второго FAQ).
9. `article.meta.json`: `article_mode: B`, `char_count`, `meta_ab` с A/B/AEO оптимизацией:
   - `title_seo`: 35–75 симв, точный `primary_query` в начале + триггер.
   - `title_ctr`: 40–100 симв, кликабельный крючок, обязательно эмодзи (например 💻, 🚀) или знаки ?, !
   - `title_aeo`: 35–90 симв, сформулирован как вопрос ИИ-поисковику (начинается с "Как", "Что", "Почему" или содержит "?").
   - `description_seo`: 100–180 симв.
10. Подзаголовки H2 должны начинаться с **глаголов действия** (создайте, настройте, проверьте) или содержать **маркеры действия** (как, чеклист, сравнение, выбор, пошагово). Минимум 3 H2 должны быть активными.
11. **RSS И ДЗЕН-СОВМЕСТИМОСТЬ (КРИТИЧЕСКИ):** Тело статьи `article.html` должно быть чистым, семантическим HTML без JS-кнопок, инлайновых стилей `style="..."` или кастомных тегов. Выжимки TL;DR оборачивай строго в тег `<blockquote>` (он нативно рендерится Дзеном как цитата), блоки «кода»/шаблонов — через `<blockquote>` / таблицу / список (теги `<pre>`/`<code>` запрещены HTML-линтером).
12. **СТРУКТУРНЫЕ ЭЛЕМЕНТЫ (TL;DR, EEAT — без оглавления):** 
    - Сразу после Lead-абзаца вставляй блок `<blockquote>` с выжимкой ключевых инсайтов (**AEO TL;DR Box**).
    - **ЗАПРЕЩЕНО:** интерактивное оглавление — `<ol>` или `<ul>` с `<a href="#...">` на заголовки H2/H3 сразу после TL;DR. После blockquote TL;DR идёт контекстный `<p>`, затем первый `<h2>`.
    - Атрибут `id` у `<h2>` — только если нужен для внешней перелинковки; не создавай оглавление в теле статьи.
    - В конце статьи (перед FAQ) вставляй блок верификации (**Fact Check Box**) через `<blockquote>` от редакции Авто-Сейлс. **Не** упоминай Wordstat и Метрику в тексте статьи.



## CTA / URL contract (согласованный)

1. **GEO QA / link-verify:** в рабочем `article.html` CTA href гидратируются из env (`CATALOG_URL`, `TELEGRAM_URL`); internal `[REDACTED]/path` → `PUBLIC_SITE_URL`. Не оставляй «мёртвый» литерал `[REDACTED]` без hydrate перед hard-gate.
2. **git commit:** secret-scan может потребовать `[REDACTED]` в committed копии — это допустимо.
3. **Publish:** снова hydrates live URL перед WP.
4. Перед `git commit` при `invalid variable name` в pre-commit: `source scripts/excalibur_blog_filter_secret_names.sh` (или положиться на filter в pre-commit.cursor).

`excalibur_blog_link_verify.py` умеет hydrate `[REDACTED]` из env по anchor text; всё равно предпочитай живые env URL на этапе QA.

## Utility markers

- В каждом H2 используй глаголы из `recommendation_markers_ru` в `memory/brief/editorial-policy.json` (`сделайте`, `не делайте`, `проверьте`, `чеклист`…), не только ярлык «Делать:».
- Не удаляй `pain_markers_ru` / `outcome_markers_ru` из editorial-policy; utility gate skip-ит пустые списки, но маркеры должны быть в policy.

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
