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

## 2026-10-16 — B01 dostavka-avto-iz-vladivostoka-zd-avtovoz-2026

- **verdict:** PASS
- **post_id:** 4233
- **permalink:** [REDACTED]/2026/10/16/dostavka-avto-iz-vladivostoka-zd-avtovoz-2026/
- **featured_image:** 4240
- **inline_images:** 4241 (`inline-01.png`), 4242 (`inline-02.png`), 4243 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`, FAQPage+HowTo+BlogPosting; meta_len≈9779)
- **skip_theme_faq_meta:** ok (`_excalibur_blog_skip_theme_faq=1`)
- **HEAD:** 200
- **method:** SSH upload (`SSH_ROOT=.`) + HTTP trigger timeout → curl fallback got nginx 504; success reconstructed via WP REST slug + SSH meta-check
- **denylist:** NEW post 4233 — do not confuse with 4227/4221/4209/4203/4197/4174/3843/4162/3707
- **note:** first partial run left orphan media 4234–4237; live content uses 4241–4243; theme RankMath JSON-LD on page differs from stored Excalibur meta
- **result:** `memory/blog/articles/B01-dostavka-avto-iz-vladivostoka-zd-avtovoz-2026/wp-publish-result.json`
