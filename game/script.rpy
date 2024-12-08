
define ivy = Character(_("Ivy"), color="#f03611")
define sterling = Character(_("Sterling"), color="#0c88ed")
define ash = Character(_("Ash"), color="#af38ff")
define reagan = Character(_("Reagan"), color="#ccb90a")
define parker = Character(_("Parker"), color="#05b317")

init:
    $ short_dissolve = Dissolve(0.1)

    $ roomList = {
        "kitchen" : False,
        "living_room" : False,
        "library" : False,
        "bedroom" : False,
        "office" : False
    }

    $ clues = {
        "computer" : False,
        "note" : False,
        "scraps" : False,
        "sketch" : False
    }

    $ parker_clues = False

    $ reagan_confront = False

    $ ash_confront = False

    $ parker_confront = False

    $ sterling_confront = False

    $ mystery_solved = {
        "reagan" : False,
        "parker" : False,
        "ash" : False,
        "sterling" : False
    }

    $ ending = False


    $ firstLoop = True


transform ivyT:
    zoom 0.4
    xzoom -1.0
    xalign 0.0
    yalign 1.0


transform parkerT:
    zoom 0.4
    xalign 1.0
    yalign 1.0


transform sterlingT:
    zoom 0.46
    xalign 1.0
    yalign 1.0


transform ashT:
    zoom 0.43
    xalign 1.0
    yalign 1.0


transform reaganT:
    zoom 0.4
    xzoom -1.0
    xalign 1.0
    yalign 1.0


