research_date: 2026-11-02
accessed_at: 2026-11-02
utility_verdict: PASS
reader_outcome: новичок откроет карточку лота на Encar (или в русскоязычном зеркале), выпишет 5 полей (VIN, цена в манвонах, пробег, тип владения, Performance Check), отметит красные флаги X/W на силовых и сверит историю через Carhistory / посредника до любого депозита
reader_pain: интерфейс на корейском, «без ДТП» выглядит как зелёный свет, а человек боится купить битое или утопленное, путая сайт-посредник «Trust Encar / Encar на русском» с самой площадкой и с отчётом проверки
success_criteria: у читателя есть заполненный мини-чеклист по одной реальной карточке; он умеет объяснить, что значит X и W, почему «ремонт есть / ДТП нет» не равно «идеал», и знает, когда остановиться и отдать лот подборщику
voice_angle: спокойный разговор механика во Владивостоке с человеком, который впервые открыл Encar и уже влюбился в красивые фото; без пафоса «экспортёра», с иронией про «кота в мешке» и прямой инструкцией «сначала поля, потом эмоции»
reader_story: Антон из Хабаровска перевёл страницу браузером, увидел «사고이력 없음 / без ДТП», цену «дешевле рынка» и уже писал посреднику про депозит – а на схеме кузова стоял W на лонжероне, а VIN он так и не сверил с Carhistory
surprising_fact: отметка «ДТП: нет» на корейском листе часто означает только то, что не трогали силовые элементы; замена капота или крыла при этом спокойно живёт рядом как «простой ремонт» – красивые фото и зелёная галочка не отменяют схему кузова (AuctionsAPI, 2026-10-01; практики AutoKoreaGroup / SferaCar)

## research_questions
1. Что новичок должен выписать из карточки Encar до разговора о деньгах?
2. Как читать Performance Check (성능점검): коды X/W/C/A/U/T и где «стоп»?
3. Чем Insurance History / Carhistory отличается от листа осмотра и почему «чистая» страховка не спасает от скрытого ремонта?
4. Как не перепутать официальный encar.com / global.encar.com с русскими зеркалами и брендом Trust Encar в выдаче?
5. Когда чтение карточки своими руками уже недостаточно и нужен подборщик / осмотр во Владивостоке?

