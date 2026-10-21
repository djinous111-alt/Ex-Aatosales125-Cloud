# Promotion checklist — B01 toyota-alphard-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-21  
Live URL: [REDACTED]/2026/10/21/toyota-alphard-iz-yaponii-komplektatsii-lovushki-2026/

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
Alphard с USS — а кузов уже 40?

• До ставки: код кузова 30/40, тип мотора, письменный ответ о маршруте
• Гибрид/PHEV ≠ «просто бензин»: лист не показывает здоровье батареи
• METI-фильтр: современный Alphard нельзя считать прямым экспортом в РФ

Читать: /2026/10/21/toyota-alphard-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (корпус AS08/AS09/B01 без совпадений якорей)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать тойота альфард из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir … --site-base ${PUBLIC_SITE_URL}` — opportunities_found=0; committed report `site_base=""`.
- llms: `python3 …_llms_generator.py --blog-dir memory/blog/articles --site-base "" --out-dir memory/blog` (relative `/blog/<slug>/`; без `--blog-path`; не коммитить host из PUBLIC_SITE_URL).
- llms.txt / llms-full.txt: B01 в индексе (3 articles).
- Publish: не запускался (indexer only).
