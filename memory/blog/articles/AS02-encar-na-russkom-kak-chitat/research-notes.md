# Research notes — AS02

research_date: 2026-11-03
accessed_at: 2026-11-03
utility_verdict: PASS
prefer_sources_after: 2026-08-05
topic_id: AS02
slug: encar-na-russkom-kak-chitat
h1: Encar на русском — как читать объявления и не купить "кота в мешке"
primary_query: encar на русском
search_intent: how_to
article_mode: B

reader_pain: Новичок открывает Encar через переводчик, видит ярлык "без ДТП" и низкий пробег, но не понимает корейские пометки на схеме кузова и боится перевести депозит за машину, которую на фото "как новая", а по документам уже чинили.
reader_outcome: После статьи новичок сам откроет карточку Encar, переведёт страницу, пересчитает цену из 만원, сохранит VIN и ID лота, прочитает схему кузова и страховую выжимку и составит короткий список "ок / стоп / отдать подборщику" до любого депозита.
success_criteria: У человека на руках чеклист из 8–10 пунктов, в заметках совпадают VIN и ID объявления, на схеме кузова он отличает навесные панели от силовых (X/W), а на "чистый" CarHistory не ставит точку без свежего протокола и живого осмотра.
voice_angle: Спокойный разговор из Владивостока: "переводчик помогает с меню, но не спасает от кота в мешке – смотрим схему и историю, а не красивый ярлык".
reader_story: Человек нашёл "идеальный" Tucson с пометкой 무사고, перевёл страницу как "без аварий", скинул предоплату посреднику, а потом узнал: капот и крыло были заменены, крупная страховая выплата по своей машине нашлась в CarHistory, а "Trust Encar" в выдаче оказался чужим сайтом-посредником, а не проверкой Encar.
surprising_fact: В корейских правилах 무사고 / "без аварий" обычно значит, что не чинили силовой каркас; замена капота, крыла, двери или багажника может остаться "простым обменом". По разбору Vinlid по ~1,5 млн протоколов "аварийный" ярлык был у ~14,4% машин, а хотя бы одну панель меняли примерно у 4 из 10 – ярлык может быть честным и всё равно не равняться "заводской краске".

## research_questions
1. Как новичку открыть Encar на русском без отдельного "русского Encar" и не потерять ID лота?
2. Что означает 만원 в цене и какие поля карточки смотреть первыми?
3. Чем 무사고 отличается от реальной картины кузова (X / W / 판금 / 용접)?
4. Что даёт CarHistory (카히스토리) и какие у него слепые зоны до депозита?
5. Чем 엔카진단 (Encar Diagnosis) отличается от 엔카믿고 (Encar Trust / Meetgo) и от RU-сайтов "Trust Encar"?
6. Какие красные флаги пробега, ДТП, проката и утопа останавливают оплату?
7. Когда безопасно отдать проверку подборщику Авто-Сейлс вместо самостоятельной "охоты" по скринам?

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Encar Diagnosis intro (официально) | https://car.encar.com/diagnosis/intro | accessed_at: 2026-11-03 | Уровни 진단 / 진단+ / 진단++; проверка каркаса; гарантия Encar 90 дней / 5 000 км |
| Encar llms.txt (официальный обзор сервисов) | https://www.encar.com/llms.txt | accessed_at: 2026-11-03 | Разводит 엔카진단 и 엔카믿고; Meetgo = доставка/визит + возврат 7 дней в Корее |
| CARHISTORY RU | https://www.carhistory.or.kr/main.car?lang=ru&retUrl= | accessed_at: 2026-11-03 | Официальная страховая история; 2 200 вон; бесплатный flood; disclaimer про незаявленные ДТП |
| XAPI Korea: Encar in English / key terms | https://xapikorea.com/blog/how-to-use-encar-in-english | accessed_at: 2026-11-03 | Перевод браузера, 만원×10 000, словарь 무사고 / 보험이력 / 침수 / 전손 |
| Vinlid: How to buy on Encar | https://vinlid.com/blog/how-to-buy-a-car-on-encar | accessed_at: 2026-11-03 | Ловушка 무사고; 14,4% vs ~40% panel replace; VIN до брокера; медианный пробег |
| BIC: проверка авто из Кореи | https://bic-auto.ru/blog/kak-proverit-avto-iz-korei | accessed_at: 2026-11-03 | Коды X/W/C/A/U/T; протокол ≤120 дней; CarHistory слепые зоны; красные флаги до оплаты |
| AZWAY: проверка Encar / VIN / осмотр | https://azway.ru/blog/proverka-avto-iz-korei-encar | accessed_at: 2026-11-03 | Цепочка карточка → VIN → страховая → протокол → осмотр до оплаты |
| SferaCar: как читать отчёт Encar | https://korean.sferacar.ru/stati/kak-chitat-otchet-encar.html | accessed_at: 2026-11-03 | Пошаговое чтение истории, выплат и схемы; противоречия документов |
| Altezza: история на Encar | https://altezza.team/blog/kak-proverit-istoriyu-avto-na-encar.html | accessed_at: 2026-11-03 | Кнопка 카히스토리 в карточке; перевод; пробелы в пробеге |
| KingStone Motors: accident history for buyers | https://kingstonemotors.com/blog/check-korean-car-accident-history-encar-uae/ | accessed_at: 2026-11-03 | Коды формы осмотра; Diagnosis ≠ механика; средний пробег ~13 100 км/год (KOTSA) |

