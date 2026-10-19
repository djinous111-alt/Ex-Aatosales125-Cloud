# Conversion map — Excalibur BLOG (Авто-Сейлс)


| CTA | URL / action | Max mentions per article | Notes |
| --- | --- | --- | --- |
| Каталог авто | https://avto-sales125.ru/ | 3 | главный оффер; расчёты и подбор только здесь |
| Telegram avtosales125 | https://t.me/avtosales125 | 2 | детали заказа, ответы менеджера |
| MAX | https://max.ru/id2508140890_biz | 1 | альтернативный мессенджер |
| Отзывы 2GIS | https://2gis.ru/vladivostok/search/авто%20сейлс%20владивосток/firm/70000001090415417/131.924668%2C43.140033/tab/reviews | 1 | доверие / E-E-A-T |
| Instagram | https://www.instagram.com/avtosales_rf | 1 | опционально, если релевантно |
| Адрес офиса | Владивосток, Днепровская 40а стр. 4 | 1 | в футере/блоке компании, не как CTA-кнопка |

## Env-backed CTA (Cloud)

Live hrefs for catalog / Telegram / MAX / site base come from env `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL`, `PUBLIC_SITE_URL`. Committed map may show `[REDACTED]`; Writer must resolve env at article time. Never commit `href="[REDACTED]"` in article.html.
Pre-commit: public CTA env names may be injected as secrets — use `scripts/excalibur_blog_filter_commit_secret_env.sh` / `scripts/excalibur_git.sh`.
