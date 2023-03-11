from game_objects import *
from classes import Weapon, Armor, Artifact, NPC, Enemy
current_location = aridel
current_character = None
backpack = []
arden = 0
equipment = {'Artifact': knowledge_eye, 'Weapon': sword, 'Armor': chain_mail}

dead = False

def choose_obj(lst):
    while True:
        if len(lst) == 1:
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

def converstation(npc, backpack, equipment):
    while True:
        print('\n')
        print(new_npc.details())
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
            else:
                battle = npc.fight(equipment)
                if battle:
                    return npc.loot
                return 'Lose'



while dead == False:
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
        converstation_ = converstation(new_npc, backpack, equipment)
        if converstation_ == None:
            continue
        elif converstation_ == 'Lose':
            print('Ви програли :(\nГра закінчена')
            break
        backpack.append(converstation_)
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
