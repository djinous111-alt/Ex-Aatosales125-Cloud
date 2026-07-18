# Research notes — AS02

research_date: 2026-07-18
accessed_at: 2026-07-18
utility_verdict: PASS

reader_outcome: новичок открывает карточку лота на Encar (через переводчик), проходит чеклист «что смотреть первым», узнаёт красные флаги X/W и страховой истории и понимает, когда остановиться и отдать проверку подборщику Авто-Сейлс
reader_pain: сайт Encar на корейском выглядит как иероглифы; человек боится купить «кота в мешке» – не понимает, где пробег, где битость, где Trust/диагностика, и путает русский зеркальный каталог с реальной проверкой лота
success_criteria: читатель может сам по ссылке лота назвать 5 полей карточки, открыть Performance Check / схему кузова, отличить замену панели (X) от шпаклёвки (W) на силовых элементах и сказать «беру / не беру / нужен осмотр» до любого депозита
voice_angle: «ты не обязан выучить корейский – тебе нужен короткий ритуал чтения карточки, как инструкция к стиральной машине, а не курс для дилеров»
reader_story: человек нашёл на русском «зеркале» красивый Kia/Hyundai с «честными 40 тыс. км», нажал «хочу», а потом в живой карточке Encar увидел красные X на стойках или Rent в истории – и понял, что почти отправил депозит за такси с подкрученным одометром
surprising_fact: у Encar нет полноценного официального русского интерфейса – «Encar на русском» в выдаче чаще ведёт на зеркала посредников; при этом полная страховая история на самом Encar часто доступна только залогиненным с корейским номером, а диагностическая схема кузова (X/W) лежит в открытом Performance Check и её многие просто не открывают

## research_questions
1. Что именно смотреть в карточке Encar в первые 5 минут (поля, фото, тип продажи)?
2. Как читать Performance Check / схему кузова: что значат X и W, где «стоп»?
3. Чем дополняют Trust/Encar Diagnostic и Carhistory, и почему одного скрина мало?
4. Какие красные флаги по пробегу, коммерческому использованию и страховым выплатам?
5. Когда новичку лучше остановиться и отдать проверку подборщику (Авто-Сейлс, Владивосток)?

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Teletype: как выбрать б/у через Encar (фильтры, X/W, страховая) | https://teletype.in/@vezemavto/B2hgUEkytih | accessed_at: 2026-07-18 | Практический how-to: переводчик, фильтры, View Performance Record, коды X/W |
| Teletype: инструкция по подбору через Encar | https://teletype.in/@rolker_auto/podborKoreaEncar | accessed_at: 2026-07-18 | Дубли объявлений, VIN в Performance Record, схема навесных vs силовых |
| WESTMOTORS: гайд по карточке Encar (EN) | https://westmotors.ae/auctions-korea/encar | accessed_at: 2026-07-18 | Структура карточки, 3 вкладки отчёта, логин для полной insurance history, порог расхождения пробега 5–10% |
| top-autoimport: проверка по VIN 2026 | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei | accessed_at: 2026-07-18 | Красные флаги VIN/Rent/выплаты >3 млн вон; чеклист до покупки |
| 1avtoyurist: коды аукционного листа Encar | https://1avtoyurist.ru/novosti/aukcionnyj-list-encar-kak-rasshifrovat-i-chto-znachat-kody.html | accessed_at: 2026-07-18 | X/W на лонжеронах и стойках = главные стоп-сигналы; лист ≠ Carhistory |
| Официальная страница Encar Diagnostic | https://car.encar.com/diagnosis/intro | accessed_at: 2026-07-18 | Официальные уровни диагностики (진단 / + / ++), гарантия диагностики Encar |
| Официальные грейды диагностики Encar | https://car.encar.com/diagnosis/grade?active=p0 | accessed_at: 2026-07-18 | Что входит в Diagnostic / Diagnostic+ / Diagnostic++ |
| AIM Group: запуск Encar Diagnostic++ (2025-07-24) | https://aimgroup.com/2025/07/24/encar-com-launches-advanced-vehicle-certification-service-encar-diagnostic/ | accessed_at: 2026-07-18 | Свежий сигнал: углублённая сертификация на площадке (после 2026-04-19 окно свежести для смежных обновлений рынка) |
| Carapis docs: что вытаскивают из лота Encar | https://docs.carapis.com/parsers/encar.com/intro | accessed_at: 2026-07-18 | Независимый техсигнал: inspection sheet + accident/mileage как ключевые поля лота |
| YouTube: как открыть Performance Check | https://www.youtube.com/watch?v=xnRE7Dj3n6c | accessed_at: 2026-07-18 | Community: X = exchange, W = weld/work; смотреть утечки ДВС/КПП |
| vc.ru: опыт заказа через Encar 2026 | https://vc.ru/transport/2125149-kak-zakazat-avto-iz-korei | accessed_at: 2026-07-18 | Конкурент в SERP «encar на русском 2026»; акцент на проверках до покупки |
| Fact-bank Авто-Сейлс | memory/brief/fact-bank.md | accessed_at: 2026-07-18 | NAP, каталог/Telegram CTA, запрет калькуляторов пошлин |

