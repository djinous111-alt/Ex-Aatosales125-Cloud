# Promotion checklist — B01 kak-rastamozhit-avto-iz-korei-2026

Дата публикации: 2026-07-25 (planned)  
Live URL: https://avtosales125.ru/blog/kak-rastamozhit-avto-iz-korei-2026/

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
Машина на СВХ – а депозита нет?

• Растаможка из Кореи — цепочка депозит → СВХ → выпуск → СБКТС/ЭПТС → ГИБДД
• Документы и обеспечение на ФТС — до прихода судна
• Готовые суммы в гайдах расходятся — расчёт под VIN

Читать: https://avtosales125.ru/blog/kak-rastamozhit-avto-iz-korei-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Writer already: B01 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`, якорь «проверку корейского авто до депозита»)
- [x] Indexer interlinker `--apply`: 0 новых opportunities (corpus=3; B01↔AS09 уже есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «растаможка авто из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir memory/blog/articles/B01-kak-rastamozhit-avto-iz-korei-2026 --site-base $PUBLIC_SITE_URL` — 0 links applied (opportunities_found=0).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles; site-name «Авто-Сейлс»).
- Cover BLOCKED (Kie 402) — featured image check после publish может FAIL до top-up credits.
- Publish: pending (не запускался indexer'ом).
