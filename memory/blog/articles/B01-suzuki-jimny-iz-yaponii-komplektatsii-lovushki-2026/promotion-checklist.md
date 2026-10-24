# Promotion checklist — B01 suzuki-jimny-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-24  
Live URL: https://avtosales125.ru/2026/10/24/suzuki-jimny-iz-yaponii-komplektatsii-lovushki-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (WP post 4507; HEAD 200)
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin; schema_meta=1 на post)
- [x] Проверить internal links из статьи (200) — link-verify pass pre-publish
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Ставка по Jimny — не лайк в объявлении

• Сначала код кузова: JB64/JB23 kei, JB74 Sierra, JC74 Nomade
• Потом лист: оценка → ремонт → пробег → карта A/U/W/C/X
• Для Jimny критичны C/S по низу и фото рамы — чеклист из 10 пунктов до денег

Читать: /blog/suzuki-jimny-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [ ] Локальный interlinker: 0 opportunities (AS08/AS09 без пересечения якорей с B01)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «сузуки джимни из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir …/B01-… --site-base ""` — 0 links applied (`opportunities_found=0`).
- llms.txt / llms-full.txt: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base "" --out-dir memory/blog` (без `--blog-path`; relative `/blog/<slug>/` для git-safe).
- Doctor mismatch: `excalibur_blog_doctor.py` всё ещё требует `--blog-path` → FAIL; см. incident queue.
