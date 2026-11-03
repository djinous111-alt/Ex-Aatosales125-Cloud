research_date: 2026-11-03
accessed_at: 2026-11-03
utility_verdict: PASS
prefer_sources_after: 2026-08-05
reader_outcome: новичок откроет карточку на encar.com через перевод браузера, переведёт цену из манвонов, найдёт Performance Check и страховую историю и по чеклисту решит "смотреть дальше / стоп до депозита"
reader_pain: сайт на корейском, перевод калечит термины, а строка "без ДТП" кажется зелёным светом – из-за этого люди влюбляются в фото и платят, не прочитав схему кузова
success_criteria: у читателя на столе есть 5 полей по лоту (цена в вонах, пробег, VIN/номер, дата отчёта, отметки X/W на схеме) и понятное правило: отметки на силовых = стоп, пока нет живого осмотра; депозит не отправлен
voice_angle: спокойный разговор "как читать менюшка на чужом языке", без пафоса про "официальный Encar на русском" и без калькулятора пошлин
reader_story: человек нашёл "красивую" Sonata на зеркале "Encar на русском", увидел "무사고 / без ДТП", скинул задаток посреднику – а на схеме кузова уже стоял W на лонжероне; выяснилось уже после перевода денег
surprising_fact: по разбору ~1,55 млн корейских листов осмотра "авария" есть у ~14,4% машин, а хотя бы одна панель кузова менялась у ~40% – то есть "без ДТП" по корейским правилам не значит "кузов не трогали"

## research_questions
1. Есть ли официальный русский Encar или только перевод браузера и зеркала посредников?
2. Какие 5–7 полей карточки новичок обязан выписать до любого депозита?
3. Как читать Performance Check: буквы X/W/C/A/U/T и где "простое крыло", а где силовой удар?
4. Чем отличаются 성능점검 (лист осмотра), 엔카진단 (диагностика Encar) и российский бренд Trust Encar в выдаче?
5. Почему страховая история (보험이력 / Carhistory) не закрывает ремонт за наличные?
6. Как не перепутать цену в 만원 с "рублями под ключ" и не выдумать пошлины в статье?
7. Где граница с AS09 (проверка до депозита через Carhistory) – что оставить в AS02?

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Encar Global export (RU lang) | https://global.encar.com/export-service/intro?lang=ru | accessed_at: 2026-11-03 | Официальный экспортный портал; покупка через партнёров, не "кнопка русский на encar.com" |
| Encar accident diagnosis criteria | https://www.encar.com/dc/dc_carsearch_v17_pp2.htm | accessed_at: 2026-11-03 | Официально: 무사고 ≠ отсутствие замен навесных панелей |
| AuctionsAPI: how to read inspection (Oct 2026) | https://auctionsapi.com/articles/encar-inspection-report | accessed_at: 2026-11-03 | Актуальная расшифровка X/W/C/A/U/T, rank 1/2 vs frame A/B/C, 엔카진단 ≠ лист |
| Vinlid: 1.5M inspection stats (Jul 2026) | https://vinlid.com/blog/korean-used-car-accident-statistics | accessed_at: 2026-11-03 | Цифры 14,4% vs ~39,7% панелей – опорный surprising_fact |
| Car Hunt: Encar на русском | https://car-hunt.ru/blog/encar-na-russkom | accessed_at: 2026-11-03 | Конкурент: перевод браузера + ловушка зеркал encar-russia / trust-encar |
| Auto.ru logbook: как выбрать на Encar | https://auto.ru/logbook/kak-vybrat-avto-na-encar-com-podrobnaia-instruktsiia-dlia-novichkov_91547be0-5fc3-4da3-bdb5-90c154a30d9e/ | accessed_at: 2026-11-03 | Beginner-first: перевод часто лучше на английский, чем на русский |
| SferaCar: как читать отчёт | https://korean.sferacar.ru/stati/kak-chitat-otchet-encar.html | accessed_at: 2026-11-03 | Пошаговая связка VIN → пробег → страховка → схема |
| vc.ru: Encar для покупателя из РФ | https://vc.ru/transport/3169117-kak-vybrat-avto-iz-korei-na-encar-dlya-pokupatelej-iz-rossii | accessed_at: 2026-11-03 | Манвон×10000; диагностика – фильтр, не гарантия после вывоза |
| Chrome Help: перевод страниц | https://support.google.com/chrome/answer/173424?hl=ru | accessed_at: 2026-11-03 | Безопасный первый шаг новичка без расширений посредников |
| Carapis docs (Encar fields) | https://docs.carapis.com/api/getting-started | accessed_at: 2026-11-03 | Документация полей listing/inspection_sheet – сигнал структуры данных карточки |
| Carapis /docs hub | https://carapis.com/docs | accessed_at: 2026-11-03 | Официальный docs-хаб для gate evidence |
| Trust Encar RU site | https://trust-encar.ru/ | accessed_at: 2026-11-03 | Коммерческий каталог в выдаче; не путать с инструментом проверки |
| Encar sellguide FAQ (성능점검) | https://www.encar.com/sg/sg_sellguide.do?bbs_no=55&method=view | accessed_at: 2026-11-03 | Официальная справка площадки про лист осмотра |

