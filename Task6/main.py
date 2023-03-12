from game_objects import *
from classes import Weapon, Armor, Artifact, NPC, Merchant
current_location = aridel
current_character = None
backpack = []
arden = 0
equipment = {'Artifact': knowledge_eye, 'Weapon': sword, 'Armor': chain_mail}
flag_ork = True
dead = False

def choose_obj(lst):
    while True:
        if len(lst) == 1:
            if isinstance(lst, dict):
                return lst[1]
            return lst[0]
        print(f'Введіть число від 1 до {len(lst)}')
        num = input('> ')
        try:
            if num == 'back':
                return None
            if 0 < int(num) <= len(lst):
                if isinstance(lst, dict):
                    return lst[int(num)]
                return lst[int(num)-1]
            print('Ви ввели неправильне значення.')
        except ValueError:
            print('Ви ввели неправильне значення.')

def trade(npc, backpack, money):
    while True:
        print(npc.available_items_for_buy())
        for_sell =npc.available_items_for_sell(backpack)
        if for_sell is not None:
            print(for_sell[0])
        print('1.Купити предмет\n2.Продати предмет')
        option = choose_obj(['buy', 'sell'])
        if option == None:
            return None
        elif option == 'buy':
            print('Оберіть предмет, який бажаєте купити')
            to_buy = choose_obj(npc.buy_items)
            if to_buy == None:
                continue
            elif money + to_buy.price < 0:
                print(f'У вас недостатньо арденів, щоб купити {to_buy.name}\n')
                continue
            return to_buy, 'Buy'
        else:
            if for_sell == None:
                print('У вас немає доступного предмету для продажу')
                return None
            print('Оберіть предмет, який бажаєте продати')
            to_sell = choose_obj(for_sell[1])
            if to_sell == None:
                return None
            return to_sell, 'Sell'

def converstation(npc, backpack, equipment, money):
    while True:
        print('\n')
        print(npc.details())
        choose_option = choose_obj([1, 2])
        if choose_option == None:
            return None
        elif choose_option == 1:
            npc.talk()
        else:
            if isinstance(npc, NPC):
                print(npc.quest_info)
                check_list = npc.quest(backpack)
                if check_list:
                    print(npc.quest_done_conv)
                    return npc.reward
                else:
                    print('Ви не виконали умову квесту')
            elif isinstance(npc, Merchant):
                trade_in = trade(npc, backpack, money)
                if trade_in == None:
                    return None
                return trade_in[0], trade_in[1]
            else:
                battle = npc.fight(equipment)
                if battle:
                    return npc.loot
                return 'Lose'

while dead == False:
    if flag_ork and sorrow.characters == []:
        sorrow.items = [scroll_ishrat]
        flag_ork = False
    print('\n')
    print(current_location.get_details()[0])
    text = input('> ').lower()
    if text == 'break':
        break
    if text.lower() == 'location' or text.lower() == 'loc':
        new_loc = choose_obj(current_location.linked_loc)
        if new_loc == None:
            continue
        current_location = new_loc

    elif text == 'character' or text == 'npc':
        if len(current_location.characters) == 0:
            print('На цій локації немає доступних персонажів')
            continue
        new_npc = choose_obj(current_location.characters)
        if new_npc == None:
            continue
        converstation_ = converstation(new_npc, backpack, equipment, arden)
        if converstation_ == None:
            continue
        elif converstation_ == 'Lose':
            print('Ви програли :(\nГра закінчена')
            break
        elif len(converstation_) == 2:
            if converstation_[0] == None:
                continue
            if converstation_[1] == 'Buy':
                backpack.append(converstation_[0])
                new_npc.buy_items.remove(converstation_[0])
            else:
                print(converstation_[0].price)
                backpack.remove(converstation_[0])
                new_npc.sell_items.remove(converstation_[0])
            if new_npc.buy_items == [] and new_npc.sell_items == []:
                current_location.characters.remove(new_npc)
            arden += converstation_[0].price
        else:
            backpack += converstation_
            if isinstance(new_npc, NPC):
                for elem in new_npc.required_item:
                    backpack.remove(elem)
            current_location.characters.remove(new_npc)

    elif text == 'item':
        if len(current_location.items) == 0:
            print('На цій локації немає доступних предметів')
            continue
        elif len(current_location.items) == 1:
            new_item = current_location.items[0]
            backpack.append(new_item)
            current_location.items.remove(new_item)
            print(f'Предмет {new_item.name} успішно додано в інвентар')
            continue
        new_item = choose_obj(current_location.items)
        if new_item == None:
            continue
        backpack.append(new_item)
        current_location.items.remove(new_item)
        print(f'Предмет {new_item.name} успішно додано в інвентар')

    elif text == 'item all':
        if len(current_location.items) == 0:
            print('На цій локації немає доступних предметів')
            continue
        backpack += current_location.items
        current_location.items = []

    elif text == 'backpack':
        if len(backpack) == 0:
            print('Ваш інвентар пустий :(')
            continue
        print('Предмети в інвентарі:')
        for elem in backpack:
            print(elem.name)

    elif text == 'tool':
        print('Ваше екіпірування:')
        for elem in equipment:
            print(f'{elem}: {equipment[elem].name}')
        print('Хочете змінити екіпірування?')
        yes_no = input('> ')
        if yes_no.lower() == 'yes':
            changing_equip = True
            count = 1
            available_equipment = []
            available_equipment_message = '\nДоступні предмети:'
            for elem in backpack:
                if isinstance(elem, Weapon) or isinstance(elem, Armor) or isinstance(elem, Artifact):
                    available_equipment_message += f'\n{count}. {type(elem)}: {elem.name}'
                    available_equipment.append(elem)
                    count += 1
            if len(available_equipment) == 0:
                print('У вас немає підходячого екіпіруваня')
                continue
            while changing_equip:
                print(available_equipment_message)
                new_equip = choose_obj(available_equipment)
                if new_equip == None:
                    break
                for equip_ in equipment:
                    if type(equipment[equip_]) == type(new_equip):
                        backpack.append(equipment[equip_])
                        backpack.remove(new_equip)
                        equipment[equip_] = new_equip
                        changing_equip = False

    elif text == 'balance':
        print(f'Ваш поточний грошовий баланс складає {arden} арденів')
