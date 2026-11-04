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

## 2026-11-05 — AS22 changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026

- **verdict:** FAIL / publish_blocked
- **blocker:** ❌ PUBLISH BLOCKER — SSH TCP/22 timeout (`ssh_tcp22_timeout` via SSH_HOST; DNS resolved; `SSH_HOST_IP` unset)
- **post_id:** none (NO LIVE write)
- **permalink:** none
- **featured_image / inline / schema_meta:** not attempted
- **preflight:** allow=yes; link-verify pass (catalog_ssl soft-pass); dry-run PASS (PHP ~6.39MB); slug not in denylist; paramiko 5.1.0 after pip
- **denylist:** untouched — no overwrite of LIVE 4758/4746/4740/3430/3394/4717/4711 or occupied model slugs
- **note:** same class as AS21 Hongqi HS5 / AS15 Arrizo 8 / AS10 GAC GS3; restore Cloud→WP SSH or verified SSH_HOST_IP before re-run
- **script note:** removed local `import re` shadow in `load_article` (UnboundLocalError on schema strip) so dry-run works
- **result:** `memory/blog/articles/AS22-changan-uni-k-iz-kitaya-komplektatsii-lovushki-2026/wp-publish-result.json`
- **incident:** `memory/pipeline-fix-queue.md#INC-20261105-2215-publish-ssh-tcp22-timeout-as22` ; `memory/pipeline-fix-queue.md#INC-20261105-2215-publish-load-article-re-shadow`
