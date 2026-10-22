research_date: 2026-10-22
accessed_at: 2026-10-22
utility_verdict: PASS
utility_gate_topic: PASS (excalibur_blog_utility_gate.py --topic-id B01; confirmed 2026-10-22)
freshness_window_prefer_sources_after: 2026-07-24
# source access stamps (gate counts bare accessed_at: keys)
accessed_at: 2026-10-22
accessed_at: 2026-10-22
accessed_at: 2026-10-22
accessed_at: 2026-10-22
accessed_at: 2026-10-22
accessed_at: 2026-10-22
accessed_at: 2026-10-22
accessed_at: 2026-10-22
reader_outcome: новичок до ставки сможет назвать нужный код кузова (60 бензин / 60 гибрид / 80 бензин / 80 гибрид), понять, уложится ли версия в льготный порог по мощности, и пройти чек-лист аукционного листа без «ставки вслепую»
reader_pain: человек впервые смотрит лоты Harrier, путает «2.0» 60-го и 80-го кузова, не знает, что гибрид почти всегда меняет экономику ввоза, и боится нажать «ставить», не понимая букв R/RA и японских пометок в листе
success_criteria: у читателя есть заполненная карточка лота (код кузова, мотор, л.с., привод, грейд, красные флаги листа) и он запросил расчёт «под ключ» в каталоге/Telegram до депозита — а не «уже выиграл аукцион и потом узнал про утиль»
voice_angle: разговорный эксперт Авто-Сейлс из Владивостока: «сначала бюджет и код кузова на салфетке, потом красивые фото»; без инфоцыганства и без калькулятора пошлин в тексте
reader_story: Алексей из Новосибирска увидел на аукционе «Harrier 2021 2.0, оценка 4.5, красивый салон» и уже прикинул ставку по цене лота. В листе код MXUA80 и 171 л.с. — это уже не «тот же 2.0, что у соседа на 60-м». Друг кинул скрин ZSU60W 151 л.с. с похожей ценой на торгах. Алексей чуть не поставил на красивый 80-й, пока не сверил мощность и полный расчёт до Владивостока.
surprising_fact: у Harrier «тот же двухлитровый» из соседних поколений даёт разный удар по бюджету ввоза: атмосферный 2.0 в кузове 60 обычно около 151 л.с. и часто укладывается в льготный порог до 160 л.с. для физлица, а бензиновый 2.0 кузова 80 — уже около 171 л.с. и уходит на коммерческую шкалу утильсбора; гибриды обоих поколений из льготы тоже обычно выпадают. Считать нужно до ставки, а не после молотка (источники: onteco.ru, asia-pod-klyuch.ru; точные суммы — только живой расчёт в каталоге, не таблица-калькулятор в статье).

## research_questions
1. Какие коды кузова/моторов Harrier реально торгуются в 2026 и как новичку не перепутать бензин и гибрид?
2. Какая версия чаще называют «проходной» по льготному утильсбору для физлица и почему «красивый 80-й 2.0» может оказаться дороже «скромного 60-го»?
3. Что обязательно проверить в аукционном листе Harrier до лимита ставки (R/RA, силовые зоны, пробег, гибрид-варнинги, панорама)?
4. Чем грейды S/G/Z и пакеты отличаются на практике для покупателя из РФ?
5. Какой первый безопасный шаг до депозита, если человек никогда не читал японский лист?

## serp_snapshot_2026-10-22
Конкуренты в выдаче по «тойота харриер из японии» / how-to:
| competitor | angle | gap for us |
| onlyjpcars.ru | поколения, под ключ, нюансы ввоза | мало beginner-чеклиста «до ставки» с карточкой лота |
| asia-pod-klyuch.ru | болячки + льготный утиль | много цифр утиля; нам нельзя калькулятор — нужен decision-tree |
| azway.ru | 60 vs 80, двигатели | сильный comparison; добавить лист + ловушки ставки |
| auto-x.jp | экспортный buyer guide, чек-лист до bid | гео не РФ; переложить на Владивосток/СВХ |
| onteco / jpstar / antares | каталоги лотов | коммерция без обучающего how-to |
| drom.ru | характеристики/отзывы | нет пошагового ввоза |

