# Cover concept — Авто-Сейлс

Единый визуальный язык обложек блога AVTO SALES.

Machine-readable: `cover-concept.json`  
Герой: `blog-hero.json`  
Референсы blueprint:

1. `assets/blog-hero-reference.png` — лицо героя (одежду менять под погоду и тему)
2. `assets/style-ref-cover-01.jpg` — стиль плашки/композиции
3. `assets/style-ref-cover-02.jpg` — доп. стиль

## Fixed

- `cover_family`, color_lock, composition 16:9
- Угол обложки: каталог `avto-sales125.ru` (не Telegram)
- Без кепки/капюшона у героя

## Variable

- Сцена из категорий blueprint (авторынок vs заказ, путь машины, радость получения, технологии vs реальность, метафоры)
- Короткий RU-заголовок на плашке под тему статьи

## Сборка промпта

```text
{global_prompt_prefix} + {topic_scene_descriptor} + {global_prompt_suffix}
+ hero prompt_fragment from blog-hero.json
```
