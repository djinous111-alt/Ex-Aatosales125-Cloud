research_date: 2026-10-12
accessed_at: 2026-10-12
utility_verdict: PASS
reader_outcome: новичок за 5–7 минут разберёт любой японский аукционный лист по порядку VIN/номер кузова → пробег → общая оценка → салон → схема кузова → заметки инспектора и решит «можно ставить» или «лучше пропустить» по чек-листу
reader_pain: человек впервые смотрит аукционник, видит «4.5» или «R» и не понимает, можно ли ставить; боится пропустить аварию на схеме или наоборот отсечь нормальную машину из-за XX на двери
success_criteria: читатель открывает лист лота и без переводчика-эксперта называет: (1) общую оценку и салон, (2) есть ли R/RA, (3) какие коды A/U/W/S/C/XX на схеме и что с ними делать, (4) итог чек-листа «ставка / пауза / пропуск»
voice_angle: спокойный разговор «до ставки, а не после выкупа» – как сосед из Владивостока, который уже обжёгся на красивой четвёрке с кучей W на стойках
reader_story: Андрей нашёл красивый Prius «оценка 4.5», поставил ставку по фото, а после выкупа увидел на схеме W2 у стойки и заметку про ремонт – деньги уже ушли; статья начинается с этой ошибки и учит читать лист ДО ставки
surprising_fact: «нет буквы R» не значит «машина никогда не билась» – по японскому стандарту 修復歴 ремонт болтовых панелей (дверь, крыло, капот, бампер с XX) не даёт R; а миф «RA = сработали подушки» японские критерии не подтверждают (актуально на 2026-10-12, источники SheetJP / Japan Vehicle Data 2026)

prefer_sources_after: 2026-07-14
freshness_note: приоритет источникам после 2026-07-14; сверка фактов на today_iso 2026-10-12

## research_questions
1. В каком порядке новичок должен читать аукционный лист, чтобы не пропустить красные флаги до ставки?
2. Что на практике значат оценки S / 6 / 5 / 4.5 / 4 / 3.5 и чем R / RA отличаются от «просто плохой четвёрки»?
3. Как расшифровать коды A, U, W, S, C, X, XX на схеме кузова и какие из них стоп для новичка?
4. Почему нельзя верить только общей оценке и фото в объявлении?
5. Какой короткий чек-лист «можно ставить / лучше пропустить» дать новичку без калькулятора пошлин и без выдуманных лотов?

