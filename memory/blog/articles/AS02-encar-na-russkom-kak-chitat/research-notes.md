research_date: 2026-11-03
accessed_at: 2026-11-03
utility_verdict: PASS
prefer_sources_after: 2026-08-05
reader_outcome: новичок открывает карточку на encar.com через перевод браузера, выписывает 5–7 полей (цена в вонах, год/месяц, пробег, VIN, топливо/объём, схема кузова, страховая сводка) и до депозита понимает, брать ли лот дальше или отложить
reader_pain: человек гуглит "encar на русском", попадает на клоны посредников, включает переводчик и всё равно не понимает: что такое "무사고", сколько стоит машина в рублях, какие буквы на схеме кузова опасны, и боится перевести депозит "на красивые фото"
success_criteria: у новичка есть заполненный мини-чеклист по одному реальному объявлению; он отличает навесные панели от силового каркаса; знает, что чистый CarHistory ≠ "никогда не били"; депозит не отправляет, пока VIN и свежий лист проверки не сверены
voice_angle: спокойный разговор "как читать меню на чужом языке в кафе": переводчик даёт слова, а смысл полей даём мы; без геройства "купи сам из Кореи за вечер" и без запугивания таможней
reader_story: Андрей из Новосибирска нашёл на зеркале "Encar на русском" белый Tucson "без ДТП" дешевле рынка на 400 тысяч, уже написал "бронируем?" – а в оригинальной карточке на encar.com у машины W на передней панели и пометка проката; депозит ещё не ушёл, и статья вовремя останавливает его рукой "сначала схема кузова, потом эмоции"
surprising_fact: в Корее ярлык "무사고 / без аварий" официально означает только то, что силовой каркас не варили и не меняли; капот, крылья и двери могли заменить, а в карточке всё равно будет "без аварий + простой ремонт" – это не ложь продавца, а корейское определение аварии

## research_questions
1. Есть ли у Encar официальный русский интерфейс в 2026, или только перевод браузера и зеркала посредников?
2. Какие поля карточки новичок обязан выписать до разговора о депозите?
3. Как читать буквы X / W / A / U / C / T и чем "사고" отличается от "단순수리"?
4. Чем отличаются обязательный лист 성능·상태점검기록부, бейдж Encar Diagnosis и российский бренд Trust Encar?
5. Что даёт CarHistory (KIDI) и какие у него дыры до оплаты?
6. Какие красные флаги заставляют отложить лот и когда логично отдать проверку подборщику во Владивостоке?

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Official CarHistory EN (KIDI) | https://www.carhistory.or.kr/main.car?lang=en | accessed_at: 2026-11-03 | Официальная цена отчёта KRW 2 200; страховые выплаты с 1996; прямо пишет, что ДТП без страховки могут не попасть |
| Encar Diagnosis intro | https://car.encar.com/diagnosis/intro | accessed_at: 2026-11-03 | Бейджи 진단 / 진단+ / 진단++: проверка каркаса Encar, не замена обязательного листа |
| Encar Global Export RU | https://global.encar.com/export-service/intro?lang=ru | accessed_at: 2026-11-03 | Официальный экспортный контур через сертифицированных партнёров; розничный "купить самому с карты РФ" не обещан |
| How to read Encar inspection (Oct 2026) | https://auctionsapi.com/articles/encar-inspection-report | accessed_at: 2026-11-03 | Свежий гайд: коды X/W/C/A/U/T, ранги панелей, 사고 vs 단순수리, Diagnosis ≠ лист |
| Азия Авто: Encar 2026 | https://aa-dv.ru/encar.html | accessed_at: 2026-11-03 | Обязательность листа по закону, срок осмотра, смысл "무사고", блок страховой истории |
| AZWAY: проверка авто из Кореи | https://azway.ru/blog/proverka-avto-iz-korei-encar | accessed_at: 2026-11-03 | Цепочка до оплаты: карточка → VIN → CarHistory → лист → живой осмотр; задержка страховых данных ~2,5–3 мес |
| Car Hunt: Encar на русском | https://car-hunt.ru/blog/encar-na-russkom | accessed_at: 2026-11-03 | Нет русской версии; клоны в SERP; перевод браузера; Encar не аукцион с таймером |
| Chrome Help: перевод страниц | https://support.google.com/chrome/answer/173424?hl=ru | accessed_at: 2026-11-03 | Практический шаг для новичка: кнопка "Перевести" |
| Trust Encar (RU company site) | https://trust-encar.ru/ | accessed_at: 2026-11-03 | Показывает, что "Trust Encar" в РФ – посредник/логистика, не кнопка внутри encar.com |
| GitHub sample history check | https://github.com/piotrv1001/how-to-check-encar-vehicle-history-in-nodejs | accessed_at: 2026-11-03 | Сигнал сообщества: смотреть accidentRecord + inspection + diagnosis вместе |

