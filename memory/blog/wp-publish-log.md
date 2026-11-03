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

## 2026-11-04 — AS10 kak-vybrat-toyota-sienta-iz-yaponii-2026

- **verdict:** FAIL / PUBLISH BLOCKER
- **post_id:** none (no LIVE write)
- **permalink:** none
- **featured_image:** none
- **inline_images:** none
- **schema_meta:** not applied
- **preflight:** env-check allow=true; link-verify pass (catalog soft_pass=catalog_ssl); dry-run PHP ~8.18MB; slug target NEW only
- **blocker:** SSH TCP/22 timeout on DNS hostname, resolved A, and documented public-site IP; `SSH_HOST_IP` secret unset; WP REST SSL handshake timeout from Cloud egress
- **denylist untouched:** 4758 / 4746 / 4740 / 3430 / 3394 / 4717 / 4711 (incl. historical Haval M6 AS10 id 4711)
- **result:** `memory/blog/articles/AS10-kak-vybrat-toyota-sienta-iz-yaponii-2026/wp-publish-result.json`
- **incident:** `memory/pipeline-fix-queue.md#INC-20261103-2208-publish-ssh-tcp22-timeout-as10-sienta`
- **next:** restore Beget SSH TCP/22 or verified `SSH_HOST_IP`, then publish ONLY slug `kak-vybrat-toyota-sienta-iz-yaponii-2026`