## wordstat

⚠️ WORDSTAT AUTH WARNING: Токен / сервер Wordstat недоступен в этом run. MCP namespace `MCP-KV` вернул `namespaceStatus: error` (live tool discovery failed; при вызове – "MCP server does not exist"). Точные показы в месяц **не получены и не выдуманы**. Обновите авторизацию Wordstat: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

Попытка: `wordstat_get_top_requests` для primary_query `encar на русском` и смежных `как читать encar`, `проверка авто корея` – **failed / unavailable**.

| phrase | impressions |
| --- | --- |
| encar на русском | unavailable (MCP-KV down) |
| как читать encar | unavailable (MCP-KV down) |
| проверка авто корея | unavailable (MCP-KV down) |
| trust encar | unavailable this run; historical AS09 research (2026-07-17) once saw ~579 – **не использовать как факт 2026-11-03** |
| carhistory | unavailable this run; historical AS09 ~105 – **не использовать как факт 2026-11-03** |

### LSI / семантика без объёмов (для Writer, не для текста статьи как "данные Wordstat")
- encar на русском, энкар, fem.encar.com, переводчик Chrome / Papago
- как читать encar, схема кузова, 성능점검, 무사고, X W
- проверка авто корея, VIN, carhistory, страховая история, утопленник
- trust encar / энка диагностик / энка митго (развести посредника и сервис)
- депозит, осмотр до оплаты, пробег, прокат, такси LPG

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| ThatMojo/encarapi-python README | https://github.com/ThatMojo/encarapi-python | Community/client access to Encar listings + inspection + accident/ownership records (не "русский сайт", а сигнал что данные лота машиночитаемы) |
| xapiauto/xapikorea-python README | https://github.com/xapiauto/xapikorea-python | Неофициальный SDK: Encar/KB search, inspection + insurance fields; подчёркивает независимость от Encar |
| ThatMojo/encarapi-node README | https://github.com/ThatMojo/encarapi-node | `frame_clean`, `inspection`, `record` – отдельные сущности; coincится с советом не схлопывать историю в один boolean |
| piotrv1001/how-to-check-encar-vehicle-history-in-nodejs | https://github.com/piotrv1001/how-to-check-encar-vehicle-history-in-nodejs | Практический пример: сравнивать `accidentRecord`, `inspection`, `diagnosis` вместе |
| markolofsen/carapis-encar-npm | https://github.com/markolofsen/carapis-encar-npm/ | Ещё один клиент к Encar-данным; подтверждает спрос на программную выгрузку карточек |
| Carapis Encar API docs | https://carapis.com/docs | Developer docs к Encar-данным (third-party); сигнал что inspection/history доступны программно |
| Community / official docs mirror | https://www.encar.com/llms.txt | Официальное текстовое описание Diagnosis vs Meetgo для AI/docs crawlers |
| Community guide | https://xapikorea.com/blog/how-to-use-encar-in-english | Живой beginner-гайд по переводу и терминам (не GitHub, но community evidence) |

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| pain: "Всё на корейском, кажется, что Encar только для местных" | solution: Встроенный перевод Chrome/Edge/Safari или Papago; сохранить ID из URL `fem.encar.com/cars/detail/...` | https://xapikorea.com/blog/how-to-use-encar-in-english | reader_result: Страница читается по-русски/английски, лот можно скинуть подборщику одним ID |
| pain: "Переводчик показал 'без аварий' – значит кузов идеальный" | solution: Читать схему протокола: X=замена, W=рихтовка/сварка; 무사고 ≈ каркас, не "никогда не красили" | https://vinlid.com/blog/how-to-buy-a-car-on-encar ; https://bic-auto.ru/blog/kak-proverit-avto-iz-korei | reader_result: Человек смотрит схему, а не ярлык, и отсекает лоты с X/W на силовых |
| pain: "В страховой истории пусто – можно платить" | solution: Помнить disclaimer CarHistory: незаявленные и cash-ремонты не видны; задержка 2,5–3 мес.; сверять с протоколом и осмотром | https://www.carhistory.or.kr/main.car?lang=ru&retUrl= ; https://azway.ru/blog/proverka-avto-iz-korei-encar | reader_result: "Чистый" отчёт = только отсутствие страховых выплат, не гарантия |
| pain: "Цены выглядят странно / кажется, что машина копеечная" | solution: Умножить число на 만원 на 10 000; цена лота ≠ под ключ в РФ; не выдумывать пошлины в статье | https://xapikorea.com/blog/how-to-use-encar-in-english ; fact-bank AVTO SALES | reader_result: Бюджет считается как "лот + логистика + таможня через каталог", без ложных калькуляторов |
| pain: "Нашёл Trust Encar в поиске и думал, что это официальная проверка" | solution: Развести: RU "Trust Encar" часто посредник; 엔카진단 = осмотр Encar; 엔카믿고 = корейский сервис покупки/доставки с возвратом 7 дней | https://www.encar.com/llms.txt ; https://car.encar.com/diagnosis/intro ; bridge AS09 | reader_result: Читатель не путает бренд посредника с CarHistory/Diagnosis |
| pain: "Боюсь депозита: вдруг пробег скручен или утопленник" | solution: Сверить пробег в протоколе/истории/износе; flood check; стоп на 침수/전손, X/W на каркасе, протокол >120 дней | https://bic-auto.ru/blog/kak-proverit-avto-iz-korei ; https://vinlid.com/blog/how-to-buy-a-car-on-encar | reader_result: Список стоп-флагов до перевода денег; сомнительные лоты – к Авто-Сейлс |