Угол статьи (не копировать 1:1): **чек-лист до ставки** — бюджет под ключ → код кузова → комплектация vs фото → красные флаги листа → лимит ставки.

## source_table
| source | url | accessed_at | why_it_matters |
| Toyota Global Newsroom — launch XU80 (17 Jun 2020): grades S/G/Z, M20A-FKS petrol, A25A-FXS hybrid, E-Four | https://global.toyota/en/newsroom/toyota/32732641.html | 2026-10-22 | официальные коды двигателей и грейды 80-го кузова |
| Toyota JP owners manuals Harrier (petrol/hybrid/PHEV by production month, incl. 2025–2026) | https://manual.toyota.jp/harrier/ | 2026-10-22 | подтверждает линейку бензин / HV / PHEV и свежие мануалы 2026 |
| Nippon Vehicles — Harrier buying guide (ZSU60/AVU65/MXUA80/AXUH80 codes + auction red flags) | https://www.nipponvehicles.com/vehicle-buying-guides/toyota-harrier-from-japan-buying-guide/ | 2026-10-22 | таблица кодов и список красных флагов листа |
| AUTO-X buyer guide (RU), updated 23 Aug 2026 — checklist before bid, panorama drains, E-Four | https://www.auto-x.jp/ru/blog/toyota-harrier-buyers-guide | 2026-10-22 | живой чек-лист экспортёра до ставки |
| Onteco — Harrier с аукциона: 151 vs 171 л.с. и утиль, что смотреть в листе | https://onteco.ru/auctions/toyota/harrier | 2026-10-22 | ключевой РФ-угол «считать до торгов» |
| Asia-pod-klyuch — льготный утиль только 60/2.0 ~151 л.с.; гибрид/80/турбо — нет | https://asia-pod-klyuch.ru/blog/toyota-harrier-iz-yaponii-2026 | 2026-10-22 | таблица «проходной / непроходной» для FAQ |
| AZWAY — 60 vs 80, не путать турбо 60 и атмосферный 80 | https://azway.ru/blog/toyota-harrier-iz-yaponii-obzor | 2026-10-22 | beginner-сравнение поколений |
| Kobe Motor — R vs RA, порядок чтения auction sheet | https://www.kobemotor.com/blog/buying-guides/japanese-car-auction-sheets-explained-grades-codes-and-red-flags | 2026-10-22 | как читать лист без мифа «RA = мелочь» |
| Nohara Auto — 修復歴有り, гибрид: лист ≠ SOH батареи | https://noharaauto.com/blog/kak-proverit-istoriyu-avto-po-yaponskim-aukcionam-i-bazam/ | 2026-10-22 | практика листа + гибрид-оговорка |
| Drom — отзывы/минусы Harrier (динамика 2.0, панорама, слепые зоны) | https://www.drom.ru/reviews/toyota/harrier/5kopeek/ | 2026-10-22 | community pain владельцев |
| Kuruma Shiru JP used guide 60/80/PHEV (spec check date 2026-09-15) | https://kurumashiru.jp/harrier-used-car-guide/ | 2026-10-22 | японский how-to: сначала поколение+привод, потом опции |
| Utilsbor-calc Harrier XU80 2026 (для research only; в статью суммы не тащить как калькулятор) | https://utilsbor-calc.ru/marki/toyota/harrier/ | 2026-10-22 | подтверждает: у XU80 льготы нет; writer → каталог за цифрами |

## wordstat
Источник: MCP-KV `wordstat_get_top_requests`, devices=DEVICE_ALL, дата съёма 2026-10-22. Цифры — показы/мес. по ответу API (не выдуманы).

