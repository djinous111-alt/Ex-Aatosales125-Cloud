# Research notes — AS09

**topic_id:** AS09  
**slug:** trust-encar-carhistory-proverka-do-depozita  
**H1:** Trust Encar и Carhistory: как проверить корейское авто до депозита  
**date_research:** 2026-07-17  
**utility_gate (topic):** PASS (how_to / mode B)  
**utility_verdict:** PASS

---

## Угол статьи (практический)

Не обзор бренда «Trust Encar» и не реклама чужого посредника. Практический гайд: **что проверить до любого депозита** при заказе авто из Кореи (Encar-лоты) через связку **диагностика/история на Encar + официальный Carhistory + живой осмотр**.

Важная семантика для копирайтера:

- В RU-выдаче «Trust Encar» часто ведёт на **российского посредника** `trust-encar.ru` (позиционирует себя как «официальный бренд Encar»). Это **не инструмент проверки**, а коммерческий канал.
- Инструменты проверки: карточка лота на **Encar.com** (Performance Check / схема кузова, Insurance History) + **Carhistory** (`carhistory.or.kr` / `carhistory.kr`) по VIN.
- Угол Авто-Сейлс: до депозита читатель умеет сам отсеять битые/утопленные/сомнительные лоты и понимает, зачем идти в каталог / Telegram за подбором под ключ (Владивосток).

**reader_outcome:** чеклист «не платить депозит, пока нет VIN + Carhistory + Performance Check + фото/видео осмотра»; список красных флагов; CTA на ${CATALOG_URL} и ${TELEGRAM_URL}. В тексте статьи **не** упоминать Wordstat и Метрику.

---

## SERP (WebSearch Cursor, 2026-07-17)

Приоритет: WebSearch Cursor. `research-serp.json` – доп. карта URL (часть сниппетов у «уток» перепутана между доменами; не копировать слепо).

### Primary / H1: проверка до депозита + Trust Encar + Carhistory

| # | Заголовок / угол | URL | Что в выдаче |
| --- | --- | --- | --- |
| 1 | Опыт заказа через Encar 2026 (vc.ru) | https://vc.ru/transport/2125149-kak-zakazat-avto-iz-korei | Требовать VIN-отчёт, Insurance History, аукционный лист, фото/видео **до покупки** |
| 2 | Проверка по VIN из Кореи 2026 | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei | Performance Check (X/W), Carhistory, пороги выплат в вонах, живой осмотр |
| 3 | Аукционный лист Encar: коды | https://1avtoyurist.ru/novosti/aukcionnyj-list-encar-kak-rasshifrovat-i-chto-znachat-kody.html | Лист = текущее состояние; Carhistory = прошлое; X/W на лонжеронах/стойках – стоп |
| 4 | Как проверить машину на Encar пошагово | https://carto-auto.ru/blog/guide-encar/ | Практический how-to по карточке лота |
| 5 | CarHistory + EncarData гайд | https://www.kmotors.shop/ru/blog/korean-car-history-check-guide | Связка двух баз; детективный тон |
| 6 | VIN на Encar – POWER Car | https://power-car.ru/articles/korean-car-vin-code-proverka-encar.html | Фокус на VIN/Carhistory |
| 7 | Сайт Trust Encar (посредник) | https://trust-encar.ru/ | Коммерческий каталог «официальный бренд»; не путать с проверкой |
| 8 | Официальный Carhistory | https://www.carhistory.or.kr/ ; https://www.carhistory.kr/ | Страховая история, flood free, fee отчёта |

**Пробел конкурентов:** много «как читать Encar» и «как проверить по VIN», мало жёсткого фрейма **«до депозита»** + разведения «Trust Encar (бренд посредника)» vs «инструменты проверки». Наш угол – stop-правила оплаты + чеклист Авто-Сейлс.

### Secondary

| Запрос | Ключевые URL | Вывод |
| --- | --- | --- |
| carhistory корея | carhistory.or.kr, korea-cars.com, avtoimport1.ru | Официальный сервис + агрегаторы проверки |
| проверка авто encar | carto-auto, altezza.team/encar-guide, encarrus VIN | Сильный how-to кластер |
| история авто корея | обзоры рынка 2026, меньше чистой «истории» | Спрос смещается в VIN/Carhistory |

