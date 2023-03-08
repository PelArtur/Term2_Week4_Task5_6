'''Week4_Task5'''
class Character():
    """
    A class representing a character in a game.

    Attributes:
    --------
    name : str
        The name of the character.
    tipe : str
        The type of the character.
    conversation : str
        The conversation dialogue of the character.
    weakness : str
        The weakness of the character.
    defeated_count : int
        The count of how many times this character has been defeated.

    Methods:
    --------
    __init__(self, name: str, type: str) -> None
        Initializes a character with a name and type.
    set_conversation(self, conversation: str) -> None
        Sets the conversation dialogue of the character.
    set_weakness(self, weakness: str) -> None
        Sets the weakness of the character.
    describe(self) -> None
        Describes the character.
    talk(self) -> None
        Outputs the conversation dialogue of the character.
    fight(self, fight_with: str) -> bool
        Simulates a fight between this character and another character. Returns True if the other
        character's
        type matches this character's weakness, and False otherwise.
    get_defeated(self) -> int
        Returns the count of how many times this character has been defeated.
    """
    defeated_count = 0
    def __init__(self, name, tipe) -> None:
        """
        Initializes a character with a name and type.

        Parameters:
        --------
        name : str
            The name of the character.
        tipe : str
            The type of the character.
        """
        self.name = name
        self.tipe = tipe
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation: str) -> None:
        """
        Sets the conversation dialogue of the character.

        Parameters:
        --------
        conversation : str
            The conversation dialogue of the character.
        """
        if isinstance(conversation, str):
            self.conversation = conversation
        else:
            print('Conversation must be string')

    def set_weakness(self, weakness: str) -> None:
        """
        Sets the weakness of the character.

        Parameters:
        --------
        weakness : str
            The weakness of the character.
        """
        if isinstance(weakness, str) or weakness is None:
            self.weakness = weakness
        else:
            print('Weakness must be a string')

    def describe(self) -> None:
        """
        Describes the character.
        """
        message = self.name + ' is here!\n' + self.tipe
        print(message)

    def talk(self) -> None:
        """
        Outputs the conversation dialogue of the character.
        """
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, fight_with: str) -> bool:
        """
        Simulates a fight between this character and another character. Returns True if the other
        character's
        type matches this character's weakness, and False otherwise.

        Parameters:
        --------
        fight_with : str
            The type of the other character.

        Returns:
        --------
        bool
            True if the other character's type matches this character's weakness, and False
            otherwise.
        """
        if fight_with == self.weakness:
            __class__.defeated_count += 1
            return True
        return False

    def get_defeated(self) -> int:
        """
        Returns the number of times the character has been defeated.

        Returns:
        --------
        int
            The number of times the character has been defeated.
        """
        return self.defeated_count

class Teammate(Character):
    """
    A class representing a teammate character in a game.

    Inherits from Character.

    Methods:
    --------
    __init__(self, name: str, tipe: str) -> None
        Initializes a teammate with a name and type.
    """
    def __init__(self, name, tipe) -> None:
        super().__init__(name, tipe)

class Enemy(Character):
    """
    A class representing an enemy character in a game.
    Inherits from Character.

    Methods:
    --------
    __init__(self, name: str, tipe: str) -> None
        Initializes an enemy with a name and type.
    """
    def __init__(self, name, tipe) -> None:
        super().__init__(name, tipe)

class Item():
    """
    A class representing an item in a game.

    Attributes:
    --------
    name : str
        The name of the item.
    description : str
        The description of the item.

    Methods:
    --------
    __init__(self, name: str) -> None
        Initializes an item with a name.
    set_description(self, description: str) -> None
        Sets the description of the item.
    describe(self) -> None
        Prints the description of the item.
    get_name(self) -> str
        Returns the name of the item.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes an item with a name.

        Parameters:
        --------
        name : str
            The name of the item.
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        Sets the description of the item.

        Parameters:
        --------
        description : str
            The description of the item.
        """
        if isinstance(description, str):
            self.description = description
        else:
            print('Description must be string')

    def describe(self):
        """
        Prints the description of the item.
        """
        message = f'The [{self.name}] is here - {self.description}'
        print(message)

    def get_name(self):
        """
        Returns the name of the item.

        Returns:
        --------
        str
            The name of the item.
        """
        return self.name