## wordstat
status: UNAVAILABLE (soft-fail)
⚠️ WORDSTAT AUTH WARNING: Сервер Wordstat (MCP-KV / wordstat_get_top_requests) на 2026-11-03 недоступен: namespaceStatus=error при live tool discovery. Точные показы в месяц не получены. Цифры спроса не выдумывать.
Авторизация при восстановлении: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

| phrase | impressions |
| --- | --- |
| encar на русском | UNAVAILABLE |
| как читать encar | UNAVAILABLE |
| проверка авто корея | UNAVAILABLE |
| энкар на русском | UNAVAILABLE |
| trust encar | UNAVAILABLE (см. внутренний срез AS09 от 2026-07-17 только как LSI-память, не как свежие показы) |

LSI / семантика для Writer (без цифр показов): encar / энкар / енкар, перевод chrome, fem.encar.com, Performance Check / 성능점검, 엔카진단, 보험이력, манвон / 만원, 무사고, Carhistory, схема кузова X W, Владивосток, под заказ из Кореи. В тексте статьи слова Wordstat / Метрика не писать.

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| ThatMojo/encarapi-python README | https://github.com/ThatMojo/encarapi-python | Клиент тянет listing + inspection + accident/ownership record отдельно – подтверждает, что "одна галочка ДТП" недостаточна |
| ThatMojo/encarapi-node | https://github.com/ThatMojo/encarapi-node | Методы inspection(id) и record(id) – два разных отчёта по одному лоту |
| xapiauto/xapikorea-python | https://github.com/xapiauto/xapikorea-python | Missing inspection ≠ accident-free; флаги inspection_available / insurance_available |
| piotrv1001/how-to-check-encar-vehicle-history-in-nodejs | https://github.com/piotrv1001/how-to-check-encar-vehicle-history-in-nodejs | Практика: смотреть accidentRecord + inspection + diagnosis вместе |
| Mikejkee/encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | Сообщество парсит карточки Encar – сигнал, что структура полей стабильно востребована |
| Carapis docs getting-started | https://docs.carapis.com/api/getting-started | Docs: в ответе могут быть inspection_sheet / accident_history |
| AuctionsAPI inspection guide | https://auctionsapi.com/articles/encar-inspection-report | Community/docs гайд Oct 2026 по кодам панели |

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| pain: "не понимаю корейский, боюсь открыть не тот сайт" | solution: открыть именно encar.com / fem.encar.com, включить перевод Chrome; зеркала "Encar на русском" считать каталогами посредников | Car Hunt; Chrome Help; global.encar.com | reader_result: знает официальный домен и не платит зеркалу "как площадке" |
| pain: "цена 1890 – это что, рубли?" | solution: 만원 (манвон) × 10 000 = воны; это цена в Корее, не под ключ во Владивосток | vc.ru 3169117; гайды конкурентов | reader_result: выписал воны на бумажку и не сравнивает с объявлением Avito 1:1 |
| pain: "написано без ДТП – значит идеал" | solution: 무사고 = нет ремонта силового каркаса по правилам листа; навесные X на крыле/капоте могут быть при "без ДТП" | encar.com dc_carsearch_v17_pp2; Vinlid 14,4% vs ~40% | reader_result: ищет схему кузова, а не одну строку |
| pain: "буквы X и W – иероглифы" | solution: шпаргалка X=замена, W=правка/сварка, C=коррозия, A=царапина, U=вмятина, T=повреждение; на силовых (лонжерон, стойка, пол) – стоп до осмотра | AuctionsAPI Oct 2026; SferaCar | reader_result: отличает "крыло" от "лонжерона" |
| pain: "боюсь скрутки и такси" | solution: сверить пробег в карточке и в отчёте (только растёт); метки 렌트/리스/영업용; страховая не ловит ремонт за наличные | AuctionsAPI; Car Hunt; SferaCar | reader_result: список красных флагов до депозита |
| pain: "Trust Encar / диагностика – одно и то же?" | solution: развести: RU-бренд trust-encar.ru ≠ 엔카진단 ≠ лист 성능점검; глубокая связка с Carhistory – тема AS09 | trust-encar.ru; AuctionsAPI; AS09 brief | reader_result: не путает бренд посредника с отчётом |

