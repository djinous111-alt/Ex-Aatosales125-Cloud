# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-10-16  
Live URL: /blog/encar-na-russkom-kak-chitat/

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
Цена 1890 — это манвоны, не рубли

• Официального «русского Encar» почти нет — перевод браузера (часто EN яснее)
• Чеклист 8 полей: год, пробег, цена, VIN, лист 성능점검, страховка, фото, тип продавца
• X/W на силовых — стоп до любого депозита

Читать: /blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Мост AS02 → AS09 уже в статье (`/2026/07/17/trust-encar-carhistory-proverka-do-depozita/`, Trust Encar / Carhistory)
- [x] Локальный interlinker `--apply`: 0 новых opportunities (slug AS09 уже в HTML; обратных keyword-match нет)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS02-encar-na-russkom-kak-chitat` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` с `--site-base ""` (relative `/blog/…`; AS02 в индексе; site-name «Авто-Сейлс»).
- Publish: pending (директор после Indexer).
