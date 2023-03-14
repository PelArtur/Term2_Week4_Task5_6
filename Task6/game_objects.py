import classes

#Items
sword = classes.Weapon('Меч героя')
chain_mail = classes.Armor('Броня героя')
knowledge_eye = classes.Artifact('Кристалічне ока знань', 'Epic')
knowledge_eye.set_description('Артефакт "Кристалічне око знань" - магічний кристал, що дозволяє своєму володарю отримувати всю інформацію про своїх ворогів. Кристал може використовувати різні методи збору інформації, такі як сканування мислення, зчитування душі, виявлення слабкостей та багато іншого. Крім того, "Кристалічне Око Знання" може також надавати своєму володарю додаткові знання та магічні здібності, які допоможуть йому перемогти своїх ворогів.')
acorn = classes.Items('Жолудь')
acorn.set_description('Жолуді з лісу Лімбел. Улюблене частування білок')
goblin_head = classes.Items('Голова ватажка гоблінів')
goblin_ear = classes.Items('Вухо гобліна', True)
damascus_ore = classes.Items('Дамаскова руда')
oak = classes.Items('Дуб')
horse_skin = classes.Items('Кінська шкіра')
steel = classes.Items('Сталь')
moon_tree_leaves = classes.Items('Листя місячного дерева')
gost_mushrooms = classes.Items('Гриби-духи')
forest_potions = classes.Items('Лісові зілля')
glowing_butterfly = classes.Items('Нічний вогник') #Метелик
clay = classes.Items('Глина')
spider_lily = classes.Items('Синя павуча лілія')
orks_bones = classes.Items('Кістки орків')
ork_sword = classes.Weapon('Хліборіз', True) #на продаж
culebra = classes.Weapon('Кулебра', True) 
power_ring = classes.Artifact('Перстень влади', True)
green_amethyst = classes.Items('Зелений аметист')
goblin_sw = classes.Weapon('Острівчик', True)
elf_aid = classes.Items('Екстракт з квітів йонклі')
dragon_fruit = classes.Items('Драконів фрукт')
river_flower = classes.Items('Водяна лицарівка')
ephedra = classes.Items('Корінь ефедри')
writing_set = classes.Items('Набір для письма')
oil_moonlight = classes.Items('Олія Місячного сяйва')
gnom_beer = classes.Items("Гном'яче пиво", True)