## wordstat
⚠️ WORDSTAT AUTH WARNING: MCP-сервер MCP-KV (wordstat_get_top_requests) недоступен – live tool discovery failed. Точные показы в месяц не получены; цифры спроса не выдумывать. Обновление OAuth-токена Wordstat (если проблема в токене после починки MCP): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

| phrase | impressions |
| --- | --- |
| encar на русском | н/д (Wordstat MCP unavailable 2026-11-03) |
| как читать encar | н/д (Wordstat MCP unavailable 2026-11-03) |
| проверка авто корея | н/д (Wordstat MCP unavailable 2026-11-03) |

Экспертная семантика без объёмов (LSI для Writer, не как verified demand): перевод encar, энкар на русском, лист диагностики encar, carhistory корея, trust encar, 무사고 что значит, скрутка пробега корея, проверка до депозита.

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| piotrv1001/how-to-check-encar-vehicle-history-in-nodejs | https://github.com/piotrv1001/how-to-check-encar-vehicle-history-in-nodejs | README советует не сводить историю к одному флагу "accident"; сравнивать insurance + inspection + diagnosis |
| ThatMojo/encarapi-node | https://github.com/ThatMojo/encarapi-node | Отдельные эндпоинты vehicle / inspection / record – подтверждает, что у лота несколько слоёв документов |
| xapiauto/xapikorea-python | https://github.com/xapiauto/xapikorea-python | get_inspection и get_insurance раздельно; отсутствие отчёта = unknown, не "чистая" |
| M1g3l14Ka/sellercars | https://github.com/M1g3l14Ka/sellercars | Парсеры явно умножают цену ×10 000 (만원) – критичный факт для новичка |
| Mikejkee/encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | Сбор страховки и диагностики вместе с карточкой – тот же пайплайн, что нужен человеку до депозита |

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| pain: "ищу Encar на русском и кликаю первый сайт из выдачи" | solution: открывать только encar.com / global.encar.com; зеркала .ru – посредники, не "официальный русский Encar" | https://car-hunt.ru/blog/encar-na-russkom ; https://global.encar.com/export-service/intro?lang=ru | reader_result: человек знает два настоящих домена и не платит "официальному Encar", которого нет |
| pain: "переводчик перевёл страницу, а я всё равно не понимаю цену и год" | solution: цена в 만원 × 10 000 = воны; отдельно смотреть 연식 / первую регистрации; топливо и объём выписать до восторга от фото | https://aa-dv.ru/encar.html ; GitHub sellercars (×10000) | reader_result: на листке есть цена в вонах и год/месяц без путаницы "модель 2021 / регистрация 2022" |
| pain: "написано без аварий – значит можно бронировать" | solution: читать схему кузова: X=замена, W=рихтовка/сварка; на силовых – стоп; 무사고 ≠ "не красили" | https://auctionsapi.com/articles/encar-inspection-report ; https://aa-dv.ru/encar.html | reader_result: новичок отличает "простой ремонт крыла" от "варили каркас" |
| pain: "боюсь скрутки и скрытого такси/проката" | solution: сверить пробег в объявлении, листе и CarHistory; искать 렌트 / 영업용 / частые смены владельца | https://www.carhistory.or.kr/main.car?lang=en ; https://azway.ru/blog/proverka-avto-iz-korei-encar | reader_result: при расхождении пробега или коммерческом прошлом лот уходит в "отложить" |
| pain: "путаю Trust Encar, Diagnosis и CarHistory" | solution: Diagnosis – бейдж проверки Encar; CarHistory – страховая база KIDI; Trust Encar в РФ – отдельная компания-посредник; глубокий разбор связки – тема AS09 | https://car.encar.com/diagnosis/intro ; https://trust-encar.ru/ ; CarHistory | reader_result: человек не путает три разных инструмента и не считает бейдж заменой живого осмотра |
| pain: "хочу уже внести депозит, пока лот не ушёл" | solution: до денег – скрин карточки, VIN, свежая дата листа, сверка страховой сводки, отказ если VIN не дают | https://azway.ru/blog/proverka-avto-iz-korei-encar ; vinlid/auctionsapi guides | reader_result: депозит только после короткого чеклиста или передачи лота подборщику Авто-Сейлс |