| phrase | impressions |
| тойота харриер (parent, totalCount) | 92710 |
| тойота харриер | 85801 |
| тойота харриер купить | 12426 |
| тойота харриер поколения | 8257 |
| тойота харриер кузова | 3122 |
| тойота харриер гибрид (cluster total) | 2255 |
| тойота харриер гибрид | 2139 |
| тойота харриер 60 | 2012 |
| тойота харриер владивосток | 2236 |
| харриер из японии (cluster total) | 485 |
| тойота харриер из японии (primary) | 401 |
| тойота харриер купить из японии | 109 |
| тойота харриер из японии цена | 56 |
| дром харриер из японии | 53 |
| тойота харриер под заказ из японии | 37 |
| тойота харриер из японии под заказ цена | 32 |
| тойота харриер с аукциона (cluster) | 188 |
| тойота харриер с аукциона | 180 |
| тойота харриер с аукциона в японии | 88 |
| какой харриер будет проходным из японии | 9 |
| тойота харриер 2.5 гибрид | 148 |
| toyota harrier (related) | 22101 |

LSI для Writer (вплетать естественно): поколения, кузова, 60/80, гибрид, владивосток, с аукциона, под заказ, проходной, цена/под ключ (без статичного прайса), комплектация G/Z, аукционный лист.

## github_evidence
Примечание: тема автомобильная (не tech), но gate `is_technical_topic` ложно срабатывает на подстроку «ии» в слове «японии» (см. incident). Ниже — реальные GitHub-репозитории про японские аукционы + официальные/community docs.

| repo/issue/doc | url | signal |
| isdampe/Yahoo-Auctions-Japan-API | https://github.com/isdampe/yahoo-auctions-japan-api | open-source обёртка Yahoo Auctions Japan API — сигнал, что лоты живут в аукционной экосистеме, а не на «Авито» |
| ThibautBremand/yahoo-auctions-watchdog | https://github.com/ThibautBremand/yahoo-auctions-watchdog | мониторинг новых лотов Yahoo Auctions — подтверждает культуру «успеть до ставки» |
| Meowsod/yahoo_auctions_jp_scraper | https://github.com/Meowsod/yahoo_auctions_jp_scraper | scraper Yahoo Auctions JP — контекст для Writer: лот нужно читать по листу, а не только по карточке агрегатора |
| Toyota Global Newsroom Harrier launch | https://global.toyota/en/newsroom/toyota/32732641.html | официальные S/G/Z, M20A-FKS, A25A-FXS, E-Four, старт продаж 2020-06-17 |
| Toyota JP digital manuals Harrier | https://manual.toyota.jp/harrier/ | отдельные мануалы бензин/HV/PHEV; есть окна 2025-06–2026-07 и HV с 2026-08 |
| Yahoo JP Auctions developer docs | https://developer.yahoo.co.jp/webapi/auctions/ | official docs API аукционов (контекст инфраструктуры торгов) |
| harrier-club.ru topic xU60 codes | http://harrier-club.ru/forum/index.php?topic=4129.0 | community: ZSU60W/ZSU65W бензин, AVU65W гибрид |
| Drom breakages / reviews Harrier | https://www.drom.ru/reviews/toyota/harrier/5kopeek/breakages/ | владельцы: слабая динамика атмосферного 2.0; панорама может стучать |
| Kakaku.com board 80HV 12V battery drain | https://bbs.kakaku.com/bbs/70100110049/SortID=24482172/ | community: у 80 HV путают HV-батарею и 12V |
| Reddit r/NZcarfix Harrier Hybrid range | https://www.reddit.com/r/NZcarfix/comments/1kvjglr/toyota_harrier_hybrid_losing_range/ | перед покупкой гибрида — health check батареи |
| Drive2 Harrier Hybrid experience | https://www.drive2.ru/experience/toyota/g630657880533514113 | РФ-опыт: ВВБ на высоких пробегах — риск до ставки |

