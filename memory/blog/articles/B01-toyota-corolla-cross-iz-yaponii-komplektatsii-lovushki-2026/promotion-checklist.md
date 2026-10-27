# Promotion checklist — B01 toyota-corolla-cross-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-28 (planned)  
Live URL: /blog/toyota-corolla-cross-iz-yaponii-komplektatsii-lovushki-2026/

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
Гибрид Z с пятёркой — уже ставим?

• Corolla Cross ≠ седан Corolla и ≠ китайский LHD Cross
• Сначала код кузова ZSG/ZVG/MXGH, потом комплектация и лист
• После 05.2025 почти вся JP-линейка гибрид — проверьте экспорт до ставки

Читать: /blog/toyota-corolla-cross-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 без пересечения якорей с B01)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «тойота королла кросс из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base ${PUBLIC_SITE_URL}` — 0 links applied (topics AS08 comfort / AS09 Trust Encar не пересекаются с Corolla Cross keywords).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir` + `--out-dir`, commit-safe `--site-base ""`, без `--blog-path`).
- Publish: pending (Indexer only; не публиковать на этом шаге).