label start:

    show bg black:
        zoom 3

    "Загадки обычно начинаются с чего-то драматичного, верно? 'Буря свистела за окнами' или что-то в этом роде?"

    "Пожалуй, не совсем так. Но это мой первый раз, когда я решаю разгадать такую тайну, и, честно говоря, я немного волнуюсь."

    show ivy_neutral at center:
        zoom 0.4
    with short_dissolve

    "Меня зовут Айви, и моя работа — выяснить, кто испортил мой семейный альбом."

    hide ivy_neutral
    with short_dissolve

    "Всё начиналось так идеально. Мы с друзьями остановились в доме моих родителей, чтобы отпраздновать моё 21-летие. Смех, веселье, воспоминания... Казалось, что этот уикенд запомнится только хорошими моментами."

    "... я не знала, что предательство уже на горизонте."

    "Я верила каждому из своих друзей, не сомневаясь. И теперь мне трудно осознать, что кто-то из них мог бы так подло предать моё доверие."

    "Четыре друга, четыре подозреваемых... И только я могу выяснить, кто это сделал."

    show sterling_neutral at center:
        zoom 0.46
    with short_dissolve

    "Стерлинг, или 'Мой идеальный парень'. Мы вместе уже несколько лет, а друзьями были гораздо дольше. Но вот в чём вопрос: мог ли он мне соврать?"

    hide sterling_neutral
    with short_dissolve

    show ash_neutral at center:
        zoom 0.43
    with short_dissolve

    "Эш, или 'Злая доверенная подруга'. Она всегда была саркастична и груба, но её преданность никогда не вызывала сомнений... Но теперь я начинаю задаваться вопросом: могла ли она нарушить моё доверие?"

    hide ash_neutral
    with short_dissolve

    show parker_neutral at center:
        zoom 0.4
    with short_dissolve

    "Паркер, или 'Ехидный лис'. Он всегда создаёт беспорядок, но ненавидит попадать в неприятности... Но мог ли он стать причиной этого хаоса?"

    hide parker_neutral
    with short_dissolve

    show reagan_neutral at center:
        zoom 0.4
        xzoom -1.0
    with short_dissolve

    "И Рейган, или 'Тревожное солнышко'. Она всегда находит способы помочь другим, её сердце всегда открыто... Но могла ли она сделать что-то столь эгоистичное?"
    hide reagan_neutral
    with short_dissolve

    "С вопросами и без ответов, я должна взять на себя роль следователя и раскрыть правду."

    "Все началось прямо перед ужином в тот вечер..."


    show bg dining room:
        zoom 2
        yalign 1.0

    show reagan_happy at reaganT
    with short_dissolve

    reagan "Еда готова! Все идите кушать!"

    hide reagan_happy
    with short_dissolve

    "Все заполнили столовую, с нетерпением ожидая вкусный ужин, который приготовила Рейган."

    "Блюда уже были расставлены, окружая всё ещё парящие макароны и чесночный хлеб, который Рейган поставила для всех."

    "Все суетились, пытаясь получить свою порцию, и комната наполнилась лёгким шумом разговоров, но вдруг звонок мобильного телефона прорезал тишину."

    show sterling_neutral at sterlingT
    with short_dissolve

    sterling "О, это я. Извините, мне нужно быстро ответить."

    hide sterling_neutral
    with short_dissolve

    "Стерлинг вышел из комнаты, и я, отвлекшись на еду, не сразу заметила. Но прежде чем я успела сделать первый укус, меня снова прервали."

    show ash_neutral at ashT
    with short_dissolve

    ash "Эй, Паркер, не мог бы ты принести мою бутылку с водой из офиса?"

    show parker_angry:
        zoom 0.4
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    show ash_inactive at ashT
    with short_dissolve

    parker "Что? У тебя есть свои ноги, идиотка."

    show parker_inactive:
        zoom 0.4
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    hide ash_inactive
    hide parker_angry
    with short_dissolve

    ash "Но ты же ближе к двери!"

    hide parker_inactive
    show ash_inactive at ashT
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Успокойтесь, ребята, я схожу и принесу её."

    hide ash_inactive
    hide ash_neutral
    hide ivy_neutral
    with short_dissolve

    "С вздохом я встала и направилась в офис, решив найти бутылку с водой и вернуться к еде."

    show bg office:
        zoom 1.75
        yalign 1.0
    
    "Но совсем другая сцена встретила мои глаза, когда я открыла дверь. На столе в комнате лежал семейный альбом."

    "Однако он был покрыт тёмными пятнами от жидкости, а страницы были вырваны и выброшены рядом."

    show ivy_sad at ivyT
    with short_dissolve

    ivy "О нет... мои родители меня убьют."

    hide ivy_sad
    with short_dissolve

    "Ладно, ладно, всё в порядке. Мне нужно только выяснить, кто это испортил, и начать с этого."

    "Схватив бутылку с водой, я поспешила обратно в столовую. В комнате снова зазвучал лёгкий разговор, как только Стерлинг вернулся."


    show bg dining room:
        zoom 2
        yalign 1.0

    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Эй, ребята."

    show ivy_inactive at ivyT
    with short_dissolve

    "Разговор затих, и все взгляды были направлены на меня."

    show ivy_sad at ivyT
    hide ivy_inactive
    with short_dissolve

    ivy "Смотрите, я нашла семейный альбом, абсолютно уничтоженный в офисе."

    hide ivy_sad
    with short_dissolve

    ivy "Теперь, я не злюсь, я просто хочу выяснить, кто это сделал, чтобы мы могли это исправить. Так кто же испортил альбом?"

    show ivy_inactive at ivyT
    with short_dissolve
    
    "В комнате наступила оглушительная тишина, пока каждый из моих друзей не начал нервно и подозрительно смотреть друг на друга."

    hide ivy_inactive
    with short_dissolve

    ivy "Давайте, ребята, кто испортил? Просто скажите мне."

    show ivy_inactive at ivyT
    with short_dissolve

    "Все снова молчат... пока-"

    show parker_neutral at parkerT
    with short_dissolve

    parker "Ну, я знаю, что Рейган была в офисе одна некоторое время."

    show parker_inactive at parkerT
    hide parker_neutral
    hide ivy_inactive
    hide ivy_neutral
    show reagan_sad:
        zoom 0.4
        xalign 0.0
        yalign 1.0
    with short_dissolve

    reagan "Ч-Что? Почему вы обвиняете меня?"

    hide reagan_sad
    show ash_neutral:
        zoom 0.43
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    with short_dissolve

    ash "Давай, Паркер, успокойся. К тому же, разве ты не был один в офисе?"

    show ash_inactive:
        zoom 0.43
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    hide parker_inactive
    hide ash_neutral
    show parker_angry at parkerT
    with short_dissolve

    parker "Я никогда не был один в офисе! О чём ты вообще говоришь?"

    hide parker_angry
    hide ash_inactive
    with short_dissolve

    "Эш и Паркер продолжают кричать друг на друга, а Рейган и Стерлинг пытаются их успокоить."

    show ivy_angry at ivyT
    with short_dissolve

    ivy "Хватит! Все заткнитесь!"

    hide ivy_angry
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Если никто не признается, кто это сделал, я сама раскрою, кто испортил. Загадка с семейным альбомом — или что-то вроде того."

    hide ivy_neutral
    with short_dissolve
    
    "Я старалась сохранять спокойствие, решая загадку, но мне было довольно приятно раскрывать её самой. Я люблю хорошие детективные истории, а теперь у меня есть одна."

    "Первый шаг: мне нужно изолировать каждого из подозреваемых, чтобы они не могли разговаривать друг с другом. Я отправлю их по разным комнатам:"

    show bg kitchen:
        zoom 0.9
        xalign 1.0

    show reagan_neutral at center:
        zoom 0.4
        xzoom -1.0
    with short_dissolve

    "Рейган в кухню," # Показываем спрайт Рейган на кухне, по центру

    hide reagan_neutral
    with short_dissolve

    show bg library:
        zoom 1.0
        xalign 1.0

    show parker_neutral at center:
        zoom 0.4
    with short_dissolve

    "Паркер в библиотеку," # Показываем спрайт Паркера в библиотеке, по центру

    hide parker_neutral
    with short_dissolve

    show bg bedroom:
        zoom 0.8
        xalign 1.0

    show sterling_neutral at center:
        zoom 0.46
    with short_dissolve

    "Стерлинг в спальню," # Показываем спрайт Стерлинга в спальне, по центру

    hide sterling_neutral
    with short_dissolve

    show bg living room:
        zoom 1.0
        xalign 1.0

    show ash_neutral at center:
        zoom 0.43
    with short_dissolve

    "и Эш в гостиную." # Показываем спрайт Эш в гостиной, по центру.

    jump invest_loop

    label invest_loop:

        scene bg hallway

        if firstLoop == True:
            "С подозреваемыми разделены, я должна расследовать место преступления и затем начать допросы..."
            $ firstLoop = False

        jump locations

    menu locations:

        "В какую комнату мне пойти?"

        "В офис.":
            jump office

        "В библиотеку.":
            jump library

        "В гостиную.":
            jump living_room

        "В спальню.":
            jump bedroom

        "На кухню.":
            jump kitchen

    label kitchen:

        $ explored = True
        scene bg kitchen:
            zoom 0.9
            xalign 1.0

        if roomList["kitchen"] == False:
            menu kitchen_search:

                "Вот кухня, где Рейган. Мне искать в комнате или поговорить с ней?"

                "Обследовать комнату.":

                    "Кухня немного беспорядочная после того, как готовился ужин, но это не катастрофа."

                    "На прилавке остались некоторые тарелки, большинство из которых в раковине... и что это?"

                    "Там лежит смятый кусок бумаги, на котором нарисованы эскизы, напоминающие семейный альбом."

                    "Если я смогу выяснить, кому принадлежат эти эскизы, мне нужно будет спросить их, что происходит."

                    $ roomList["kitchen"] = True
                    $ clues["sketch"] = True

                    menu kitchen_post_search:

                        "Все остальное кажется нормальным. Мне поговорить с Рейган или исследовать другую комнату?"

                        "Поговорить с Рейган.":
                            jump reagan_talk
                        
                        "Пойти в другую комнату.":
                            jump invest_loop
                
                "Поговорить с Рейган.":
                    jump reagan_talk
        else:
            "Я уже обследовала комнату, нужно поговорить с Рейган."
            jump reagan_talk
        
    label reagan_talk:

        show ivy_inactive at ivyT
        show reagan_sad at reaganT
        with short_dissolve

        reagan "Привет, Айви. Слушай, извини, что альбом был испорчен. Надеюсь, твое расследование идет хорошо."

        hide reagan_sad
        show reagan_neutral at reaganT
        with short_dissolve

        menu reagan_qs:

            reagan "Чем могу помочь?"

            "Ты это испортила?" if parker_clues == False or reagan_confront == False:
                
                show reagan_sad at reaganT
                hide reagan_neutral
                with short_dissolve
                
                reagan "Я... Я не испортила, но могу заплатить. Я не хочу создавать проблем, если это затянется."

                show ivy_neutral at ivyT
                hide ivy_inactive
                show reagan_inactive at reaganT
                hide reagan_sad
                with short_dissolve

                ivy "Рейган, я не ищу кого-то, кто заплатит. Я просто хочу понять, кто это испортил."

                show ivy_inactive at ivyT
                hide ivy_neutral
                show reagan_neutral at reaganT
                hide reagan_inactive
                with short_dissolve

                reagan "О... ну, это была не я."

                jump reagan_qs
            
            "Каков был твой график сегодня?" if parker_clues == False or reagan_confront == False:
                reagan "Ну, я провела время с Паркером в офисе около 13:00, а потом готовила ужин на кухне после 15:00."

                show reagan_inactive at reaganT
                hide reagan_neutral
                with short_dissolve

                "Хм, интересно. Мне нужно поговорить с Паркером, чтобы он подтвердил это."

                show reagan_neutral at reaganT
                hide reagan_inactive
                with short_dissolve

                jump reagan_qs
            
            "Есть ли что-то, что ты знаешь, что могло бы мне помочь?" if parker_clues == False or reagan_confront == False:
                reagan "Хм, я не уверена. Какую информацию ты ищешь?"

                show ivy_neutral at ivyT
                show reagan_inactive at reaganT
                hide reagan_neutral
                with short_dissolve

                ivy "Ну, может быть, если кто-то вёл себя подозрительно или как-то странно. Что-то, что поможет сузить круг подозреваемых."

                show reagan_sad at reaganT
                show ivy_inactive at ivyT
                hide ivy_neutral
                hide reagan_inactive
                with short_dissolve

                reagan "Ну, это немного жестко, но Аш зашла в офис, когда я уходила, и была там одна."

                show reagan_neutral at reaganT
                hide reagan_sad
                with short_dissolve

                jump reagan_qs
            
            "Могу я спросить тебя о найденном предмете?" if parker_clues == False or reagan_confront == False:
                reagan "Конечно, что это?"

                menu reagan_clues:
                    "Показать ей компьютерные поиски." if clues["computer"] == True:
                        reagan "О, это? Да, это мои поиски. Пока я была в офисе."

                        show reagan_inactive at reaganT
                        hide reagan_neutral
                        show ivy_neutral at ivyT
                        hide ivy_inactive
                        with short_dissolve

                        ivy "Ну и что это за поиски? Ты что-то скрываешь?"

                        show reagan_sad at reaganT
                        hide reagan_inactive
                        show ivy_inactive at ivyT
                        hide ivy_neutral
                        with short_dissolve

                        reagan "Ну, я просто... думала, что кто-то лжет мне, вот и искала."

                        show reagan_inactive at reaganT
                        hide reagan_sad
                        with short_dissolve

                        if parker_clues == False:
                            "Хм... странный ответ. Мне нужно найти больше улик, прежде чем обвинять её."
                        else:
                            "Паркер сказал, что Рейган была в офисе одна, и очевидно, что она что-то скрывает... Мне нужно заставить её рассказать правду."

                        $ reagan_confront = True

                        show reagan_neutral at reaganT
                        hide reagan_inactive
                        with short_dissolve

                        jump reagan_qs
                    
                    "Показать ей смятый 'извини' записку." if clues["note"] == True and parker_confront == False:
                        reagan "Это не мое, я не узнаю почерк."

                        jump reagan_qs
                    
                    "Показать ей клей и обрывки." if clues["scraps"] == True and ash_confront == False:
                        reagan "Не уверена, что это такое, это не мое."

                        jump reagan_qs
                    
                    "Показать ей эскизы из беспорядочного альбома." if clues["sketch"] == True and sterling_confront == False:
                        reagan "Я никогда не видела этот эскиз, не знаю, для чего он."

                        jump reagan_qs
                    
                    "Ничего.":
                        jump reagan_qs
            
            "Рейган, нам нужно поговорить." if reagan_confront == True and parker_clues == True and mystery_solved["reagan"] == False:

                show ivy_inactive at ivyT
                show reagan_inactive at reaganT
                with short_dissolve

                "Рейган явно что-то скрывает, с её ответом о компьютерных эскизах. И Паркер сказал, что она была в офисе одна. Мне нужно выяснить правду."

                show ivy_neutral at ivyT
                with short_dissolve
                
                ivy "Ладно, Рейган, я знаю, что ты лжешь. История с поисками на компьютере явно твоя, и я знаю, что ты была в офисе одна."

                show ivy_sad at ivyT
                hide ivy_neutral
                with short_dissolve

                ivy "Что происходит?"

                hide ivy_sad
                show reagan_angry at reaganT
                with short_dissolve

                reagan "Как ты смеешь обвинять меня...! Я не..."

                reagan "..."

                hide reagan_angry
                show reagan_sad at reaganT
                with short_dissolve

                reagan "Хорошо, да, я лгала. Извините, что скрывала что-то не только от тебя, но и от всех моих друзей..."

                reagan "... Я записалась на учебу за границей в следующем семестре. Я буду отсутствовать и занята какое-то время, и не хотела огорчать никого."

                reagan "Но чем дольше я скрывала, тем больше волновалась, и мне было страшно рассказать всем."

                hide reagan_sad
                with short_dissolve
                
                "Рейган выглядит стыдно и раскаивается, у меня мало сомнений, что она лжет в этом."

                show ivy_happy at ivyT
                with short_dissolve

                ivy "Эй, все в порядке, Рейган. Я рада, что ты собираешься исследовать мир и надеюсь, что тебе будет весело!"

                hide ivy_happy
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Тем не менее, возможно, в следующий раз стоит признаться в этом, когда я расследую \"преступление\" вроде этого."

                hide ivy_neutral
                show reagan_sad at reaganT
                
                reagan "Простите! Я знаю, что должна была быть честной с самого начала... Надеюсь, что ты все же найдешь настоящего преступника!"

                $ mystery_solved["reagan"] = True

                if mystery_solved["ash"] == True and mystery_solved["parker"] == True and mystery_solved["sterling"] == True:
                    $ ending = False
                    
                    hide ivy_inactive
                    hide reagan_neutral
                    hide reagan_inactive
                    hide reagan_sad
                    with short_dissolve
                    
                    jump solving
                else:

                    hide reagan_sad
                    with short_dissolve

                    "Ну, у Рейган есть довольно хорошее объяснение... мне нужно поговорить с остальными подозреваемыми."
                    jump invest_loop

            "Это все на сейчас.":
                show reagan_happy at reaganT
                hide reagan_neutral
                with short_dissolve

                reagan "Я буду рядом, если тебе нужно что-то еще. Удачи, Айви!"

                jump invest_loop

        jump invest_loop
