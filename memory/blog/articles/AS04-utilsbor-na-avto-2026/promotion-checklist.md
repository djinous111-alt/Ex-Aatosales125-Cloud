# Promotion checklist — AS04 utilsbor-na-avto-2026

Дата публикации: 2026-11-01  
Live URL: ${PUBLIC_SITE_URL}/2026/07/18/utilsbor-na-avto-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — HEAD 200; featured_media=4733; post=3430
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
Чужой скрин утиля — и бюджет в огне?

• Страна KR/CN/JP при прямом ввозе формулу не меняет
• Считайте от статуса, возраста, объёма и мощности в кВт (порог 160 л.с.)
• Цифру по лоту — в каталоге до депозита, не со скрина соседа

Читать: ${PUBLIC_SITE_URL}/2026/07/18/utilsbor-na-avto-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09/AS04 в memory; якоря AS04 не встретились в текстах соседей)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «утильсбор на авто 2026» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir … --site-base $PUBLIC_SITE_URL` — 0 links applied; suggestions empty.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 статьи; commit-safe relative `/blog/…` URLs).
- Publish: pending.
