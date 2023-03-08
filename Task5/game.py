class Character():
    defeated_count = 0
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation: str):
        if isinstance(conversation, str):
            self.conversation = conversation
        else:
            print('Conversation must be string')

    def set_weakness(self, weakness: str):
        if isinstance(weakness, str) or weakness is None:
            self.weakness = weakness
        else:
            print('Weakness must be a string')

    def describe(self):
        message = self.name + ' is here!\n' + self.type
        print(message)

    def talk(self):
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, fight_with):
        if fight_with == self.weakness:
            __class__.defeated_count += 1
            return True
        return False

    def get_defeated(self):
        return self.defeated_count

class Teammate(Character):
    def __init__(self, name, type) -> None:
        super().__init__(name, type)

class Enemy(Character):
    def __init__(self, name, type) -> None:
        super().__init__(name, type)

class Item():
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = None

    def set_description(self, description):
        if isinstance(description, str):
            self.description = description
        else:
            print('Description must be string')

    def describe(self):
        message = f'The [{self.name}] is here - {self.description}'
        print(message)

    def get_name(self):
        return self.name

class Room():
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.linked_rooms = {}

    def set_description(self, description):
        if isinstance(description, str):
            self.description = description
        else:
            print('Description must be a string')

    def set_character(self, character: Character) -> None:
        if isinstance(character, Character) or character is None:
            self.character = character
        else:
            print('The enemy must be of the Enemy class')

    def set_item(self, item: Item) -> None:
        if isinstance(item, Item) or item is None:
            self.item = item
        else:
            print('The item must be of the Item class')

    def get_details(self) -> None:
        message = self.name + '\n' + '--------------------' + '\n' + self.description
        for cardinal in self.linked_rooms:
            message += f'\nThe {self.linked_rooms[cardinal].name} is {cardinal}'
        print(message)

    def get_character(self) -> Enemy:
        return self.character

    def get_item(self) -> Item:
        return self.item

    def link_room(self, room, cardinal: str) -> str:
        if cardinal.lower() in ["south", "north", "west", "east"]:
            self.linked_rooms[cardinal.lower()] = room
            return self.linked_rooms
        return 'Cardinal must be south, north, west or east'

    def move(self, cardinal: str) -> str:
        if cardinal.lower() in self.linked_rooms:
            return self.linked_rooms[cardinal.lower()]
        print(f'There is no rooms in the {cardinal}')
        return
