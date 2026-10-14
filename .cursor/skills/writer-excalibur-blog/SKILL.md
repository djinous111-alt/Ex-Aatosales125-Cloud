# Excalibur BLOG — Writer

## Вход

- `research-notes.md` с **utility_verdict: PASS**
- `shared/excalibur-article-writing-contract.md`
- `shared/editorial-utility-only.md`
- `memory/brief/site-brief.md`, `conversion-map.md`

## Задача

1. **Только режим B** — инструкция/гайд/чеклист/comparison. Режим A запрещён.
2. Outline H2 = подзадачи с **действием** (не «вообще про тему»).
3. **ПРОСТОЙ ЧЕЛОВЕЧЕСКИЙ ЯЗЫК (ГЛАВНОЕ ПРАВИЛО):** Пиши максимально понятно и доступно для простого человека (предпринимателя, новичка, не-программиста). Исключай сложный технический снобизм. Любой используемый термин (API, RAG, Self-hosted, Docker) **обязан** иметь моментальную расшифровку и объяснение «на пальцах» (на простых аналогиях).
4. **ОФОРМЛЕНИЕ ТЕКСТА (БЕЗ ДЛИННЫХ ТИРЕ И ЁЛОЧЕК):** Запрещено использовать длинные тире («—») и кавычки-ёлочки (««», «»»). Всегда используй среднее тире («–») или обычный дефис («-»), а вместо кавычек-ёлочек — стандартные прямые двойные кавычки («"`»).
5. Hook 350–500 символов: боль → ответ → **что сделает читатель**.
6.  Минимум **5** нумерованных шагов `<ol>` + workflow (`→`) или таблица.
7. Каждый H2: рекомендация словами из `memory/brief/editorial-policy.json` → `recommendation_markers_ru` (**«сделайте» / «не делайте»**, «проверьте», «избегайте»…). Формы «Делать/Не делать» utility gate не считает.
8. Body 8 500–9 500 знаков, FAQ 5–7 пар — **ответы-действия**, **один** блок `<h2>Частые вопросы</h2>` (без второго FAQ).
9. `article.meta.json`: `article_mode: B`, `char_count`, `meta_ab` с A/B/AEO оптимизацией:
   - `title_seo`: 35–75 симв, точный `primary_query` в начале + триггер.
   - `title_ctr`: 40–100 симв, кликабельный крючок, обязательно эмодзи или знаки ?, !
   - `title_aeo`: 35–90 симв, вопрос ИИ-поисковику («Как», «Что», «Почему» или «?»).
   - `description_seo`: 100–180 симв.
10. Подзаголовки H2 — глаголы действия (проверьте, сравните, соберите) или маркеры (как, чеклист, сравнение, выбор, пошагово). Минимум 3 активных H2.
11. **RSS / ДЗЕН:** чистый HTML без JS и `style="..."`. TL;DR — `<blockquote>`. **Не** используй `<pre>`/`<code>` (линтер whitelist); код/шаблоны — blockquote/table/list.
12. **Структура:** после Lead — blockquote-инсайт; **без** оглавления с `href="#..."`; Fact Check Box перед FAQ от редакции Авто-Сейлс (без Wordstat/Метрики в тексте).
13. **CTA href и secret-scan (критично):**
    - В runtime/publish CTA ведут на живые `CATALOG_URL` и Telegram из `conversion-map.md`.
    - В **закоммиченном** `article.html` подставь `href="[REDACTED]"` для значений Cloud Secrets (`CATALOG_URL` / `TELEGRAM_URL` / `PUBLIC_SITE_URL`); видимый anchor-текст оставляй человекочитаемым («каталог Авто-Сейлс», «Telegram @avtosales125»).
    - Не оставляй литерал `[REDACTED]` в href на этапе GEO QA link-verify: перед verify временно подставь URL из env, после — снова redact перед commit.
    - Коммиты: `bash scripts/excalibur_git.sh add|commit …` (фильтрует битые имена в `CLOUD_AGENT_INJECTED_SECRET_NAMES`).
14. **Utility markers:** lead называет боль (`pain_markers_ru`), до FAQ — явный результат (`outcome_markers_ru`). Списки маркеров — в `editorial-policy.json`; не удаляй ключи при sync brief.

## Выход

```text
memory/blog/articles/<topic_id>-<slug>/article.html
memory/blog/articles/<topic_id>-<slug>/article.meta.json
```

## Blockers

- нет research-notes.md
- utility-only нарушен (вода, нет шагов, пустые pain/outcome markers в тексте)
- CTA href = placeholder на этапе link-verify
- объём вне диапазона после 1 правки

References: `article-archetypes.md` (§ B only), `geo-writing-checklist.md`, `ai-slop-blocklist.md`
