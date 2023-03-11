import random

class Character:
    def __init__(self, name, tipe) -> None:
        self.name = name
        self.type = tipe
        self.description = 'test'
        self.converstation = None

    def set_converstation(self, converstation):
        self.converstation = converstation

    def talk(self):
        print(f'{self.name}: {self.converstation}')

class Enemy(Character):
    def __init__(self, name, tipe) -> None:
        self.weakness = []
        self.loot = None
        super().__init__(name, tipe)

    def set_weakness(self, weakness: list):
        self.weakness += weakness

    def fight(self, equipment):
        battle_point = 0
        flag = random.randint(1, 4)
        for elem in equipment:
            if equipment[elem] in self.weakness:
                battle_point += 1
        print(flag, battle_point)
        if (battle_point == 1 and flag == 1) or (battle_point == 2 and flag < 3) or battle_point == 3:
            return True
        return False

    def details(self):
        message = self.name + '\n' + '--------------------' + '\n' + self.description + '\nДоступні взаємодії:\n1. Поговорити\n2. Вступити в бійку'
        return message

class NPC(Character):
    def __init__(self, name, tipe) -> None:
        self.quest_info = None
        self.required_item = []
        self.quest_done_conv = None
        self.reward = None
        super().__init__(name, tipe)
    
    def set_quest(self, quest):
        self.quest_info = quest

    def set_reward(self, reward):
        self.reward = reward

    def quest(self, backpack):
        flag = 0
        for item in backpack:
            if item in self.required_item:
                flag += 1
        if flag == len(self.required_item):
            return True
        return False

    def details(self):
        message = self.name + '\n' + '--------------------' + '\n' + self.description + '\nДоступні взаємодії:\n1. Поговорити\n2. Квест/поторгуватись'
        return message

class Items():
    def __init__(self, name) -> None:
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f'{self.name}\n{self.description}')

    def get_name(self):
        return self.name

class Artifact(Items):
    def __init__(self, name, rarity) -> None:
        self.rarity = rarity
        self_isbroken = False
        self_bonus = None
        super().__init__(name)

class Weapon(Items):
    def __init__(self, name, damage) -> None:
        self.damage = damage
        super().__init__(name)
    
    def set_damage(self, damage: int):
        self.damage = damage

class Armor(Items):
    def __init__(self, name, protection) -> None:
        self.protection = protection
        super().__init__(name)
    
    def set_protection(self, protection):
        self.protection = protection

class Scroll(Items):
    def __init__(self, name) -> None:
        super().__init__(name)

class Locations:
    def __init__(self, name) -> None:
        self.name = name
        self.description = None
        self.characters = []
        self.items = []
        self.linked_loc = {}

    def set_description(self, description):
        self.description = description
    
    def set_character(self, character):
        self.characters.append(character)
    
    def set_item(self, item):
        self.items.append(item)

    def set_linked_loc(self, linked_loc, cardinal):
        self.linked_loc[cardinal] = linked_loc

    def get_details(self):
        message = self.name + '\n' + '--------------------' + '\n' + self.description + '\nДоступні локації:'
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
        return message, {'Location': self.linked_loc, 'Characters': self.characters, 'Items': self.items}

        
    
    def move(self, number):
        if number in self.linked_loc:
            return self.linked_loc[number]
