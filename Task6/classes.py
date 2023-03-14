"""In classes.py there are all necessary classes for the game"""
import random

class Character:
    """
    A class representing a character in the game.

    Attributes:
    -----------
    name : str
        The name of the character.
    description : str
        A brief description of the character.
    conversation : str
        The conversation of the character.

    Doctests:
    -----------
    >>> torin = Character('Торін', 'Гном-копач')
    >>> torin.converstation = 'Привіт, друже!'
    >>> torin.name
    'Торін'
    >>> torin.description
    'Гном-копач'
    >>> torin.converstation
    'Привіт, друже!'
    >>> torin.talk()
    Торін: Привіт, друже!
    """
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.converstation = None

    def talk(self) -> None:
        """
        Prints the conversation of the character.
        """
        print(f'{self.name}: {self.converstation}')

class Enemy(Character):
    """
    A class representing an enemy in the game.

    Attributes:
    -----------
    weakness: list
        A list of weaknesses of the enemy.
    loot: Item
        The item that can be looted from the enemy.

    Methods:
    -----------
    set_weakness(self, weakness: list):
        Adds the given list of weaknesses to the enemy's existing weaknesses.
    fight(self, equipment: list) -> bool:
        Simulates a battle between the player and the enemy.
        Returns True if the player wins, False otherwise.
    details(self) -> str:
        Returns a string containing the enemy's name, description, and available interactions.

    Doctests:
    -----------
    >>> grum = Enemy('Грум', 'Орк')
    >>> grum.set_weakness(['Ельф', 'Люди', 'Маги'])
    >>> grum.loot = 'Ork sword'
    >>> grum.weakness
    ['Ельф', 'Люди', 'Маги']
    >>> grum.loot
    'Ork sword'
    >>> grum.fight({1: 'Ельф', 2: 'Люди', 3: 'Маги'})
    True
    """
    def __init__(self, name: str, description: str) -> None:
        """
        Initializes an Enemy object.

        Parameters:
        -----------
        name: str
            The name of the enemy.
        description: str
            The description of the enemy.
        """
        self.weakness = []
        self.loot = None
        super().__init__(name, description)

    def set_weakness(self, weakness: list):
        """
        Adds the given list of weaknesses to the enemy's existing weaknesses.

        Parameters:
        -----------
        weakness: list
            A list of weaknesses of the enemy.
        """
        self.weakness += weakness

    def fight(self, equipment: list):
        """
        Simulates a battle between the player and the enemy.

        Parameters:
        -----------
        equipment: list
            The equipment used by the player to fight the enemy.

        Returns:
        -----------
        bool:
            True if the player wins the battle, False otherwise.
        """
        battle_point = 0
        flag = random.randint(1, 4)
        for elem in equipment:
            if equipment[elem] in self.weakness:
                battle_point += 1
        if (battle_point == 1 and flag == 1) or (battle_point == 2 and flag < 3) or (
            battle_point == 3):
            return True
        return False

    def details(self):
        """
        Returns a string containing the enemy's name, description, and available interactions.

        Returns:
        -----------
        str:
            The string containing the enemy's name, description, and available interactions.
        """
        message = self.name + '\n' + '--------------------' + '\n' + self.description + '\nДоступні\
 взаємодії:\n1. Поговорити\n2. Вступити в бійку'
        return message

