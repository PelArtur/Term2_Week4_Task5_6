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
arion = classes.NPC('Аріон', 'Ельф')
oliviar.required_item = [orks_bones]
oliviar.reward = [elves_blade]
arion.required_item = [green_amethyst, forest_potions]
arion.reward = [elf_aid]

torin = classes.NPC('Торін', 'Гном-копач')
gloin = classes.NPC('Глоїн', 'Гном-копач')
torin.required_item = [damascus_ore, oak]
gloin.required_item = [horse_skin, steel]
torin.reward = [damascus_sw]
gloin.reward = [lammelar]

grum = classes.Enemy('Грум', 'Орк')
krum = classes.Enemy('Крум', 'Орк')
grum.set_weakness([damascus_sw, lantern, lammelar])
krum.set_weakness([damascus_sw, lantern, lammelar])
grum.loot = [orks_bones, ork_sword, green_amethyst]
krum.loot = [culebra, power_ring]

reina = classes.NPC('Рейна', 'Німфа')
reina.required_item = [wind, rock, fire, water]
reina.reward = [scroll_gekaty]

shepit = classes.NPC('Шепіт', 'Лісовий дух')
galunka = classes.NPC('Галунка', 'Лісовий дух')
shepit.required_item = [writing_set, oil_moonlight]
shepit.reward = [elegy_horn]
galunka.required_item = [dragon_fruit, river_flower, ephedra]
galunka.reward = [forest_potions]

stefan = classes.Merchant('Стефан', 'Купець')
alisa = classes.Merchant('Аліса', 'Купець')
#Для продажу: storm_cloack, storm_heart, horse_skin
stefan.buy_items = [storm_cloack, storm_heart]
stefan.sell_items = [ork_sword, culebra, power_ring, goblin_sw]
#Додати ціни!!!!!!!!!
alisa.buy_items = [horse_skin]
alisa.sell_items = [writing_set, oil_moonlight]



grubokist = classes.Enemy('Грубокіст', 'Ватажок гоблінів')
tarkan = classes.Enemy('Таркан', 'Гоблін')
grubokist.set_weakness([elves_blade, elegy_horn, light_mail])
tarkan.set_weakness([elves_blade, elegy_horn, light_mail])
grubokist.loot = [rock, goblin_head]
tarkan.loot = [goblin_ear]

bilka = classes.NPC('Білка', 'Охоронець поля Хортін')
bilka.required_item = [acorn]
bilka.reward = [wind]

crustalyna = classes.NPC('Кристаліна', 'Магічна істота')
crustalyna.required_item = [glowing_butterfly, clay, spider_lily]
crustalyna.reward = [water]

morgan = classes.Enemy('Капітан Морган', 'Головний серед піратів')
morgan.set_weakness([storm_cloack, storm_heart, storm_staff])
morgan.loot = [scroll_odina]

savana = classes.NPC('Савана', 'Пустельник')
hakim = classes.NPC('Хакім', 'Пустельник')
savana.required_item = [goblin_head]
savana.reward = [fire]
hakim.required_item = [elf_aid]
hakim.reward = [light_mail]

arcandor = classes.NPC('Аркандор', 'Маг')
arcandor.required_item = [scroll_ishrat, scroll_odina, scroll_gekaty]
arcandor.reward = [god_artifact]

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
