# Promotion checklist — B01 kak-rastamozhit-avto-iz-korei-2026

Дата публикации: 2026-10-19  
Live URL: (после publish)

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
Депозит без сверки л.с. — лотерея

• Растаможка = пошлина + утильсбор + сбор, не одна сумма
• До оплаты сверьте мощность по документам (порог 160 л.с.)
• Этапы через Владивосток: СВХ → СБКТС → ЭПТС

Читать: /blog/kak-rastamozhit-avto-iz-korei-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (B01 + AS08 + AS09 в memory; анкоры не совпали)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «растаможка авто из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-kak-rastamozhit-avto-iz-korei-2026 --site-base $PUBLIC_SITE_URL` — 0 links applied; report `memory/blog/interlink-suggestions.json`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir` + `--out-dir`, без `--blog-path`).
- Publish: pending.
