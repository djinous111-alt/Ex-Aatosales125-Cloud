research_date: 2026-09-28
accessed_at: 2026-09-28
utility_verdict: PASS
reader_outcome: новичок откроет карточку на encar.com, переведёт её, проверит пять полей и лист Performance Check и сможет сказать "беру на осмотр" или "мимо" до любого депозита
reader_pain: хочу смотреть авто из Кореи, но Encar на корейском, боюсь не понять отчёт и купить битую или со скрученным пробегом машину
success_criteria: по одной живой карточке заполнен мини-чеклист из 7 пунктов (год/пробег/VIN/схема кузова/коды X-W/страховая/стоп-флаг) без оплаты и без посредника
voice_angle: как инструкция к стиральной машине, а не курс для дилеров: вы не обязаны выучить корейский, нужен ритуал "открыл → сверил цифры → закрыл вкладку"
reader_story: человек нашёл "идеальный" Tucson за красивую цену в вонах, включил автоперевод, увидел зелёные галочки, уже пишет в Telegram "берите", а на схеме кузова стоит W на лонжероне и дата Performance Check просрочена больше 120 дней
surprising_fact: в русскоязычных гайдах часто путают коды X и W; официальный Encar Media пишет наоборот официальной логике многих клонов: X = обмен детали (교환), W = рихтовка и сварка (판금·용접), а "чистая" страховая история Carhistory официально называется только вспомогательным документом и не ловит ремонт за наличные

freshness_window_prefer_sources_after: 2026-06-30
year_context: 2026

## research_questions
1. Есть ли у Encar официальная русская версия и какой домен считать первоисточником в 2026?
2. Какие 5–7 полей карточки новичок обязан проверить до любой предоплаты?
3. Что означают коды на листе 성능·상태점검기록부 (Performance Check) по официальным корейским источникам?
4. Сколько действует Performance Check и что делать, если лист просрочен?
5. Чем Trust Encar / диагностика площадки отличается от Carhistory (KIDI) и чего обе базы не показывают?
6. Какие стоп-флаги до депозита понятны человеку без корейского и без опыта импорта?
7. Когда новичку безопаснее отдать проверку подборщику (Авто-Сейлс), а не "дожимать" лот самому?

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Encar Media: как читать Performance Check | https://www.encar.com/mg/post.do?method=view&pagetype=bible&postid=57889&subid=bible4 | accessed_at: 2026-09-28 | официальные коды X/W/C, авария vs навесные панели, гарантия 1 мес / 2000 км |
| Dong-A: срок действия листа 120 дней | https://www.donga.com/news/It/article/all/20250326/131288703/1 | accessed_at: 2026-09-28 | законная обязанность дилера выдавать лист; просрочка = новый осмотр |
| Carhistory EN sample / limitations | https://www.carhistory.kr/guide/sample.page?lang=en | accessed_at: 2026-09-28 | total loss / flood / rental; ремонт без страховки не виден; отчёт auxiliary |
| Carhistory service info (KIDI) | https://www.carhistory.or.kr/serviceInfo/carhistory.page | accessed_at: 2026-09-28 | только страховые выплаты; без детального ремонта |
| Chest Import: пользоваться Encar и читать отчёт | https://chest-import.com/stati/encar-kak-polzovatsya | accessed_at: 2026-09-28 | beginner-first: манвоны, фильтры, 120 дней, границы Encar vs Carhistory |
| Chest Import: проверка авто из Кореи | https://chest-import.com/stati/kak-proverit-avto-iz-korei | accessed_at: 2026-09-28 | связка KIDI + техосмотр Encar; живой осмотр обязателен |
| Carto: Encar гайд 2026 | https://carto-auto.ru/blog/guide-encar/ | accessed_at: 2026-09-28 | конкурент SERP; полезен как карта боли, но коды X/W спорные |
| Altezza: как читать Encar | https://altezza.team/blog/encar-guide.html | accessed_at: 2026-09-28 | структура карточки; миф "аукцион"; Hidden.Y; цена ≠ под ключ |
| Auto.ru logbook: руководство Encar | https://auto.ru/logbook/cars/genesis/g90/23205402/encar-rukovodstvo-po-pokupke-avtomobiley-iz-korei_d4f393d3-6f50-4a36-b773-38b69505a3f0/ | accessed_at: 2026-09-28 | community: перевод лучше на EN, кнопка performance inspection history |
| Habr / Maxilect: плагин к Encar | https://habr.com/ru/companies/maxilect/articles/701354/ | accessed_at: 2026-09-28 | автоперевод ломает цифры и вёрстку - страх новичка подтверждён |
| Top-autoimport: VIN и Performance Check 2026 | https://top-autoimport.ru/blog/kak-proverit-mashinu-iz-korei | accessed_at: 2026-09-28 | X на каркасе = стоп; Rent/Lease как красный флаг |
| GitHub EnCarAPI Python client | https://github.com/ThatMojo/encarapi-python | accessed_at: 2026-09-28 | programmatic vehicle detail включает inspection |
| GitHub encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | accessed_at: 2026-09-28 | сигнал спроса на разбор полей карточки Encar |
| GitHub e9t/encar crawler | https://github.com/e9t/encar | accessed_at: 2026-09-28 | исторический парсер карточек Encar |

