---

## name: excalibur-research
description: Excalibur BLOG Research — topic research перед статьёй (SERP, факты, угол). Gate до article.html.

# Excalibur BLOG — Research

## Когда

**Шаг 0 (скрипт, обязательно):** перед любым research — зафиксировать дату и собрать свежий SERP.

```bash
python scripts/excalibur_blog_research_start.py --topic-id B01
```

Создаёт в папке статьи:

- `research-context.json` — сегодняшняя дата, год, окно свежести, тема, список поисковых запросов
- `research-serp.json` — результаты web-поиска по запросам с `{year}` и текущим месяцем

`--dry-run` — только дата и запросы без HTTP.

Перед **каждой** статьей затем пиши `research-notes.md`. Без него нельзя утверждать цены, даты, версии, статистику.

## Вход

- Карточка из `memory/topics/blog-topics.md`
- `memory/brief/site-brief.md`, `fact-bank.md`
- `shared/quality-blog.md`
- MCP сервер `user-mcp-kv` со всеми инструментами `wordstat_*`

## Выход

`memory/blog/articles/<topic_id>-<slug>/research-context.json`  
`memory/blog/articles/<topic_id>-<slug>/research-serp.json`  
`memory/blog/articles/<topic_id>-<slug>/research-notes.md` (с разделом по Вордстату!)

## Обязательное использование Yandex Wordstat MCP и WebSearch Курсора

1. **Анализ спроса через Wordstat API:**
  Каждый прогон исследования **обязан** задействовать инструмент `wordstat_get_top_requests` сервера `user-mcp-kv` для анализа спроса:
  - Вызови `wordstat_get_top_requests` для `primary_query` и ключевых `secondary_queries`.
  - Если вызов вернул `401 Unauthorized` (токен устарел):
    - Запиши в `research-notes.md` предупреждение: `⚠️ WORDSTAT AUTH WARNING: Токен Wordstat устарел. Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40`
    - Сделай экспертную оценку семантики, но явно укажи, что точные объемы спроса не получены из-за авторизации.
  - Если вызов успешен:
    - Сформируй в `research-notes.md` таблицу спроса: Фраза | Показы в месяц.
    - Выдели сопутствующие LSI-запросы из топа выдачи Вордстата для использования копирайтером.
2. **Замена уличных поисковиков (DuckDuckGo) на WebSearch Курсора:**
  Мы **отказываемся** от ненадежных сторонних утилит и парсеров DuckDuckGo («уток»).
  - Агент имеет полноценный доступ в интернет через нативный инструмент `**WebSearch`** (или `WebFetch` для чтения конкретных страниц).
  - Для анализа конкурентов в SERP **всегда используй инструмент `WebSearch`**. Ищи статьи, руководства, гайды по `primary_query` и ключевым словам в Яндексе и Google.
  - Игнорируй сырой `research-serp.json` из шага 0, если он пуст, неполный или нерелевантный. Твой собственный поиск через `WebSearch` — приоритетный источник свежих данных 2026 года.

## Правила

1. **Сначала** `excalibur_blog_research_start.py` (шаг 0) — для валидации даты/года и utility-gate темы.
2. Web research 15–25 мин: используй инструмент `**WebSearch`** Курсора для глубинного анализа ТОП-5 конкурентов в реальном времени. GitHub/docs/community нужны для фактов, но итоговый угол обязан быть beginner-first: что новичку нажать, подключить, проверить и как не сломать процесс. Приоритетный источник фактов — `fact-bank.md`.
3. Микро-исследование Wordstat через `user-mcp-kv` -> `wordstat_get_top_requests` (см. выше).
4. Извлеки минимум 10–15 проверенных фактов (цифр/утверждений) с точными URL источников из твоего интернет-поиска.
5. Каждая цифра → таблица фактов в `research-notes.md` или не использовать.
6. Не копировать структуру конкурента 1:1.
7. `reader_pain`, `reader_outcome`, `success_criteria`, `pain_solution_map` формулируй для обычного человека без технического бэкграунда. Если тема звучит как для профи/архитектора и не даёт новичку первого результата — это research blocker.

## Официальные gov/customs порталы (flaky WebFetch)

- `customs.gov.ru` и `edata.customs.ru` часто отвечают **5xx / 504 / SSL timeout** из агентского egress.
- При 5xx/timeout на этих доменах **разрешены surrogate official sources**: ConsultantPlus, акты Минфина/ФТС на отраслевых порталах, TKS/гайды с цитатой приказа — с явной пометкой в `source_table` (`accessed_at` + note про 504/timeout).
- URL ЛК/портала **оставляй** в `source_table` (официальная точка входа); перед publish GEO QA / link-verify soft-fail SSL timeout на этих хостах.
- Повтори WebFetch портала один раз с backoff; не блокируй research только из‑за недоступности HTML портала, если факты сверены через surrogate.

## Формат для research-notes-gate

- В `source_table` даты пиши как `accessed_at: YYYY-MM-DD` (gate ищет `accessed_at`).
- В `pain_solution_map` каждая строка должна содержать слова `боль` / `решение` / `результат`.
- `github_evidence` обязателен как секция; жёсткие ≥3 `github.com` URL требуются только для **technical** тем (AI/API/агенты). Авто/таможня — не tech: достаточно docs/community evidence без принудительных GitHub URL.

## Blockers

- `❌ RESEARCH BLOCKER` — тема не найдена и не создана из запроса пользователя
- `❌ RESEARCH BLOCKER` — нет источников для ключевых утверждений
- `❌ RESEARCH BLOCKER` — research angle ушёл в материал для профи/архитекторов и не даёт новичку первого понятного результата

