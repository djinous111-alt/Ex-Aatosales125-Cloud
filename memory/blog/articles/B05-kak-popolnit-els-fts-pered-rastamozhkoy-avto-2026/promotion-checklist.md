# Promotion checklist — B05 kak-popolnit-els-fts-pered-rastamozhkoy-avto-2026

Дата публикации: 2026-10-18  
Live URL: https://avtosales125.ru/2026/10/18/kak-popolnit-els-fts-pered-rastamozhkoy-avto-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL (HEAD 200) — title, excerpt, featured image, FAQ
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
Машина на пути — а ЕЛС пуст?

• С 01.04.2026 чужой платёж на ЕЛС почти не зачисляют
• Путь: ЛК ФТС через Госуслуги → СБП своей картой → скрин остатка менеджеру
• До СВХ: свой ИНН, свой остаток, небольшой запас под курс

Читать: https://avtosales125.ru/2026/10/18/kak-popolnit-els-fts-pered-rastamozhkoy-avto-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (корпус AS08/AS09/B05 — темы не пересекаются по якорям)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как пополнить елс фтс» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir …/B05-… --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir` + `--out-dir`, без `--blog-path`).
- Publish: PASS post_id=4310; featured=4311; inline=4312/4313/4314; schema_meta ok; Live HEAD 200.