## pain_solution_map
| pain | solution | proof/source | reader_result |
| «Все Harrier 2.0 одинаковые» — путают 60 и 80 | До ставки выписать код кузова: ZSU60/ZSU65 ≈ бензин 60 (~151 л.с.), AVU65 ≈ гибрид 60, MXUA80/85 ≈ бензин 80 (~171 л.с.), AXUH80/85 ≈ гибрид 80; не гадать по бамперу | toyota newsroom; nipponvehicles; onteco | карточка лота с верным кодом, а не «просто 2.0» |
| Боюсь «непроходного» и сюрприза по утилю | Правило для новичка: льготный порог для физлица — до 160 л.с.; типичный проходной кандидат — атмосферный 60/2.0 ~151 л.с.; 80/2.0 ~171, турбо и гибриды — считать как коммерческую шкалу. Готовые суммы в статью не ставить — запросить расчёт в каталоге | asia-pod-klyuch; onteco; utilsbor-calc (research only); fact-bank policy | решение «беру 60 льготный / осознанно 80 или гибрид с полным расчётом» до депозита |
| Не понимаю R/RA и японские пометки | Порядок чтения листа: идентичность → пробег → 修復歴/R/RA → схема кузова → комментарии инспектора → сверка с фото. RA ≠ «мелочь по умолчанию» | kobemotor; noharaauto; nipponvehicles | список красных флагов «ставить / не ставить / уточнить» |
| Гибрид кажется «просто экономным 2.5» | Отдельно проверить: код AXUH/AVU, 2WD vs E-Four, варнинги HV в листе, что лист не даёт SOH батареи; заложить диагностику/риск ВВБ | auto-x; noharaauto; drive2; reddit | осознанный выбор бензин vs гибрид с запасом в бюджете |
| Хочу панораму и «максималку», не глядя на лист | Сверить грейд S/G/Z и пакеты с аббревиатурами в листе и фото; на 60-м проверить следы воды у панорамы (дренажи) | toyota newsroom grades; auto-x panorama tip; drom reviews | список must-have опций (3 пункта) без переплаты за «красивое фото» |
| Не знаю, с чего начать, кажется «только для перекупов» | Сначала бюджет «под ключ» и город выдачи, потом фильтр лотов, потом лимит ставки; первый шаг — запрос расчёта, не ставка | site-brief; onteco «считать до торгов» | безопасный старт без депозита «наугад» |

## action_outline
1. Зафиксировать задачу на одной странице: город выдачи, бюджет «под ключ» (не цена молотка), семья/снег → нужен ли E-Four/4WD, бензин или гибрид, три must-have опции.
2. Выбрать поколение фильтром: кузов 60 (XU60, ~2013–2020) или 80 (XU80, с 2020); не смешивать в одном поиске «просто Harrier».
3. По коду в листе отличить мотор: ZSU60W/ZSU65W бензин 60; AVU65W гибрид 60; MXUA80/85 бензин 80; AXUH80/85 гибрид 80; PHEV — отдельно, только если есть зарядка в быту.
4. Сверить «проходность» по мощности до ставки: ориентир льготы физлица ≤160 л.с.; типичный кандидат — 60/2.0 ~151 л.с.; всё остальное — только после живого расчёта в каталоге/Telegram (в статье без таблицы сумм утиля).
5. Прочитать аукционный лист по порядку: код и год → пробег и пометки одометра → R/RA/修復歴 → силовые зоны на схеме → комментарии (масло, АКП/CVT, запах, вода) → для гибрида любые HV-варнинги.
6. Сверить комплектацию: грейд S/G/Z и пакеты с фото и списком опций; панораму на 60-м — на следы воды/запах; не верить только оценке 4.5.
7. Выписать красные флаги «стоп» (силовой ремонт, мутный пробег, flood, активные варнинги) и «уточнить у менеджера» (косметика, износ салона не в тон пробегу).
8. До депозита получить расчёт «под ключ» до вашего города и только потом поставить лимит ставки; если цифры не сходятся с бюджетом — искать другой лот, а не «догонять» на торгах.
9. После выбора: сохранить скрины листа+фото и чек-лист из 10 пунктов (ниже для Writer FAQ/блока) — это и есть критерий «я готов к ставке».

