# Promotion checklist — B01 mitsubishi-delica-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-26  
Live URL: (после publish) /blog/mitsubishi-delica-iz-yaponii-komplektatsii-lovushki-2026/

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
Красивый лот Delica ≠ быстрый пригон

• Грейд G / G-Power / P — до ставки, не по заголовку лота
• Дизель 4N14 (~2267 см³) + AdBlue + порог 1.9 л → третья страна
• Сначала аукционный лист, потом ставка

Читать: /blog/mitsubishi-delica-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 ↔ B01 — нет пересечений якорей)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «делика из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base ${PUBLIC_SITE_URL}` — applied_count=0.
- llms.txt / llms-full.txt: `--blog-dir memory/blog/articles --out-dir memory/blog --site-base ""` (relative `/blog/…` URLs).
- Skill/agent ещё документируют stale `--blog-path` — incident для fixer.