#Effective tools vs orks
damascus_sw = classes.Weapon('Меч з дамаску')
lantern = classes.Artifact('Ліхтар', 'Default')
lammelar = classes.Armor('Пластинчаста броня')
#Effective tools vs pirats
storm_heart = classes.Weapon('Серце шторму')
storm_heart.set_description('Це магічний меч з іскристим клинком, який може генерувати потужні бурі та грози. Кожен удар мечем випромінює магічний вибух.')
storm_staff = classes.Artifact('Посох бурі', 'Legendary')
storm_staff.set_description('Це магічний посох, який може викликати потужні бурі та грози, що можуть знищити будь-яку армію. Його можна використовувати як зброю, але його справжня сила полягає у магічних заклинаннях, які можна виконувати з його допомогою.')
storm_cloack = classes.Armor('Плащ бурі')
storm_cloack.set_description('Це магічний плащ, що дозволяє носителю рухатись зі швидкістю бурі. Виготовлений з тканини, яка зміцнена магією')
#Effective tool vs goblins
elves_blade = classes.Weapon('Клинок Ельфів')
elegy_horn = classes.Artifact('Ріг Елегії')
light_mail = classes.Armor('Легка кольчуга')
#Amulets
wind = classes.Items('Амулет повітря')
rock = classes.Items('Амулет землі')
fire = classes.Items('Амулет вогня')
water = classes.Items('Амулет води')
wind.set_description('Амулет надає власнику можливість керувати повітрям і контролювати його стихійність.')
rock.set_description('Цей амулет дарує власнику магічну силу землі і контроль над грунтом. Його можна використовувати для створення гір, спотворення ландшафту або утворення землетрусів.')
fire.set_description('Цей амулет дозволяє власнику контролювати вогонь і використовувати його для створення вогняних куль або струменів, знищення ворогів і розжарювання металу.')
water.set_description("Цей амулет надає власнику контроль над водою і дозволяє створювати водні струмени, контролювати приплив і відплив. З його допомогою також можна створювати магічні водяні бар'єри.")
#Scrolls
scroll_ishrat = classes.Scroll('Сувій Іштар')
scroll_ishrat.set_description('Сувій отриманий після перемоги над братами орками в печері Печалі.\nЗа його допомоги артефакт може пробити навіть найтвердіший шар прокляття')
scroll_odina = classes.Scroll('Сувій Одіна')
scroll_odina.set_description('Сувій отриманий після перемоги над капітаном Морганом.\nЗа його допомоги артефакт дозволить проникнути в глибини джерела прокляття та знищити його.')
scroll_gekaty = classes.Scroll('Сувій Гекати')
scroll_gekaty.set_description('Сувій отриманий в німфи Рейни.\nЗа його допомоги артефакт зможе знайти джерело прокляття та ослабити його, зробивши доступним для знищення.')
god_artifact = classes.Artifact('Триумф Божеств', 'Divine')
god_artifact.set_description("Артефакт, який об'єднує силу богів")
#Characters
oliviar = classes.NPC('Олівіяр', 'Ельф')
oliviar.converstation = "Ласкаво просимо до нашого лісу! Я - Олівіяр, один з небагатьох ельфів, які живуть тут. Розкажи мені про себе, мій шановний гостю."
arion = classes.NPC('Аріон', 'Ельф')
arion.converstation = "Вітаю тебе, мій друг. Я - Аріон, ельфійський майстер алхімії. Якщо тобі потрібні різноманітні зілля, то можеш звертатись до мене."
oliviar.required_item = [orks_bones]
oliviar.quest_info = "Привіт, мандрівнику. Я чую, що ти шукаєш пригод. Якщо ти бажаєш допомогти мені, я можу запропонувати тобі один цікавий квест. Я шукаю кістки орка, щоб виготовити новий лук. Якщо зможеш принести мені кістки орка, я винагороджу тебе Клинком ельфів, мечем, створеним нашими найкращими майстрами. Чи зможеш допомогти мені?"
oliviar.reward = [elves_blade]
oliviar.quest_done_conv = "Ласкаво просимо назад, мій друже! Я бачу, що вам вдалося знайти ті кістки орка. Як обіцяв, тримайте свій Клинок ельфів. Він відомий своєю точністю та міцністю. Нехай він допоможе вам у вашому подальшому шляху!"
arion.required_item = [green_amethyst, forest_potions]
arion.quest_info = 'Вітаю тебе, мандрівнику. Я чув, що ти майстер знахідок. Можливо, ти зможеш мені допомогти. Мені потрібен зелений аметист, який знаходиться в печерах, і лісове зілля, яке можна отримати в лісового духа. Я збираю їх для виготовлення ельфійського зілля для відновлення ран. Якщо ти мені допоможеш, то я винагороджу тебе ельфійським зіллям, яке допоможе тобі відновитись у важких боях.'
arion.reward = [elf_aid]
arion.quest_done_conv = "Ах, що це я бачу? Ви принесли той зелений аметист та лісове зілля. Ви зробили великий внесок в мій пошук правди та мирного злагодження з природою. Я бачу, що ви є справжнім захисником нашого лісу. Я використовую ці інгредієнти для створення ельфійського зілля, яке можна використовувати для швидкого відновлення сил під час бою. Ось, будь ласка, візьміть ампулу цього зілля як мій дарунок тобі. Нехай воно служить тобі доброю послугою в твоїх подорожах."