### Конкурентный разрыв (для копирайтера)

1. Не копировать структуру vc.ru / top-autoimport 1:1.  
2. Явно: **депозит только после пакета проверок**.  
3. Развести Trust Encar (маркет/посредник в выдаче) и Encar + Carhistory (инструменты).  
4. Без сумм пошлин, цен лотов, выдуманных VIN; пороги выплат в вонах – как ориентиры осторожности, не как «гарантия».  
5. CTA: каталог + Telegram Авто-Сейлс (лимиты conversion-map).

---

## Яндекс Wordstat (MCP user-mcp-kv, `wordstat_get_top_requests`)

**Статус API:** OK для ключевых фраз (401 не было). Цифры только из ответа MCP. Дата съёма: 2026-07-17.  
Фраза «проверка авто encar» / «encar проверка» вернула усечённый ответ `{"totalCount":"5"}` без списка – точный топ по этой формулировке не зафиксирован.

### Сводная таблица спроса

| Фраза | Показы в месяц (как в ответе API) |
| --- | --- |
| trust encar | 579 |
| trust encar авто | 135 |
| trust encar корея | 101 |
| trust encar авто из кореи | 95 |
| сайт trust encar | 43 |
| trust encar официальный сайт | 42 |
| trust encar ru | 37 |
| trust encar отзывы | 23 |
| траст энкар (похожий) | 212 |
| carhistory | 105 |
| carhistory or kr | 47 |
| carhistory or kr на русском | 19 |
| проверка авто из кореи | 529 |
| проверка авто по вину корея | 237 |
| проверка авто по вин из кореи | 184 |
| проверка авто по вин коду корея | 134 |
| проверка авто из кореи бесплатно | 71 |
| проверка авто из кореи по vin | 63 |
| корея карс проверка авто | 60 |
| проверка пробега авто из кореи | 29 |
| история авто из кореи | 46 |
| история авто по вин корея | 16 |
| как проверить историю авто в корее | 5 |

Кластер «проверка авто корея» (сумма топа API): **813** показов по ответу «всего показов».

### LSI для копирайтера (из топов; не писать названия инструментов аналитики в статье)

- trust encar, авто из koreи, официальный сайт, отзывы  
- carhistory, carhistory.or.kr  
- проверка авто из koreи, проверка по VIN/вин, бесплатно, пробег  
- история авто из koreи  
- смежно в выдаче: Performance Check, Insurance History, аукционный лист, утопленник / flood, толщина ЛКП

---

## Факты с URL (для статьи; без выдуманных цен лотов)

