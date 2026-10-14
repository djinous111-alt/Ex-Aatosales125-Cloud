# Promotion checklist — B01 kak-kupit-avto-s-auktsiona-yaponii-2026

Дата публикации: 2026-10-15  
Live URL: [REDACTED]/2026/10/15/kak-kupit-avto-s-auktsiona-yaponii-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (HEAD 200; post=4203)
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
Физлицу на USS напрямую хода нет — только через посредника

• Сначала договор и депозит, потом лимит ставки в иенах
• После выигрыша — инвойс за 2–5 банковских дней
• Путь: площадка → порт Японии → ро-ро → Владивосток (часто 3–8 недель)

Читать: [REDACTED]/2026/10/15/kak-kupit-avto-s-auktsiona-yaponii-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply` для B01: opportunities_found=0 (изменений HTML нет)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как купить авто из японии с аукциона» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir ... --site-base $PUBLIC_SITE_URL` — 0 links applied (3 articles loaded).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (B01 включён; CLI без `--blog-path`, только `--blog-dir`).
- Publish: PASS — WP post=4203; featured=4204; inline=4205/4206/4207; schema_meta=1; skip_theme_faq=1; method SSH+HTTP.
