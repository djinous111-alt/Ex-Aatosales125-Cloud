# Promotion checklist — AS15 dostavka-avto-iz-vladivostoka-2026

Дата публикации: 2026-07-21
Live URL: /2026/07/21/dostavka-avto-iz-vladivostoka-2026/  <!-- pragma: allowlist secret -->

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200) — в т.ч. СВХ / СБКТС / ЭПТС
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
После СВХ три совета в чате — лотерея

• Сравнивайте общий срок, не «дни в пути»
• Ж/д 10–14 в пути часто = 20–45 до выдачи
• Перегон «дешевле» съедают авиа, топливо и сколы

Читать: /2026/07/21/dostavka-avto-iz-vladivostoka-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 новых opportunity (в memory только AS08/AS09/AS15; темы не пересекаются)
- [x] Уже в body: ручные ссылки на СВХ Владивосток 2026 и СБКТС/ЭПТС

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «доставка авто из владивостока» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS15-… --site-base $PUBLIC_SITE_URL` — opportunities_found=0 (total_articles=3).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (AS15 в индексе).
- published: WP post 3553; featured 3566; inline 3567/3568/3569; schema_meta ok.
