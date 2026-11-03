# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-11-03 (ожидает publish)  
Live URL: /blog/encar-na-russkom-kak-chitat/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200), в т.ч. `/blog/trust-encar-carhistory-proverka-do-depozita/`
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Официальной русской версии encar.com нет — а «2450» часто = 24,5 млн вон

• Перевод браузера на encar.com, не на первом «красивом» клоне
• 만원 × 10 000; 무사고 ≠ идеальный кузов (смотрите X/W)
• Чистый CarHistory / Diagnosis — не замена осмотру до депозита

Читать: /blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: AS02 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`, якорь «Trust Encar»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir ... --site-base ${PUBLIC_SITE_URL}` — opportunities=1, applied=1 (AS02→AS09).
- llms generator: CLI only `--blog-dir` (no `--blog-path`; cite INC-20261103-0906-director-llms-blog-path). Committed `memory/blog/llms.txt` + `llms-full.txt` with relative `/blog/...` paths (3 articles, AS02 included).
- Publish: not started by indexer.