## wordstat

Источник: MCP-KV `wordstat_get_top_requests`, регион 225 (Россия), дата съёма 2026-07-18. Цифры только из ответа API. В тексте статьи для читателя Wordstat/Метрику не упоминать.

| phrase | impressions |
| --- | --- |
| encar | 31035 |
| encar com | 8278 |
| сайт encar | 3165 |
| encar официальный | 2631 |
| encar на русском | 1886 |
| encar корея | 1722 |
| encar авто | 1454 |
| encar com на русском | 1161 |
| сайт encar com | 1104 |
| encar com официальный | 947 |
| encar авто из кореи | 782 |
| сайт encar на русском | 702 |
| trust encar | 569 |
| encar на русском языке | 543 |
| encar на русском официальный | 449 |
| encar корея на русском | 441 |
| encar на русском официальный сайт | 436 |
| encar com на русском сайт | 415 |
| проверка авто из кореи | 526 |
| проверка авто по вину корея | 233 |
| проверка авто по вин из кореи | 177 |
| проверка авто из кореи по вин коду | 120 |
| проверка авто из кореи бесплатно | 70 |
| проверка авто из кореи по vin | 66 |
| проверка пробега авто из кореи | 33 |
| trust encar авто | 127 |
| trust encar корея | 97 |
| trust encar авто из кореи | 89 |
| сайт trust encar | 43 |

Кластеры «всего показов» по ответу API: `encar на русском` = 1886; `проверка авто корея` = 812; `trust encar` = 569; база `encar` = 31035.

⚠️ Примечание research (не auth): фразы `как читать encar` и `читать encar` вернули усечённый ответ `{"totalCount":"2"}` без списка – точный топ по ним не зафиксирован; семантика «как читать» покрыта кластером «encar на русском» + «проверка авто из koreи».

