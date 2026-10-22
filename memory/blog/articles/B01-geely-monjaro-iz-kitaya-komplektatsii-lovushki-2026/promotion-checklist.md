# Promotion checklist — B01 geely-monjaro-iz-kitaya-komplektatsii-lovushki-2026

Дата публикации: 2026-10-22 (pending WP publish)  
Live URL: /blog/geely-monjaro-iz-kitaya-komplektatsii-lovushki-2026/

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
Депозит за «Flagship 4WD» — а в спецификации FWD?

• 8 версий CN-линейки 2026; AWD — не бонус объявления
• До оплаты: задача поездок → ветка → кВт → смета по строкам
• Льготный утиль на практике не «подарок»

Читать: /blog/geely-monjaro-iz-kitaya-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (corpus=3: AS08, AS09, B01; exact keyword match)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «джили монжаро из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-geely-monjaro-iz-kitaya-komplektatsii-lovushki-2026 --site-base [REDACTED]` — 0 links.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (B01 listed; URLs relative `/blog/<slug>/`).
- CLI llms: `--blog-dir` + `--site-base` + `--out-dir` — без `--blog-path` (флаг отсутствует в скрипте; doctor всё ещё FAIL).
- Publish: not run (Indexer only).