label bedroom:

    $ explored = True
    scene bg bedroom:
        zoom 0.8
        xalign 1.0

    # Спросить у игрока, хочет ли он осмотреть комнату или поговорить с подозреваемым.
    # Если он уже осмотрел комнату, значение в словаре будет True

    if roomList["bedroom"] == False:
        menu bedroom_search:

            "Вот спальня, где находится Стерлинг. Мне осмотреть комнату или поговорить с ним?"

            "Осмотреть комнату.":
                "Гостевая спальня слегка в беспорядке, после того как здесь побывали друзья в последние дни. Кровать не заправлена, а багаж раскидан по комнате."

                "Мне, наверное, стоит избегать рыться в чужих вещах, но если нужно... для безопасности начну с того, что осмотрю просто комнату."

                "Тумбочки полны бесполезного хлама, а стол в шкафу пуст... подожди-ка, мусорное ведро полно!"

                "Похоже, что это куча смятых бумаг... я плохо их читаю, но это кажется попытками написания письма с извинениями."

                "Тот, кто писал это, явно был раздражен, пытаясь подобрать правильные слова. Интересно, не он ли испортил альбом? Мне стоит расспросить об этом."

                $ roomList["bedroom"] = True

                $ clues["note"] = True
                
                menu bedroom_post_search:

                    "В комнате больше ничего важного не осталось. Поговорить с Стерлингом или пойти в другую комнату?"

                    "Поговорить с Стерлингом.":
                        jump sterling_talk
                    
                    "Пойти в другую комнату.":
                        jump invest_loop
            
            "Поговорить с Стерлингом.":
                jump sterling_talk
    else:
        "Я уже осмотрел комнату, мне нужно поговорить с Стерлингом."
        jump sterling_talk

