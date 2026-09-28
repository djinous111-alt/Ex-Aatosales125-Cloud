# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-09-28 (planned; pre-publish)  
Live URL: /blog/encar-na-russkom-kak-chitat/ (после WP publish)

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
Красивая цена — кот в мешке?

• Официальной русской версии encar.com нет — цифры сверяйте с оригиналом
• X = обмен детали, W = рихтовка/сварка; лист 120 дней
• Carhistory — вспомогательный слой, не замена Performance Check

Читать: /blog/encar-na-russkom-kak-chitat/
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

- Indexer: interlinker `--apply --article-dir …/AS02-encar-na-russkom-kak-chitat --site-base $PUBLIC_SITE_URL` — 3 links applied (AS08×1, AS09×2 → AS02); relative `/blog/…` anchors.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir memory/blog/articles --site-base "" --out-dir memory/blog`; без устаревшего `--blog-path`; relative URLs для commit-safe).
- Publish: pending после Indexer.