## source_table
| source | url | accessed_at | why_it_matters |
| JapanAuc grading (RU) | https://www.japanauc.com/ru/auctions/grading/ | accessed_at: 2026-10-12 | Пошаговая карта листа: блоки 1–7, таблица S–R, коды A/U/W/S/C/XX, совет 4+ / салон B+ |
| SheetJP R vs RA (upd. 2026-09-25) | https://sheetjp.com/guides/what-does-r-and-ra-grade-mean | accessed_at: 2026-10-12 | R/RA = 修復歴 на скелете; XX на двери ≠ R; миф про airbag развенчан |
| Japan Vehicle Data R vs RA (2026-07-31) | https://japanvehicledata.com/auction-sheet-r-vs-ra/ | accessed_at: 2026-10-12 | Стандарт NAK/AFTC, правило «только сварные детали», порог 2019, порядок чтения листа |
| Carscom расшифровка | https://carscom.ru/auction-list/ | accessed_at: 2026-10-12 | RU-таблица кодов A/U/W/S/C/X/XX, пробег, эры H/R, заметки инспектора |
| Provide Cars grades | https://providecars.co.jp/about-auction/japanese-auction-houses-use-a-grading-system | accessed_at: 2026-10-12 | Шкала S–R, XX на bolt-on ≠ 修復歴, разница калибровки TAA vs USS |
| Tonari Japan таблица оценок | https://tonari-japan.ru/informatsiya/avtoauktsiony-yaponii/rasshifrovka-yaponskih-auktsionnyh-listov | accessed_at: 2026-10-12 | Классическая RU-таблица S/6/5/4.5/4/R с ориентирами по пробегу |
| KMC Japan R/RA (2026-09-07) | https://kmcjapan.co.jp/blog/japanese-auction-sheet-r-ra-repair-history | accessed_at: 2026-10-12 | Свежий 2026: R – категория, не «балл красоты»; RA всё ещё repair history |
| USS inspection PDF | https://www.uss-engine.com/info_items/rules/inspection_20121001.pdf | accessed_at: 2026-10-12 | Официальный регламент USS: определение 修復歴車 по скелетным элементам |
| JU Tokyo criteria PDF | https://ju-tokyo.net/data/202505/bin68294bd572438.pdf | accessed_at: 2026-10-12 | Критерии JU: 修復歴 по NAK, поправки включая апрель 2019 |
| AFTC repair-history PDF | https://www.aftc.or.jp/content/files/pdf/aftc_info/aftcinfo_20190326.pdf | accessed_at: 2026-10-12 | Отраслевой критерий 修復歴 (ссылка из разборов 2026) |
| Drom forum pain | https://www.forumsdrom.ru/vybor-pr/t1150953657.html | accessed_at: 2026-10-12 | Community: XX = замена панели; лонжероны – в японских комментариях |
| MS-AUTO how-to | https://ms-auto.ru/kak-chitat-aukczionnyj-list-yaponskogo-avtomobilya-rasshifrovka-oczenok-i-oboznachenij/ | accessed_at: 2026-10-12 | Типичная ошибка новичка: смотреть только общий балл |
| Carto 2026 competitor | https://carto-auto.ru/blog/kak-chitat-aukcionnyy-list-iz-yaponii-i-korei-2026/ | accessed_at: 2026-10-12 | SERP-конкурент 2026: оценки + коды + пробег; наш gap – чек-лист до ставки |
| Autoprofiasia 2026 | https://autoprofiasia.ru/blog/rasshifrovka-aukcionnogo-lista-yaponii-2026/ | accessed_at: 2026-10-12 | Конкурент 2026 с акцентом на R/RA; сверять факты, не копировать структуру |

## wordstat
Источник: MCP-KV `wordstat_get_top_requests`, regions `["225"]` (Россия), devices DEVICE_ALL, дата съёма 2026-10-12. Цифры только из ответа API, без выдумок.

| phrase | impressions |
| аукционный лист | 28853 |
| аукционный лист япония | 6690 |
| расшифровка аукционного листа | 5266 |
| японские аукционные листы | 3844 |
| аукционный лист автомобиля | 3464 |
| что значит в аукционном листе | 2048 |
| что означает в аукционном листе | 1916 |
| расшифровка аукционного листа из японии | 1660 |
| оценка r на японском аукционе | 1453 |
| перевод аукционного листа | 1448 |
| аукционный лист на русском | 1421 |
| оценка в аукционном листе | 970 |
| читаем аукционный лист | 922 |
| как читать аукционный лист | 811 |
| что значит оценка r на японском аукционе | 651 |
| аукционный лист расшифровка на русском | 613 |
| читаем аукционный лист япония | 505 |
| как читать аукционный лист японии | 489 |
| оценка r в аукционном листе | 286 |
| оценка в аукционном листе японии | 290 |

### LSI для копирайтера (не писать «Wordstat» в статье)
- расшифровка аукционного листа / на русском
- оценка R / RA / 4.5 / S
- буквы и обозначения на схеме
- повреждения A U W S C XX
- перевод заметок инспектора
- проверить лист по номеру кузова
- японский аукцион, статистика аукционов (смежный спрос)

### Конкурентный gap vs SERP 2026-10-12
В выдаче много таблиц оценок (Carto, Carscom, JapanAuc, vc.ru, Aleado). Мало жёсткого beginner-first сценария «ошибка Андрея → порядок чтения → чек-лист ставки/пропуска» с акцентом Авто-Сейлс (Владивосток, каталог, Telegram) и без статичных цен/пошлин. На live WP уже есть «первая ставка» и «проходные», но нет отдельного гайда чтения листа – карточка B01 закрывает gap.

