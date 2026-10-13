# WP publish log — Авто-Сейлс

Сайт: https://[REDACTED]/
FTP/SFTP: djinoum7.beget.tech → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** https://[REDACTED]/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
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
- **permalink:** https://[REDACTED]/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-10-13 — B01 rastamozhka-avto-iz-korei-2026

- **verdict:** PASS
- **post_id:** 3505
- **permalink:** [REDACTED]/2026/07/19/rastamozhka-avto-iz-korei-2026/
- **featured_image:** 4145
- **inline_images:** 4146 (`inline-01.png`), 4147 (`inline-02.png`), 4148 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok (`_excalibur_blog_skip_theme_faq=1`)
- **method:** SSH upload + HTTP trigger OK (~157s; no 504 / no WebFetch fallback this run)
- **note:** slug new vs akkreditiv/VIN; WP found existing post-by-path from 2026-07-19 → `wp_update_post` (id 3505); media ids new 4145–4148; live HEAD 200; content verified (ПТД/СВХ/Encar/FAQ/inline)
- **preflight:** link-verify soft-pass brand catalog HTTP 503; telegram 200; `paramiko` installed; `memory/site.env.local` generated with `SSH_ROOT=.`
- **result:** `memory/blog/articles/B01-rastamozhka-avto-iz-korei-2026/wp-publish-result.json`