label sterling_talk:
    
    show sterling_happy at sterlingT
    show ivy_inactive at ivyT
    with short_dissolve

    sterling "Привет, Айви! Как продвигается расследование? Уверен, ты быстро разгадаешь эту тайну."
    
    show sterling_neutral at sterlingT
    hide sterling_happy
    with short_dissolve

    menu sterling_qs:
        
        sterling "Какие вопросы у тебя ко мне, детка?"

        "Ты это испортил?" if parker_clues == False or sterling_confront == False:
            
            show sterling_sad at sterlingT
            with short_dissolve

            sterling "Нет, я этого не делал. Я знаю, как важен был этот альбом для твоей семьи."

            hide sterling_sad
            with short_dissolve

            jump sterling_qs
        
        "Как был твой день?" if parker_clues == False or sterling_confront == False:
            sterling "Ну, я перекусил на кухне около часа дня, а потом просто слонялся, пока не настало время ужина."

            show sterling_inactive at sterlingT
            show ivy_neutral at ivyT
            with short_dissolve
            
            ivy "Дорогой, я тебя люблю, но мне нужно больше конкретики."

            hide sterling_inactive
            hide ivy_neutral
            with short_dissolve

            sterling "Правда, извини. Ну, я начал в спальне, там сидел до трех. Потом пошел в библиотеку, а затем в кабинет."

            show sterling_happy at sterlingT
            with short_dissolve

            sterling "Надеюсь, теперь это более конкретно!"

            hide sterling_happy
            with short_dissolve

            jump sterling_qs
        
        "Есть ли что-то, что ты знаешь, что может помочь?" if parker_clues == False or sterling_confront == False:
            sterling "Хмм... ничего подозрительного я не замечал."

            sterling "О! Когда я вышел из кухни, Аш и Паркер вошли. Они начали шептаться, а как только меня заметили, сразу же замолчали."

            show sterling_angry at sterlingT
            with short_dissolve

            sterling "Они были довольно грубыми, и я быстро ушел."

            hide sterling_angry
            with short_dissolve

            jump sterling_qs
        
        "Могу я показать тебе этот предмет, который я нашла?" if parker_clues == False or sterling_confront == False:
            sterling "Конечно, что ты мне принесла?"

            menu sterling_clues:
                "Показать ему поиск на компьютере." if clues["computer"] == True and reagan_confront == False:
                    sterling "Эти поиски не мои, я не трогал компьютер, когда был в кабинете."

                    jump sterling_qs
                
                "Показать ему смятый 'извинительный' лист." if clues["note"] == True and parker_confront == False:
                    sterling "Ух, почерк какой-то неразборчивый. Я не знаю, что это."

                    jump sterling_qs
                
                "Показать ему клей и обрезки." if clues["scraps"] == True and ash_confront == False:
                    sterling "Извини, детка, не могу понять, что это должно быть."

                    jump sterling_qs
                
                "Показать ему эскизы альбома." if clues["sketch"] == True:
                    sterling "О, да, я знаю, что это."

                    show sterling_inactive at sterlingT
                    show ivy_neutral at ivyT
                    with short_dissolve

                    ivy "Ну так что это? Ты сам их рисовал?"

                    hide ivy_neutral
                    hide sterling_inactive
                    with short_dissolve

                    sterling "Н-нет! Мой друг мне это дал, сказал, что это роман, который мне стоит прочитать. Наверное, я уронил его где-то."

                    show sterling_inactive at sterlingT
                    show ivy_neutral at ivyT
                    with short_dissolve

                    ivy "Роман? Но эскизы как-то слишком похожи на альбом моей семьи..."

                    hide ivy_neutral
                    hide sterling_inactive
                    with short_dissolve

                    sterling "Похоже, да, но мой друг мне сказал, что это книга."

                    show sterling_inactive at sterlingT
                    with short_dissolve

                    if parker_clues == False:
                        "Его ответ странный, но правдоподобный. Мне нужно больше информации, чтобы решить, виновен ли он или нет."
                    else:
                        "Паркер сказал, что Стерлинг избегал его, а теперь он ведет себя странно относительно этого \"друзья\". Нужно разобраться, что на самом деле происходит."

                    hide sterling_inactive
                    with short_dissolve

                    $ sterling_confront = True

                    jump sterling_qs
                
                "Ничего.":
                    jump sterling_qs
        
        "Стерлинг, нам нужно поговорить." if sterling_confront == True and parker_clues == True and mystery_solved["sterling"] == False:
            
            show sterling_inactive at sterlingT
            with short_dissolve

            "Если Стерлинг действительно избегал людей весь день и лжет насчет эскизов, он явно что-то скрывает."

            show ivy_angry at ivyT
            with short_dissolve

            ivy "Стерлинг, дорогой. Я прошу тебя сказать мне правду прямо сейчас, ладно? Потому что что-то не сходится."

            hide ivy_angry
            show sterling_sad at sterlingT
            with short_dissolve

            sterling "Айви, прости, что это выглядит подозрительно, но я не лгу. Мне действительно посоветовали эту книгу мой друг."

            hide sterling_sad
            show sterling_happy at sterlingT
            with short_dissolve

            sterling "Слушай, может быть, это поможет. Я не мог вспомнить название романа, который мне порекомендовал мой друг, так что я его спросил. Он сказал, что это 'Гордость и предубеждение'."

            hide sterling_happy
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Подожди... твой друг порекомендовал тебе 'Гордость и предубеждение'?"

            hide sterling_inactive
            hide ivy_neutral
            with short_dissolve

            sterling "Да! А что, это странно?"

            show ivy_neutral at ivyT
            show sterling_inactive at sterlingT
            with short_dissolve

            ivy "Ну, это хорошая книга. Просто немного удивлена, вот и все."

            hide ivy_neutral
            hide sterling_inactive
            with short_dissolve

            sterling "Так я слышал! Ха..."

            show sterling_sad at sterlingT
            with short_dissolve
            
            sterling "..."

            hide sterling_sad
            show sterling_inactive at sterlingT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Эй, что случилось? Ты так тихо..."

            hide ivy_neutral
            hide sterling_inactive
            with short_dissolve

            sterling "Я... должен тебе кое-что сказать. Мне очень жаль, но когда я пришел в кабинет в 4:00, я нашел... альбом уже испорченным."

            show sterling_inactive at sterlingT
            show ivy_angry at ivyT
            with short_dissolve

            ivy "Что? И ты не подумал сказать мне это раньше? Стерлинг!"

            hide ivy_angry
            hide sterling_inactive
            with short_dissolve

            sterling "Прости, прости! Но я не уверен, кто был в кабинете до меня, поэтому не хотел безосновательно обвинять кого-то!"

            show ivy_neutral at ivyT
            show sterling_inactive at sterlingT

            ivy "Хм... ну, это справедливо. Спасибо, что сказал мне сейчас, хотя бы это полезно."

            $ mystery_solved["sterling"] = True
            
            if mystery_solved["ash"] == True and mystery_solved["parker"] == True and mystery_solved["reagan"] == True:
                $ ending = False

                hide ivy_inactive
                hide ivy_neutral
                hide sterling_neutral
                hide sterling_inactive
                with short_dissolve

                jump solving
            else:

                hide ivy_neutral
                with short_dissolve

                "Если Стерлинг нашел альбом уже испорченным, мне нужно выяснить, кто еще был в офисе сегодня."
                jump invest_loop

        "Это все на данный момент.":
                show sterling_happy at sterlingT
                with short_dissolve

                sterling "Звучит отлично! Найди виновного, детка!"

                jump invest_loop

    jump invest_loop
label library:

    $ explored = True
    scene bg library:
        zoom 1.0
        xalign 1.0

    if roomList["library"] == False:
        menu library_search:

            "Вот библиотека, где находится Паркер. Мне стоит обыскать комнату или поговорить с ним?"

            "Обыскать комнату.":
                "Библиотека осталась аккуратной, пока все здесь. По крайней мере, книги на своих местах."

                "Один из столов почти чист, а на другом, похоже, было совершено нечто страшное! Клей и скотч везде!"

                "Постойте... бумажные обрывки, оставшиеся здесь, выглядят как один из узоров из альбома. Наверное, кто-то пытался починить альбом!"

                "Или, может, испортил его специально... Но я надеюсь, что ни один из моих друзей не сделал бы этого."

                "В любом случае, мне нужно выяснить, кто оставил эти обрывки и над чем они работали."

                $ roomList["library"] = True

                $ clues["scraps"] = True
                
                menu library_post_search:

                    "Все остальное кажется нормальным. Мне стоит поговорить с Паркером или пойти в другую комнату?"

                    "Поговорить с Паркером.":
                        jump parker_talk
                    
                    "Пойти в другую комнату.":
                        jump invest_loop
            
            "Поговорить с Паркером.":
                jump parker_talk
    else:
        "Я уже обыскал комнату, давай поговорим с Паркером."
        jump parker_talk

