research_date: 2026-10-16
accessed_at: 2026-10-16
# batch access stamps for gate (WebSearch / Wordstat / GitHub / official Encar / competitor fetches)
# accessed_at: 2026-10-16 — WebSearch Cursor SERP
# accessed_at: 2026-10-16 — Wordstat MCP
# accessed_at: 2026-10-16 — GitHub evidence
# accessed_at: 2026-10-16 — global.encar.com + car.encar.com/diagnosis
utility_verdict: PASS
reader_outcome: новичок откроет карточку Encar (через перевод браузера), пройдёт чеклист из 8 полей и отсеет «красивую, но мутную» машину до разговора о деньгах
reader_pain: сайт на корейском, перевод кривой, непонятно что смотреть первым — боязнь купить «кота в мешке» по красивым фото
success_criteria: у читателя есть заполненный мини-чек «год / пробег / цена в вонах / VIN / схема кузова / страховая строка / фото / дилер-частник» и понятное правило «что стоп, что можно смотреть дальше»
voice_angle: как читать объявление на чужом языке без корейского — будто инструкцию к стиральной машине: сначала ярлыки на карточке, потом «мелкий шрифт» в отчёте
reader_story: человек открыл encar.com, включил перевод на русский, увидел цену «1890» и подумал, что машина стоит тысячу девятьсот рублей/долларов — а на самом деле это манвоны; параллельно пролистал фото и не заметил, что нет кнопки с листом диагностики
surprising_fact: «официального русского Encar.com» как переключателя языка почти нет — люди ищут «encar на русском» (~2253 показ/мес), а реальный путь новичка: браузерный перевод или русскоязычный каталог посредника; при этом перевод на английский часто понятнее, чем на русский

## research_questions
1. Как новичку открыть Encar и сделать карточку читаемой на русском/английском без знания корейского?
2. Какие поля карточки смотреть первыми (до Trust Encar / Carhistory и до депозита)?
3. Как правильно читать цену в 만원 (манвонах) и не путать её с ценой «под ключ»?
4. Что означают отметки X/W/A/U/C/T на схеме кузова в листе 성능점검 и где «красный флаг»?
5. Чем карточка объявления отличается от глубокой проверки Trust/Carhistory (AS09) — куда отсылать, не каннибализируя?
6. Когда новичку лучше остановиться и отдать лот подборщику (Авто-Сейлс / Владивосток)?

