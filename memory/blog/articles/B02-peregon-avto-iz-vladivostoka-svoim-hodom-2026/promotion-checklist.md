# Promotion checklist — B02 peregon-avto-iz-vladivostoka-svoim-hodom-2026

Дата публикации: 2026-10-17  
Live URL: /blog/peregon-avto-iz-vladivostoka-svoim-hodom-2026/

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
Ключи есть — ехать ещё нельзя

• До выезда: ЭПТС, ОСАГО на VIN, осмотр на стоянке
• 10 суток на заявление в ГИБДД — не путать с «можно без полиса»
• Зима / дальняк / нежная машина — чаще автовоз, не своим ходом

Читать: /blog/peregon-avto-iz-vladivostoka-svoim-hodom-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] В тексте уже есть ручная ссылка на AS08 (`/blog/samye-komfortnye-avto-myagkaya-podveska-2026/`, якорь «мягкую подвеску»)
- [x] Локальный interlinker `--apply`: 0 новых opportunities (corpus=3; suggestions пустые)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «перегон авто из владивостока своим ходом» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir memory/blog/articles/B02-peregon-avto-iz-vladivostoka-svoim-hodom-2026 --site-base ${PUBLIC_SITE_URL}` — opportunities_found=0.
- llms.txt / llms-full.txt: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base ${PUBLIC_SITE_URL} --out-dir memory/blog` (без `--blog-path`: класс не принимает флаг; doctor всё ещё ждёт его).
- Publish: pending (после Indexer).
