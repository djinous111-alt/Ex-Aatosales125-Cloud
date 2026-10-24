# Promotion checklist — B01 honda-freed-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-24  
Live URL: /blog/honda-freed-iz-yaponii-komplektatsii-lovushki-2026/

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
Красивый Hybrid — ещё не ставка

• Freed №1 ввоза янв–авг 2026 (~14,7 тыс.) — спрос не отменяет фильтр
• До ставки: кузов GB/GP/GT, бензин или гибрид, двери + Sensing, лист
• Hybrid в лоте = пауза на код кузова и маршрут, не «бери»

Читать: /blog/honda-freed-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08, AS09, B01) — suggestions пустые

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «хонда фрид из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir … --site-base ${PUBLIC_SITE_URL}` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (CLI: `--blog-dir` + `--out-dir`, empty `--site-base` → relative `/blog/<slug>/`; без `--blog-path`).
- Publish: не запускался (зона publish-агента).
