# Promotion checklist — B01 mitsubishi-outlander-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-26 (план; live после publish)  
Live URL: /blog/mitsubishi-outlander-iz-yaponii-komplektatsii-lovushki-2026/

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
Красивый лот Outlander — а вывоз в 2026?

• Сначала код кузова (XL/GF/GG/GN), потом ставка
• PHEV и мотор >1900 cc — стоп без подтверждённого маршрута
• R/RA на листе — не «мелочь», а история ремонта силовых

Читать: /blog/mitsubishi-outlander-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: opportunities_found=0 (ключевые совпадения с AS08/AS09 не найдены; ручная перелинковка после publish)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «аутлендер из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …B01… --site-base $PUBLIC_SITE_URL` — 0 links applied.
- llms.txt / llms-full.txt: `--blog-dir memory/blog/articles --out-dir memory/blog --site-base ""` → relative `/blog/<slug>/` (3 articles).
- Publish: не запускался (директор → следующий Task).
