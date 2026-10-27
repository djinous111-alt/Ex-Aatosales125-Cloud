# Conversion map — Excalibur BLOG (Авто-Сейлс)

## CTA URL lifecycle (secret-scan safe)

1. **Authoring source of truth:** Cloud Secrets / env — `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`.
2. **В `article.html` пиши плейсхолдеры**, не живые secret URL и не выдуманные хосты:
   - `href="${CATALOG_URL}"`
   - `href="${TELEGRAM_URL}"`
   - `href="${MAX_URL}"`
3. **Публичные URL** (2GIS, Instagram) — обычные литералы, их можно коммитить.
4. **Перед commit / после QA:** если href уже развернули из env, верни плейсхолдеры:
   ```bash
   python3 scripts/excalibur_blog_cta_hrefs.py --article-html <article_dir>/article.html --redact --write
   ```
5. **QA / link-verify** могут временно expand:
   ```bash
   python3 scripts/excalibur_blog_cta_hrefs.py --article-html <article_dir>/article.html --expand --write
   ```
   После проверки снова `--redact --write`.
6. **Publish** сам expand'ит плейсхолдеры / legacy `href="[REDACTED]"` в WP payload из env (файл на диске не обязан содержать секреты).
7. Legacy `href="[REDACTED]"` допустим (AS08/AS09); предпочитай `${CATALOG_URL}` / `${TELEGRAM_URL}` / `${MAX_URL}`.
8. **Запрещено:** выдумывать хосты каталога/Telegram; коммитить живые значения secret URL.

| CTA | URL / action | Max mentions per article | Notes |
| --- | --- | --- | --- |
| Каталог авто | `${CATALOG_URL}` | 3 | главный оффер; расчёты и подбор только здесь |
| Telegram avtosales125 | `${TELEGRAM_URL}` | 2 | детали заказа, ответы менеджера |
| MAX | `${MAX_URL}` | 1 | альтернативный мессенджер |
| Отзывы 2GIS | https://2gis.ru/vladivostok/search/авто%20сейлс%20владивосток/firm/70000001090415417/131.924668%2C43.140033/tab/reviews | 1 | доверие / E-E-A-T |
| Instagram | https://www.instagram.com/avtosales_rf | 1 | опционально, если релевантно |
| Адрес офиса | Владивосток, Днепровская 40а стр. 4 | 1 | в футере/блоке компании, не как CTA-кнопка |
