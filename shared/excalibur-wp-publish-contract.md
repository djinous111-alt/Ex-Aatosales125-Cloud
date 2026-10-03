# Excalibur BLOG — WordPress publish contract

Excalibur BLOG готовит артефакты локально; публикация — через `scripts/excalibur_blog_wp_publish.py` и FTP bootstrap.

## Prerequisites

- `article.html`, `article.meta.json`, `article-qa.md` (verdict PASS)
- `schema.jsonld`
- `cover/cover.png` + `cover-registry.json` (alt)
- `link-verify.json` (verdict pass)
- `memory/site.env.local` — FTP + `FTP_ROOT` (корень WP, где `wp-load.php`) + `PUBLIC_SITE_URL` + `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`

## Скрипт

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/B01-slug/article.html \
  -o memory/blog/articles/B01-slug/link-verify.json \
  --site-base https://avtosales125.ru

python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/B01-slug
```

`--dry-run` — проверка payload без upload (уже с expand CTA placeholders).


## CTA placeholders (обязательно)

В git-tracked `article.html` / `schema.jsonld` допустимы только токены:

- `[CATALOG_URL]` / `<CATALOG_URL>`
- `[TELEGRAM_URL]` / `<TELEGRAM_URL>`
- `[REDACTED]` для host/page URL в schema

`excalibur_blog_wp_publish.py` читает `CATALOG_URL` / `TELEGRAM_URL` / `PUBLIC_SITE_URL` из env, расширяет payload **в памяти** и **абортит**, если остались нерезолвленные `[A-Z_]+_URL`. Значения secrets обратно в git не пишутся.

`excalibur_blog_link_verify.py` резолвит те же токены из env для HTTP-проверки и маскирует URL в `link-verify.json`.

## Что делает publish

1. Expand CTA/host placeholders из env (не трогая файлы на диске)
2. `wp_insert_post` / `wp_update_post` — title, slug, content, excerpt
3. Featured image из `cover/cover.png` + alt
4. **Inline images** — все локальные `<img src="cover/...">` загружаются в Media Library, `src` заменяется на WP URL
5. Post meta `_excalibur_blog_schema_jsonld` — JSON-LD для `single.php`
6. Post meta `_excalibur_blog_skip_theme_faq` = `1` — сигнал теме **не** добавлять глобальный FAQ-блок

## Дубли FAQ на live-странице (важно)

Excalibur кладёт в `post_content` **один** FAQ по теме (`<h2>Частые вопросы</h2>`).

Тема WordPress на avtosales125.ru может **дописывать** после контента глобальные блоки темы — это **не** часть `article.html`. Тематический FAQ пишет только Excalibur Writer.

**Исправление в теме WordPress** (`single.php` или фильтр `the_content`):

```php
$skip_theme_faq = get_post_meta(get_the_ID(), '_excalibur_blog_skip_theme_faq', true);
if ($skip_theme_faq === '1') {
    // не выводить глобальный FAQ-блок темы для постов Excalibur BLOG
}
```

Publish-скрипт выставляет meta `_excalibur_blog_skip_theme_faq` автоматически при каждой публикации.

## Артефакты после publish

```text
memory/blog/articles/<topic_id>-<slug>/wp-publish-result.json
memory/blog/wp-publish-log.md
```

## Schema в теме WP

```php
$schema = get_post_meta(get_the_ID(), '_excalibur_blog_schema_jsonld', true);
if ($schema) {
    echo '<script type="application/ld+json">' . wp_kses_post($schema) . '</script>';
}
```

## Blockers

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет credentials
- Production HTML не должен содержать MCP URLs — только WP media для featured image

Skill: `skills/publish-excalibur-blog/SKILL.md` (alias: `skills/excalibur-wp-publish/SKILL.md`)
