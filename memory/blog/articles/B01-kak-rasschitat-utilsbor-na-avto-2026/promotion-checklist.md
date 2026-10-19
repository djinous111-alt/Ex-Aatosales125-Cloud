# Promotion checklist — B01 kak-rasschitat-utilsbor-na-avto-2026

Дата публикации: 2026-10-19 (pending publish)  
Live URL: /blog/kak-rasschitat-utilsbor-na-avto-2026/

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
Утильсбор 2026: цифра из чата уже не та?

• Страна JP/KR/CN формулу РФ не меняет — важны возраст, объём, документальная мощность
• Сначала паспорт лота из 8–10 полей, потом свежий расчёт в каталоге
• Не копируйте сумму из скриншота чата до депозита

Читать: /blog/kak-rasschitat-utilsbor-na-avto-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (корпус 3 статьи, пересечений якорей с AS08/AS09 нет)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «утильсбор на авто 2026» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir ... --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir` + `--out-dir`, `--site-base ""` для relative `/blog/<slug>/`; без `--blog-path`).
- Publish: не запускался (зона Indexer).
