# Promotion checklist — B02 dostavka-avto-iz-vladivostoka-zhd-avotovoz-peregon-2026

Дата публикации: 2026-10-05 (ожидаемая; publish pending)  
Live URL: (после publish) `/blog/dostavka-avto-iz-vladivostoka-zhd-avotovoz-peregon-2026/`

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
Машина на СВХ, а вы смотрите три прайса и не понимаете, за что платите

• Ж/д vs автовоз vs перегон — срок, риск кузова, контроль
• До оплаты: фотоакт крыши, ярус, страховка груза
• Default Владивосток–Москва: автовоз с договором

Читать: [URL после publish]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 тематически не пересекаются с inland-доставкой)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «доставка авто из владивостока» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir ... --site-base $PUBLIC_SITE_URL` — opportunities_found=0; report `memory/blog/interlink-suggestions.json`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles; B02 в индексе). CLI: `--blog-dir` (без `--blog-path`).
- Publish: pending (Indexer не publish).
