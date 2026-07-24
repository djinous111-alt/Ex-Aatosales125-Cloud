# Promotion checklist — B04 avtovoz-iz-vladivostoka-2026-kak-vybrat

Дата публикации: 2026-07-24 (ожидаемая; publish pending)  
Live URL: (после publish) `/2026/07/24/avtovoz-iz-vladivostoka-2026-kak-vybrat/` · llms index: `/blog/avtovoz-iz-vladivostoka-2026-kak-vybrat/`

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (+ HowTo)
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
Автовоз «на слово» — риск без акта

• После СВХ: 3 оффера по одному ТЗ, не карта физлица
• До Москвы ориентир 18–22 дня + слот 3–7 дней
• До погрузки: договор, акт и свои фото/видео

Читать: (live URL после publish)
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (корпус AS08/AS09/B04 без пересечения якорей)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «автовоз из владивостока» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B04-… --site-base $PUBLIC_SITE_URL` — 0 links applied (suggestions empty).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (B04 в индексе; site-name «Авто-Сейлс»).
- Schema ready: BlogPosting + FAQPage + HowTo; cover inject ok.
- Publish: pending (Indexer не публикует).