## github_evidence
Отдельного mature-парсера оценок USS/TAA auction sheet в топе GitHub на 2026-10-12 нет. Ниже – смежные repo + официальные PDF/docs и community (сигнал для Writer: опираться на PDF/стандарт, не на scraper).

| repo/issue/doc | url | signal |
| nbrette/YahooAuctionScrapper | https://github.com/nbrette/YahooAuctionScrapper | Community tooling вокруг JP auctions; не заменяет чтение auction sheet |
| Meowsod/yahoo_auctions_jp_scraper | https://github.com/Meowsod/yahoo_auctions_jp_scraper | Сбор карточек Yahoo Auctions JP; grades USS/TAA здесь не декодируются |
| ylvan-ayes/jp-yahooauctions-scraper | https://github.com/ylvan-ayes/jp-yahooauctions-scraper | Structured listing fields; подтверждает спрос на разбор JP auction data |
| USS 検査規程 (PDF) | https://www.uss-engine.com/info_items/rules/inspection_20121001.pdf | Официальное определение 修復歴車: скелет (frame/member/pillar/floor/roof), не косметика |
| JU Tokyo 検査基準 (PDF) | https://ju-tokyo.net/data/202505/bin68294bd572438.pdf | JU ссылается на критерий NAK; поправки до апреля 2019 |
| AFTC info PDF 2019 | https://www.aftc.or.jp/content/files/pdf/aftc_info/aftcinfo_20190326.pdf | Отраслевой критерий раскрытия 修復歴 |
| SheetJP guide (2026-09) | https://sheetjp.com/guides/what-does-r-and-ra-grade-mean | Docs-уровень: RA ≠ airbag; XX bolt-on ≠ R |
| Japan Vehicle Data (2026-07-31) | https://japanvehicledata.com/auction-sheet-r-vs-ra/ | Разбор стандарта + конфликт английских мифов |
| JapanAuc grading doc | https://www.japanauc.com/ru/auctions/grading/ | Практическая карта разделов листа для покупателя |
| Provide Cars grading | https://providecars.co.jp/about-auction/japanese-auction-houses-use-a-grading-system | Venue variance USS/TAA; XX ≠ 修復歴 |
| Drom community thread | https://www.forumsdrom.ru/vybor-pr/t1150953657.html | Живой опыт: XX = замена панели; лонжероны – в японских комментариях |
| Nissan U-Car inspection help | https://u-car.nissan.co.jp/INSPECTION/ | Публичная шкала S–R и пояснение 修復歴 для покупателя |
| Aleado help: read auction sheet | https://aleado.ru/help/auctions/read-auction-sheet.html | Help-док конкурента SERP: оценки и нюансы до покупки |

## verified_facts_for_writer
Цифры и утверждения только со ссылкой; в статье не выдумывать VIN/лоты/суммы пошлин.

1. Лист обычно содержит: шапку лота, общую оценку + салон, пробег/год/КПП, схему кузова, заметки инспектора (JapanAuc, Carscom; accessed_at: 2026-10-12).
2. Шкала состояния при отсутствии 修復歴: S → 6 → 5 → 4.5 → 4 → 3.5 → 3…; 4 – самый частый «рабочий» балл (JapanAuc; accessed_at: 2026-10-12).
3. S / 6 – почти новые; 5 – отличное; 4.5 – очень хорошее с лёгким износом; ниже 3.5 – новичок без эксперта лучше пропускает (Tonari, JapanAuc, Carscom).
4. R / RA – не «балл красоты», а категория 修復歴あり: ремонт/замена сварного скелетного элемента (SheetJP 2026-09-25; Japan Vehicle Data 2026-07-31; USS PDF).
5. RA там, где площадка его пишет, обычно «более лёгкий» объём той же категории; это всё ещё repair history, не «четвёрка с опечаткой» (SheetJP, KMC 2026-09-07).
6. Миф «A в RA = airbag» японскими критериями не подтверждается (SheetJP; Japan Vehicle Data).
7. Болтовые панели (дверь, крыло, капот, бампер) с XX/W сами по себе не делают машину R (Provide Cars; SheetJP; Japan Vehicle Data).
8. Коды схемы: A – царапина, U – вмятина, W – след ремонта/волна, S – ржавчина, C – коррозия, X – нужна замена, XX – уже заменена; цифра 1–3/4 = размер (Carscom, JapanAuc; accessed_at: 2026-10-12).
9. Главная ошибка новичков – смотреть только общий балл и фото, игнорируя схему и заметки (MS-AUTO; Drom; Japan Vehicle Data порядок чтения).
10. Калибровка площадок разная: «4.5 на TAA» часто строже, чем «4.5 на USS» – балл сравнивают внутри площадки и всегда со схемой (Provide Cars).
11. Wordstat RU-225 на 2026-10-12: parent «аукционный лист» 28853; «как читать…» 811; «расшифровка…» 5266; «аукционный лист япония» 6690; «оценка r…» 1453.
12. Редакционный запрет Авто-Сейлс: не публиковать готовые суммы пошлин/утильсбора как калькулятор; расчёт – в каталоге (fact-bank).

