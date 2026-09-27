# Promotion checklist — AS10 tank-300-iz-kitaya-ramnik-ili-krossover-2026

Дата публикации: 2026-09-27 (pending WP publish)  
Live URL: (pending) /blog/tank-300-iz-kitaya-ramnik-ili-krossover-2026/

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
Депозит за красивый скрин? Сначала рамник или кроссовер

• Tank 300 – рамник (клиренс 224 мм, прицеп до 2500 кг), не «красивый кроссовер»
• Типичный мотор РФ ~220 л.с. – выше порога льготного утильсбора (≤160 л.с. и ≤3 л)
• Депозит – только после VIN и комплектации в договоре

Читать: (после publish вставить live URL)
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [ ] Локальный interlinker: 0 opportunities (в memory 3 статьи; AS10 тематически не пересекается с AS08/AS09 по якорям)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «tank 300 из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …AS10… --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir` + `--out-dir`; без `--blog-path`).
- Publish: ещё не выполнен (Indexer only).
