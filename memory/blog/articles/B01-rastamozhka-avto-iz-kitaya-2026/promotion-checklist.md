# Promotion checklist — B01 rastamozhka-avto-iz-kitaya-2026

Дата публикации: 2026-10-03  
Live URL: [PUBLIC_SITE_URL]/2026/07/22/rastamozhka-avto-iz-kitaya-2026/

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
Смета в чате — а на СВХ сюрприз?

• Растаможка из Китая 2026: СВХ → декларация → выпуск → СБКТС → ЭПТС → ГИБДД
• Документы и мощность в л.с. фиксируйте до оплаты
• Уссурийск янв–май 2026: 33,5 тыс. авто, корректировка цены ~1,6%

Читать: [PUBLIC_SITE_URL]/2026/07/22/rastamozhka-avto-iz-kitaya-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (B01 ↔ AS08/AS09 — нет совпадения primary/secondary/anchor в body)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «растаможка авто из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply --article-dir …/B01-rastamozhka-avto-iz-kitaya-2026` — links applied: 0.
- llms.txt / llms-full.txt: `memory/blog/` с относительными URL (`--site-base /`, без PUBLIC_SITE_URL в артефакте).
- Cover ✅ + Schema ✅; GEO QA PASS; publish PASS (post=3601, featured=3974, inline=3975/3976/3977).
