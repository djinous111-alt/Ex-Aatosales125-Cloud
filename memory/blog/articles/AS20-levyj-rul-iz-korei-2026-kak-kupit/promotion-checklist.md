# Promotion checklist — AS20 levyj-rul-iz-korei-2026-kak-kupit

Дата публикации: 2026-07-22 (ожидается после publish)  
Live URL: (после publish) [REDACTED]/blog/levyj-rul-iz-korei-2026-kak-kupit/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200) — локально: `/blog/trust-encar-carhistory-proverka-do-depozita/`
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Депозит красивой карточке Encar — лотерея

• Левый руль из Кореи: VIN + Performance Check без X/W + Carhistory без Rent
• Договор с юрлицом — до перевода
• 12 пунктов чек-листа → решение да/нет по лоту

Читать: [REDACTED]/blog/levyj-rul-iz-korei-2026-kak-kupit/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: AS20 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`, якорь «Trust Encar»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «левый руль из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir ... --site-base $PUBLIC_SITE_URL` — 1 link applied (AS20→AS09).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (AS20 в индексе; 3 articles loaded).
- Publish: pending (Директор → excalibur-blog-publish).