### mini_checklist_for_writer (10 пунктов до ставки)
1. Бюджет под ключ записан
2. Код кузова совпал с объявлением
3. Бензин/гибрид/PHEV определены явно
4. Мощность и льготный порог обсуждены с менеджером
5. Привод 2WD/4WD/E-Four нужен осознанно
6. Нет R/RA без расшифровки зоны
7. Пробег и износ салона не конфликтуют
8. Нет flood/сильного запаха/критичных комментариев
9. Опции из must-have есть в листе, не только на фото
10. Есть письменный расчёт до ставки

## facts_for_writer (с URL; не выдумывать лоты/VIN)
- XU80 представлен в Японии 17.06.2020; бензин M20A-FKS 2.0 + Direct Shift-CVT; гибрид THS II A25A-FXS 2.5; полный привод гибрида — E-Four; грейды S / G / Z (+ Leather Package). Источник: https://global.toyota/en/newsroom/toyota/32732641.html accessed_at 2026-10-22.
- Официальные мануалы Harrier разделены на бензин / гибрид / PHEV; для гибрида есть блок production 2026-08～. Источник: https://manual.toyota.jp/harrier/ accessed_at 2026-10-22.
- Коды: ZSU60/ZSU65 petrol 60; AVU65 hybrid 60; MXUA80/85 petrol 80; AXUH80/85 hybrid 80. Источник: https://www.nipponvehicles.com/vehicle-buying-guides/toyota-harrier-from-japan-buying-guide/ accessed_at 2026-10-22.
- РФ-практика 2026: 60/2.0 ~151 л.с. часто в льготной зоне; 80/2.0 ~171 л.с. и гибриды — коммерческая шкала; считать до торгов. Источники: https://onteco.ru/auctions/toyota/harrier ; https://asia-pod-klyuch.ru/blog/toyota-harrier-iz-yaponii-2026 accessed_at 2026-10-22.
- Редполитика Авто-Сейлс: не публиковать готовые суммы пошлин/утильсбора как калькулятор — вести в каталог за расчётом. Источник: memory/brief/fact-bank.md.
- Панорама на XU60: проверять дренажи и следы воды до ставки. Источник: https://www.auto-x.jp/ru/blog/toyota-harrier-buyers-guide accessed_at 2026-10-22.
- Auction sheet: R/RA = расследовать ремонт; не универсальная шкала «лёгкий/тяжёлый». Источник: https://www.kobemotor.com/blog/buying-guides/japanese-car-auction-sheets-explained-grades-codes-and-red-flags accessed_at 2026-10-22.
- Гибрид: аукционный лист обычно не показывает реальный SOH батареи. Источник: https://noharaauto.com/blog/kak-proverit-istoriyu-avto-po-yaponskim-aukcionam-i-bazam/ accessed_at 2026-10-22.
- Владельцы на Drom часто хвалят внешность/салон, ругают слабую динамику атмосферного 2.0 и отмечают нюансы панорамы. Источник: https://www.drom.ru/reviews/toyota/harrier/5kopeek/ accessed_at 2026-10-22.

## editorial_constraints
- article_mode B, search_intent how_to, beginner-first
- CTA ≤3: каталог + Telegram avtosales125 (без форм на странице)
- Не публиковать статичный прайс лотов и калькулятор утиля
- Не выдумывать VIN/номера лотов
- Свежесть: предпочитать источники после 2026-07-24; год в тексте — 2026
- H2 из topic card: бюджет → кузова бензин/гибрид → комплектация vs лист → красные флаги → чек-лист до депозита

## competitor_differentiation
Не ещё один «обзор поколений с ценами». Обещание статьи: **после чтения новичок может отказать лоту или поставить лимит ставки по чек-листу**, а не «узнал, что Harrier красивый».
