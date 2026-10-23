# Promotion checklist — B01 hyundai-sonata-iz-korei-komplektatsii-lovushki-2026

Дата публикации: 2026-10-23 (pending publish)  
Live URL: ${PUBLIC_SITE_URL}/blog/hyundai-sonata-iz-korei-komplektatsii-lovushki-2026/

Excalibur создаёт этот файл после Indexer (до WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200), в т.ч. Trust Encar → AS09
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
До депозита за Sonata из Кореи сверьте мощность, газ и trim — иначе ловушка в утильсборе.

• фильтр ≤160 л.с. до выбора лота
• LPi заводской ≠ rental/taxi
• trim только по фото салона Encar

Читать: ${PUBLIC_SITE_URL}/blog/hyundai-sonata-iz-korei-komplektatsii-lovushki-2026/
```

## Перелинковка

- [x] Interlinker --apply: 1 link B01 → AS09 (Trust Encar)
- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «соната из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer 2026-10-23: interlink count=1; llms.txt + llms-full.txt regenerated (3 articles).
- GEO QA PASS score 87; cover+schema ready. Publish next.
- Doctor false FAIL: expects `--blog-path` on llms generator; CLI has only `--blog-dir`/`--out-dir` — see INC-20261023-1326-indexer-doctor-llms-blog-path.