class NPC(Character):
    """
    A class representing a non-playable character (NPC) in the game.

    Attributes:
    -----------
    quest_info: str
        Information about the quest given by the NPC.
    required_item: list
        A list of items required to complete the quest.
    quest_done_conv: str
        Conversation dialogue when the quest is completed.
    reward: Item
        The reward for completing the quest.

    Methods:
    -----------
    quest(self, backpack: list) -> bool:
        Checks if the player has all the required items to complete the quest.
        Returns True if the player has all the required items, False otherwise.
    details(self) -> str:
        Returns a string containing the NPC's name, description, and available interactions.

    Doctests:
    -----------
    >>> reina = NPC('Рейна', 'Німфа')
    >>> reina.required_item = ['wind', 'rock', 'fire', 'water']
    >>> reina.reward = ['scroll_gekaty']
    >>> reina.required_item
    ['wind', 'rock', 'fire', 'water']
    >>> reina.reward
    ['scroll_gekaty']
    >>> reina.quest(['wind', 'rock', 'fire', 'water'])
    True
    >>> reina.quest(['wind', 'rock', 'water'])
    False
    """
    def __init__(self, name: str, description: str) -> None:
        """
        Constructor method for NPC class.

        Parameters:
        -----------
        name: str
            The name of the NPC.
        description: str
            A description of the NPC.

        Attributes:
        -----------
        quest_info: None or str
            Information about the NPC's quest.
        required_item: list
            A list of items required for the quest.
        quest_done_conv: None or str
            Conversation to be triggered after completing the quest.
        reward: None or str
            Reward for completing the quest.
        assortment: None or str
            List of items available to trade or sell.
        super().__init__(name, description)
            Call to the superclass constructor.
        """
        self.quest_info = None
        self.required_item = []
        self.quest_done_conv = None
        self.reward = None
        super().__init__(name, description)

    def quest(self, backpack: list) -> bool:
        """
        Check if the player has all the required items for the NPC's quest.

        Parameters:
        -----------
        backpack: list
            A list of items in the player's backpack.

        Returns:
        -----------
        bool:
            True if the player has all the required items, False otherwise.
        """
        flag = 0
        for item in backpack:
            if item in self.required_item:
                flag += 1
        if flag == len(self.required_item):
            return True
        return False

    def details(self) -> str:
        """
        Returns a string containing the NPC's name, description, and available interactions.

        Returns:
        --------
        str:
            The string containing the NPC's name, description, and available interactions.
        """
        message = self.name + '\n' + '--------------------' + '\n' + self.description + '\nДоступні\
 взаємодії:\n1. Поговорити\n2. Квест'
        return message

class Merchant(Character):
    """
    A class representing a merchant character.

    Attributes:
    -----------
    buy_items : list
        A list of items that the merchant sells.
    sell_items : list
        A list of items that the merchant buys.

    Methods:
    -----------
    available_items_for_buy() -> str:
        Returns a string representation of the items available for purchase.
    available_items_for_sell(backpack: list) -> Union[str, Tuple[str, List[Item]]]:
        Returns a string representation of the items available for sale and a list of items
        that the merchant can buy.
    details() -> str:
        Returns a string representation of the merchant's details.

    Doctests:
    -----------
    >>> stefan = Merchant('Стефан', 'Купець')
    >>> stefan.buy_items = ['storm_cloack', 'storm_heart']
    >>> stefan.sell_items = ['ork_sword', 'culebra', 'power_ring', 'goblin_sw', 'goblin_ear']
    >>> stefan.buy_items
    ['storm_cloack', 'storm_heart']
    >>> stefan.sell_items
    ['ork_sword', 'culebra', 'power_ring', 'goblin_sw', 'goblin_ear']
    """
    def __init__(self, name: str, description: str) -> None:
        """
        Constructs a new Merchant object with the given name and description.

        Parameters:
        -----------
        name : str
            The name of the merchant.
        description : str
            A short description of the merchant.
        """
        self.buy_items = []
        self.sell_items = []
        super().__init__(name, description)

    def available_items_for_buy(self) -> str:
        """
        Returns a string representation of the items available for purchase.

        Returns:
        -----------
        str:
            A string representing the available items for purchase.
        """
        if len(self.buy_items) == 0:
            return None
        message = 'Доступні предмети для купівлі:'
        num = 1
        for item in self.buy_items:
            message += f'\n{num}. {item.name}: {item.price * -1} арденів'
            num += 1
        return message + '\n'

    def available_items_for_sell(self, backpack: list) -> str:
        """
        Returns a string representation of the items available for sale and a list of items that
        the merchant can buy.

        Parameters:
        -----------
        backpack : list
            A list of items in the player's backpack.

        Returns:
        -----------
        Union[str, Tuple[str, List[Item]]]:
            A string representing the available items for sale and a list of items that the merchant
            can buy, or None if there are no items available for sale.
        """

        message = 'Доступні предмети для продажу:'
        num = 1
        available_to_sell = []
        for item in backpack:
            if item in self.sell_items:
                message += f'\n{num}. {item.name}: {item.price} арденів'
                available_to_sell.append(item)
                num += 1
        if num == 1 or len(self.sell_items) == 0:
            return None
        return message + '\n', available_to_sell

    def details(self) -> str:
        """
        Returns a string representation of the merchant's details.

        Returns:
        -----------
        str:
            A string representing the merchant's details.
        """
        message = self.name + '\n' + '--------------------' + '\n' + self.description + '\nДоступні\
 взаємодії:\n1. Поговорити\n2. Поторгуватись'
        return message