### LSI для копирайтера (из топов; не писать названия аналитики в статье)
- encar на русском / encar com на русском / официальный сайт / корея
- проверка авто из koreи, проверка по VIN/вин, бесплатно, пробег
- trust encar (в RU-выдаче часто путают с посредником – развести с диагностикой Encar)
- смежно по смыслу SERP: Performance Check, схема кузова, X/W, Insurance History, Carhistory, утопленник/flood

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| ThatMojo/encarapi-python | https://github.com/ThatMojo/encarapi-python | Community/client: лоты Encar отдают как структурированные поля (specs, photos, price history) – подтверждает, что «карточка» = набор проверяемых полей, не картинка |
| markolofsen/carapis-encar-pypi | https://github.com/markolofsen/carapis-encar-pypi | Python-клиент к данным Encar; сигнал спроса на парсинг листингов для экспортёров |
| e9t/encar (legacy crawler) | https://github.com/e9t/encar | Старый краулер рынка Encar – площадка давно объект автоматического чтения лотов |
| Carapis Encar parser docs | https://docs.carapis.com/parsers/encar.com/intro | Docs: inspection sheet + accident/mileage – «фишки» лота, ради которых читают карточку |
| Официальный Encar Diagnostic intro | https://car.encar.com/diagnosis/intro | Официальный продукт диагностики/доверия на стороне площадки (не «русский зеркальный сайт») |

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| pain: Не понимаю корейский интерфейс, кажется «только для профи» | solution: Открыть encar.com в Chrome/Яндекс.Браузере, перевести на английский (русский часто кривой), идти по полям чеклиста | https://teletype.in/@vezemavto/B2hgUEkytih ; https://westmotors.ae/auctions-korea/encar | reader_result: видит понятные поля цена KRW, год, пробег, топливо, тип продажи |
| pain: Боюсь купить битую машину по красивым фото | solution: Открыть Performance Check / схему кузова; стоп при X/W на силовых (лонжероны, стойки, пол) | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei ; https://1avtoyurist.ru/novosti/aukcionnyj-list-encar-kak-rasshifrovat-i-chto-znachat-kody.html ; https://www.youtube.com/watch?v=xnRE7Dj3n6c | reader_result: решение «не беру / нужен осмотр» по схеме, а не по эмоции от фото |
| pain: Не знаю, верить ли пробегу | solution: Сверить пробег в объявлении с Performance Check и историей; расхождение >5–10% – тревога; смотреть Rent/Lease и износ салона | https://westmotors.ae/auctions-korea/encar ; https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei | reader_result: умеет поймать «слишком красивый» пробег до депозита |
| pain: Путаю «Encar на русском» и реальную проверку | solution: Развести зеркало/каталог посредника и отчёт; Trust/Diagnostic на encar.com и Carhistory по VIN – инструменты проверки | https://car.encar.com/diagnosis/intro ; SERP конкуренты encar.expert / encar-russia.ru | reader_result: не платит, пока не открыл живую карточку и историю |
| pain: Не знаю, когда звать подборщика | solution: Если нет VIN, нет доступа к insurance history, есть X на каркасе, Rent, крупные выплаты или нет времени – стоп и Авто-Сейлс | https://westmotors.ae/auctions-korea/encar ; memory/brief/fact-bank.md | reader_result: критерий «сам отсеял или отдал профессионалам до депозита» |

## action_outline
1. Открыть официальный encar.com (не только русское зеркало), включить переводчик браузера (лучше EN), сохранить ссылку на лот.
2. В карточке зафиксировать базовые поля: цена в вонах, год/дата производства, пробег, топливо (LPG для экспорта обычно мимо), тип продажи (только General / обычная продажа, не Lease/Rental).
3. Просмотреть все фото: зазоры, салон, пробег на приборке vs заявка, следы коммерции; описание дилера – «2 ключа», окрасы, экспорт.
4. Открыть диагностику / View Performance Record: найти VIN, дату осмотра, схему кузова; отметить X (замена) и W (шпаклёвка/правка); силовые элементы с метками – стоп или обязательный осмотр.
5. Проверить блоки двигателя/КПП в Performance Check на утечки и «needs attention»; дата осмотра старше нескольких месяцев – запросить свежую проверку.
6. Открыть историю (Insurance / vehicle history): владельцы, коммерческое использование, выплаты «своему» vs «чужому» авто; ориентир практиков: выплаты этому авто >~3 млн вон – красный флаг (эвристика блогов, не закон).
7. Дополнить связкой Trust/Encar Diagnostic (если лот с меткой диагностики) и/или Carhistory по VIN (flood + страховая); помнить: ДТП без страховки в базе может не быть.
8. Свести вердикт: «ок к осмотру» / «отказ» / «нужен подборщик». Депозит – только после пакета. Если затык – каталог Авто-Сейлс и Telegram @avtosales125 (без форм на странице, без сумм пошлин).

## SERP gap (для Writer, 2026-07-18)

