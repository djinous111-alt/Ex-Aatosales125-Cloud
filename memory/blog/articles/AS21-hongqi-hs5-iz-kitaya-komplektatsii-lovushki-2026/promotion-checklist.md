# Promotion checklist — AS21 hongqi-hs5-iz-kitaya-komplektatsii-lovushki-2026

Дата публикации: pending (indexer pre-publish)  
Live URL: /blog/hongqi-hs5-iz-kitaya-komplektatsii-lovushki-2026/

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
Депозит до сверки trim — лотерея

• В Китае HS5 MY2026: QiYun / QiXiang / Shadow + привод 2WD/4WD
• Comfort/Deluxe с сайта РФ ≠ китайское имя trim
• Депозит — только после CN-имени, привода и VIN-milestone в договоре

Читать: /blog/hongqi-hs5-iz-kitaya-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: opportunities_found=0 (corpus AS08/AS09/AS21; нет релевантных якорей)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «hongqi hs5 комплектации» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS21-… --site-base ${PUBLIC_SITE_URL}` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-name «Авто-Сейлс»; relative `/blog/<slug>/`).
- CLI workaround: `--blog-path` отсутствует в `excalibur_blog_llms_generator.py` (doctor FAIL / sanitizer wipe) → генерация без флага, `--site-base ""` для commit-safe relative URLs.
- Publish: not started by indexer.

## Publish status (2026-11-04)

- Live URL: **blocked** — SSH TCP/22 timeout; no permalink
- Ledger: `publish_blocked`
- Do not promote until live publish succeeds for this NEW slug only
