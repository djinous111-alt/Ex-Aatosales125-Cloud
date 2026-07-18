# Promotion checklist — AS04 utilsbor-na-avto-2026

Дата публикации: 2026-07-18  
Live URL: [REDACTED]/2026/07/18/utilsbor-na-avto-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
2 л.с. в рекламе — и бюджет сгорел

• Утильсбор 2026 зависит от кВт, возраста и статуса, не от страны
• До депозита: паспорт параметров + сверка мощности в документах
• Точную цифру — в каталоге, не в случайном калькуляторе

Читать: [REDACTED]/2026/07/18/utilsbor-na-avto-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS04 ↔ AS08/AS09 — нет общих keyword/anchor matches; AS08→AS09 уже есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «утильсбор на авто 2026» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS04-utilsbor-na-avto-2026 --site-base [REDACTED]` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base `[REDACTED]`, site-name «Авто-Сейлс»; CLI без `--blog-path`, только `--blog-dir`).
- Cover + Schema PASS до Indexer; publish — следующий шаг.
