"""In function.py there are all necessary functions for the game"""
from classes import NPC, Merchant, Character

def choose_obj(lst: list):
    """
    Prompts the user to choose an item from a list and returns the selected item.

    Attributes:
    -----------
    lst: list
        The list of items to choose from.

    Returns:
    -----------
    Any:
        The selected item from the list.
    """
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

def trade(npc: Character, backpack: list, money: int) -> tuple:
    """
    Function allows the player to trade with an NPC. The NPC has items for sale and may also buy
    items from the player. The player can buy an item by selecting the desired item from the list of
    available items and paying for it with their money. The player can sell an item by selecting the
    desired item from their backpack and receiving money in exchange. The function returns the item
    that was bought or sold and the type of the transaction.

    Attributes:
    -----------
    npc: Character
        an instance of the NPC class that the player is trading with
    backpack: list
        a list of Items objects that the player currently has in their backpack
    money: int
        an integer representing the amount of money the player has

    Returns:
    -----------
    tuple:
        A tuple containing the item that was bought or sold (an instance of the Item class) and the
        type of transaction ('Buy' or 'Sell'). Returns None if the player cancels the trade.
    """
    while True:
        print(npc.available_items_for_buy())
        for_sell =npc.available_items_for_sell(backpack)
        if for_sell is not None:
            print(for_sell[0])
        print('1.Купити предмет\n2.Продати предмет')
        option = choose_obj(['buy', 'sell'])
        if option is None:
            return None
        elif option == 'buy':
            print('Оберіть предмет, який бажаєте купити')
            to_buy = choose_obj(npc.buy_items)
            if to_buy is None:
                continue
            elif money + to_buy.price < 0:
                print(f'У вас недостатньо арденів, щоб купити {to_buy.name}\n')
                continue
            print(f'Ви успішно купили {to_buy.name} за {to_buy.price*-1} арденів')
            return to_buy, 'Buy'
        else:
            if for_sell is None:
                print('У вас немає доступного предмету для продажу')
                return None
            print('Оберіть предмет, який бажаєте продати')
            to_sell = choose_obj(for_sell[1])
            if to_sell is None:
                return None
            print(f'Ви успішно продали {to_sell.name} за {to_sell.price} арденів')
            return to_sell, 'Sell'

def converstation(npc: Character, backpack: list, equipment: dict, money: int):
    """
    Conducts a conversation between the player and an NPC or merchant or a fight with an enemy.

    Attributes:
    -----------
    npc: Character
        The NPC or enemy the player is conversing with.
    backpack: list
        A list of Items objects representing the player's inventory.
    equipment: dict
        A dictionary of Items objects representing the player's equipped items.
    money: int
        The amount of money the player has.

    Returns:
    -----------
    - If the conversation is with an NPC and the player completes the quest, returns a tuple of an
    Items object representing the quest reward and the string "Quest".
    - If the conversation is with a merchant and the player buys an item, returns a tuple of an
    Items object representing the item bought and the string "Buy".
    - If the conversation is with a merchant and the player sells an item, returns a tuple of an
    Items   object representing the item sold and the string "Sell".
    - If the conversation is with an enemy and the player wins the fight, returns a string "Win"
    and an Item object  representing the loot. Otherwise, returns a string "Lose".
    - If the conversation is cancelled by the player, returns None.
    """
    while True:
        print('\n')
        print(npc.details())
        choose_option = choose_obj([1, 2])
        if choose_option is None:
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
                print('Ви не виконали умову квесту')
            elif isinstance(npc, Merchant):
                trade_in = trade(npc, backpack, money)
                if trade_in is None:
                    return None
                return trade_in[0], trade_in[1]
            else:
                battle = npc.fight(equipment)
                if battle:
                    return npc.loot
                return 'Lose'