## differentiation
- Live WP уже имеет близкий пост `encar-na-russkom-kak-chitat-obyavleniya-i-bezopasno-kupit-avto` (угол «объявления + безопасно купить»). AS02 не копирует чужой текст и не разворачивает полный цикл покупки/растаможки.
- AS09 закрывает «до депозита» глубже (Trust Encar vs инструменты + Carhistory-чеклист). AS02 = beginner how-to **чтения карточки**: 5 полей → красные флаги → короткий мост к Trust Encar/Carhistory → когда отдать проверку.
- Freshness window prefer_sources_after: 2026-08-04; приоритет источников октября–ноября 2026 и официальных docs.

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Encar official llms.txt – 엔카진단 / 엔카믿고 | https://www.encar.com/llms.txt | accessed_at: 2026-11-02 | Официальные уровни диагностики и сервисов площадки; не путать с RU-посредниками |
| Encar Export (RU intro) | https://global.encar.com/export-service/intro?lang=ru | accessed_at: 2026-11-02 | Официальный экспорт только через сертифицированных партнёров; 3 шага выбора лота |
| Carhistory RU | https://www.carhistory.or.kr/main.car?lang=ru&retUrl= | accessed_at: 2026-11-02 | Страховая история с 1996; fee 2 200 вон; disclaimer про незаявленные ДТП; flood free |
| Carhistory EN search fee | https://www.carhistory.kr/search/carhistory/search.car?lang=en | accessed_at: 2026-11-02 | Подтверждение стоимости отчёта KRW 2,200 incl. VAT |
| Carhistory flood free | https://www.carhistory.kr/search/carhistory/freeSearch.car?lang=en | accessed_at: 2026-11-02 | Бесплатная проверка затопления по страховым записям |
| AuctionsAPI: how to read inspection (Oct 1, 2026) | https://auctionsapi.com/articles/encar-inspection-report | accessed_at: 2026-11-02 | Канон кодов X/W/C/A/U/T, ранг панелей vs каркас, red flags; лист пишет цех, не Encar |
| Chest Import: пользоваться Encar (14 Aug 2026) | https://chest-import.com/stati/encar-kak-polzovatsya | accessed_at: 2026-11-02 | Манвоны, фильтры, границы диагностики, Carhistory + экспорт ≥2.0 л |
| Car Hunt: Encar на русском | https://car-hunt.ru/blog/encar-na-russkom | accessed_at: 2026-11-02 | Нет «официальной русской версии»; перевод браузера; клоны в выдаче |
| Altezza: история / пробег | https://altezza.team/blog/kak-proverit-istoriyu-avto-na-encar.html | accessed_at: 2026-11-02 | Пробег растёт год к году; провалы = скрутка; отчёт ≠ ресурс агрегатов |
| SferaCar: как читать отчёт | https://korean.sferacar.ru/stati/kak-chitat-otchet-encar.html | accessed_at: 2026-11-02 | Читать совокупность: VIN, пробег, страховка, схема, техника |
| Trust Encar (RU посредник) | https://trust-encar.ru/ | accessed_at: 2026-11-02 | Коммерческий канал в выдаче «Trust Encar»; не кнопка проверки |
| AIM Group: Encar Trust rebrand | https://aimgroup.com/2024/06/21/encar-com-to-consolidate-transaction-brands-under-encar-trust-banner/ | accessed_at: 2026-11-02 | В Корее «Encar Trust / 엔카믿고» – сервис площадки; путаница с RU-брендом |
| Encar Russia disclaimer | https://encar-russia.ru/otkaz-ot-otvetstvennosti/ | accessed_at: 2026-11-02 | Сами признают: не продавцы и не официальные представители encar.com |
| Community client Encar-easy | https://github.com/Dmitriy190424/Encar-easy | accessed_at: 2026-11-02 | Community-клиент к данным Encar через публичный интерфейс данных |
| Community encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | accessed_at: 2026-11-02 | Парсеры тянут диагностику/страховку – сигнал, какие поля важны |

## wordstat
status: UNAVAILABLE
reason: MCP namespace `MCP-KV` / `user-mcp-kv` failed live tool discovery; `wordstat_get_top_requests` недоступен в этом run (не 401, а transport/discovery error).
rule: точные показы в месяц **не выдумывать**.

| phrase | impressions |
| --- | --- |
| encar на русском | UNAVAILABLE |
| как читать encar | UNAVAILABLE |
| проверка авто корея | UNAVAILABLE |
| trust encar | UNAVAILABLE (см. AS09 snapshot 2026-07-17 только как ориентир семантики, не как свежий замер) |
| carhistory | UNAVAILABLE |

LSI для копирайтера (из SERP/WebSearch 2026-11-02, без объёмов): Performance Check, 성능점검, Insurance History, 보험이력, X/W на лонжероне, Carhistory, VIN, манвон, 엔카진단, утопленник/flood, перевод браузера, клоны encar-russia / trust-encar.

⚠️ WORDSTAT UNAVAILABLE WARNING: точные объёмы спроса не получены. При восстановлении MCP-KV повторить `wordstat_get_top_requests` для primary/secondary. Auth URL (если будет 401): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| Dmitriy190424/Encar-easy | https://github.com/Dmitriy190424/Encar-easy | Лёгкий клиент к полям Encar – карточка = набор проверяемых значений, не «картинка» |
| Mikejkee/encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | Скрапер под Encar (обновлялся 2026-09) – спрос на разбор лотов по полям диагностики |
| i146akm/encarnn | https://github.com/i146akm/encarnn | Пайплайн тянет машину, страховку, диагностику – те же блоки, что новичок читает вручную |
| AuctionsAPI help article (inspection) | https://auctionsapi.com/articles/encar-inspection-report | Гайд/справка по полям inspection – proof, что X/W и conclusions читаемы одинаково |
| Encar public machine-readable summary | https://www.encar.com/llms.txt | Официальное краткое описание сервисов 엔카진단 / 엔카믿고 для машинного и человеческого чтения |