label parker_talk:

    show ivy_inactive at ivyT
    show parker_neutral at parkerT
    with short_dissolve

    parker "О, привет, Айви. Как идет твое \"расследование\"? Почти закончено?"

    menu parker_qs:

        parker "Что ты хочешь узнать?"

        "Ты это испортил?" if parker_clues == False or parker_confront == False:
            
            show parker_angry at parkerT
            with short_dissolve

            parker "Нет, я не испортил. Боже, не знаю, почему все думают, что это сделал я!"

            hide parker_angry
            show parker_inactive at parkerT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Паркер, я тебя не обвиняю. Я спрашивал у всех, испортил ли кто-то."

            hide ivy_neutral
            hide parker_inactive
            with short_dissolve

            parker "О. Ну, это все равно не я."

            jump parker_qs
        
        "Каков был твой график сегодня?" if parker_clues == False or parker_confront == False:
            parker "Ну, я был с Рейган в офисе около 1:00, затем пошел в кухню с Эшем, а потом просто сидел в спальне до ужина."

            jump parker_qs
        
        "Есть ли что-то, что ты знаешь и что может помочь мне?" if parker_clues == False or parker_confront == False:
            
            show parker_happy at parkerT
            with short_dissolve

            parker "Ну, раз уж ты упомянул, у меня есть несколько интересных деталей."

            hide parker_happy
            with short_dissolve

            parker "Во-первых, когда я ушел из офиса около 2:00, Рейган осталась там одна. Кто знает, чем она занималась..."

            show parker_inactive at parkerT
            with short_dissolve

            if reagan_confront == False:
                "Рейган была в офисе одна... это интересно, но мне нужно еще несколько улик, прежде чем ее обвинять."
            else:
                "Рейган и ее поисковые запросы на компьютере, а еще она была одна в офисе. Она явно что-то скрывает. Мне нужно выяснить что."

            hide parker_inactive
            with short_dissolve

            parker "А еще, Стерлинга вообще не было видно весь день! Может, он избегал людей по какой-то причине..."

            show parker_inactive at parkerT
            with short_dissolve

            if sterling_confront == False:
                "Хотя Стерлинг очень общительный, странно, что он избегал людей... Мне нужно найти больше улик, прежде чем обвинить его."
            else:
                "Сначала его \"рекомендация по книге\", а теперь он избегает людей. Я должен обвинить его, чтобы узнать больше."

            hide parker_inactive
            with short_dissolve

            parker "Плюс, Эш вела себя немного странно. Когда я сидел в спальне, она зашла, но как только меня увидела, сразу ушла."

            show parker_inactive at parkerT
            with short_dissolve

            if ash_confront == False:
                "Это странное поведение для Эш, особенно учитывая, что они с Паркером хорошие друзья... Мне нужно собрать больше улик перед тем, как обвинить ее."
            else:
                "Она вела себя подозрительно насчет обрывков, а теперь еще и скрывает что-то. Мне нужно разобраться в этом."

            show parker_happy at parkerT
            with short_dissolve

            parker "Это все важные моменты, надеюсь, это было полезно."

            hide parker_happy
            with short_dissolve

            $ parker_clues = True

            if parker_confront == False:
                "Как-то подозрительно быстро Паркер переложил вину на других... но мне нужно найти больше улик, прежде чем обвинить его."
            else:
                "После того как я нашел его письмо с извинениями и теперь он пытается обвинить других, Паркер явно что-то скрывает. Я собираюсь это выяснить."

            hide parker_inactive
            with short_dissolve

            jump parker_qs
        
        "Могу я показать тебе вещь, которую я нашел?" if parker_clues == False or parker_confront == False:
            parker "Да, дай-ка я на это посмотрю."

            menu parker_clues:
                "Показать ему поисковые запросы на компьютере." if clues["computer"] == True and reagan_confront == False:
                    parker "Эти поисковые запросы такие жалкие! Это явно не мои."

                    jump parker_qs
                
                "Показать ему помятую записку с извинениями." if clues["note"] == True:
                    
                    show parker_sad at parkerT
                    with short_dissolve

                    parker "..."
                    
                    show parker_inactive at parkerT
                    with short_dissolve

                    "Когда я показал ему записку, он побледнел."

                    hide parker_inactive
                    with short_dissolve

                    parker "... Да, это мое. Я думал, что я ее выбросил."

                    show parker_inactive at parkerT
                    show ivy_neutral at ivyT
                    with short_dissolve

                    ivy "Ну, как же хороший детектив не заглянет в мусор?"

                    hide ivy_neutral
                    hide parker_inactive
                    with short_dissolve

                    parker "Хех, справедливо. Послушай, это довольно личное... Почему я ее написал, пожалуйста, просто игнорируй это."

                    show parker_inactive at parkerT
                    with short_dissolve

                    if parker_clues == False:
                        "Он явно растерян из-за того, что я нашел его записку... мне нужно больше информации, чтобы понять почему."
                    else:
                        "После того как он пытался обвинить всех, а теперь его реакция на записку... мне нужно узнать правду."

                    hide parker_inactive
                    hide parker_sad
                    with short_dissolve

                    $ parker_confront = True
                    
                    jump parker_qs
                
                "Показать ему клей и обрывки." if clues["scraps"] == True and ash_confront == False:
                    parker "Что это, черт побери? Просто выглядит как мусор."

                    jump parker_qs
                
                "Показать ему эскизы в грязном альбоме." if clues["sketch"] == True and sterling_confront == False:
                    parker "Что, просто какие-то рисунки книги? Это странно, но не мое."

                    jump parker_qs
                
                "Ничего.":
                    parker "Ладно, как хочешь."

                    jump parker_qs

        "Паркер, нам нужно поговорить." if parker_confront == True and parker_clues == True and mystery_solved["parker"] == False:
            
            show parker_inactive at parkerT
            with short_dissolve
            
            "Все эти обвинения и странное поведение... Паркер явно что-то скрывает."

            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Слушай, Паркер, я буду с тобой честна. Ты был таким подозрительным, что происходит?"

            hide ivy_neutral
            show parker_angry at parkerT
            with short_dissolve

            parker "Ч-чего? Я не был подозрительным! Назови хоть один момент, когда я был подозрительным!"

            show ivy_neutral at ivyT
            hide parker_angry
            with short_dissolve

            ivy "Ну, ты же предал своих друзей..."

            hide ivy_neutral
            show parker_angry at parkerT
            with short_dissolve

            parker "Ты попросила меня о информации! Я тебе ее дал!"

            hide parker_angry
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "... и плюс, есть твоя записка с извинениями, которую я нашел. Ты еще не сказал мне, что это все значит."

            hide ivy_neutral
            show parker_angry at parkerT
            with short_dissolve
            
            parker "Я совершенно не обязан! Это личное дело, спасибо большое."

            hide parker_angry
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Паркер, пожалуйста, мне нужно знать, ты не испортил мой семейный альбом. Пожалуйста, будь честен."

            hide parker_inactive
            hide ivy_neutral
            with short_dissolve

            parker "Просто... ну, это..."

            show parker_sad at parkerT
            with short_dissolve

            parker "Извини, что кричал. Слушай, моя биологическая мать в больнице. Я получил письмо от нее несколько дней назад..."

            show parker_inactive at parkerT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Твоя биологическая мать? Но вы же не общались последние несколько лет?"

            hide ivy_neutral
            hide parker_inactive
            with short_dissolve

            parker "Да... и всё ещё не общаемся, кроме этого письма. Я не знаю, что думать, когда узнал, что с ней что-то не так..."

            parker "... это как-то заставило меня что-то сказать, понимаешь? Она была плохой матерью, но и я тоже не был лучшим ребенком."

            show parker_inactive at parkerT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "То есть, записка была для нее?"

            hide ivy_neutral
            hide parker_inactive
            with short_dissolve

            parker "Ну, она была для нее. Но я так и не придумал, как написать это так, как мне хотелось."

            parker "Извини, что солгал, но я не хотел, чтобы кто-то еще знал."

            show parker_inactive at parkerT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Не переживай, я никому не скажу. Спасибо, что был честен, Паркер."

            $ mystery_solved["parker"] = True

            if mystery_solved["ash"] == True and mystery_solved["reagan"] == True and mystery_solved["sterling"] == True:
                $ ending = False

                hide ivy_inactive
                hide ivy_neutral
                hide parker_neutral
                hide parker_sad
                hide parker_inactive
                with short_dissolve

                jump solving
            else:

                hide ivy_neutral
                with short_dissolve

                "Паркер определенно переживает многое, я не думаю, что он испортил альбом с учетом всего, что происходит."

                "Мне нужно поговорить с другими подозреваемыми, чтобы выяснить, кто это сделал."

                jump invest_loop

        "Это все на данный момент.":
                parker "Ладно, звучит как план. Увидимся, Айви."

                jump invest_loop

    jump invest_loop