## wordstat
Источник: MCP-KV `wordstat_get_top_requests`, регион 225 (Россия), дата запроса 2026-09-28.

| phrase | impressions |
| --- | ---: |
| encar | 32935 |
| encar com | 9003 |
| сайт encar | 4056 |
| encar официальный | 3624 |
| encar корея | 2142 |
| encar на русском | 2036 |
| encar авто | 1533 |
| encar com на русском | 1254 |
| енкар на русском | 1199 |
| сайт encar на русском | 711 |
| encar корея сайт | 700 |
| encar авто из кореи | 688 |
| encar на русском языке | 677 |
| trust encar | 635 |
| проверка авто из кореи | 557 |
| encar на русском официальный | 449 |
| encar на русском официальный сайт | 446 |
| encar авто на русском | 414 |
| проверка кореи авто по вину | 256 |
| carhistory | 171 |

LSI для Writer (не в H1, в подзаголовках/FAQ): сайт encar на русском, encar com на русском языке, енкар на русском, trust encar, проверка авто из кореи, проверка пробега авто из кореи, carhistory.

⚠️ Wordstat secondary note: запрос `как читать encar` вернул неожиданный формат API (`totalCount: 7` без списка фраз) - точные показы по этой фразе не зафиксированы; для семантики опираемся на кластер `encar на русском` + `проверка авто корея`.

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| ThatMojo/encarapi-python | https://github.com/ThatMojo/encarapi-python | клиент EnCarAPI: `vehicle(id)` отдаёт specs + inspection; подтверждает, что лист диагностики - отдельный структурированный блок карточки |
| Mikejkee/encar_scraper_system | https://github.com/Mikejkee/encar_scraper_system | парсер полей Encar + расчёт пошлин - спрос на разбор параметров лота, не только на "купить под ключ" |
| e9t/encar | https://github.com/e9t/encar | ранний crawler карточек Encar; поля бренда/модели исторически вытаскивают из HTML лота |
| autoapicom/auto-api-php | https://github.com/autoapicom/auto-api-php | единый API с source=`encar`; лоты адресуются по listing id как на витрине |

