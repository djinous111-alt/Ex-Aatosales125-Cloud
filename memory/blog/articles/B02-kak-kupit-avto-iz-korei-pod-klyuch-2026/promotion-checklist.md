# Promotion checklist — B02 kak-kupit-avto-iz-korei-pod-klyuch-2026

Дата публикации: 2026-10-03  
Live URL: https://avtosales125.ru/2026/10/03/kak-kupit-avto-iz-korei-pod-klyuch-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (WP post 3967; HEAD 200)
- [x] View source — JSON-LD BlogPosting (AIOSEO); custom FAQPage/HowTo в post meta `_excalibur_blog_schema_jsonld` (theme echo отдельно)
- [x] Проверить internal links из статьи (200), в т.ч. `/trust-encar-carhistory-proverka-do-depozita/`
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Цена Encar — ещё не «под ключ»

• Смета по строкам до любого депозита
• Encar + Carhistory + осмотр до оплаты
• Море → таможня → СБКТС/ЭПТС во Владивостоке (ориентир 30–55 дней)

Читать: [LIVE_URL]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Writer уже поставил internal link B02 → `/trust-encar-carhistory-proverka-do-depozita/`
- [x] Interlinker `--apply`: 0 новых opportunities (3 articles in memory; suggestions empty)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как купить авто из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir memory/blog/articles/B02-kak-kupit-avto-iz-korei-pod-klyuch-2026 --site-base $PUBLIC_SITE_URL` → 0 opportunities; report `memory/blog/interlink-suggestions.json`.
- llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (без `--blog-path`; CLI его не принимает) → `memory/blog/llms.txt`, `memory/blog/llms-full.txt`; B02 в индексе.
- Cover+Schema PASS до indexer; publish — следующий шаг.