## pain_solution_map
| pain | solution | proof/source | reader_result |
| pain: не понимает, с чего начать чтение листа | solution: жёсткий порядок VIN/кузов → пробег → оценка → салон → схема → заметки → фото | JapanAuc разделы 1–7; Japan Vehicle Data §7 | result: читатель знает, куда смотреть первым |
| pain: путает 4.5 и R, думает что R – «чуть хуже четвёрки» | solution: таблица S/6/5/4.5/4 vs отдельная ось R/RA = 修復歴 | SheetJP; USS PDF; KMC 2026-09 | result: R/RA выносит в «нужен разбор», не в «чуть дешевле 4» |
| pain: видит XX на крыле и паникует / или наоборот игнорирует W у стойки | solution: таблица A/U/W/S/C/X/XX + правило bolt-on ≠ скелет | Carscom; Provide Cars; Drom | result: отличает косметику от красного флага |
| pain: верит фото объявления сильнее листа | solution: сверка листа с фото + перевод заметок; без листа ставки нет | MS-AUTO; Carscom FAQ; likeauto/community о подмене листов | result: правило «нет читаемого листа – нет ставки» |
| pain: кажется, что это только для перекупов | solution: beginner чек-лист «можно / пауза / пропуск» на 7 пунктов | outline B01; JapanAuc tip 4+/B+ | result: новичок сам отсеивает лот до звонка в Telegram |

## action_outline
1. Открыть аукционный лист лота (оригинал, не обрезанный скрин) и сверить номер кузова / лота / дату с карточкой.
2. Проверить пробег и пометки рядом (неясный пробег, замена панели приборов) – при сомнении ставить паузу.
3. Считать общую оценку: S/6/5/4.5/4 – рабочая зона новичка; 3.5 и ниже – только с разбором; R/RA – отдельный сценарий.
4. Прочитать оценку салона (A–D): для ежедневной машины ориентир A/B; C и ниже – заложить химчистку/ремонт обивки.
5. Пройти схему кузова: выписать все A/U/W/S/C/X/XX; отметить кластеры у стоек, пола, крыши, «носа».
6. Перевести заметки инспектора (特記事項): ржавчина, ремонт, запах, течи, «исправлено» – не пропускать иероглифы.
7. Сверить лист с фото лота: где на схеме W/XX – должны быть кадры; расхождение = стоп.
8. Прогнать чек-лист «можно ставить / лучше пропустить» и только потом идти в каталог / Telegram @avtosales125 за ставкой под ключ.

## writer_constraints
- Язык: русский; mode B; utility-only how_to.
- Без эмодзи; без длинных тире; кавычки прямые `"..."`.
- Не упоминать Wordstat / Метрику в тексте статьи.
- Не публиковать калькулятор пошлин и цены конкретных лотов; CTA ≤ 3: каталог + Telegram @avtosales125.
- Не копировать структуру Carto/Carscom 1:1; lead = история Андрея + боль до ставки.
- Внутренние ссылки из карточки B01: проходные авто, первая ставка (как в topics).
- Год в H1/контексте: 2026.