## competitor_gaps
| конкурент | что делает | чего не хватает новичку | наш угол |
| --- | --- | --- | --- |
| carto-auto.ru/guide-encar | длинный SEO-гайд "как купить" | спорные коды X/W; много цен под ключ | ритуал чтения одной карточки + стоп до депозита |
| altezza encar-guide | коды A/B/C, Hidden.Y | мало про 120 дней и Carhistory limitations | связка Performance Check + Carhistory без калькулятора |
| chest-import | сильный how-to | чужой бренд; слабее soft CTA Владивосток | тот же beginner-ритуал + когда звать Авто-Сейлс |
| vc.ru / Rutube / YouTube | опыт заказа | развлекательный формат, мало чеклиста | печатный чеклист 7 пунктов |
| клоны encar-russia / encar.expert | витрина "на русском" | подменяют первоисточник | сначала encar.com, потом каталог Авто-Сейлс |

## verified_facts
1. Официальной русской версии encar.com нет; рабочий путь новичка - перевод браузера или EN-интерфейс, цифры сверять с оригиналом. accessed_at: 2026-09-28. Sources: carto-auto, youcar, habr.
2. Encar - маркетплейс с фиксированной ценой, не классический аукцион с повышением ставки. accessed_at: 2026-09-28. Sources: chest-import, altezza.
3. Performance Check (중고자동차 성능·상태점검기록부) выдаёт сертифицированная площадка; по Encar Media: X = обмен, W = рихтовка/сварка, C = коррозия. accessed_at: 2026-09-28. Source: encar.com media.
4. Аварией в корейском смысле считают ремонт/обмен/сварку силового каркаса; замена внешней панели сама по себе не делает машину "사고차". accessed_at: 2026-09-28. Sources: encar media, donga.
5. Срок действия Performance Check - 120 дней с даты выдачи; просроченный лист силы не имеет. accessed_at: 2026-09-28. Sources: donga 2025-03-26, chest-import 2026-08-14.
6. Гарантия по листу в Корее ориентирно 1 месяц или 2000 км (что наступит раньше) - для покупателя внутри Кореи, не "страховка после Владивостока". accessed_at: 2026-09-28. Sources: encar media, donga.
7. Цена в карточке часто в 만원 (манвонах): 1890 = 18 900 000 ₩; это цена в Корее, не под ключ в РФ. accessed_at: 2026-09-28. Source: chest-import. В статье не публиковать готовые суммы пошлин/утиля - только отправлять в каталог.
8. Carhistory (KIDI) показывает страховые выплаты с 1990-х; официально подчёркивает: это auxiliary info; ремонт за наличные / без покрытия может отсутствовать. accessed_at: 2026-09-28. Source: carhistory.kr guide EN.
9. В отчёте Carhistory смотреть: Total Loss, Theft, Water/Flood, Rental/Business use, суммы Car Damage vs Opponent's Car Damage, число владельцев. accessed_at: 2026-09-28. Source: carhistory sample.
10. Автоперевод Chrome/Яндекса часто ломает вёрстку и цифры на Encar - Habр/Maxilect фиксирует это как причину писать плагин. accessed_at: 2026-09-28. Source: habr.com.
11. Кнопка в карточке: Performance Inspection History / 성능·상태점검기록부; отдельно - Insurance / vehicle history. accessed_at: 2026-09-28. Sources: auto.ru logbook, teletype SERP snippet, chest-import.
12. Trust/диагностика площадки и Carhistory - разные слои: первый про осмотр кузова/узлов, второй про страховые кейсы; оба не заменяют толщиномер и осмотр в Корее. accessed_at: 2026-09-28. Sources: chest-import check guide, carhistory terms.
13. Wordstat (Россия): `encar` ~32.9k, `encar на русском` ~2.0k, `енкар на русском` ~1.2k, `trust encar` ~0.6k, `проверка авто из кореи` ~0.6k. accessed_at: 2026-09-28.

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| Не понимаю корейский интерфейс (pain) | Открыть encar.com → перевод Chrome/Яндекс → цифры и коды сверить с оригиналом (solution) | carto-auto; habr Maxilect; auto.ru logbook | result: карточка читается по-русски без "официального сайта на русском" |
| Боюсь купить битую, не зная X/W (pain) | Открыть Performance Check: X=обмен, W=сварка/рихтовка, C=коррозия; W/X на каркасе = стоп (solution) | encar.com media; donga; top-autoimport | result: один взгляд на схему кузова даёт вердикт "можно смотреть дальше / закрыть" |
| Верю красивому пробегу в объявлении (pain) | Сверить пробег в карточке с пробегом на листе; флаг неисправности одометра = не гарантируют пробег (solution) | donga (계기상태); encar media | result: поймана развилка "пробег ок / пробег не доверяем" |
| Думаю, что "без ДТП в страховке" = идеал (pain) | Прочитать Carhistory как вспомогательный отчёт: смотреть total loss/flood/rental и суммы, помнить про ремонт за наличные (solution) | carhistory.kr EN guide; chest-import | result: нет ложного зелёного света только из-за пустой страховки |
| Путаю клон "Encar на русском" с первоисточником (pain) | Сначала лот на encar.com, русские витрины - только как удобный перевод с наценкой (solution) | carto-auto; youcar FAQ; SERP клоны | result: новичок знает, откуда брать цену и VIN |
| Не знаю, когда остановиться и позвать людей (pain) | Чеклист стоп-флагов → если 2+ красных или нет листа/VIN - в Telegram Авто-Сейлс / каталог, не депозит (solution) | site-brief CTA; chest-import; fact-bank | result: безопасный выход без стыда "я ничего не понял" |

