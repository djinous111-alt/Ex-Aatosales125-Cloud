# Promotion checklist — AS11 proverka-kitayskogo-avto-po-vin-2026

Дата публикации: 2026-09-28  
Live URL: [PUBLIC_SITE_URL]/2026/09/28/proverka-kitayskogo-avto-po-vin-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (HEAD 200)
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
Депозит без VIN — лотерея с авансом

• Сначала фото VIN с кузова и сверка с инвойсом
• Китайский отчёт (пробег/ДТП) + реестр залогов ФНП + Госуслуги — не «чисто по ГИБДД»
• Нет зелёного пакета — нет перевода

Читать: /blog/proverka-kitayskogo-avto-po-vin-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (corpus AS08/AS09/AS11; suggestions empty)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как проверить китайское авто по vin до депозита» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS11-proverka-kitayskogo-avto-po-vin-2026` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (AS11 в индексе; CLI: `--blog-dir`, `--site-base ""` relative URLs; без `--blog-path`).
- Publish: pending (директор → excalibur-blog-publish; publish может абсолютизировать URL).