## action_outline
1. Открыть encar.com в Chrome или Яндекс.Браузере → "Перевести на русский"; закладку на клон .ru не считать официальной версией.
2. Выбрать одно объявление "под себя" и выписать: цена (만원×10000), год/месяц, пробег, топливо, объём, коробка, цвет, корейский номер и VIN.
3. Открыть лист 성능·상태점검기록부: сверить VIN и дату осмотра; на схеме сначала силовые элементы, потом навесные; запомнить X/W/A/U/C/T.
4. Прочитать страховую сводку в карточке и (если доступен VIN) ориентир CarHistory: выплаты, затопление, смена владельцев, прокат; помнить про ремонт "за наличные" вне базы.
5. Отметить красные флаги: отказ дать VIN, X/W на каркасе, 침수/화재, такси/прокат без адекватной цены, старый лист, противоречие "무사고" vs крупные выплаты.
6. Если флаги есть или термины всё ещё каша – не депозит, а запрос подборщику Авто-Сейлс (Владивосток) с ссылкой на лот; детальную связку Trust/Carhistory до депозита раскрывать в AS09, здесь – мост "что проверить самому за 20 минут".

## facts_for_writer
| claim | url | accessed_at | note |
| --- | --- | --- | --- |
| Официальной русской версии encar.com нет; в SERP много зеркал посредников | https://car-hunt.ru/blog/encar-na-russkom | 2026-11-03 | Lead + H2 про перевод |
| Цена на Encar часто в единицах 만원 (= ×10 000 вон) | https://aa-dv.ru/encar.html ; sellercars README | 2026-11-03 | Мини-пример пересчёта без "цены под ключ" |
| 무사고 = нет ремонта силового каркаса; простой ремонт навесных допустим при ярлыке "без аварий" | https://aa-dv.ru/encar.html ; https://auctionsapi.com/articles/encar-inspection-report | 2026-11-03 | Центральный surprising_fact |
| Коды схемы: X замена, W рихтовка/сварка, C коррозия, A царапина, U вмятина, T повреждение | https://auctionsapi.com/articles/encar-inspection-report | 2026-11-03 | Таблица-глоссарий |
| Обязательный лист пишет инспекция, не "сам Encar"; Encar Diagnosis – отдельный бейдж | https://auctionsapi.com/articles/encar-inspection-report ; https://car.encar.com/diagnosis/intro | 2026-11-03 | Не путать слои |
| CarHistory: ~KRW 2 200/отчёт; данные страховых с 1996; ДТП без страховки могут отсутствовать | https://www.carhistory.or.kr/main.car?lang=en | 2026-11-03 | Без выдуманных VIN |
| Свежие страховые события могут появляться с задержкой порядка 2,5–3 месяцев | https://azway.ru/blog/proverka-avto-iz-korei-encar | 2026-11-03 | "Чистая" свежая машина ≠ гарантия |
| Экспортный контур Encar Global – через партнёров, не "оплата с телефона в РФ на encar.com" | https://global.encar.com/export-service/intro?lang=ru | 2026-11-03 | Мягкий мост к подборщику |
| Trust Encar в русскоязычном поиске часто = компания-посредник, не кнопка внутри Encar | https://trust-encar.ru/ | 2026-11-03 | FAQ "что такое Trust Encar" |
| Не публиковать готовые суммы пошлин/утильсбора; расчёт – в каталоге | memory/brief/fact-bank.md | 2026-11-03 | Редполитика Авто-Сейлс |

## competitor_gaps
- Много гайдов сразу прыгают в "полный заказ под ключ" или прайс-таблицы – у нас фокус: 20 минут чтения одной карточки до депозита.
- Клоны продают себя как "Encar на русском" – мы явно разделяем площадку и посредника.
- Глубокий Trust + CarHistory до депозита не раздувать: мост на AS09; здесь глоссарий + чеклист + красные флаги.

## writer_must_use
- Сценарий Андрея с Tucson и W на передней панели.
- Таблица-глоссарий полей + букв схемы.
- Чеклист "до депозита" из action_outline.
- Фраза-якорь: "무사고 – это про каркас, не про идеальный кузов".
- CTA мягкий: каталог / Telegram avtosales125 без форм на странице; без выдуманных лотов и сумм растаможки.