## action_outline
1. Открыть официальный encar.com (не клон) и включить перевод страницы; решить, что цифры смотрите в оригинале.
2. Выбрать один лот из выдачи и выписать с карточки: год/регистрация, пробег, объём/топливо, цена в вонах или манвонах, VIN.
3. Открыть фотогалерею: есть ли VIN-табличка, днище/проёмы, салон; если фото 5–7 и без VIN - пометить как риск.
4. Нажать Performance Check / 성능·상태점검기록부 и проверить дату листа (не старше 120 дней) и подписи.
5. На схеме кузова найти коды X / W / C / U / A; отдельно отметить, есть ли метки на силовом каркасе (лонжероны, стойки, крыша).
6. Сверить пробег объявления с пробегом на листе; если стоит неисправность одометра - поставить стоп.
7. Открыть страховую историю / Carhistory-слой: total loss, flood, rental/business, крупные суммы выплат; помнить, что ремонт за наличные может отсутствовать.
8. Пройти мини-чеклист из 7 пунктов и вынести вердикт: "на независимый осмотр" или "мимо".
9. Если вердикт сомнительный или лот хочется взять - не слать депозит самому: отправить ссылку лота в каталог / Telegram Авто-Сейлс для проверки под ключ.

## writer_brief
- H1 держать близко к карточке AS02: "Encar на русском: как читать объявления и не купить кота в мешке".
- Lead = reader_story (Tucson + W на лонжероне + просроченный лист).
- H2 закрывают pain_solution_map; до FAQ обязателен заполненный чеклист как success_criteria.
- Не путать Trust Encar (диагностика/бренд проверки площадки) и Carhistory (KIDI страховая база) - это разные кнопки/отчёты.
- Запрет редакции: без готовых сумм пошлин/утильсбора и без выдуманных VIN/лотов; CTA только каталог + @avtosales125.
- Не упоминать Wordstat/Метрику в тексте статьи.
- Тире: среднее "–", кавычки прямые "..."; без эмодзи.
- FAQ-заготовки: "есть ли официальный Encar на русском?"; "что такое Trust Encar?"; "можно ли верить пробегу?"; "что значат X и W?"; "когда звать подборщика?".

## angle_vs_cannibalization
Смежные темы пула: AS09 Trust/Carhistory (глубже отчёты), AS01/AS08 про заказ из Кореи. AS02 = только ритуал чтения карточки Encar на русском до депозита. Не уходить в полный импорт/растаможку и не дублировать глубокий разбор Carhistory - только связка "где кнопка и что стоп".