## fact_bank_check
| факт | статус | note |
| --- | --- | --- |
| Авто-Сейлс: привоз из Японии/Кореи/Китая, офис Владивосток | OK | memory/brief/fact-bank.md |
| Не публиковать готовые суммы пошлин/утильсбора как калькулятор | OK | только отсылка в каталог |
| Не выдумывать VIN/лоты/цены авто | OK | в статье – только методика чтения |
| CTA: каталог + Telegram avtosales125, без форм на странице | OK | site-brief |

## pain_solution_map
| боль (pain) | решение (solution) | proof/source | результат (reader_result) |
| --- | --- | --- | --- |
| боль: Не понимаю корейский интерфейс / кажется, что Encar «только для профи» | решение: Открыть encar.com + перевод браузера; помнить: официальных «encar на русском» от самой площадки почти нет, RU-сайты – посредники | car-hunt.ru/blog/encar-na-russkom; encar-russia.ru disclaimer; global.encar.com | результат: Читатель отличает площадку от зеркала и не платит «как официальному Encar» |
| боль: Боюсь не понять термины и купить «кота в мешке» | решение: Чеклист 5 полей: VIN, цена (만원), пробег, 용도/General|Lease|Rental, кнопка Performance Check | auctionsapi.com inspection guide; chest-import; car-hunt | результат: Заполненный лист по одному лоту до любого чата о депозите |
| боль: «Без ДТП» усыпляет – страшно пропустить битое | решение: Учить: X=замена, W=правка/сварка; на силовых (лонжерон, стойка, пол) – стоп; «ДТП нет + ремонт да» нормально для навесных | auctionsapi 2026-10-01; sferacar; Altezza guide | результат: Читатель читает схему кузова, а не только галочку |
| боль: Не знаю, верить ли пробегу | решение: Сверять хронологию одометра в страховой/Carhistory; провал год к году = красный флаг; износ салона vs цифра | altezza.team history; sferacar; carhistory disclaimer | результат: Решение «смотреть дальше / отложить лот» без самообмана |
| боль: Путаю Trust Encar, Encar Trust и Carhistory | решение: Trust Encar в RU-выдаче часто = посредник; 엔카믿고/Encar Trust = сервис площадки в Корее; Carhistory = страховой отчёт по VIN; Performance Check = лист состояния | trust-encar.ru; aimgroup 2024; carhistory.or.kr; encar.com/llms.txt; AS09 angle | результат: Понимает, какой инструмент за что отвечает, и идёт к подборщику / материалу AS09 за полной проверкой до депозита |

## action_outline
1. Открыть официальный `encar.com` (или карточку в каталоге Авто-Сейлс) и включить перевод браузера – не путать с `encar-russia.ru` / `trust-encar.ru` / `encar.com.ru`.
2. Выписать пять полей: VIN (차대번호), цена в манвонах (1万 = 10 000 вон), пробег км, тип владения (General vs Lease/Rental), дата/наличие Performance Check.
3. Открыть Performance Check (성능점검): сначала галочки flood/fire/odometer/VIN marking, потом схема кузова.
4. На схеме найти X и W: навесные панели – торг/осторожность; силовые элементы – стоп до осмотра.
5. Сверить Insurance History / заказать Carhistory по VIN (около 2 200 вон) + бесплатный flood-check; помнить: незаявленные в страховую случаи не видны.
6. Сверить пробег: хронология только растёт; «слишком мало для возраста» + идеальный салон = повод насторожиться, не радоваться.
7. Красные флаги до депозита: нет VIN, нет листа у дилера, W/X на каркасе, flood/fire, Lease без закрытия, цена «слишком сладкая» без объяснения, отказ прислать фото VIN/одометра.
8. Если хоть один стоп-флаг или язык/отчёт «плывут» – остановить оплату и отдать лот подборщику Авто-Сейлс (каталог / Telegram); полный чеклист до депозита – в связке с материалом про Trust Encar и Carhistory.

## competitor_gap
Конкуренты дают либо «как купить под ключ», либо длинный разбор всего рынка. Свободная ниша AS02: короткий beginner-first разбор **чтения одной карточки** + таблица красных флагов + ясное разведение зеркал/Trust Encar/Carhistory без дубля AS09 и без копирования live-поста про «безопасно купить».
