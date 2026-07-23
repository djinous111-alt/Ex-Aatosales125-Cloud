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

## 2026-07-24 — B01 avto-iz-yaponii-pod-zakaz-2026

- **verdict:** PASS
- **post_id:** 3672
- **permalink:** https://avtosales125.ru/2026/07/24/avto-iz-yaponii-pod-zakaz-2026/
- **featured_image:** 3692
- **inline_images:** 3693 (`inline-01`), 3696 (`inline-02`), 3698 (`inline-03`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld` len=13002; FAQPage+HowTo+BlogPosting; skip_theme_faq=1)
- **live_HEAD:** 200
- **method:** SSH upload (SSH_ROOT fallback to `.`) + HTTP trigger → nginx **504** @ ~120s; PHP completed server-side; Cloud WebFetch/curl fallback reconstructed from live WP REST after confirm
- **note:** payload ~9.1MB (base64 cover+inlines); CLI `php` on host is 5.6 (cannot run WP); web PHP-FPM OK. Duplicate media from retries (cover-1..4) — live uses cover-4 / inline-*-3/4.
- **result:** `memory/blog/articles/B01-avto-iz-yaponii-pod-zakaz-2026/wp-publish-result.json`