## cannibalization_guard_vs_AS09
AS09 (published): Trust Encar + Carhistory до депозита — отчёты, VIN-история, stop-правила оплаты.
AS02 (эта статья): чтение самой карточки объявления Encar — перевод, поля, цена, фото, красные флаги на схеме/в шапке.
Связка: в AS02 упомянуть «после карточки — отдельная проверка истории (см. материал про Trust/Carhistory)», не разворачивать Carhistory как основной гайд.

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| AuctionsAPI: how to read Encar inspection report (Oct 2026) | https://auctionsapi.com/articles/encar-inspection-report | 2026-10-16 | Канон кодов X/W/C/A/U/T, разница 사고 vs 단순수리, Encar diagnosis ≠ обязательный лист |
| AutoKoreaGroup: как читать отчёт Encar (9 Oct 2026) | https://autokoreagroup.com/blog/kak-chitat-otchet-encar | 2026-10-16 | Свежая русская расшифровка схемы кузова + статистика по 45k отчётов |
| Carto-Auto: гайд Encar 2026 | https://carto-auto.ru/blog/guide-encar/ | 2026-10-16 | Пробег/KHIS, красные флаги, как открыть лист 성능·상태점검기록부 |
| Altezza: как читать Encar (19 May 2026) | https://altezza.team/blog/encar-guide.html | 2026-10-16 | Поля карточки, Hidden.Y, цена ≠ под ключ |
| Auto.ru logbook: инструкция для новичков | https://auto.ru/logbook/kak-vybrat-avto-na-encar-com-podrobnaia-instruktsiia-dlia-novichkov_91547be0-5fc3-4da3-bdb5-90c154a30d9e/ | 2026-10-16 | Перевод: лучше EN, чем кривой RU |
| Auto.ru: руководство по покупке | https://auto.ru/logbook/cars/genesis/g90/23205402/encar-rukovodstvo-po-pokupke-avtomobiley-iz-korei_d4f393d3-6f50-4a36-b773-38b69505a3f0/ | 2026-10-16 | Шапка карточки: пробег, дата учёта, двигатель, цвет |
| Teletype Rolker: подбор через Encar | https://teletype.in/@rolker_auto/podborKoreaEncar | 2026-10-16 | ПК-версия + перевод на English как рабочий старт |
| vc.ru: Encar для покупателя из РФ | https://vc.ru/transport/3169117-kak-vybrat-avto-iz-korei-na-encar-dlya-pokupatelej-iz-rossii | 2026-10-16 | Манвоны: 1890 = 18 900 000 ₩; Encar ≠ аукцион ставок |
| AutoKoreaGroup: как купить с Encar | https://autokoreagroup.com/blog/kak-kupit-avto-s-encar | 2026-10-16 | Формула цены: цифра × 10 000 вон |
| Official Encar Global Export (lang=ru) | https://global.encar.com/export-service/intro?lang=ru | 2026-10-16 | Официальный экспортный контур; прямой «русский сайт лотов» ≠ encar.com |
| Encar Diagnosis intro (офиц.) | https://car.encar.com/diagnosis/intro | 2026-10-16 | 엔카진단 — отдельная проверка площадки, не замена листа |
| GitHub encar-scoring-chrome-extension | https://github.com/hjhj97/encar-scoring-chrome-extension | 2026-10-16 | Реальные поля карточки, которые смотрят практики: страховка, 성능점검, рента |
| GitHub Mikejkee/encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | 2026-10-16 | Сигнал: с карточки парсят страховку и диагностику |
| GitHub ThatMojo/encarapi-python | https://github.com/ThatMojo/encarapi-python | 2026-10-16 | Структура данных лота: specs / inspection / price |
| ReefAPI Encar docs (price_manwon) | https://reefapi.com/docs/encar | 2026-10-16 | Подтверждение: цена в 만원, ×10 000 = KRW |
| Fact-bank Авто-Сейлс | memory/brief/fact-bank.md | 2026-10-16 | Ниша: пригон JP/KR/CN, хаб Владивосток; без выдуманных пошлин |

## wordstat
Источник: MCP-KV `wordstat_get_top_requests` / `wordstat_get_dynamics`, регион 225 (Россия), съём 2026-10-16. Цифры только из API.

| phrase | impressions |
| --- | --- |
| encar (кластер totalCount) | 34760 |
| encar | 34108 |
| encar com | 9571 |
| энкар (кластер) | 9126 |
| энкар | 8990 |
| сайт encar (кластер) | 4370 |
| encar сайт | 4328 |
| encar официальный сайт | 3687 |
| энкар корея | 2608 |
| encar на русском (кластер totalCount) | 2296 |
| encar на русском | 2253 |
| encar корея | 2093 |
| энкар авто | 2056 |
| энкар авто из koreи | 1634 |
| энкар сайт | 1562 |
| encar авто | 1474 |
| сайт encar com | 1406 |
| encar com на русском | 1305 |
| trust encar | 638 |
| энкар на русском | 609 |
| проверка авто корея (кластер) | 831 |
| проверка авто из koreи | 549 |
| проверка авто из koreи по вин | 170 |
| проверка пробега авто из koreи | 49 |
| сайт encar на русском | 733 |
| encar на русском языке | 757 |

**Узкий how-to:** фраза `как читать encar` вернула только `{"totalCount":"7"}` без списка — low-result signal (не fatal); угол статьи опираем на широкий parent «encar на русском» + LSI «сайт / официальный / com на русском».

**Динамика** `wordstat_get_dynamics` (PERIOD_MONTHLY, toDate=2026-09-30 — последний полный месяц; первый вызов с toDate=2026-10-16 дал API 400 InvalidArgument):

| month | impressions |
| --- | --- |
| 2025-10 | 6129 |
| 2025-11 | 3655 |
| 2025-12 | 2369 |
| 2026-01 | 2803 |
| 2026-02 | 2356 |
| 2026-03 | 2183 |
| 2026-04 | 2271 |
| 2026-05 | 1989 |
| 2026-06 | 1752 |
| 2026-07 | 1963 |
| 2026-08 | 1891 |
| 2026-09 | 2016 |

Спрос стабильный ~1.8–2.8k/мес в 2026 после пика осени 2025.

