# Promotion checklist — B03 avto-iz-kitaya-pod-zakaz-2026

Дата публикации: 2026-07-23  
Live URL: https://avtosales125.ru/2026/07/23/avto-iz-kitaya-pod-zakaz-2026/

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
Красивая цена из чата ≠ под ключ

• До депозита: мощность (~160 л.с.), возраст, топливо
• Договор с юрлицом + разбивка статей «под ключ»
• Хаб выдачи — Владивосток; карта физлица = стоп

Читать: https://avtosales125.ru/2026/07/23/avto-iz-kitaya-pod-zakaz-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (3 articles in memory; no keyword overlap for B03)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «авто из китая под заказ» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir memory/blog/articles/B03-avto-iz-kitaya-pod-zakaz-2026 --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir` (без устаревшего `--blog-path`; doctor check всё ещё ждёт `--blog-path`).
- Publish PASS: post_id=3660; Live URL set.