class Items():
    """
    A class that represents a game item.

    Attributes:
    -----------
    name: str
        The name of the item.
    description: str
        The description of the item.
    is_sellable: bool
        A boolean value indicating whether the item is sellable.
    price: int or None
        The price of the item.

    Doctests:
    -----------
    >>> bearskin = Items('Шкіра ведмедя', True)
    >>> bearskin.price = 400
    >>> bearskin.name
    'Шкіра ведмедя'
    >>> bearskin.is_sellable
    True
    >>> bearskin.price
    400
    """
    def __init__(self, name, is_sellable=False) -> None:
        """
        Initializes an item object.

        Parameters:
        -----------
        name: str
            The name of the item.
        is_sellable: bool, optional
            A boolean value indicating whether the item is sellable. Defaults to False.
        """
        self.name = name
        self.description = None
        self.is_sellable = is_sellable
        self.price = None

class Artifact(Items):
    """
    A class that represents an artifact, a type of item in the game.
    Inherits from the Items class.
    """

class Weapon(Items):
    """
    A class that represents a weapon, a type of item in the game.
    Inherits from the Items class.
    """

class Armor(Items):
    """
    A class that represents an armor, a type of item in the game.
    Inherits from the Items class.
    """

class Scroll(Items):
    """
    A class that represents a scroll, a type of item in the game.
    Inherits from the Items class.
    """

class Locations:
    """
    A class that represents a location in the game.

    Attributes:
    -----------
    name: str
        The name of the location.
    description: str
        The description of the location.
    characters: list
        A list of Character objects that are currently in the location.
    items: list
        A list of Item objects that are currently in the location.
    linked_loc: dict
        A dictionary that maps the cardinal directions to other Location objects.

    Methods:
    -----------
    set_description(description: str) -> None:
        Sets the description of the location.
    set_character(character: Character) -> None:
        Adds a character to the location.
    set_item(item: Items):
        Adds an item to the location.
    set_linked_loc(linked_loc, cardinal):
        Sets the location that is in the given cardinal direction.
    get_details():
        Returns a message with details about the location and a dictionary of the location's
        attributes.

    Doctests:
    -----------
    >>> nirder = Locations('місто Нірдер')
    >>> nirder.set_character('arcandor')
    >>> nirder.set_item('raspberry')
    >>> nirder.items
    ['raspberry']
    >>> nirder.characters
    ['arcandor']
    >>> nirder.set_character('arcandor2')
    >>> nirder.characters
    ['arcandor', 'arcandor2']
    """
    def __init__(self, name: str) -> None:
        """
        Sets the description of the location.

        Parameters:
        -----------
        description: str
            The description of the location.
        """
        self.name = name
        self.description = None
        self.characters = []
        self.items = []
        self.linked_loc = {}

    def set_description(self, description: str) -> None:
        """
        Sets the description of the location.

        Parameters:
        -----------
        description: str
            The description of the location.
        """
        self.description = description

    def set_character(self, character: Character) -> None:
        """
        Adds a character to the location.

        Parameters:
        -----------
        character: Character
            The character to add to the location.
        """
        self.characters.append(character)

    def set_item(self, item: Items) -> None:
        """
        Adds an item to the location.

        Parameters:
        -----------
        item: Items
            The item to add to the location.
        """
        self.items.append(item)

    def set_linked_loc(self, linked_loc, cardinal: int) -> None:
        """
        Sets the location that is in the given cardinal direction.

        Parameters:
        -----------
        linked_loc: Location
            The location that is in the given cardinal direction.
        cardinal: str
            The cardinal direction to set the location for.
        """
        self.linked_loc[cardinal] = linked_loc

    def get_details(self) -> tuple:
        """
        Returns a message with details about the location and a dictionary of the location's
        attributes.

        Returns:
        -----------
        tuple:
            A tuple containing a message with details about the location and a dictionary of
            the location's attributes.
        """
        message = self.name + '\n' + '--------------------' + '\n' + self.description + '\nДоступні\
 локації:'
        for location in self.linked_loc:
            message += f'\n{location}. {self.linked_loc[location].name}'
        if len(self.characters) != 0:
            message += '\nДоступні персонажі:'
            for i, character in enumerate(self.characters):
                message += f'\n{i+1}. {character.name}'
        if len(self.items) != 0:
            message += '\nДоступні предмети:'
            for i, item in enumerate(self.items):
                message += f'\n{i+1}. {item.name}'
        return message, {'Location': self.linked_loc, 'Characters': self.characters, 'Items':
                         self.items}

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
