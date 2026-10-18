# Promotion checklist — B08 kia-sportage-iz-korei-komplektatsii-lovushki-2026

Дата публикации: 2026-10-19  
Live URL: [REDACTED]/2026/10/19/kia-sportage-iz-korei-komplektatsii-lovushki-2026/

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
Signature на фото ≠ льготный утиль

• До депозита сверьте fuel и л.с.: LPG 146 — кандидат под льготу физлица, 1.6T 180 — коммерческий утиль
• В актуальном каталоге Kia KR дизеля в линейке Sportage нет
• Депозит — только после VIN, Performance Check и стоп-правил

Читать: /blog/kia-sportage-iz-korei-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (3 статьи; точных якорей meta AS08/AS09 в HTML B08 и наоборот не найдено)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «спортейдж из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B08-… --site-base $PUBLIC_SITE_URL` → opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (без `--blog-path`; CLI: `--blog-dir` + `--out-dir`).
- Publish: ещё не выполнен (Indexer only).
