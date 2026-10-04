# Promotion checklist — B02 postanovka-na-uchet-avto-iz-yaponii-2026

Дата публикации: 2026-10-04 (ожидается после publish)  
Live URL: [REDACTED]blog/postanovka-na-uchet-avto-iz-yaponii-2026/

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
Забрали авто со СВХ, распечатали ЭПТС — в ГИБДД развернули: «незавершённый»

• В МРЭО едут только со статусом ЭПТС «действующий»
• СБКТС + ПТД/ТПО + ОСАГО с реальной датой начала
• Госуслуги и осмотр — один визит до СТС и номеров

Читать: [REDACTED]blog/postanovka-na-uchet-avto-iz-yaponii-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: opportunities_found=0 (3 articles in corpus; no safe anchor match for B02)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «постановка на учет авто из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir memory/blog/articles/B02-postanovka-na-uchet-avto-iz-yaponii-2026 --site-base $PUBLIC_SITE_URL` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir memory/blog/articles` (без устаревшего `--blog-path` как каталога статей).
- Publish: pending (indexer only).