## action_outline
1. Открыть encar.com (или карточку fem.encar.com) в Chrome / Яндекс.Браузере и включить перевод страницы; не путать с encar-russia / trust-encar / encarrus.
2. Выписать с карточки: марка/модель, год, пробег, топливо, объём, коробка, цена в 만원 → воны (×10 000).
3. Найти и открыть Performance Check / 성능점검 (лист осмотра): дата, VIN, пробег на дату осмотра.
4. Прочитать схему кузова: где X/W; навесные панели vs силовые (лонжерон, стойки, пол, усилители).
5. Открыть страховую историю 보험이력: выплаты, смена владельцев, прокат/лизинг; помнить про "дыры" ремонта за наличные.
6. Сверить фото с отчётом: моторный отсек, багажник, болты крыльев; старый скрин отчёта не принимать.
7. Применить стоп-правила: X/W на силовых, затопление/пожар, обременение, странный пробег – не слать депозит.
8. Если лот прошёл фильтр – сохранить ссылку/ID и идти в каталог Авто-Сейлс / Telegram за расчётом и осмотром до оплаты (без сумм пошлин в статье).
9. Для углублённой проверки Carhistory + пакет "до депозита" – следующий материал AS09; здесь достаточно уметь читать карточку.

## competitor_gap
Конкуренты либо продают свой "Encar на русском" каталог, либо пишут длинный "как купить под ключ". Пробел Авто-Сейлс: короткий beginner how-to именно по чтению объявления (5 полей + схема + стоп-правила), с мостом на Владивосток и без выдуманных цен/пошлин. Не копировать структуру Car Hunt / AutoKoreaGroup 1:1. Не каннибалить AS09: без глубокого разбора Carhistory fee и депозитного чеклиста.

## facts_for_writer
| # | факт | url | accessed_at |
| --- | --- | --- | --- |
| 1 | Официальной полной русской версии encar.com нет; global.encar.com – экспорт через партнёров | https://global.encar.com/export-service/intro?lang=ru | accessed_at: 2026-11-03 |
| 2 | 1 만원 = 10 000 KRW | https://vc.ru/transport/3169117-kak-vybrat-avto-iz-korei-na-encar-dlya-pokupatelej-iz-rossii | accessed_at: 2026-11-03 |
| 3 | X = 교환 (замена), W = 판금/용접 (правка/сварка), C/A/U/T – коррозия/царапина/вмятина/повреждение | https://auctionsapi.com/articles/encar-inspection-report | accessed_at: 2026-11-03 |
| 4 | "ДТП/사고" в листе – про силовой каркас; замена болтовых панелей = простая починка | https://www.encar.com/dc/dc_carsearch_v17_pp2.htm | accessed_at: 2026-11-03 |
| 5 | 엔카진단 – отдельная проверка сотрудников Encar, не замена законного листа | https://auctionsapi.com/articles/encar-inspection-report | accessed_at: 2026-11-03 |
| 6 | Vinlid: ~14,4% с accident history vs ~39,7% с заменой хотя бы одной панели (n≈1,55 млн) | https://vinlid.com/blog/korean-used-car-accident-statistics | accessed_at: 2026-11-03 |
| 7 | Гарантия инспектора в Корее (ориентир 30 дней / 2 000 км) почти не помогает уже уехавшей машине | https://auctionsapi.com/articles/encar-inspection-report | accessed_at: 2026-11-03 |
| 8 | Страховая история не видит ремонт без страховки | https://car-hunt.ru/blog/encar-na-russkom | accessed_at: 2026-11-03 |
| 9 | Авто-Сейлс: Владивосток, Днепровская 40а стр.4; CTA в каталог/Telegram без форм на странице и без калькулятора пошлин | fact-bank / site-brief | accessed_at: 2026-11-03 |
| 10 | В RU-SERP "Trust Encar" часто = коммерческий сайт посредника, не кнопка диагностики | https://trust-encar.ru/ | accessed_at: 2026-11-03 |

## cannibalization_note
AS09 закрывает "Trust Encar + Carhistory до депозита". AS02 закрывает "как читать карточку Encar на русском". Перекрёстные ссылки допустимы; дублировать fee Carhistory и полный депозитный чеклист нельзя.