### LSI для Writer (не писать «Wordstat» в статье)
encar на русском, сайт encar, encar com на русском, официальный сайт, энкар корея, проверка авто из koreи, пробег, VIN, перевод страницы, манвон / 만원, схема кузова, лист диагностики.

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| hjhj97/encar-scoring-chrome-extension | https://github.com/hjhj97/encar-scoring-chrome-extension | Практики скорят лот по страховке (내차피해/타차가해), 성능점검 (каркас A/B vs 외판 1/2), ренте, владельцам, пробегу — чеклист полей карточки |
| Mikejkee/encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | ETL парсит encar.com: машина + страховка + диагностика |
| ThatMojo/encarapi-python | https://github.com/ThatMojo/encarapi-python | Нормализованный лот: specs, options, inspection, price |
| e9t/encar crawl.py | https://github.com/e9t/encar/blob/master/crawl.py | Исторически с карточки снимают mileage, accidents, seller, price |
| M1g3l14Ka/sellercars | https://github.com/M1g3l14Ka/sellercars | Цена ×10 000 (만원→₩) при нормализации |

## verified_facts
| # | fact | url | accessed_at |
| --- | --- | --- | --- |
| 1 | Encar — корейский маркетплейс б/у авто; для иностранца прямая покупка «как на Авито» обычно недоступна, нужен канал в Корее | https://altezza.team/blog/encar-guide.html | 2026-10-16 |
| 2 | Официальный русскоязычный экспортный лендинг: global.encar.com/export-service/intro?lang=ru — это сервис экспорта/партнёров, не «русский интерфейс всех лотов» | https://global.encar.com/export-service/intro?lang=ru | 2026-10-16 |
| 3 | Новичкам советуют ПК-версию + автоперевод; на русский перевод часто кривой — удобнее English | https://auto.ru/logbook/kak-vybrat-avto-na-encar-com-podrobnaia-instruktsiia-dlia-novichkov_91547be0-5fc3-4da3-bdb5-90c154a30d9e/ | 2026-10-16 |
| 4 | Цена в карточке в 만원: цифра × 10 000 = воны (пример: 1869 → 18 690 000 ₩) | https://autokoreagroup.com/blog/kak-kupit-avto-s-encar | 2026-10-16 |
| 5 | Цена на Encar — цена у дилера в Корее, не «под ключ» в РФ (добавляются логистика, таможня, оформление) | https://vc.ru/transport/3169117-kak-vybrat-avto-iz-korei-na-encar-dlya-pokupatelej-iz-rossii | 2026-10-16 |
| 6 | Обязательный лист 성능·상태점검기록부 открывается кнопкой 성능점검; его заполняет инспектор, Encar только показывает | https://auctionsapi.com/articles/encar-inspection-report | 2026-10-16 |
| 7 | Коды схемы: X=замена, W=рихтовка/сварка, C=коррозия, A=царапина, U=вмятина, T=повреждение | https://auctionsapi.com/articles/encar-inspection-report | 2026-10-16 |
| 8 | «ДТП» в отчёте = работа по силовым (каркас); замена капота/двери часто «простой ремонт», не «авария» | https://autokoreagroup.com/blog/kak-chitat-otchet-encar | 2026-10-16 |
| 9 | По выборке ~45k отчётов (09.10.2026): ~80% без отметок на кузове; отметки на силовых ~3,3% | https://autokoreagroup.com/blog/kak-chitat-otchet-encar | 2026-10-16 |
| 10 | 엔카진단 (Encar Diagnosis) — отдельный бейдж площадки, не замена юридического листа | https://car.encar.com/diagnosis/intro | 2026-10-16 |
| 11 | У частных продавцов лист часто отсутствует — для экспорта обычно берут дилерские лоты с отчётом | https://auctionsapi.com/articles/encar-inspection-report | 2026-10-16 |
| 12 | Красные флаги пробега: скачок вниз на графике; «5 лет / 30 тыс км» без объяснения; расхождение одометр vs база | https://carto-auto.ru/blog/guide-encar/ | 2026-10-16 |
| 13 | В шапке карточки обычно: пробег, дата постановки на учёт, двигатель, цвет, дата публикации | https://auto.ru/logbook/cars/genesis/g90/23205402/encar-rukovodstvo-po-pokupke-avtomobiley-iz-korei_d4f393d3-6f50-4a36-b773-38b69505a3f0/ | 2026-10-16 |
| 14 | Не публиковать в статье готовые суммы пошлин/утильсбора как «калькулятор» — отправлять за расчётом в каталог | memory/brief/fact-bank.md | 2026-10-16 |
| 15 | Кластер Wordstat «encar на русском» ≈ 2296 показов/мес (Россия) на 2026-10-16 | MCP wordstat_get_top_requests | 2026-10-16 |

