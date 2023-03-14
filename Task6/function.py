from classes import NPC, Merchant

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