torin = classes.NPC('Торін', 'Гном-копач')
torin.converstation = "Ласкаво прошу до моєї кузні! Я можу виковати для вас мечі, кинджали, сокири та іншу зброю, яка стане в нагоді у вашій наступній пригоді."
gloin = classes.NPC('Глоїн', 'Гном-копач')
gloin.converstation = "Вітаю тебе, мандрівнику. Шукаєш надійного захисту від ворогів? Я можу зробити тобі найкращу броню, яку ти коли-небудь бачив. Ти просто повернися, коли знайдеш необхідні матеріали."
torin.required_item = [damascus_ore, oak]
torin.quest_info = "Ах, мій дорогий друже! Я побачив, що ти маєш багато сили та вправності у роботі зі зброєю. Але я маю задачу, яка вимагає особливої зброї - меча з дамаску. Якщо ти знайдеш для мене дамаскову руду та дуб, я зроблю тобі такий меч, який зможе пройти через будь-який броню."
gloin.required_item = [horse_skin, steel]
gloin.quest_info = "Слухай, мій дорогий друг. Я знаю, що ти не боїшся труднощів та не втомлюєшся від подорожей. Мені потрібна твоя допомога в одній дуже важливій справі. Якщо принесеш мені конячу шкуру та трохи сталі, то я зможу зробити для тебе пластинчасту броню, яка допоможе тобі у битвах."
torin.reward = [damascus_sw]
torin.quest_done_conv = "Ой, а ти так бистро вернувся. Тоді давай усе необхідне і вже за хвильку отримаєш свій новий меч"
gloin.reward = [lammelar, gnom_beer]
gloin.quest_done_conv = "Вітаю, мій шановний герой! Я бачу, що тобі вдалося зібрати все необхідне для створення пластинчастої броні. Я не помилився в тобі, ти виявився надзвичайно вправним і майстерним. Відтепер ти будеш добре захищений у своїх подорожах і пригодах. А тепер дозволь мені віддячитися за твою допомогу. Я дарую тобі цей маленький знак вдячності - справжнє гном'яче пиво, яке варилось протягом століть. Нехай воно додасть тобі сили та мужності в подальших випробуваннях!"

grum = classes.Enemy('Грум', 'Орк')
grum.converstation = "Ми не вітаємо жодну іншу живу істоту на нашій території. Що тобі потрібно тут?\nКрум: Ти зайшов занадто далеко. Це наша земля, і ми не дозволимо тобі зайти сюди і забрати те, що не є твоїм."
krum = classes.Enemy('Крум', 'Орк')
krum.converstation = "Тут не місце для людей. Ти не маєш права знаходитись тут. Прийдеш на нашу територію - заплатиш за це кров'ю!\nГрум: Ми даємо тобі можливість піти, інакше я з Крумом церемонитись не будемо\nКрум: Ти все почув, тепер вибір лишається за тобою."
grum.set_weakness([damascus_sw, lantern, lammelar])
krum.set_weakness([damascus_sw, lantern, lammelar])
grum.loot = [orks_bones, ork_sword, green_amethyst]
krum.loot = [culebra, power_ring]

reina = classes.NPC('Рейна', 'Німфа')
reina.converstation = "Вітаю тебе, мандрівнику. Я німфа Рейна, і я дбаю про цю прекрасну річку. Але останнім часом я відчуваю погану магію, яка забруднює її воду. Чи зможеш ти мені допомогти очистити Рейну від цього зла?"
reina.required_item = [wind, rock, fire, water]
reina.quest_info = "...я можу допомогти вам. Але щоб віддати вам сувій, мені знадобляться деякі амулети: амулет повітря, амулет землі, амулет вогню і амулет води. Якщо ви принесете мені ці амулети, я зможу віддати вам сувій Гекати. Це допоможе вам створити потужний артефакт, який здатен побороти прокляття."
reina.reward = [scroll_gekaty]
reina.quest_done_conv = "Вітаю з поверненням, герою! Я бачу, що тобі вдалося зібрати 4 амулета. Тепер я можу виконати обіцянку та віддати тобі сувій Гекати. Цей предмет може бути ключем до створення артефакту, який здатен зрушити прокляття з нашої землі. Дякуємо за допомогу та бажаю тобі успіху у твоїх подальших пригодах."

