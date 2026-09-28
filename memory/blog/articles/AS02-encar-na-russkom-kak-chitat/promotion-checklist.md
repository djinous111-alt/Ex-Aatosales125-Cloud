# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-09-28  
Live URL: /2026/07/18/encar-na-russkom-kak-chitat/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)
- [x] Live HEAD 200 после publish (post_id 3394)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Красивая цена — кот в мешке?

• Официальной русской версии encar.com нет — цифры сверяйте с оригиналом
• X = обмен детали, W = рихтовка/сварка; лист 120 дней
• Carhistory — вспомогательный слой, не замена Performance Check

Читать: /2026/07/18/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: AS08 → AS02 (`/blog/encar-na-russkom-kak-chitat/`, якорь «Carhistory»)
- [x] Локальный interlinker: AS09 → AS02 (`/blog/encar-na-russkom-kak-chitat/`, якоря «trust encar», «Carhistory»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply` — 3 links applied (AS08×1, AS09×2 → AS02); relative `/blog/…` anchors.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (relative URLs; commit-safe).
- Publish PASS: post 3394; featured 3767; inline 3768/3769/3770; schema_meta ok; live HEAD 200.
