# Promotion checklist — AS14 jaecoo-j7-iz-kitaya-komplektatsii-lovushki-2026

Дата публикации: 2026-11-02 (planned; pre-publish)  
Live URL: /blog/jaecoo-j7-iz-kitaya-komplektatsii-lovushki-2026/

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
Депозит за «J7 Престиж» без VIN — лотерея

• Explore 06 / Tansuo 06 = Jaecoo J7
• Сначала привод 2WD 150 или 4WD 186 и trim Актив/Комфорт/Престиж
• Деньги — только после договора, сметы и VIN

Читать: /blog/jaecoo-j7-iz-kitaya-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 новых opportunities (каталог memory/blog/articles = 3 статьи)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать jaecoo j7 из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …AS14…` — opportunities_found=0.
- llms.txt / llms-full.txt: `memory/blog/` с relative URLs `/blog/<slug>/` (workaround: `--site-base ""`; `--blog-path` / `--relative-urls` aliases missing).
- Publish: next step (yes).