shepit = classes.NPC('Шепіт', 'Лісовий дух')
shepit.converstation = "Ласкаво прошу, мандрівнику! Я Шепіт, лісовий дух цих місць. Я рада бачити тебе в нашому чарівному лісі. Якщо ти хочеш дізнатися більше про наш світ, я завжди готова допомогти тобі знайти відповіді на твої запитання."
galunka = classes.NPC('Галунка', 'Лісовий дух')
galunka.converstation = "Ласкаво просимо в наш ліс, мандрівнику! Я - Галунка, лісовий дух, який любить гратися з природою та експериментувати зі здобутими знаннями. І якщо ви захочете, я з радістю покажу вам, як виготовляти зілля з рослин та фруктів, що зростають у цьому прекрасному лісі. Хай ваша подорож буде повна нових знань та пригод, а я завжди буду тут, готова поділитися своїм знанням з вами!"
shepit.required_item = [writing_set, oil_moonlight]
shepit.quest_info = "Серце лісу радіє, коли людина знаходить свій шлях до нас. Ти шукаєш Ріг Елегії, а я потребую набору для письма та олії місячного сяйва. Набір можна придбати у торговця на ринку, а олію можна знайти біля ставка на північній околиці лісу. І якщо ти допоможеш мені, я з радістю передам тобі Ріг Елегії - символ єднання лісу та людей."
shepit.reward = [elegy_horn]
shepit.quest_done_conv = "Вітаю, мандрінику. Ви виконали мої вимоги та принесли потрібні предмети. Ось ваша обіцяна винагорода - Ріг Елегії, що володіє могутньою силою. Нехай він служить вам на благо у вашій подальшій подорожі."
galunka.required_item = [dragon_fruit, river_flower, ephedra]
galunka.quest_info = "Вітаю, мандрівнику. Я дуже потребую деяких рідкісних інгредієнтів для мого зілля. Можливо, ти зможеш допомогти мені. Я шукаю Драконій фрукт, Водяну лицарівку та Корінь ефедри. Якщо ти зможеш їх знайти, я виготовлю для тебе зілля, яке може допомогти тобі у твоїх подорожах. Ти погоджуєшся на цю угоду?"
galunka.reward = [forest_potions]
galunka.quest_done_conv = "Дякуємо тобі, мандрівнику, за твої послуги. Твоя майстерність допомогла мені створити потужне зілля, яке може допомогти тим, хто стикається зі складними проблемами. Я віддам тобі частину цього зілля, яке може бути корисним у твоїх подальших пригодах"

stefan = classes.Merchant('Стефан', 'Купець')
stefan.converstation = "Вітаю, шановний герою! Я завжди радий бачити тебе в моєму магазині. Чим я можу тобі допомогти сьогодні?"
alisa = classes.Merchant('Аліса', 'Купець')
alisa.converstation = "Вітаю тебе в моєму скромному магазині! Якщо ти шукаєш щось конкретне, дай мені знати, можливо, я зможу допомогти."
stefan.buy_items = [storm_cloack, storm_heart]
stefan.sell_items = [ork_sword, culebra, power_ring, goblin_sw]
#Додати ціни!!!!!!!!!
alisa.buy_items = []
alisa.sell_items = [writing_set, horse_skin]



grubokist = classes.Enemy('Грубокіст', 'Ватажок гоблінів')
grubokist.converstation = "Хто ти і що ти робиш тут, на моїй території? Відповідай швидко, бо я не люблю зайвих слів."
tarkan = classes.Enemy('Таркан', 'Гоблін')
tarkan.converstation = "Моя зброя завжди готова до бою. А як з тобою, чужинець? Встигнеш попрощатись з життям, перш ніж я розправлю свої кулаки."
grubokist.set_weakness([elves_blade, elegy_horn, light_mail])
tarkan.set_weakness([elves_blade, elegy_horn, light_mail])
grubokist.loot = [rock, goblin_head]
tarkan.loot = [goblin_ear]