label living_room:

    $ explored = True
    scene bg living room:
        zoom 1.0
        xalign 1.0

    if roomList["living_room"] == False:
        menu living_room_search:

            "Вот и гостиная, где находится Эш. Стоит ли мне осмотреть комнату или поговорить с ней?"

            "Осмотреть комнату":

                "Гостиная довольно беспорядочна, так как здесь они провели больше всего времени на выходных. Телевизор и игры явно заняли их внимание."

                "Кроме беспорядка, в комнате не так много интересного. Логично, что здесь нет следов, ведь здесь было много людей."

                $ roomList["living_room"] = True
                
                menu living_room_post_search:

                    "Комната осмотрена. Стоит ли поговорить с Эш или идти в другую комнату?"

                    "Поговорить с Эш.":
                        jump ash_talk
                    
                    "Пойти в другую комнату.":
                        jump invest_loop
            
            "Поговорить с Эш.":
                jump ash_talk
    else:
        "Я уже осмотрела комнату, давай поговорим с Эш."
        jump ash_talk

label ash_talk:

    show ivy_inactive at ivyT
    show ash_neutral at ashT
    with short_dissolve

    ash "Ах, привет, Айви. Я как раз думала, когда ты начнешь меня расспрашивать."

    menu ash_qs:

        ash "Что случилось?"

        "Ты это испортила?" if parker_clues == False or ash_confront == False:

            show ash_angry at ashT
            with short_dissolve

            ash "Абсолютно нет. Я в шоке, что ты даже спросила меня об этом."

            hide ash_angry
            show ash_inactive at ashT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Послушай, я спросила всех."

            hide ash_inactive
            hide ivy_neutral
            with short_dissolve

            ash "Да, конечно."

            jump ash_qs
        
        "Какой у тебя был график сегодня?" if parker_clues == False or ash_confront == False:

            show ash_angry at ashT
            with short_dissolve

            ash "Что? Почему?"

            hide ash_angry
            show ash_inactive at ashT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Я пытаюсь понять, где кто был, чтобы выяснить, кто испортил альбом."

            hide ivy_neutral
            hide ash_inactive
            with short_dissolve
            
            ash "Конечно, конечно. Ну, я была в спальне, на кухне, в офисе и потом в библиотеке."

            show ivy_neutral at ivyT
            show ash_inactive at ashT
            with short_dissolve
            
            ivy "Хорошо, звучит нормально. Ты была всегда одна, или видела кого-то еще?"

            hide ivy_neutral
            hide ash_inactive
            with short_dissolve

            ash "Я тусовалась с Паркером на кухне, а так — была одна."

            jump ash_qs
        
        "Есть ли что-то, что ты знаешь, что может мне помочь?" if parker_clues == False or ash_confront == False:

            show ash_angry at ashT
            with short_dissolve

            ash "Слушай, я знаю, что Рейган все о дружбе и доброте, но ты серьезно!"

            ash "Она явно что-то скрывает! Нет, ну ты что, не думаешь, что она лжет, чтобы показать себя хорошей?"

            hide ash_angry
            show ash_inactive at ashT
            show ivy_angry at ivyT
            with short_dissolve
            
            ivy "Ну, это довольно грубо так предполагать. Есть ли что-то подозрительное, что заставляет тебя так думать?"

            hide ash_inactive
            hide ivy_angry
            with short_dissolve
            
            ash "Она просто излучает такую атмосферу, понимаешь? Я чувствую, что что-то не так. Сходи и поговори с ней."

            jump ash_qs
        
        "Могу я показать тебе одну вещь, которую я нашла?" if parker_clues == False or ash_confront == False:
            ash "Конечно, что там?"

            menu ash_clues:
                "Показать ей поисковые запросы на компьютере." if clues["computer"] == True and reagan_confront == False:
                    ash "Ха, глупо. Эти поисковые запросы — ерунда, и они не мои."

                    jump ash_qs
                
                "Показать ей смятый «извиняющийся» записку." if clues["note"] == True and parker_confront == False:
                    ash "Ого, что за ужасное письмо, ты что, взяла его у третьеклассника?"

                    jump ash_qs
                
                "Показать ей клей и обрезки." if clues["scraps"] == True:
                    ash "Что? Где ты это нашла?"

                    show ash_inactive at ashT
                    show ivy_neutral at ivyT
                    with short_dissolve

                    ivy "О, в библиотеке. Ты их узнаешь?"

                    hide ash_inactive
                    hide ivy_neutral
                    with short_dissolve

                    ash "Нет, это просто грязь. Я бы их выбросила, зачем хранить этот мусор?"

                    show ash_inactive at ashT
                    show ivy_neutral at ivyT
                    with short_dissolve

                    ivy "Это очевидно улика, бумага очень похожа на материал из семейного альбома."

                    hide ash_inactive
                    hide ivy_neutral
                    with short_dissolve
                    
                    ash "Хмм... Я этого не вижу. Просто выбрось их, Айви."

                    show ash_inactive at ashT
                    show ivy_neutral at ivyT
                    with short_dissolve

                    ivy "Я не собираюсь выбрасывать улику, Эш, успокойся."

                    show ash_angry at ashT
                    hide ivy_neutral
                    with short_dissolve

                    ash "Просто. Выбрось это. Черт возьми, ты становишься слишком навязчивой с этим «расследованием»."

                    hide ash_angry
                    show ivy_neutral at ivyT
                    with short_dissolve

                    ivy "Да, ладно. Спасибо, что показала их..."

                    hide ivy_neutral
                    with short_dissolve

                    if parker_clues == False:
                        "Она, наверное, хочет, чтобы я выбросила эти обрезки, потому что они её, но мне нужно больше информации, прежде чем я с ней буду говорить."
                    else:
                        "Если Эш действительно что-то скрывает от всех, даже от Паркера, и настаивает, чтобы эти обрезки были выброшены, мне нужно разобраться в правде."

                    $ ash_confront = True

                    hide ash_inactive
                    with short_dissolve

                    jump ash_qs
                
                "Показать ей эскизы из альбома." if clues["sketch"] == True and sterling_confront == False:
                    ash "Хм, я никогда не видела этого раньше."

                    jump ash_qs
                
                "Ничего.":
                    ash "Ну и ладно."

                    jump ash_qs
        
        "Эш, нам нужно поговорить." if ash_confront == True and parker_clues == True and mystery_solved["ash"] == False:

            show ash_inactive at ashT
            with short_dissolve

            "Эш так настаивала, чтобы я выбросила эти обрезки, они точно её."

            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Эш, я знаю, что обрезки из альбома — это твои. И я знаю, что ты что-то скрываешь от всех."

            ivy "Пора сказать правду."

            hide ivy_neutral
            hide ash_inactive
            with short_dissolve

            ash "Что? Нет, ты ошибаешься."

            show ash_inactive at ashT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Правда? Можешь объяснить, что это за обрезки? Никто их не узнал, кроме тебя."

            hide ivy_neutral
            show ash_angry at ashT
            with short_dissolve

            ash "Я их не узнала, просто настояла, чтобы ты выбросила этот мусор."

            hide ash_angry
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Но ты также избегала Паркера в спальне, когда увидела его там. Что ты скрываешь даже от него?"

            show ash_angry at ashT
            hide ivy_neutral
            with short_dissolve
            
            ash "Ничего. Я ничего не скрываю."

            show ivy_angry at ivyT
            hide ash_angry
            with short_dissolve

            ivy "Эш, ты просто закрылась. Ты не можешь этого избегать, я знаю, что ты что-то скрываешь!"

            hide ivy_angry
            show ash_angry at ashT
            with short_dissolve

            ash "Я не скрываю ничего."

            hide ash_angry
            show ivy_angry at ivyT
            with short_dissolve

            ivy "О, не строй из себя невиновную, я знаю, что ты что-то скрываешь. Признайся."

            hide ivy_angry
            show ash_angry at ashT
            with short_dissolve

            ash "..."

            hide ash_angry
            show ivy_angry at ivyT
            with short_dissolve

            ivy "Ну что? Я не уйду, пока не узнаю правду. Или мне просто подумать, что ты испортила альбом?"

            ivy "Или ещё хуже — что ты сделала это специально."

            show ash_sad at ashT
            hide ivy_angry
            with short_dissolve

            ash "Айви, ты же знаешь, я никогда бы не сделала этого с тобой или с твоей семьей!"

            hide ash_sad
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "Может быть, но ты ведешь себя так странно, что это становится возможным."

            hide ivy_neutral
            show ash_angry at ashT
            hide ash_inactive
            with short_dissolve

            ash "Слушай..."

            show ash_sad at ashT
            hide ash_angry
            with short_dissolve

            ash "Да... я вру уже некоторое время. Меня уволили несколько недель назад. Была проблема с интеллектуальной собственностью в программе, которую я создала."

            ash "Вместо того, чтобы нормально оплатить мою работу, они просто меня уволили. Я общалась с юристами по этому поводу, но до тех пор..."

            ash "Я не хотела, чтобы вы знали, что у меня проблемы. Я едва могла позволить себе приехать сюда на выходные."

            show ivy_sad at ivyT
            hide ash_sad
            show ash_inactive at ashT
            with short_dissolve
            
            ivy "Эш... тебе не нужно было лгать. Если бы я знала, что это тебе тяжело, мы бы что-то придумали."

            show ash_sad at ashT
            hide ivy_sad
            with short_dissolve

            ash "Я не хотела помощи, и не хотела, чтобы вы знали, что создаю проблемы."

            show ivy_neutral at ivyT
            hide ash_sad
            with short_dissolve

            ivy "Я понимаю, правда. Подожди, а как насчет этих обрезков? Это твои?"

            hide ash_inactive
            hide ivy_neutral
            with short_dissolve

            ash "Да... так как у меня не было денег, я попыталась создать страницу для твоего альбома, как подарок на день рождения."

            ash "Я даже использовала твой семейный альбом как вдохновение, но потом сразу же положила его обратно."

            show ash_inactive at ashT
            show ivy_neutral at ivyT
            with short_dissolve

            ivy "А, теперь понятно, почему шаблон так похож."

            $ mystery_solved["ash"] = True

            if mystery_solved["reagan"] == True and mystery_solved["parker"] == True and mystery_solved["sterling"] == True:
                $ ending = True
                jump solving
            else:

                hide ivy_neutral
                with short_dissolve

                "Эш использовала альбом, но говорит, что не испортила его. Я должна продолжить расследовать других подозреваемых."
                jump invest_loop

        "На этом всё.":
            ash "Круто, надеюсь, тебе не нужно будет снова меня беспокоить."

            jump invest_loop

    jump invest_loop
