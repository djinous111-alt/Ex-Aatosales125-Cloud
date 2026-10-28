# Promotion checklist — B01 toyota-crown-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-28  
Live URL: https://avtosales125.ru/2026/10/28/toyota-crown-iz-yaponii-komplektatsii-lovushki-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL (HEAD 200 + REST id=4639) — title, excerpt, featured image, FAQ
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
Красивый Sport RS — а это уже PHEV?

• Сначала кузов Crown (Crossover/Sport/Sedan/Estate) — потом ставка
• Буквы G/Z/RS ≠ один и тот же гибрид: Sport/Estate RS часто PHEV
• Стоп-флаги листа R/RA — до депозита

Читать: https://avtosales125.ru/2026/10/28/toyota-crown-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (3 articles in memory; no hub-spoke match for Crown ↔ AS08/AS09)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «тойота краун из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir …/B01-… --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (без `--blog-path`; CLI его не принимает).
- `memory/blog/llms.txt` + `memory/blog/llms-full.txt` содержат B01 Crown.
- Publish: PASS post_id=4639; featured=4640; inline=[4641, 4642, 4643]; HEAD 200.