bilka = classes.NPC('Білка', 'Охоронець поля Хортін')
bilka.converstation = "Привіт, мій дорогий герой! Я Білка, і я рада вітати тебе в моїй домівці. Я дбаю про поле Хортін і всіх його мешканців, і я відчуваю, що ти можеш бути великим помічником для нашої спільної мети. Розкажи мені про себе та про свої пригоди, а я розкажу тобі про наші звичаї та традиції."
bilka.required_item = [acorn]
bilka.quest_info = "Вітаю, мандрівнику. Якщо у тебе є трохи вільного часу, можеш допомогти мені з одним завданням? Я потребую допомоги зі збором жолудів з лісу поблизу, але не можу туди піти, бо потрібно охороняти цю землю. Якщо ти збереш для мене деяку кількість жолудів, я можу віддати тобі цец дивний амулет, який можливо буде тобі потрібним. Так ти можеш допомогти мені і отримати винагороду одночасно."
bilka.reward = [wind]
bilka.quest_done_conv = "Дуже дякую, мандрівнику! Ти дійсно допоміг мені зібрати жолуді. В знак вдячності, я хочу віддати тобі цей амулет. Він може не виглядати як дуже корисний предмет, але якщо зберігати його з собою, то він може дати тобі вдачу у подорожах та захист від злих духів. Будь завжди обережним та дбайливим у своїх пригодах!"

crustalyna = classes.NPC('Кристаліна', 'Магічна істота')
crustalyna.converstation = "Ласкаво прошу, шукачу пригод! Я Кристаліна - магічна істота, яка живе в глибинах печери. Хоча я не можу побачити квіти, я дуже люблю їхні аромати і розмаїття. Можливо колись я знову зможу відчути їх прекрасний аромат."
crustalyna.required_item = [glowing_butterfly, clay, spider_lily]
crustalyna.quest_info = "Можливо ти зможеш допомогти збутись моїй мрії знову відчути аромат квітів? Мені потрібні глина, Синя павуча лілія та світло для життя цієї рослини. Якщо ви зможете мені допомогти, я віддам вам цей амулет, який знайшла під час блукання вздовж підземних вод."
crustalyna.reward = [water]
crustalyna.quest_done_conv = "О, я дійсно не очікувала, що ви зможете зібрати все, що я просила. Ви справді дивовижний герой, і я дуже вдячна вам за допомогу. Ось ваш амулет, він захистить вас від небезпек, що можуть чатувати на вас в майбутньому."

morgan = classes.Enemy('Капітан Морган', 'Головний серед піратів')
morgan.converstation = "Хто ти і що тобі потрібно на моєму острові? Бажаєш приєднатися до мого екіпажу або ти просто намагаєшся викрасти мої скарби? Говори швидко, бо я не маю часу на зайві розмови!"
morgan.set_weakness([storm_cloack, storm_heart, storm_staff])
morgan.loot = [scroll_odina]

savana = classes.NPC('Савана', 'Пустельник')
savana.converstation = "Привіт, незнайомче! Я Савана, пустельниця та авантюристка. Здається, ти теж не боїшся ризикувати. Можливо, ми зможемо домовитися про спільну подорож?"
hakim = classes.NPC('Хакім', 'Пустельник')
hakim.converstation = "Ласкаво просимо в наш конвой. Наш шлях простягається через небезпечні для непідготовлениї мандрівникій території, але ми не зупинимося поки не дістанемося до нашого пункту призначення. Якщо ви з нами, то наші шанси на успіх збільшуються."
savana.required_item = [goblin_head]
savana.quest_info = "Ти хочеш отримати цей амулет? Ну якщо ти якимось дивом принесеш мені голову гобліна, то тоді я тобі його віддам"
savana.reward = [fire]
savana.quest_done_conv = "Ну що ж, ти насправді зробив це! Я не думала, що ти зможеш принести мені голову гобліна. Ось твій амулет, я обіцяла його винагороду, і я завжди дотримую своїх обіцянок. Але слухай, будь обережним, не варто так жертвувати своїм життям заради якоїсь нісенітниці"
hakim.required_item = [elf_aid]
hakim.quest_info = "Доброго дня, герою. Ви не допомогли бідному пустельнику і його підопічним? Багато з моїх товаришів є сильно порененими і їм складно продовжувати подорож. Я шукав цілий день цілющі трави, але так і не зміг знайти їх. Якщо ви зможете принести мені цілющого зілля, я з радістю віддам вам одну з наших кольчуг, вона знадобиться вам у подорожі по пустелі."
hakim.reward = [light_mail]
hakim.quest_done_conv = "Дякую тобі за твою допомогу, мій друг. Ти зберіг життя моїй товаришів і я не забуду про це. І ось, як обіцяв, я даю тобі цю кольчугу. Нехай вона служить тобі у твоїх мандрівках."