label office:

    $ explored = True
    scene bg office:
        zoom 1.75
        yalign 1.0
    
    if roomList["office"] == False:

        "Вот офис, место преступления. Мне стоит осмотреться."
        
        "альбом все еще лежит на столе, вокруг него кусочки бумаги и мокрые страницы."
        
        "Мне так жаль, что он был испорчен, надеюсь, я смогу разобраться, что случилось."
        
        "Все остальное в комнате удивительно чисто и аккуратно."
        
        "Компьютер тоже выключен... нет, просто в спячке. Экран загорелся, когда я пошевелил мышку."
        
        "Подожди... кто-то использовал компьютер в последний раз, и у него было много открытых вкладок."
        
        "Они искали 'как лгать', 'как хранить секреты' и другие варианты этого вопроса."
        
        "Как странно, зачем кому-то искать, как лгать? Мне нужно записать это и спросить у подозреваемых."
        
        "Больше ничего важного в этой комнате нет, и здесь никого нет. Мне стоит пойти в другую комнату."
        
        $ roomList["office"] = True
        
        $ clues["computer"] = True
        
        jump invest_loop

    else:
        "Я уже осмотрел эту комнату, больше нечего здесь делать."
        jump invest_loop

    jump invest_loop

label solving:
    
    if ending == True:
        
        hide ash_inactive
        hide ivy_neutral
        hide ash_neutral
        hide ivy_inactive
        show ivy_neutral at ivyT
        show ash_inactive at ashT
        with short_dissolve

        ivy "Подожди секунду... ты убрал альбом сразу после? Он был поврежден?"
        
        show ivy_inactive at ivyT
        show ash_neutral at ashT
        with short_dissolve

        ash "Что? Нет, он был в идеальном состоянии. Почему?"
        
        hide ash_neutral
        hide ivy_inactive
        with short_dissolve

        ivy "Ну, Стерлинг сказал, что он нашел его поврежденным, когда вошел в офис в 4:00, а ты был там перед ним."
    
    else:
        "Черт, все алиби кажутся довольно убедительными. Но, к счастью, я знаю, что Стерлинг нашел альбом поврежденным около 4:00."
        
        "Если я правильно помню, то человек, который был там до него, это... ты."
        

        show bg living room:
            zoom 1.0
            xalign 1.0

        show ivy_inactive at ivyT
        show ash_neutral at ashT
        with short_dissolve

        ash "Ах, с возвращением. Как идет расследование?"

        show ivy_neutral at ivyT
        show ash_inactive at ashT
        with short_dissolve

        ivy "Нормально, но у меня почти не осталось улик. Но есть еще одна зацепка."

        hide ivy_neutral
        hide ash_inactive
        with short_dissolve

        ash "О? И я думаю, это как-то связано со мной?"

        show ivy_neutral at ivyT
        show ash_inactive at ashT
        with short_dissolve

        ivy "Да, связано. Слушай, Стерлинг признался мне, что он нашел альбом поврежденным, когда вошел в офис около 4:00."

        ivy "Если посмотреть на расписание всех, то человек, который был там перед ним, это... ты."

        hide ivy_neutral
        hide ash_inactive
        with short_dissolve
        
        ash "Подожди, ты думаешь, что это я испортил альбом? И просто оставил его там?"

        show ivy_neutral at ivyT
        show ash_inactive at ashT
        hide ash_neutral
        hide ivy_inactive
        with short_dissolve
        
        ivy "Я имею в виду, что это единственная зацепка, которая у меня осталась, так что... да, я так думаю."
    
    show ivy_inactive at ivyT
    show ash_angry at ashT
    with short_dissolve

    ash "Что?! Нет, я оставил комнату в идеальном состоянии!"

    show ash_neutral at ashT
    hide ash_angry
    with short_dissolve

    ash "Подожди, тебе не нужно мое слово на это. Я сделала несколько фотографий альбома для вдохновения."

    hide ash_neutral
    with short_dissolve
    
    "Эш показывает мне свой телефон, и на нем несколько фотографий семейного альбома, как она и сказала. Он выглядит совершенно неповрежденным."

    hide ivy_inactive
    with short_dissolve
    
    ivy "Ладно, значит, он не был поврежден, когда ты была там. А ты сразу его убрала?"

    show ivy_inactive at ivyT
    show ash_neutral at ashT
    with short_dissolve

    ash "Да! Клянусь, я так и сделала."

    hide ash_neutral
    with short_dissolve

    "Хмм... фотографии определенно не лгут. Мне стоит поговорить со Стерлингом по поводу этой новой информации."

    hide ash_inactive
    hide ivy_inactive
    hide ivy_neutral
    with short_dissolve


    show bg bedroom:
        zoom 0.8
        xalign 1.0

    show sterling_neutral at sterlingT
    show ivy_inactive at ivyT
    with short_dissolve

    sterling "Привет, Иви. Что тебя снова привело?"

    show ivy_neutral at ivyT
    show sterling_inactive at sterlingT
    with short_dissolve

    ivy "Ладно, Стерлинг, я знаю, что что-то не так."

    hide ivy_neutral
    hide sterling_inactive
    with short_dissolve

    sterling "Ч-Что? Что это значит?"

    show ivy_neutral at ivyT
    show sterling_inactive at sterlingT
    with short_dissolve

    ivy "Я поговорила с Эш, и она сказала, что альбом не был поврежден, когда она была в офисе. Она утверждает, что это не она."

    hide ivy_neutral
    hide sterling_inactive
    with short_dissolve

    sterling "А, она так сказала? Как ты знаешь, что она говорит правду?"

    show ivy_neutral at ivyT
    show sterling_inactive at sterlingT
    with short_dissolve

    ivy "Ну, у нее есть фотографии, подтверждающие, что он был в целости, когда она его забрала."

    hide ivy_neutral
    hide sterling_inactive
    show sterling_sad at sterlingT
    with short_dissolve

    sterling "О..."

    sterling "Что если она его испортила после этого?"

    hide sterling_sad
    show sterling_inactive at sterlingT
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Я не думаю, что это так, она уверяет, что он был в идеальном состоянии, когда ушла."

    hide ivy_neutral
    hide sterling_inactive
    with short_dissolve

    sterling "Я знаю, она твоя подруга, но я видел, что видел, Иви."

    show ivy_neutral at ivyT
    show sterling_inactive at sterlingT
    with short_dissolve

    ivy "Ты уверен? Потому что мне трудно спорить с фото-доказательствами. Есть ли у тебя еще какие-либо факты, подтверждающие, что ты видел?"

    hide ivy_neutral
    hide sterling_inactive
    with short_dissolve
    
    sterling "Я, эм... видел, как Паркер выходил из офиса за несколько минут до того, как я вошел. Может, Эш просто прикрывает его, знаешь?"

    show ivy_neutral at ivyT
    show sterling_inactive at sterlingT
    with short_dissolve
    
    ivy "Я не понимаю, как это возможно, если Паркер был в спальне, когда Эш вошла после того, как она покинула офис."

    hide ivy_neutral
    hide sterling_inactive
    with short_dissolve

    sterling "О-О, эмм..."

    show sterling_inactive at sterlingT
    show ivy_angry at ivyT
    with short_dissolve

    ivy "Стерлинг. Что здесь происходит? Из всех я никогда не думала, что это будешь ты, но вот мы и здесь."

    hide ivy_angry
    hide sterling_inactive
    with short_dissolve
    
    sterling "Иви, детка... я..."

    show sterling_inactive at sterlingT
    with short_dissolve

    "Он выпускает немного нервного смеха, пристально следя за моим выражением."

    hide sterling_inactive
    with short_dissolve

    sterling "Ладно, это был я. Я испортил альбом."

    show sterling_inactive at sterlingT
    show ivy_angry at ivyT
    with short_dissolve

    ivy "Ч-Что? Ты серьезно?"

    hide ivy_angry
    hide sterling_inactive
    with short_dissolve

    sterling "Подожди, пожалуйста, не кричи на меня!"

    sterling "Я уже связался с твоими родителями по поводу испорченного альбома, и мы решаем, что делать дальше."

    sterling "Это был как раз звонок, который я получил раньше за ужином."

    show sterling_inactive at sterlingT
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Правда? С какого времени ты связался с моими родителями по поводу этой ситуации?"

    hide ivy_neutral
    hide sterling_inactive
    with short_dissolve

    sterling "Ну... я спрашивал их об этом еще до этого уикенда."

    show sterling_inactive at sterlingT
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Окей... почему? Ты так и не ответил на мой вопрос, Стерлинг."

    hide ivy_neutral
    hide sterling_inactive
    with short_dissolve

    sterling "Я просто... я был..."

    show sterling_inactive at sterlingT
    with short_dissolve

    "Он выпускает вздох, плечи опускаются в разочаровании."

    show sterling_sad at sterlingT
    with short_dissolve

    sterling "Я тайно пытался придумать, как сделать тебе предложение. Твои родители на самом деле упомянули альбом..."

    sterling "... как они думали, что это может помочь мне найти вдохновение. Так что, когда я получил шанс, я подкрался в офис, чтобы взглянуть на него."

    sterling "Сначала все было нормально. Я увидел несколько милых фотографий и все такое. Но все пошло не так, когда я пролил на него газировку."

    sterling "Я попытался вытереть это своей курткой, но понял, что просто размазываю ее и даже порвал несколько страниц."

    sterling "Когда я понял, какой ущерб я нанес, это был бардак. Я отчаянно пытался позвонить твоим родителям, чтобы объяснить, что я натворил."

    sterling "Но потом Рейган позвал всех на ужин, и я просто... оставил это там. Я думал, что никто этого не заметит до ночи."

    sterling "Очевидно, это не сработало. Извини, Иви, это все моя вина."

    hide sterling_sad
    with short_dissolve

    "Честно говоря, я переживала целую гамму эмоций. Злая из-за его лжи, смущена, что он хотел сделать предложение, моя голова шла кругом."

    show ivy_sad at ivyT
    with short_dissolve

    ivy "Я... Стерлинг... что? Мне приятно, что ты хотел сделать предложение, но... зачем лгать обо всем этом? Ты мог бы сказать мне раньше!"

    hide ivy_sad
    hide sterling_inactive
    with short_dissolve
    
    sterling "Ну... мое объяснение немного эгоистично. Я устроил весь этот спектакль, лгал и обвинял..."

    show sterling_happy at sterlingT
    with short_dissolve

    sterling "... потому что я знаю, как ты любишь мистические подкасты и шоу, и думал, что тебе будет приятно раскрыть дело самой."

    hide sterling_happy
    show sterling_inactive at sterlingT
    show ivy_happy at ivyT
    with short_dissolve

    ivy "О, детка, это так мило... и мне действительно было немного весело, надо признаться."

    hide ivy_happy
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Но в следующий раз не лги мне, идиот."

    hide ivy_neutral
    show sterling_happy at sterlingT
    with short_dissolve

    sterling "Ладно, обещаю, больше не буду."

    hide sterling_happy
    show sterling_inactive at sterlingT
    with short_dissolve

    "Ну, этот результат я точно не ожидала. Но, с разгаданной тайной и только с небольшой шуткой над Стерлингом..."

    "... я действительно отлично провела уикенд. Какой странный день рождения!"

    return

return
