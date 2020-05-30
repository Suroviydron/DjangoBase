from django.db import migrations


def forwards_func(apps, schema_editor):
    pro_cat_model = apps.get_model("mainapp", "ProductCategory")
    pro_model = apps.get_model("mainapp", "Product")
    con_model = apps.get_model("mainapp", "Contact")

    pro_cat_obj = pro_cat_model.objects.create(pk=1, name="Новинки")
    # Create new products in this category
    pro_model.objects.create(
        pk=1,
        category=pro_cat_obj,
        name="DOOM Eternal",
        image="products_images/doom.jpg",
        description= "DOOM Eternal — прямое продолжение хита DOOM 2016 года, завоевавшего множество наград. "
                     "Сокрушая всё на своём пути с невероятной силой и скоростью, прорывайтесь сквозь измерения в игре, "
                     "задающей новый стандарт для шутеров с видом от первого лица. Она создана на движке idTech 7 и "
                     "сопровождается взрывным саундтреком от композитора Мика Гордона. Хватайте мощное оружие и "
                     "отправляйтесь вместе с Палачом Рока (DOOM Slayer) разносить в клочья новых и хорошо знакомых "
                     "демонов, заполонивших неизведанные миры DOOM Eternal.\r\nНовый арсенал. Станьте еще более "
                     "быстрым, сильным и подвижным с помощью новых и усовершенствованных видов оружия, в числе которых "
                     "наплечный огнемет и выдвижной наручный клинок, а также новых возможностей, таких как способность "
                     "«Рывок».\t\r\nВыживайте и совершенствуйтесь. Воспользуйтесь своими врагами. Совершайте казни "
                     "славы, чтобы получить дополнительное здоровье, сжигайте врагов, чтобы получить броню, и кромсайте"
                     " демонов бензопилой, чтобы пополнить боеприпасы –превратитесь в самого грозного убийцу демонов."
                     "\r\nИграйте в режиме Battlemode. Окунитесь в новый сетевой режим формата «2 против 1», "
                     "разработанный студией id Software. Вооруженному до зубов Палачу Рока предстоит в течение 5 "
                     "раундов бороться с двумя опасными демонами под управлением игроков-соперников.\r\nНовые "
                     "незабываемые локации. Станьте свидетелем пришествия ада на Землю, сражайтесь с врагами во время "
                     "вторжения на Фобос и откройте древние тайны вселенной DOOM.\r\nРазрывайте демонов на куски."
                     "К обожаемым поклонниками демонам присоединятся орды новых исчадий Ада, в числе которых Охотник, "
                     "Мародер и Гладиатор Рока. Благодаря новой системе расчленения врагов вы теперь сможете кромсать "
                     "врагов на мелкие кусочки. \r\nВ течение года со дня выхода DOOM Eternal выйдут два сюжетных "
                     "дополнения. Каждая из этих самостоятельных историй позволит иначе взглянуть на события игры и "
                     "расскажет о катастрофе, которая привела к завоеванию Земли демонами.",
        price=3600,
        quantity=100,
        developer="id Software",
        genre="Шутер от первого лица",
        image01="products_images/doom01.jpg",
        image02="products_images/doom02.jpg",
        image03="products_images/doom03.jpg",
        image04="products_images/doom04.jpg",
        image05="products_images/doom05.jpg",
        image06="products_images/doom06.jpg",
        language="Русский",
        platform="PS4",
        publisher="Bethesda Softworks",
        released="20.03.2020",
        video_url="https://www.youtube.com/embed/HmyUmGWEqXc",
        age="18+"
    )
    pro_model.objects.create(
        pk=2,
        name="Nioh 2",
        image="products_images/nioh.jpg",
        description="Дайте волю тьме внутри. Познайте боевые искусства самураев в этой жестокой RPG… иначе смерть заберет вас. В 1555 году когда-то прекрасные, мирные земли Японии заполонили злобные твари и духи, и над страной нависла ужасная угроза. Вы одинокий наемник, который использует сверхъестественные способности в бою с врагами. Сможете ли вы пережить смутные времена в конце периода Сэнгоку?\r\n\r\nОтточите свои навыки. Приготовьтесь к битве всей своей жизни при помощи обновленной механики, основанной на самых обожаемых элементах Nioh и требующей еще больше сосредоточенности и мастерства.\t\r\nВыберите способ ведения боя. Пройдите путь самурая, вооружившись традиционным оружием, в том числе мечами и топорами, или заполните шкалу амрита, чтобы овладеть могучими способностями ёкая и уничтожить чудовищных врагов несколькими мощными атаками.\r\nПомогайте другим игрокам и получайте помощь от них. Призовите на помощь призраков, оставленных другими игроками Nioh 2, чтобы помочь вам в битве. Их дух будет помогать вам до самого конца уровня... или пока вы не погибнете.\r\nНа данный момент запланировано три крупных дополнения, каждое из которых будет посвящено своей собственной истории, причём эти истории предшествуют событиям Nioh 2. Каждое дополнение рассчитано на несколько часов игры и станет достойным испытанием для тех, кто жаждет сложностей.",
        price=4000,
        quantity=60,
        category=pro_cat_obj,
        developer="Koei Tecmo / Team Ninja",
        genre="Боевик / Ролевая игра",
        image01="products_images/nioh01.jpg",
        image02="products_images/nioh02.jpg",
        image03="products_images/nioh03.jpg",
        image04="products_images/nioh04.jpg",
        image05="products_images/nioh05.jpg",
        image06="products_images/nioh06.jpg",
        language="Русские субтитры",
        platform="PS4",
        publisher="Sony Interactive Entertainment",
        released="13.03.2020",
        video_url="https://www.youtube.com/embed/FJq7nvv_Z6s",
        age="18+"
    )
    pro_model.objects.create(
        pk=3,
        name="Resident Evil 3 Remake",
        image="products_images/resident.jpg",
        description="Только Джилл Валентайн знает о преступлениях корпорации «Амбрелла». Чтобы остановить её, «Амбрелла» использует секретное оружие: Немезис!\r\nВ комплект входит новая сетевая игра Resident Evil Resistance, в которой четверо выживших бросают вызов зловещему Высшему разуму и пытаются сбежать из его плена.\r\nДжилл Валентайн возвращается.<\/b> Загляните в лицо своим страхам в роли Джилл Валентайн, члена специального отряда полицейского Департамента Раккун-Сити S.T.A.R.S. Выбравшись из кошмарного особняка во время событий первой игры Resident Evil, Джилл начинает собственное расследование с целью узнать, кто же является создателем смертоносного Т-вируса, в результате чего становится участницей еще более жуткой истории.Насладитесь классическим игровым процессом Resident Evil.Расположенная за плечом персонажа камера и обновленное управление позволит насладиться более современным игровым процессом и классическим дизайном знаменитой игры ужасов на выживание совершенно по-новому.\r\nВас ждет напряжение в высшей степени.Погрузитесь в апокалиптическую атмосферу благодаря движку RE Engine, воссоздающему фотореалистичные локации с отвратительными зомби, кровожадными тварями и сверхъестественным охотником, неустанно рыскающим в темноте.",
        price=3900,
        quantity=20,
        category=pro_cat_obj,
        developer="Capcom",
        genre="Боевик / Триллер",
        image01="products_images/resident01.jpg",
        image02="products_images/resident02.jpg",
        image03="products_images/resident03.jpg",
        image04="products_images/resident04.jpg",
        image05="products_images/resident05.jpg",
        image06="products_images/resident06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Capcom",
        released="03.04.2020",
        video_url="https://youtu.be/YgqKMelDwfc",
        age="18+"
    )
    del pro_cat_obj  # Delete link for category

    pro_cat_obj = pro_cat_model.objects.create(
        pk=2,
        name="Эксклюзивы PlayStation"
    )

    pro_model.objects.create(
        pk=4,
        name="Death Stranding",
        image="products_images/deathstranding.jpg",
        description="Death Stranding – загадочный приключенческий триллер с открытым миром, ставший знаковым для жанра еще до своего выхода. Отважьтесь преодолеть мир, трансформированный Петлей смерти. Держите в своих руках бессвязные остатки нашего будущего и отправляйтесь в дорогу, чтобы восстановить связь между осколками мира.\r\n\t\tЗадача по воссоединению человечества в Death Stranding – далеко не единственная ваша головная боль. Помимо этой метафорической ноши, на ваши плечи также ляжет доставка огромного количества посылок в разные места страны. Вам придется переносить на себе еду, игры, бытовые принадлежности, медикаменты и информационные носители различного рода –  все, что может пригодиться для воссоединения изолированных граждан с цивилизацией.\r\n\t\tКак и в любом деле, где вы новичок, первые шаги по потрепанным американским просторам дадутся вам непросто. Иногда из-за труднопроходимой местности доставка груза становится невероятно сложным испытанием.\r\n\t\tВ главных ролях: Норман Ридус, Мадс Миккельсен, Леа Сейду и Линдси Вагнер.",
        price=3500,
        quantity=0,
        category=pro_cat_obj,
        developer="Kojima Productions",
        genre="Боевик / Приключение",
        image01="products_images/deathstranding01.jpeg",
        image02="products_images/deathstranding02.jpg",
        image03="products_images/deathstranding03.jpg",
        image04="products_images/deathstranding04.jpg",
        image05="products_images/deathstranding05.jpg",
        image06="products_images/deathstranding06.jpg",
        language="Русский",
        platform="PS4",
        publisher="Sony Interactive Entertainment",
        released="08.11.2019",
        video_url="https://www.youtube.com/embed/54RVcDgWuw8",
        age="18+"
    )

    pro_model.objects.create(
        pk=5,
        name="Days Gone",
        image="products_images/daysgone.jpg",
        description="Сражайтесь и гоняйте по смертельно опасным дорогам постапокалиптической Америки. Хватит ли вам навыков – и нервов – чтобы пережить ужасы расколотого мира в этом грандиозном приключенческом боевике с открытым миром?\r\n\t\tПримерьте заляпанную грязью обувь бывшего преступника, байкера Дикона Сент-Джона, охотника за головами, который пытается найти причину жить дальше там, где царит смерть. Находите ресурсы в заброшенных поселениях, чтобы затем мастерить из них полезные предметы и оружие, или налаживайте контакт с другими выжившими, занятыми честной торговлей... или более кровавыми делами.\r\nПоразительный мир. Северо-западное побережье Тихого океана с его величественными лесами, необъятными лугами, заснеженными горными вершинами и пустынными вулканическими плато настолько же прекрасно, насколько и опасно. Исследуйте горы, пещеры, ущелья и небольшие поселения, на протяжении миллионов лет страдавшие от извержений.\r\nЖестокие схватки. На этих землях нередко можно встретить агрессивно настроенных бандитов или толпы фриков, поэтому вы должны уметь находить применение своим ловушкам, оружию и улучшаемым навыкам, чтобы остаться в живых. И, конечно же, не забывайте о своем номадском байке, бесценном средстве передвижения по этим обширным землям.\r\nПостоянно меняющееся окружение. <\/b>Садитесь за руль верного мотоцикла Дикона и исследуйте живой мир с постоянно меняющимися погодными условиями, сменой дня и ночи, эволюционирующими фриками, которые приспосабливаются к окружению – и немногими выжившими.\r\nУвлекательная история. Погрузитесь в мощную историю об отчаянии, предательстве и сожалении, где вы возьмете на себя роль Дикона Сент-Джона, который пытается увидеть хотя бы проблеск надежды, чтобы оправиться от тяжелой утраты. Что делает нас людьми в ежедневной борьбе за выживание?",
        price=3300,
        quantity=10,
        category=pro_cat_obj,
        developer="Bend Studio",
        genre="Боевик / Приключение",
        image01="products_images/daysgone01.jpg",
        image02="products_images/daysgone02.jpg",
        image03="products_images/daysgone03.jpg",
        image04="products_images/daysgone04.jpg",
        image05="products_images/daysgone05.jpg",
        image06="products_images/daysgone06.jpg",
        language="Русский",
        platform="PS4",
        publisher="Sony Interactive Entertainment",
        released="26.04.2019",
        video_url="https://www.youtube.com/embed/ThxhPmwGQR4",
        age="18+"
    )
    pro_model.objects.create(
        pk=6,
        name="God of War",
        image="products_images/godofwar.jpg",
        description="Выбравшись из тени богов, Кратос обязан приспособиться к жизни в незнакомых землях с их "
                    "неожиданными опасностями, а еще стать хорошим отцом. Вместе со своим сыном Атреем он отправится "
                    "в очень личное путешествие по суровым скандинавским пустошам, где им вдвоем предстоит сражаться "
                    "с разнообразным злом. Отправляйтесь в мрачное царство стихий, где обитают грозные существа и "
                    "беспощадные боги, сошедшие со страниц скандинавской мифологии, Побеждайте врагов в неистовых"
                    "ближних схватках, проникнитесь трогательной историей отца и сына.\r\nНовая смелая история. "
                    "Будучи наставником и защитником своего сына, который стремится заслужить уважение отца, "
                    "Кратос получил неожиданную возможность научиться контролировать собственный гнев, который "
                    "долгое время определял его поступки. Задаваясь вопросами о том, какое темное наследие он "
                    "оставляет своему отпрыску, Кратос надеется исправить ошибки и ужасы своего прошлого.\t\r\n"
                    "Более мрачный мир. В диких лесах, горах и землях скандинавской мифологии вам предстоит "
                    "оказаться в совершенно новых и опасных местах со своим пантеоном существ, чудовищ и богов.\r\n"
                    "Беспощадные сражения. С новой камерой за плечом главного героя, игроки окажутся ближе к схваткам, "
                    "чем когда-либо, а сами бои станут яростнее и решительнее. Топор Кратоса – мощное магическое "
                    "оружие, которое также может выполнять роль универсального инструмента для исследования мира, "
                    "всегда вас защитит.",
        price=1300,
        quantity=1,
        category=pro_cat_obj,
        developer="Santa Monica Studio",
        genre="Боевик / Приключение",
        image01="products_images/godofwar01.png",
        image02="products_images/godofwar02.jpg",
        image03="products_images/godofwar03.jpg",
        image04="products_images/godofwar04.jpg",
        image05="products_images/godofwar05.jpg",
        image06="products_images/godofwar06.jpg",
        language="Русский",
        platform="PS4",
        publisher="Sony Interactive Entertainment",
        released="20.04.2018",
        video_url="https://www.youtube.com/embed/jCB36uNrZ9I",
        age="18+"
    )
    del pro_cat_obj  # Delete link for category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=3,
        name="Популярные игры"
    )

    pro_model.objects.create(
        pk=7,
        name="Control",
        image="products_images/control.jpg",
        description="Control - сверхъестественный экшен-шутер от третьего лица, который предложит вам освоить сверхъестественные способности, модифицируемое оружие и реактивную среду и ринуться с боем в таинственный и непредсказуемый мир.\r\nПогрузитесь в жуткий сверхъестественный кошмар в приключенческой игре от третьего лица от разработчиков Max Payne. Игра бросает вам вызов: сможете ли вы освоить сверхъестественные способности, собрать все необходимое и не погибнуть в пропитанном опасностью месте, сражаясь с неизвестным в глубоком и непредсказуемом игровом мире.\r\nИсследуйте огромный бетонный небоскреб, известный как «Старейший дом» (The Oldest House), вооружившись надежным табельным оружием – меняющим форму пистолетом. Это огромное, непрестанно меняющееся здание внутри еще более необъятное, чем может показаться снаружи, да еще и хранит множество тайн.",
        price=2500,
        quantity=12,
        category=pro_cat_obj,
        developer="Remedy Entertainment Oyj",
        genre="Боевик / Приключение",
        image01="products_images/control01.jpg",
        image02="products_images/control02.jpeg",
        image03="products_images/control03.jpg",
        image04="products_images/control04.jpg",
        image05="products_images/control05.jpg",
        image06="products_images/control06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="505 Games",
        released="27.08.2019",
        video_url="https://www.youtube.com/embed/_jr8HkUAyJ4",
        age="18+"
    )
    pro_model.objects.create(
        pk=8,
        name="The Outer Worlds",
        image="products_images/outer_worlds.jpg",
        description="The Outer Worlds — новая однопользовательская научно-фантастическая ролевая игра с видом от первого лица.\r\nВ The Outer Worlds вы пробуждаетесь после гибернации на корабле поселенцев, пропавшем по пути к Альциону — самой дальней земной колонии на краю галактики. Вы оказываетесь в центре масштабного заговора, который угрожает существованию всей колонии. Созданный вами персонаж сможет повлиять на ход этой истории, исследуя глубины космоса и встречая многочисленные группировки, которые сражаются за власть. В системе уравнений корпоративной колонии возникает новая непредсказуемая переменная — это вы.\r\nСоздайте свое приключение. Студия Obsidian не изменяет своим традициям, поэтому события в The Outer Worlds зависят от вас. Ваши решения влияют не только на сюжет, но и на развитие персонажа, судьбы спутников и финал игры.\t\r\nПревратите свои недостатки в достоинства.<\/b> Характер вашего героя формируется его слабыми и сильными сторонами. Игра The Outer Worlds анализирует ваши действия и определяет, что вы делаете хуже всего, а затем предлагает вам добавить этот недостаток в характер вашего персонажа в обмен на дополнительную способность.\r\nУправляйте спутниками. Исследуя далекую колонию, вы встретите немало персонажей, готовых вступить в вашу команду. В них заложены уникальные способности, задачи, мотивы и идеалы. Вы можете помочь каждому спутнику в достижении заветной цели или же использовать его для своей выгоды.\r\nИсследуйте корпоративную колонию. Альцион – колония на краю галактики, которой владеет и управляет корпоративный совет директоров, и вы должны проникнуть в его тайны. Соберите команду, добудьте корабль и отправляйтесь исследовать поселения, космические станции и другие уголки Альциона, полные загадок.",
        price=3200,
        quantity=2,
        category=pro_cat_obj,
        developer="Obsidian Entertainment",
        genre="Ролевая игра / Боевик",
        image01="products_images/outer_worlds01.jpg",
        image02="products_images/outer_worlds02.jpg",
        image03="products_images/outer_worlds03.jpg",
        image04="products_images/outer_worlds04.jpg",
        image05="products_images/outer_worlds05.jpeg",
        image06="products_images/outer_worlds06.jpeg",
        language="Русский",
        platform="PS4 \/ Xbox One",
        publisher="Private Division",
        released="25.10.2019",
        video_url="https://www.youtube.com/embed/-UXBXi5VDxc",
        age="18+",
    )
    pro_model.objects.create(
        pk=9,
        name="Sekiro: Shadows Die Twice",
        image="products_images/sekiro.jpg",
        description="Составляйте и воплощайте собственные планы мести в новом приключенческом боевике от студии "
                    "FromSoftware, создавшей серию Dark Souls. Эта игра получила премии 'Лучшая игра gamescom' и"
                    " 'Лучшая игра жанра Action' на выставке GAMESCOM 2018.\r\n\t\tВ игре Sekiro: Shadows Die "
                    "Twice вы станете «одноруким волком», изуродованным воином-изгоем, которого спасли от верной "
                    "смерти. Поклявшись защищать молодого господина, являющегося наследником древнего рода, вы "
                    "наживаете много опасных противников, среди которых — безжалостный клан Асина. Когда молодой "
                    "господин оказывается в плену, вы отправляетесь в опасный путь, чтобы спасти его, и ничто не "
                    "помешает вам восстановить свою честь.\r\nГлубокая и напряженная боевая система. Освойте до "
                    "мелочей проработанную систему боев на мечах и использование протеза руки, который очень "
                    "сильно влияет на то, как вы сражаетесь.  Объедините эти боевые навыки со скрытностью и "
                    "способностью преодолевать препятствия при помощи крюка-кошки, чтобы одолеть даже самых "
                    "сильных противников.\r\n\tИстория о предательстве. Станьте невероятно талантливым шиноби, "
                    "«одноруким волком». Потерпев поражение от скрывающегося в тени самурая Ашина, вернитесь к "
                    "жизни, чтобы изменить свою судьбу, спасти своего господина и отомстить врагам любой ценой."
                    "\r\nВпечатляющее путешествие. Исследуйте яркие локации, вдохновленные Японией кровавого периода"
                    " Сэнгоку, и используйте все доступные инструменты, чтобы находить тайные места, новые предметы, "
                    "готовых пообщаться с вами персонажей и скрытых врагов.\r\n\t\t\tЗнайте своего врага. Темные, "
                    "сверхъестественные силы – это то, с чем вам предстоит столкнуться в Sekiro в час кровавого периода"
                    " Сэнгоку, одного из самых жестоких в японской истории, пока искусные мечники и лучники орудуют на "
                    "землях Ашина, а еще большая опасность только приближается.",
        price=3000,
        quantity=5,
        category=pro_cat_obj,
        developer="From Software",
        genre="Боевик / Приключение",
        image01="products_images/sekiro01.jpg",
        image02="products_images/sekiro02.jpeg",
        image03="products_images/sekiro03.jpg",
        image04="products_images/sekiro04.jpg",
        image05="products_images/sekiro05.jpg",
        image06="products_images/sekiro06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Activision",
        released="22.03.2019",
        video_url="https://www.youtube.com/embed/kQaygYspsh8",
        age="18+"
    )
    pro_model.objects.create(
        pk=10,
        name="Borderlands 3",
        image="products_images/borderlands.jpg",
        description="Вернитесь в пустоши Пандоры, где царит беззаконие, в следующей главе саги лутер-шутера "
                    "Borderlands. Вам предстоит покорить доселе невиданные миры, играя за одного из четырех "
                    "новых искателей Хранилища, – нереально крутых перцев, у каждого из которых уникальные навыки, "
                    "способности и модификации. Действуя в одиночку или в компании друзей, вы должны будете дать "
                    "бой яростным противникам, нагрести побольше трофеев и спасти свой дом от безжалостных психопатов, "
                    "возглавляющих самую опасную секту в галактике.\r\nСтреляйте, перезаряжайтесь и собирайте добычу. "
                    "Горы стволов разбросаны по всем уровням — каждая схватка может пополнить ваш арсенал. "
                    "Есть оружие, стреляющее взрывающимися лезвиями, есть такое, которое никогда не нужно перезаряжать, "
                    "или такое, которое отращивает ноги и само гоняется за врагами.\r\nБезостановочное совместное "
                    "приключение. Играйте с другими игроками в любое время по сети или в режиме разделенного экрана, "
                    "независимо от вашего уровня или опыта в прохождении игры. Уничтожайте врагов и проходите испытания "
                    "в команде, но получайте отдельные награды – трофеев хватит на всех!\r\n\t\tСражения с опасными "
                    "фанатиками.Помешайте фанатичным близнецам Калипсо объединить бандитские кланы и стать самой мощной"
                    " силой в галактике. Только у вас, отважного искателя Хранилища, есть союзники и арсенал, "
                    "позволяющие тягаться с ними.",
        price=2900,
        quantity=10,
        category_id=3,
        developer="Gearbox Software",
        genre="Шутер от первого лица",
        image01="products_images/borderlands01.jpg",
        image02="products_images/borderlands02.jpg",
        image03="products_images/borderlands03.jpg",
        image04="products_images/borderlands04.jpg",
        image05="products_images/borderlands05.jpg",
        image06="products_images/borderlands06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Take-Two Interactive",
        released="13.09.2019",
        video_url="https://www.youtube.com/embed/s7Ho3BvqvXg",
        age="18+"
    )
    del pro_cat_obj  # Delete link for category
    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=4,
        name="Хиты Ubisoft"
    )
    # Create new products in this category
    pro_model.objects.create(
        pk=11,
        name="Assassin's Creed Bundle",
        image="products_images/assassin_bundle.jpg",
        description="Признанная критиками франшиза Assassin’s Creed возвращается на PlayStation 4 вместе с новыми "
                    "историями и заданиями, новым впечатляющим миром и полностью обновленной боевой системой."
                    "\r\nAssassins Creed Odyssey: Пройдите путь от изгоя до живой легенды: отправьтесь в далекое "
                    "странствие, чтобы раскрыть тайны своего прошлого и изменить будущее Древней Греции. Вас ждет "
                    "совершенно новая боевая система и морские путешествия в огромном бесшовном мире, который "
                    "постоянно развивается и реагирует на каждое ваше действие.\r\nAssassins Creed Origins: "
                    "Раскройте тайны Древнего Египта и узнайте, как было создано Братство ассасинов.",
        price=3200,
        quantity=50,
        category=pro_cat_obj,
        developer="Ubisoft",
        genre="Боевик / Приключение",
        image01="products_images/assassin_bundle01.jpg",
        image02="products_images/assassin_bundle02.jpg",
        image03="products_images/assassin_bundle03.jpg",
        image04="products_images/assassin_bundle04.jpg",
        image05="products_images/assassin_bundle05.jpg",
        image06="products_images/assassin_bundle06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Ubisoft",
        released="05.10.2018",
        video_url="https://www.youtube.com/embed/xgHoVQ0uZXk",
        age="18+"
    )
    pro_model.objects.create(
        pk=12,
        name="Assassin's Creed: Odyssey",
        image="products_images/assassin_odyssey.jpg",
        description="Assassins Creed Odyssey: Пройдите путь от изгоя до живой легенды: отправьтесь в далекое "
                    "странствие, чтобы раскрыть тайны своего прошлого и изменить будущее Древней Греции. "
                    "Вас ждет совершенно новая боевая система и морские путешествия в огромном бесшовном мире, "
                    "который постоянно развивается и реагирует на каждое ваше действие.\r\nСоздайте своего "
                    "легендарного героя. Впервые за всю историю франшизы Assassin’s Creed вы сможете выбрать, "
                    "за какого персонажа играть – Алексиоса или Кассандру. Улучшайте снаряжение, совершенствуйте "
                    "способности и изменяйте свой корабль в путешествии, которое сделает вас легендой Древней "
                    "Греции.\r\nОткройте для себя землю мифов и легенд. Исследуйте всю страну с величественными "
                    "городами и удивительной природой, от заснеженных вершин высоких гор до глубин Эгейского моря "
                    "в самый расцвет Золотого века Греции. Откройте для себя мир мифов и легенд. Узнайте больше "
                    "о древних ритуалах и знаменитых статуях, повстречайтесь с легендарными личностями Греции лицом "
                    "к лицу и раскройте правду, окутанную мифами.\r\nВыберите свой путь. Ваши решения будут изменять "
                    "мир вокруг, в игре вас ждет более 30 часов диалогов и несколько вариантов концовок. Наслаждайтесь"
                    " живым и динамичным миром, который постоянно изменяется и реагирует на каждое ваше действие."
                    "\r\nВступайте в сражения на суше и на море. Проявите необыкновенные воинские способности и "
                    "измените ход сражений Пелопоннесской войны. Сражайтесь за Спарту или Афины в грандиозных битвах"
                    " с участием до 150 воинов с обеих сторон. Соберите собственный флот для морских сражений. "
                    "Изменяйте облик своего корабля и нанимайте членов экипажа с уникальными характеристиками, "
                    "наиболее подходящими вашему игровому стилю.",
        price=2000,
        quantity=3,
        category=pro_cat_obj,
        developer="Ubisoft",
        genre="Боевик / Приключение",
        image01="products_images/assassin_odyssey01.jpg",
        image02="products_images/assassin_odyssey02.jpg",
        image03="products_images/assassin_odyssey03.jpg",
        image04="products_images/assassin_odyssey04.jpg",
        image05="products_images/assassin_odyssey05.png",
        image06="products_images/assassin_odyssey06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Ubisoft",
        released="05.10.2018",
        video_url="https://www.youtube.com/embed/xgHoVQ0uZXk",
        age="18+"
    )
    pro_model.objects.create(
        pk=13,
        name="Tom Clancy's Ghost Recon: Breakpoint",
        image="products_images/breakpoint_p.jpg",
        description="Tom Clancy’s Ghost Recon Breakpoint — это военный шутер, действие которого происходит в "
                    "полном разнообразия, враждебном и таинственном открытом мире. Вы можете играть в одиночку "
                    "или в команде из четырех игроков.\r\nИсследуйте опасный архипелаг. Исследуйте Авроа, где "
                    "нашла себе приют гигантская компания Кремниевой долины Skell Technology, по воздуху, морю и "
                    "суше. Перенеситесь на загадочный остров, где архитектурно выдающиеся сооружения смешиваются "
                    "с необъятной дикой природой. От заснеженных горных вершин до самых глубоких болот – местность "
                    "здесь чрезвычайно разнообразна.\r\nСразитесь со смертельно опасным врагом из своего прошлого."
                    " «Волки» – бывшая смертоносная военная организация США, которая вышла из-под контроля и готова "
                    "использовать самые эффективные технологии, чтобы уничтожить вас. Более того, они отлично вас "
                    "знают, ведь прошли ту же боевую подготовку, что и вы. «Волки» захватили Авроа, взяв под контроль "
                    "важнейшие ресурсы острова: беспилотники. Их лидер – ваш бывший брат по оружию, полковник Коул Д. "
                    "Уокер, и вам придется его уничтожить.\r\nИзменяйте своего Призрака. Создайте своего персонажа "
                    "и выбирайте из тысяч вариантов настроек, чтобы ваш Призрак выглядел именно так, как вы хотите. "
                    "Исследуйте игровой мир, собирая материалы, создавая и улучшая свое оружие, а также настраивайте "
                    "снаряжение Призрака под свой стиль игры. В Tom Clancy's Ghost Recon Breakpoint все решает ваш "
                    "выбор.\r\nОбъединитесь с друзьями. Объединитесь с друзьями и вместе проходите основную кампанию "
                    "или участвуйте в сражениях PvP-режима. Разблокируйте доступ к множеству дополнительных "
                    "материалов, "
                    "например, к рейдам для четверых игроков. Как бы вы ни решили играть, в Tom Clancy’s Ghost Recon "
                    "Breakpoint у вас всегда будет один и тот же персонаж: тот же внешний вид, те же навыки и то же "
                    "оружие.",
        price=2600,
        quantity=5,
        category=pro_cat_obj,
        developer="Ubisoft",
        genre="Тактический шутер",
        image01="products_images/breakpoint01.jpg",
        image02="products_images/breakpoint02.jpg",
        image03="products_images/breakpoint03.jpg",
        image04="products_images/breakpoint04.jpg",
        image05="products_images/breakpoint05.jpg",
        image06="products_images/breakpoint06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Ubisoft",
        released="04.10.2019",
        video_url="https://www.youtube.com/embed/oYeQGhcLxvU",
        age="18+"
    )
    pro_model.objects.create(
        pk=14,
        name="Tom Clancy's The Division 2",
        image="products_images/division.jpg",
        description="Семь месяцев прошло с тех пор, как смертельно опасный вирус поразил Нью-Йорк и остальной мир "
                    "и унес жизни многих людей. Когда разразилась эпидемия, в качестве последней линии обороны был "
                    "задействован Спецотряд «The Division» - группа агентов, которые до поры вели мирную жизнь под "
                    "прикрытием. С тех пор члены Спецотряда неустанно защищают то, что еще можно спасти.\r\n\t\tДля "
                    "них ставки высоки как никогда. Вашингтону, самому защищенному городу на Земле, угрожает "
                    "опасность, "
                    "а значит, целое государство находится на грани катастрофы. Если Вашингтон будет потерян, "
                    "американский народ ждет гибель. Вы - агент Спецотряда, сражающийся на передовой в течение "
                    "последних семи месяцев. Только вы и ваша команда можете предотвратить крах общества.\r\n"
                    "Измененный "
                    "облик Вашингтона. Пандемия, сопровождаемая ураганами и наводнениями, навсегда изменила облик "
                    "Вашингтона. Вам предстоит исследовать реалистичный открытый мир, поражающий разнообразием "
                    "ландшафта: "
                    "от затопленных урбанистических кварталов до узнаваемых исторических объектов, на которые наложило "
                    "отпечаток самое жаркое лето в истории. Множество враждующих группировок, преследующих собственные "
                    "цели, пытаются установить контроль над округом Колумбия, из-за чего на улицах Вашингтона "
                    "воцарился настоящий хаос. А задача по освобождению города и защите того, что осталось от "
                    "общества, ложится на вас.",
        price=1900,
        quantity=3,
        category=pro_cat_obj,
        developer="Massive Entertainment",
        genre="Тактический шутер",
        image01="products_images/division01.jpg",
        image02="products_images/division02.jpg",
        image03="products_images/division03.jpg",
        image04="products_images/division04.jpg",
        image05="products_images/division05.jpg",
        image06="products_images/division06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Ubisoft",
        released="15.03.2019",
        video_url="https://youtu.be/7NTKO4Y-JmY",
        age="18+"
    )
    del pro_cat_obj  # Delete link for category
    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=5,
        name="Игры Electronic Arts")

    pro_model.objects.create(
        pk=15,
        name="Need For Speed Heat",
        image="products_images/nfs_heat.jpg",
        description="Устраивайте гонки днём и ставьте на кон всё ночью в Need for Speed Heat — захватывающей игре, "
                    "в которой вам предстоит столкнуться с лучшими силами полиции и покорить мир уличных гонок. "
                    "Новейшая часть культовой гоночной серии, которая вновь попытается удивить игроков.\r\nРискуйте. "
                    "Участвуйте в местных гонках и побеждайте в соревнованиях, чтобы сорвать банк, а затем рискните "
                    "навлечь на себя гнев представителей закона во время заездов на запрещенных трассах."
                    "\t\r\nВыделитесь из толпы. Настройте управление и другие характеристики автомобиля, чтобы они "
                    "соответствовали вашему стилю игры, а затем пригласите друзей в свою команду и зажгите на улицах "
                    "Палм-Сити.\r\nДержите удар. Выступите против главы спецгруппы – лейтенанта Мёрсера, который "
                    "проводит незаконные операции и продаёт конфискованные автомобили по частям. Разоблачите его "
                    "грязные сделки.",
        price=3000,
        quantity=15,
        category=pro_cat_obj,
        developer="Ghost Games",
        genre="Гонки",
        image01="products_images/nfs_heat01.jpg",
        image02="products_images/nfs_heat02.jpg",
        image03="products_images/nfs_heat03.jpg",
        image04="products_images/nfs_heat04.jpg",
        image05="products_images/nfs_heat05.jpg",
        image06="products_images/nfs_heat06.jpg",
        language="Русский",
        platform="PS4 / Xbox One",
        publisher="Electronic Arts",
        released="08.11.2019",
        video_url="https://www.youtube.com/embed/9ewiJJe_nYI",
        age="16+",
    )

    del pro_cat_obj  # Delete link for category

   # Create contacts
    con_model.objects.create(
        pk=1,
        phone="+7-918-123-4567", email="Top-Games@mail.ru", city="Сочи", address="Возле Олимпийского парка"
    )
    con_model.objects.create(
        pk=2,
        phone="+7-777-777-7777",
        email="Top-Games@mail.ru",
        city="Краснодар",
        address="ул. Гидростроителей, 8",
    )
    con_model.objects.create(
        pk=3,
        phone="+7-999-999-9999",
        email="Top-Games@mail.ru",
        city="Краснодар",
        address="ул. Красная, 66",
    )


def reverse_func(apps, schema_editor):
    pro_cat_model = apps.get_model("mainapp", "ProductCategory")  # Load model for make changes
    con_model = apps.get_model("mainapp", "Contact")  # Load model for make changes

    # Delete all objects
    pro_cat_model.objects.all().delete()
    con_model.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0005_remove_contact_map'),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
