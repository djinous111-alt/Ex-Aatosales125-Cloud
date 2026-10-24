# Promotion checklist — B01 toyota-raize-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-24  
Live URL: /2026/10/24/toyota-raize-iz-yaponii-komplektatsii-lovushki-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (HEAD 200; WP REST id=4495 featured_media=4496)
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
До ставки: код кузова важнее названия

• A201A = 1.2 FWD; A210A = 1.0T 4WD; гибрид A202A — мимо
• Возраст для пошлины — от месяца выпуска до декларации
• 10 стоп-пунктов по аукционному листу до ставки

Читать: /blog/toyota-raize-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 не содержат якорей Raize / primary_query B01)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать toyota raize из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base ""` — 0 links applied (topic mismatch с AS08 soft-suspension / AS09 Trust Encar).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (relative URLs, 3 articles, B01 включён).
- Publish: PASS — post_id=4495; featured=4496; inline=4497/4498/4499; schema_meta ok; skip_theme_faq=1.
- Post-publish interlinker `--apply --blog-dir memory/blog/articles`: 0 inbound opportunities (AS08/AS09).