arcandor = classes.NPC('Аркандор', 'Маг')
arcandor.converstation = "Ласкаво прошу, мій шановний герой! Я, Аркандор, радий вас привітати. Знати, що у нашому світі є такі майстри пригод, як ви, дарує мені неймовірну радість. Якщо вам буде потрібна якась магічна допомога або порада щодо виготовлення божественних артефактів, будь ласка, звертайтеся до мене."
arcandor.required_item = [scroll_ishrat, scroll_odina, scroll_gekaty]
arcandor.quest_info = "Твоя мета не звичайна, але від тебе залежить багато. Я можу допомогти знищити це прокляття, але для цього потрібні три сувія: Іштар, Одіна і Гекати. Будь обережним у пошуках, бо вони можуть бути дуже небезпечні, але я впевнений, що ти зможеш їх знайти. Успіхів, герою!"
arcandor.reward = [god_artifact]
arcandor.quest_done_conv = "Ти насправді здійснив неможливе і приніс мені три рідкісних сувої. Тепер мій Триумф Божеств зможе врятувати світ від прокляття, яке нависло над нами. Я дуже вдячний тобі за твою мужність та відвагу. Народ Ардентії гідно оцінить твій вчинок! "

#Locations
nirder = classes.Locations('місто Нірдер')
nirder.set_description('Місце, де проживають люди та знаходиться королівський замок, i яке знаходиться в центрі Ардентії.')
nirder.set_character(arcandor)

limbel = classes.Locations('Ліс Лімбел')
limbel.set_description('Місце, де проживають ельфи та де можна знайти джерело магічної енергії.')
limbel.set_character(oliviar)
limbel.set_character(arion)
limbel.set_item(glowing_butterfly)

glorin = classes.Locations('Гора Глорін')
glorin.set_description('Домівка гномів, де знаходиться їхня зброя та механізми.')
glorin.set_character(torin)
glorin.set_character(gloin)
glorin.set_item(ephedra)

sorrow = classes.Locations('Печера Печаль')
sorrow.set_description('Місце, де живуть орки і темні ельфи, що прагнуть підкорити світ.')
sorrow.set_character(grum)
sorrow.set_character(krum)
sorrow.set_item(damascus_ore)

rhine = classes.Locations('Річка Рейн')
rhine.set_description('Річка, що оточена лісом, яка забруднена магією, що може викликати хвороби та інші небезпеки.')
rhine.set_character(reina)
rhine.set_item(river_flower)

deep_forest = classes.Locations('Глибокий ліс')
deep_forest.set_description('Місце, де можна зустріти диких тварин та чарівних створінь.')
deep_forest.set_character(shepit)
deep_forest.set_character(galunka)
deep_forest.set_item(oak)
deep_forest.set_item(gost_mushrooms)
deep_forest.set_item(moon_tree_leaves)
deep_forest.set_item(oil_moonlight)

aridel = classes.Locations('Місто Арідель')
aridel.set_description('Місце, де можна купити різні види зброї, речей і еліксирів.')
aridel.set_character(stefan)
aridel.set_character(alisa)

