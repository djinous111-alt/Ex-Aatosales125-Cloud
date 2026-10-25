# WP publish log — Авто-Сейлс

Сайт: https://avtosales125.ru/
FTP/SFTP: djinoum7.beget.tech → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** https://avtosales125.ru/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
- **featured_image:** 3349
- **inline_images:** 3351 (`inline-01.png`), 3355 (`inline-02.png`), 3358 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch timeout; curl `--max-time 300` OK)
- **note:** в `article.meta.json` добавлены `title`/`h1`/`description`/`cover_alt` для payload; `FTP_ROOT` исправлен на `/`
- **result:** `memory/blog/articles/AS08-samye-komfortnye-avto-myagkaya-podveska-2026/wp-publish-result.json`

## 2026-07-17 — AS09 trust-encar-carhistory-proverka-do-depozita

- **verdict:** PASS
- **post_id:** 3364
- **permalink:** https://avtosales125.ru/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-10-25 — B01 toyota-corolla-iz-yaponii-komplektatsii-lovushki-2026

- **verdict:** PASS (reconstructed)
- **post_id:** 4525
- **permalink:** /2026/10/25/toyota-corolla-iz-yaponii-komplektatsii-lovushki-2026/
- **featured_image:** 4531
- **inline_images:** 4532 (`inline-01-1.png`), 4534 (`inline-02-1.png`), 4535 (`inline-03-1.png`)
- **schema_meta:** ok (len=11955, BlogPosting+FAQPage, env expanded live)
- **skip_theme_faq_meta:** ok (`1`)
- **method:** SSH (`SSH_ROOT=.`) upload OK (~6.75MB) → HTTP RemoteDisconnected → FALLBACK curl nginx 504 → REST+meta-check reconstruct (**no republish**)
- **foreign_guard:** Honda Fit 4513 untouched; denylist not rewritten
- **orphans:** media 4526–4529 from overlapping first HTTP attempt; content points at *-1.png IDs
- **result:** `memory/blog/articles/B01-toyota-corolla-iz-yaponii-komplektatsii-lovushki-2026/wp-publish-result.json`
- **incident:** INC-20261025-1001-publish-http-fallback-504-reconstruct
