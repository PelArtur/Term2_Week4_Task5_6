import classes

#Items
sword = classes.Weapon('Меч героя', 50)
chain_mail = classes.Armor('Броня героя', 25)
knowledge_eye = classes.Artifact('Кристалічне ока знань', 'Epic')
knowledge_eye.set_description('Артефакт "Кристалічне око знань" - магічний кристал, що дозволяє своєму володарю отримувати всю інформацію про своїх ворогів. Кристал може використовувати різні методи збору інформації, такі як сканування мислення, зчитування душі, виявлення слабкостей та багато іншого. Крім того, "Кристалічне Око Знання" може також надавати своєму володарю додаткові знання та магічні здібності, які допоможуть йому перемогти своїх ворогів.')

acorn = classes.Items('Жолудь')
acorn.set_description('Жолуді з лісу Лімбел. Улюблене частування білок')


#Effective tools vs orks
damascus_sw = classes.Weapon('Меч з дамаску', 75)
lantern = classes.Artifact('Ліхтар', 'Default')
lammelar = classes.Armor('Пластинчаста броня', 50)
#Effective tools vs pirats
storm_heart = classes.Weapon('Серце шторму', 75)
storm_heart.set_description('Це магічний меч з іскристим клинком, який може генерувати потужні бурі та грози. Кожен удар мечем випромінює магічний вибух.')
storm_staff = classes.Artifact('Посох бурі', 'Legendary')
storm_staff.set_description('Це магічний посох, який може викликати потужні бурі та грози, що можуть знищити будь-яку армію. Його можна використовувати як зброю, але його справжня сила полягає у магічних заклинаннях, які можна виконувати з його допомогою.')
storm_cloack = classes.Armor('Плащ бурі', 50)
storm_cloack.set_description('Це магічний плащ, що дозволяє носителю рухатись зі швидкістю бурі. Виготовлений з тканини, яка зміцнена магією')
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

torin = classes.NPC('Торін', 'Гном-копач')
gloin = classes.NPC('Глоїн', 'Гном-копач')

grum = classes.Enemy('Грум', 'Орк')
krum = classes.Enemy('Крум', 'Орк')
grum.set_weakness([damascus_sw, lantern, lammelar])
krum.set_weakness([damascus_sw, lantern, lammelar])

reina = classes.NPC('Рейна', 'Німфа')

shepit = classes.NPC('Шепіт', 'Лісовий дух')
galunka = classes.NPC('Галунка', 'Лісовий дух')

stefan = classes.NPC('Стефан', 'Купець')
alisa = classes.NPC('Аліса', 'Купець')

grubokist = classes.Enemy('Грубокіст', 'Ватажок гоблінів')
tarkan = classes.Enemy('Таркан', 'Гоблін')

bilka = classes.NPC('Білка', 'Охоронець поля Хортін')

crustalyna = classes.NPC('Кристаліна', 'Магічна істота')

morgan = classes.Enemy('Капітан Морган', 'Головний серед піратів')
morgan.set_weakness([storm_cloack, storm_heart, storm_staff])

savana = classes.NPC('Савана', 'Пустельник')
hakim = classes.NPC('Хакім', 'Пустельник')

#Locations
nirder = classes.Locations('місто Нірдер')
nirder.set_description('Місце, де проживають люди та знаходиться королівський замок, i яке знаходиться в центрі Ардентії.')

limbel = classes.Locations('Ліс Лімбел')
limbel.set_description('Місце, де проживають ельфи та де можна знайти джерело магічної енергії.')
limbel.set_character(oliviar)
limbel.set_character(arion)

glorin = classes.Locations('Гора Глорін')
glorin.set_description('Домівка гномів, де знаходиться їхня зброя та механізми.')
glorin.set_character(torin)
glorin.set_character(gloin)

sorrow = classes.Locations('Печера Печаль')
sorrow.set_description('Місце, де живуть орки і темні ельфи, що прагнуть підкорити світ.')
sorrow.set_character(grum)
sorrow.set_character(krum)

rhine = classes.Locations('Річка Рейн')
rhine.set_description('Річка, що оточена лісом, яка забруднена магією, що може викликати хвороби та інші небезпеки.')
rhine.set_character(reina)

deep_forest = classes.Locations('Глибокий ліс')
deep_forest.set_description('Місце, де можна зустріти диких тварин та чарівних створінь.')
deep_forest.set_character(shepit)
deep_forest.set_character(galunka)

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

deep_cave = classes.Locations('Глибинні печери')
deep_cave.set_description('Місце, де можна знайти рідкісні магічні кристали та знаряддя.')
deep_cave.set_character(crustalyna)

tropical_island = classes.Locations('Тропічний острів')
tropical_island.set_description('місце, де живуть пірати та можна знайти затонулий корабель зі скарбами., де живуть пірати та можна знайти затонулий корабель зі скарбами.')
tropical_island.set_character(morgan)

desorah = classes.Locations('Пустеля Дезора')
desorah.set_description('Небезпечна пустеля, де можна знайти джерело енергії, але й зустріти ворожі створіння та пастки.')
desorah.set_character(savana)
desorah.set_character(hakim)

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
nirder.set_item(wind)
nirder.set_item(fire)
nirder.set_item(water)
sorrow.set_item(lantern)
sorrow.set_item(lammelar)
sorrow.set_item(damascus_sw)

tropical_island.set_item(storm_cloack)
tropical_island.set_item(storm_heart)

alisa.required_item = [storm_cloack, storm_heart, wind]
alisa.reward = acorn
alisa.set_quest('Принесіть такі-то предмети')
alisa.quest_done_conv = 'Дякую!'

grum.converstation = 'Hello'
grum.description = 'Abobus'
grum.loot = god_artifact