| # | Факт | Источник |
| --- | --- | --- |
| 1 | Carhistory – сервис истории б/у авто в Корее на базе страховых данных; отчёт по VIN | https://www.carhistory.kr/search/carhistory/search.car?lang=en ; https://www.carhistory.or.kr/ |
| 2 | Стоимость полного Car History Report: **KRW 2,200** за запрос (включая VAT), по официальной странице поиска | https://www.carhistory.kr/search/carhistory/search.car?lang=en |
| 3 | История страховых ДТП ведётся с акцентом на данные **с 1996** | тот же URL Carhistory |
| 4 | Есть **бесплатная** проверка истории ущерба от затопления (Flood Damage History) по страховым записям | https://www.carhistory.kr/search/carhistory/freeSearch.car?lang=en ; https://www.carhistory.or.kr/main.car?lang=en |
| 5 | Официальный disclaimer: случаи **без обращения в страховую** / без покрытия могут **не отображаться**; отчёт – вспомогательная информация | freeSearch + sample guide Carhistory |
| 6 | На Encar у лота есть диагностическая карта (Performance Check): схема кузова; пометки **X** (замена) и **W** на силовых элементах – типичный стоп-сигнал у практиков | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei ; https://1avtoyurist.ru/novosti/aukcionnyj-list-encar-kak-rasshifrovat-i-chto-znachat-kody.html |
| 7 | Аукционный лист / Performance Check показывает **текущее** состояние; Carhistory – **прошлое** (владельцы, страховые выплаты, ДТП по страховке) | https://1avtoyurist.ru/novosti/aukcionnyj-list-encar-kak-rasshifrovat-i-chto-znachat-kody.html |
| 8 | Практики советуют до оплаты: VIN обязателен; Performance Check; Carhistory (крупные выплаты / такси / утопленник); затем живой осмотр (толщиномер, болты, мотор) | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei |
| 9 | Ориентиры выплат в отчётах (в вонах, у импортёров): до ~0.5 млн – мелочь; 0.5–2 млн – средний риск; **>3 млн** – красный флаг (нужен осмотр). Это эвристика блогов, не закон | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei |
| 10 | В карточке Encar отдельно смотрят страховую историю (Insurance History) и дату производства (важна для таможни) | https://teletype.in/@vezemavto/B2hgUEkytih ; https://vc.ru/transport/2125149-kak-zakazat-avto-iz-korei |
| 11 | Надёжный посредник/подборщик даёт отчёты, фото и видео осмотра **до** выкупа; без пакета документов покупать рискованно | https://vc.ru/transport/2125149-kak-zakazat-avto-iz-korei |
| 12 | `trust-encar.ru` позиционирует себя как «официальный бренд Encar в России» и каталог под заказ – коммерческий канал, не замена Carhistory | https://trust-encar.ru/ |
| 13 | Авто-Сейлс: привоз из Кореи (и JP/CN) под заказ; каталог ${CATALOG_URL} ; Telegram ${TELEGRAM_URL} ; офис Владивосток, Днепровская 40а стр. 4 | memory/brief/fact-bank.md, site-brief.md, conversion-map.md |
| 14 | Кластер спроса «проверка авто из koreи» – 529 показов/мес; «trust encar» – 579; «carhistory» – 105 (внутренние цифры research, не для текста статьи) | MCP wordstat_get_top_requests, 2026-07-17 |
| 15 | Корейские VIN (часто с префиксом K…) проверяют через Carhistory / данные Encar; полная картина = несколько источников, не один скрин | https://www.carspy.io/ru/journal/check-car-by-vin-code-complete-guide-2026 + Carhistory |

**Не использовать в статье без перепроверки:** чужие «средние чеки», фиксированные суммы доставки/пошлин, гарантии «чистой истории» только по одному отчёту, чужие номера лотов/VIN из примеров конкурентов.

---

## action_outline (8 шагов)

1. Зафиксировать лот: ссылка Encar, модель/год, заявленный пробег, цена в вонах – и **потребовать полный VIN** (нет VIN – нет разговора о депозите).  
2. Открыть Performance Check / схему кузова на карточке: искать **X/W** на лонжеронах, стойках, панелях каркаса; силовые повреждения – отказ или жёсткий дисконт только после осмотра.  
3. Сверить Insurance History на Encar (даты, выплаты «своему» / «чужому» авто) с заявленным пробегом и числом владельцев.  
4. Пробить VIN в **Carhistory** (платный отчёт) + бесплатный **flood**; помнить: без страховки ДТП может не быть в базе.  
5. Оценить красные флаги отчёта: крупные выплаты, total loss, кража, коммерческое использование/такси (если видно), скачки пробега.  
6. Заказать **живой осмотр** в Корее (фото/видео, толщиномер, следы перекраса, работа ДВС) – до любого депозита.  
7. Свести пакет: VIN + Carhistory + Performance Check + осмотр; только после этого обсуждать бронь/депозит и логистику через Владивосток.  
8. Если нет времени/доступа к базам – уйти в каталог ${CATALOG_URL} или Telegram ${TELEGRAM_URL} за проверкой и подбором до оплаты (без форм на странице статьи).

---

## reader_outcome

Читатель получает стоп-правила депозита и пошаговый чеклист проверки корейского лота (Encar + Carhistory + осмотр), понимает лимиты страховой истории и знает, куда обратиться за проверкой/подбором у Авто-Сейлс.

---

## CTA / conversion (из conversion-map)

- Каталог: ${CATALOG_URL} (до 3 упоминаний)  
- Telegram: ${TELEGRAM_URL} (до 2)  
- Без лид-форм и без калькулятора пошлин на странице  
- В тексте статьи не упоминать Wordstat / Метрику

---

## utility_verdict

**PASS** – intent how_to, mode B, практический угол «до депозита» + action_outline 8 шагов + измеримый reader_outcome; Wordstat и WebSearch выполнены; источники с URL собраны.
