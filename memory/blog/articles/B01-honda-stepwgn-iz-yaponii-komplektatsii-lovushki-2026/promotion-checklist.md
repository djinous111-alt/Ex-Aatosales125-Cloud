# Promotion checklist — B01 honda-stepwgn-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-24 (planned; pre-publish)  
Live URL: /blog/honda-stepwgn-iz-yaponii-komplektatsii-lovushki-2026/

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
Балл 4.5 не спасает: Spada с сюрпризом до ставки?

• Spada — trim, не «другой мотор»; на 5G RP3/4, на 6G снова пакет
• До ставки: код кузова одним предложением + ★★ у пробега и двери
• Waku Waku была только у 5G — на 6G калитки нет

Читать: /blog/honda-stepwgn-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 без пересечения ключей B01; apply no-op)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать honda stepwgn из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir … --site-base ""` → 0 links.
- llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base "" --out-dir memory/blog` (без `--blog-path`).
- llms.txt / llms-full.txt: B01 indexed with relative `/blog/...` URLs.