## competitor_gap
Конкуренты либо уводят в «как купить под ключ / растаможка», либо сразу в глубокий отчёт. Пробел AS02: **пошаговое чтение карточки за 10–15 минут** — перевод → 8 полей → стоп/дальше → когда звать подборщика. Не копировать структуру Altezza/Carto 1:1. Не разворачивать Carhistory (это AS09).

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| боль: Не понимаю корейский интерфейс, боюсь «сломать» поиск | решение: Открыть ПК-версию encar.com / car.encar.com, включить перевод браузера (лучше EN, RU — запасной) | auto.ru logbook; teletype Rolker | результат: Карточка читается, фильтры не пугают |
| боль: Цена «1890» кажется абсурдно маленькой | решение: Объяснить 만원: ×10 000 вон; это цена в Корее, не под ключ | AutoKoreaGroup; vc.ru | результат: Правильно переводит цену в воны и не сравнивает с Авито «влоб» |
| боль: Не знаю, с чего начать в карточке | решение: Чеклист 8 пунктов: год/учёт, пробег, двигатель, цена, VIN, лист 성능점검, страховка-строка, фото+тип продавца | auto.ru Genesis guide; AuctionsAPI | результат: Заполненный чек по одному лоту |
| боль: Боюсь битую «на красивых фото» | решение: Схема кузова: X/W на силовых = стоп; навесные — не паника, но сверка со страховкой | AuctionsAPI; AutoKoreaGroup 45k | результат: Умеет отличить «дверь меняли» от «лонжерон варили» |
| боль: Путает Trust Encar / Carhistory с чтением объявления | решение: Короткая развилка: сначала карточка → потом история до депозита (ссылка на AS09) | AS09 research + published | результат: Не уходит в чужую тему и знает следующий шаг |
| боль: Кажется, что без «своего человека в Корее» нельзя даже смотреть | решение: Разрешить безопасный просмотр: читать и отсеивать можно самому; покупать/платить — через проверенный канал (Авто-Сейлс) | Altezza; fact-bank | результат: Спокойно смотрит лоты и понимает, когда звать подбор |

## action_outline
1. Открыть encar.com (ПК), включить перевод страницы (EN предпочтительно; RU — если так удобнее).
2. Найти 1–2 модели «на посмотреть» фильтрами: год, пробег, топливо — без покупки.
3. Открыть карточку и выписать шапку: год/дата учёта, пробег, двигатель, цвет, цена в манвонах → воны (×10 000).
4. Найти VIN (차대번호) и сверить глазами с фото таблички, если фото есть.
5. Открыть лист 성능점검 / схему кузова: отметить X/W и на каких деталях; затопление/пожар/одометр — сразу стоп.
6. Открыть блок страховой истории в карточке (если есть): крупные выплаты vs «чистая» схема — повод насторожиться.
7. Проверить фото: много ракурсов, салон, багажник, под капотом; мало фото / нет отчёта у «слишком выгодного» лота — в отложку или отказ.
8. Применить правило: зелёный / жёлтый / красный лот; красный — не обсуждать депозит.
9. Если лот «жёлтый» или нужен расчёт под ключ — передать ссылку подборщику Авто-Сейлс (каталог / Telegram), а глубокую историю до денег — по гайду Trust/Carhistory (AS09).

## writer_constraints
- Beginner-first, без тона «для брокеров».
- Не каннибализировать AS09: Carhistory/Trust — короткий мост, не H2-ядро.
- Не публиковать суммы пошлин/утильсбора как готовый калькулятор (fact-bank).
- Не выдумывать VIN и цены конкретных лотов.
- FAQ-действия: как включить перевод; как читать манвоны; что такое X/W; можно ли верить пробегу в карточке; когда звать подборщика.
- CTA ≤ 3: каталог Корея / Telegram подбор — после пользы чеклиста.
- prefer_sources_after: 2026-07-18 — в статье опираться на свежие гайды Oct 2026 (AuctionsAPI, AutoKoreaGroup) + evergreen официальные страницы Encar.
)