Конкуренты в выдаче «encar на русском 2026»: зеркала-каталоги (encar.expert, encar-russia.ru, carskorea), vc.ru-опыт заказа, Rutube-разборы. Мало жёсткого beginner-чеклиста «как читать карточку за 10 минут» с красными флагами и стоп-правилом до депозита. Не копировать структуру конкурентов 1:1. Не путать тему AS02 (чтение карточки) с AS09 (глубокая проверка Trust/Carhistory до депозита) – в AS02 дать связку кратко + внутреннюю отсылку.

## Факты с URL (минимум для статьи; без выдуманных VIN/цен лотов)

| # | Факт | URL | accessed_at |
| --- | --- | --- | --- |
| 1 | Encar – крупнейший корейский маркетплейс б/у; интерфейс корейский, переводчик обязателен; EN надёжнее кривого RU | https://westmotors.ae/auctions-korea/encar | 2026-07-18 |
| 2 | В карточке смотреть: цена KRW, год, пробег, топливо, тип продажи, владельцы, фото 10–20 шт. | https://westmotors.ae/auctions-korea/encar | 2026-07-18 |
| 3 | Отчёт состояния: схема кузова + Performance check + Insurance history | https://westmotors.ae/auctions-korea/encar | 2026-07-18 |
| 4 | X = заменённая деталь; W = шпаклёвка/правка металла | https://teletype.in/@vezemavto/B2hgUEkytih ; https://www.youtube.com/watch?v=xnRE7Dj3n6c | 2026-07-18 |
| 5 | X/W на лонжеронах и стойках – главные красные флаги | https://1avtoyurist.ru/novosti/aukcionnyj-list-encar-kak-rasshifrovat-i-chto-znachat-kody.html | 2026-07-18 |
| 6 | Полная insurance history на Encar часто только для залогиненных с KR-номером | https://westmotors.ae/auctions-korea/encar | 2026-07-18 |
| 7 | Расхождение пробега объявление vs осмотр >5–10% – повод подозревать скрутку | https://westmotors.ae/auctions-korea/encar | 2026-07-18 |
| 8 | Практики: нет VIN = нет разговора; Rent = риск такси/каршеринга; выплаты >3 млн вон – стоп до осмотра | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei | 2026-07-18 |
| 9 | Encar Diagnostic / + / ++ – официальные уровни проверки кузова/состояния на площадке; Diagnostic++ анонсирован July 2025 | https://car.encar.com/diagnosis/intro ; https://aimgroup.com/2025/07/24/encar-com-launches-advanced-vehicle-certification-service-encar-diagnostic/ | 2026-07-18 |
| 10 | Лист/Performance Check = текущее состояние; Carhistory = прошлое по страховке; вместе лучше, чем по отдельности | https://1avtoyurist.ru/novosti/aukcionnyj-list-encar-kak-rasshifrovat-i-chto-znachat-kody.html | 2026-07-18 |
| 11 | LPG и коммерческая история – типичный отказ для экспорта у практиков | https://teletype.in/@vezemavto/B2hgUEkytih | 2026-07-18 |
| 12 | Спрос: «encar на русском» 1886 показов/мес (внутренняя цифра research, не в текст статьи) | MCP wordstat_get_top_requests | 2026-07-18 |
| 13 | Авто-Сейлс: подбор из Кореи/Японии/Китая, хаб Владивосток; CTA каталог + Telegram @avtosales125; без форм и калькуляторов пошлин на странице | memory/brief/fact-bank.md ; memory/brief/site-brief.md | 2026-07-18 |

**Не использовать без перепроверки:** чужие «цены под ключ», фиксированные суммы пошлин/утильсбора, выдуманные VIN/номера лотов, гарантии «чистой истории» только по одному скрину зеркала.

## CTA / conversion
- Каталог Авто-Сейлс + Telegram @avtosales125 (лимиты conversion-map)
- Без лид-форм на странице статьи
- Без статичных калькуляторов пошлин
- В тексте статьи не упоминать Wordstat / Метрику

## utility_verdict
PASS – how_to / mode B, beginner-first чеклист чтения карточки Encar, измеримый reader_outcome, Wordstat + WebSearch 2026-07-18, источники с accessed_at, action_outline 8 шагов.