## action_outline
1. Открыть карточку на `fem.encar.com` / `car.encar.com`, включить перевод браузера, сохранить ссылку и числовой ID лота.
2. Пересчитать цену: число в 만원 × 10 000 = воны; зафиксировать, что это цена в Корее, не "под ключ".
3. Выписать год/месяц регистрации, model year в скобках, топливо, КПП, пробег, регион, кто продавец.
4. Найти VIN (차대번호) в 성능·상태점검기록부; если VIN не дают – стоп до объяснения.
5. Открыть схему кузова: отметить X/W/C/A/U/T; отдельно силовые элементы vs навесные панели; не останавливаться на ярлыке 무사고.
6. Открыть страховую выжимку / CarHistory по VIN или кнопке в карточке: свои выплаты, чужие, 침수, 전손, 도난, прокат/такси, смены владельцев.
7. Проверить свежесть протокола (ориентир ≤120 дней), совпадение VIN во всех блоках, логичность пробега (не "назад", не необъяснимый разрыв).
8. Если есть бейдж 엔카진단 – записать уровень (진단/+/++), но всё равно спланировать независимый осмотр до депозита; не путать с 엔카믿고 и с RU "Trust Encar".
9. Собрать вердикт: ок / нужны фото-толщиномер / стоп; депозит только после пакета проверок или передачи лота подборщику Авто-Сейлс (каталог / Telegram).

