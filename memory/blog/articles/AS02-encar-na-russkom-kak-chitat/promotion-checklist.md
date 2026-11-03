# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-11-03  
Live URL: /blog/encar-na-russkom-kak-chitat/

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
Официальной полной русской версии encar.com нет

• Перевод браузера + пять полей карточки до «цены под ключ»
• 만원 × 10 000 = воны; X/W на силовых = стоп до депозита
• «Без ДТП» ≠ идеальный кузов

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

- Indexer: interlinker `--apply --article-dir …/AS02-encar-na-russkom-kak-chitat` — 1 link applied (AS02→AS09).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles; relative `/blog/...`; CLI `--blog-dir`, без `--blog-path`).
- ready_for_publish=yes; publish выполняет Директор, не Indexer.