goblins_ter = classes.Locations('Територія Гоблінів')
goblins_ter.set_description('Місце, де проживають гобліни та знаходиться їхня фортеця.')
goblins_ter.set_character(grubokist)
goblins_ter.set_character(tarkan)

hortin = classes.Locations('Поля Хортін')
hortin.set_description('Місце, де можна знайти різні види тварин і рослин, що можуть допомогти у пригоді.')
hortin.set_character(bilka)
hortin.set_item(spider_lily)

deep_cave = classes.Locations('Глибинні печери')
deep_cave.set_description('Місце, де можна знайти рідкісні магічні кристали та знаряддя.')
deep_cave.set_character(crustalyna)
deep_cave.set_item(lantern)
deep_cave.set_item(steel)

tropical_island = classes.Locations('Тропічний острів')
tropical_island.set_description('місце, де живуть пірати та можна знайти затонулий корабель зі скарбами., де живуть пірати та можна знайти затонулий корабель зі скарбами.')
tropical_island.set_character(morgan)
tropical_island.set_item(dragon_fruit)

desorah = classes.Locations('Пустеля Дезора')
desorah.set_description('Небезпечна пустеля, де можна знайти джерело енергії, але й зустріти ворожі створіння та пастки.')
desorah.set_character(savana)
desorah.set_character(hakim)
desorah.set_item(clay)

nirder.set_linked_loc(deep_forest, 1)
nirder.set_linked_loc(goblins_ter, 2)
nirder.set_linked_loc(aridel, 3)
nirder.set_linked_loc(desorah, 4)
nirder.set_linked_loc(limbel, 5)
nirder.set_linked_loc(hortin, 6)

deep_forest.set_linked_loc(goblins_ter, 1)
deep_forest.set_linked_loc(tropical_island, 2)
deep_forest.set_linked_loc(nirder, 3)
deep_forest.set_linked_loc(glorin, 4)
deep_forest.set_linked_loc(sorrow, 5)

sorrow.set_linked_loc(deep_forest, 1)

goblins_ter.set_linked_loc(deep_cave, 1)
goblins_ter.set_linked_loc(deep_forest, 2)
goblins_ter.set_linked_loc(aridel, 3)
goblins_ter.set_linked_loc(nirder, 4)

aridel.set_linked_loc(goblins_ter, 1)
aridel.set_linked_loc(desorah, 2)
aridel.set_linked_loc(nirder, 3)

desorah.set_linked_loc(aridel, 1)
desorah.set_linked_loc(limbel, 2)
desorah.set_linked_loc(nirder, 3)

limbel.set_linked_loc(desorah, 1)
limbel.set_linked_loc(hortin, 2)
limbel.set_linked_loc(nirder, 3)
limbel.set_linked_loc(rhine, 4)

rhine.set_linked_loc(limbel, 1)

hortin.set_linked_loc(limbel, 1)
hortin.set_linked_loc(nirder, 2)

deep_cave.set_linked_loc(goblins_ter, 1)
deep_cave.set_linked_loc(glorin, 2)

tropical_island.set_linked_loc(deep_forest, 1)
tropical_island.set_linked_loc(glorin, 2)

glorin.set_linked_loc(deep_cave, 1)
glorin.set_linked_loc(deep_forest, 2)
glorin.set_linked_loc(tropical_island, 3)


#For TEST
# nirder.set_item(wind)
# nirder.set_item(fire)
# nirder.set_item(water)
# sorrow.set_item(lantern)
# sorrow.set_item(lammelar)
# sorrow.set_item(damascus_sw)

# tropical_island.set_item(storm_cloack)
# tropical_island.set_item(storm_heart)

# alisa.required_item = [storm_cloack, storm_heart, wind]
# alisa.reward = acorn
# alisa.set_quest('Принесіть такі-то предмети')
# alisa.quest_done_conv = 'Дякую!'

# grum.converstation = 'Hello'
# grum.description = 'Abobus'
# grum.loot = god_artifact

# krum.converstation = 'Hello'
# krum.description = 'Abobus'
# krum.loot = god_artifact
