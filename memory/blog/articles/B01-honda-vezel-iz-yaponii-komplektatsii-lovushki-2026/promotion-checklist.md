# Promotion checklist — B01 honda-vezel-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-23  
Live URL: /blog/honda-vezel-iz-yaponii-komplektatsii-lovushki-2026/

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
Депозит за красивый скрин e:HEV RS — лотерея

• G в Японии ≠ топ-гибрид; гибрид пишут e:HEV (RV5/RV6)
• До ставки: код кузова + лист + мощность 30 мин vs 117,68 кВт
• Япония с листом ≠ «Vezel из Китая» без аукциона

Читать: /blog/honda-vezel-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (ключевые фразы B01 не встречаются в AS08/AS09 body)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «хонда везел из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base $PUBLIC_SITE_URL` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (empty `--site-base` → git-relative `/blog/<slug>/`; без `--blog-path` — CLI его не принимает).
- Publish: pending (indexer не публикует).
