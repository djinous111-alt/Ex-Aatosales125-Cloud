# Promotion checklist — B01 kia-sorento-iz-korei-komplektatsii-lovushki-2026

Дата публикации: (pending publish)  
Live URL: (pending)

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
Депозит до брифа — ловушка на Encar

• Сначала лист «моя версия»: мотор, места, привод, минимум Prestige–X-Line
• Gravity с 2026 MY = X-Line; гибрид ≠ автольгота
• Красный флаг Trust Encar / Carhistory — стоп перевода

Читать: (URL после publish)
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: B01 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`, якорь «Trust Encar»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «киа соренто из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base $PUBLIC_SITE_URL` — 1 link applied (B01→AS09).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir` / `--out-dir`; без `--blog-path`).
- Publish: не запускался (indexer only).