## competitor_gaps
- Много "Encar на русском" = каталоги посредников и "как заказать под ключ", мало beginner-чеклиста чтения карточки до денег.
- Путают Trust Encar (RU) / Encar Diagnosis / Meetgo / CarHistory.
- Редко объясняют 만원 и 무사고 простым языком с конкретным "что нажать".
- Наш угол: чтение объявления + красные флаги + мост на AS09 (проверка до депозита), без цен лотов и без калькулятора пошлин.

## facts_for_writer (только с URL; не выдумывать VIN/цены лотов)
1. Encar Diagnosis: мастер проверяет кузов/низ/каркас; в Diagnosis пускают только с нормальным frame; ошибка диагноза – компенсация по правилам в пределах 90 дней или 5 000 км (https://car.encar.com/diagnosis/intro , accessed 2026-11-03).
2. 엔카믿고 (Meetgo): отдельный сервис удалённой покупки в Корее с выбором доставки/визита и окном возврата ~7 дней; это не русскоязычный "Trust Encar" из выдачи (https://www.encar.com/llms.txt).
3. CarHistory: данные страховых возмещений с 1996; полный отчёт ~2 200 вон с НДС; бесплатная проверка затопления; незаявленные ДТП не видны (https://www.carhistory.or.kr/main.car?lang=ru&retUrl=).
4. 만원 = 10 000 KRW; пример 2 350만원 = 23 500 000 KRW (https://xapikorea.com/blog/how-to-use-encar-in-english , Sep 2026).
5. 무사고 обычно про отсутствие ремонта силового каркаса; bolt-on панели могут быть заменены без ярлыка "accident car" (Vinlid 2026-10-11; BIC 2026-10-17).
6. Vinlid: в выборке ~1,5 млн протоколов accident record ~14,4%, ≥1 panel replaced ~4/10 (https://vinlid.com/blog/how-to-buy-a-car-on-encar).
7. Коды схемы: X замена, W рихтовка/сварка, C коррозия, A царапина, U вмятина, T повреждение (BIC).
8. Протокол осмотра дилера ориентировочно не старше 120 дней; гарантия эксперта ≥30 дней / 2 000 км почти бесполезна для экспорта в РФ (BIC).
9. Средний пробег в Корее порядка 10–13 тыс. км/год (Vinlid ~10–12k; KingStone цитирует KOTSA ~36 км/день ≈13,1k/год за 2024, материал 2025–2026) – аномально низкий пробег = повод сверить цепочку показаний.
10. Редакция Авто-Сейлс: не публиковать готовые суммы пошлин/утильсбора; расчёт – через каталог; офис Владивосток (fact-bank).

## writer_must_use
- Lead: reader_story про Tucson / 무사고 / предоплату.
- H2 закрывают pain_solution_map; до FAQ – success_criteria.
- FAQ-подсказки из карточки темы: что такое Trust Encar; можно ли верить пробегу в Encar.
- Internal bridge: тема AS09 (Trust Encar + Carhistory до депозита) – углубление проверки, не дублировать 1:1.
- Запреты site-brief: без эмодзи, без ёлочек и длинных тире в финальном article.html, без Wordstat/Метрики в тексте статьи, без выдуманных VIN.

## utility_notes
Beginner-first how_to: первый результат – разобранная карточка + чеклист стоп-флагов до депозита. Не новость рынка Кореи 2026, не материал для перекупщиков-профи.