class Room():
    """
    Represents a room in a game world.

    Attributes:
    -----------
    name : str
        The name of the room.
    description : str
        The description of the room.
    character : Character or None
        The character present in the room.
    item : Item or None
        The item present in the room.
    linked_rooms : dict
        A dictionary containing the linked rooms, where the keys are the cardinal directions
        (north, south, east, west) and the values are the linked rooms.

    Methods:
    --------
    set_description(description: str) -> None
        Sets the description of the room.
    set_character(character: Character or None) -> None
        Sets the character present in the room.
    set_item(item: Item or None) -> None
        Sets the item present in the room.
    get_details() -> None
        Prints the name, description and linked rooms of the room.
    get_character() -> Character or None
        Returns the character present in the room.
    get_item() -> Item or None
        Returns the item present in the room.
    link_room(room: Room, cardinal: str) -> dict
        Links the room with another room in the specified cardinal direction.
        Returns a dictionary containing the linked rooms or an error message if the cardinal
        direction is invalid.
    move(cardinal: str) -> Room or None
        Returns the linked room in the specified cardinal direction.
        Returns None and prints an error message if there is no linked room in the specified
        direction.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes an room with a name.

        Parameters:
        --------
        name : str
            The name of the room.
        """
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.linked_rooms = {}

    def set_description(self, description):
        """
        Sets the description of the room.

        Parameters:
        --------
        description : str
            The description of the room.

        Returns:
        --------
        None
        """
        if isinstance(description, str):
            self.description = description
        else:
            print('Description must be a string')

    def set_character(self, character: Character) -> None:
        """
        Sets the character in the room.

        Parameters:
        --------
        character : Character(class)
            The character in the room.

        Returns:
        --------
        None
        """
        if isinstance(character, Character) or character is None:
            self.character = character
        else:
            print('The enemy must be of the Enemy class')

    def set_item(self, item: Item) -> None:
        """
        Sets the item in the room.

        Parameters:
        --------
        item : Item(class)
            The item in the room.

        Returns:
        --------
        None
        """
        if isinstance(item, Item) or item is None:
            self.item = item
        else:
            print('The item must be of the Item class')

    def get_details(self) -> None:
        """
        Print an information about the room
        """
        message = self.name + '\n' + '--------------------' + '\n' + self.description
        for cardinal in self.linked_rooms:
            message += f'\nThe {self.linked_rooms[cardinal].name} is {cardinal}'
        print(message)

    def get_character(self) -> Enemy:
        """
        Return character present in the room

        Returns:
        --------
        Enemy
            class object of Enemy
        """
        return self.character

    def get_item(self) -> Item:
        """
        Return item present in the room

        Returns:
        --------
        Item
            class object of Item
        """
        return self.item

    def link_room(self, room, cardinal: str) -> dict:
        """
        Links the room with another room in the specified cardinal direction.
        Returns a dictionary containing the linked rooms or an error message if the cardinal
        direction is invalid.

        Parameters:
        --------
        room : Room(class)
            The linked room
        cardinal: str
            Cardinal direction of linked room

        Returns:
        --------
        dict
            The dictionary with keys of cardinal and appropriate Room
        """
        if cardinal.lower() in ["south", "north", "west", "east"]:
            self.linked_rooms[cardinal.lower()] = room
            return self.linked_rooms
        print('Cardinal must be south, north, west or east')

    def move(self, cardinal: str):
        """
        Returns the linked room in the specified cardinal direction.
        Returns None and prints an error message if there is no linked room in the specified
        direction.

        Parameters:
        --------
        cardinal: str
            Cardinal direction of linked room

        Returns:
        --------
        Room
            The linked room in the specified cardinal direction
        """
        if cardinal.lower() in self.linked_rooms:
            return self.linked_rooms[cardinal.lower()]
        print(f'There is no rooms in the {cardinal}')
