class Character:
    def __init__(self, name, tipe, hitpoints) -> None:
        self.name = name
        self.type = tipe
        self.hitpoints = hitpoints
        self.converstation = None

    def set_converstation(self, converstation):
        self.converstation = converstation

    def details(self):
        message = f'A ось i {self.name}\n{self.type}'
        print(message)

    def talk(self):
        print(f'{self.name}: {self.converstation}')

class Enemy(Character):
    def __init__(self, name, tipe, hitpoints) -> None:
        self.weakness = None
        super().__init__(name, tipe, hitpoints)

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self):
        pass

class NPC(Character):
    def __init__(self, name, tipe, hitpoints) -> None:
        self.quest = None
        super().__init__(name, tipe, hitpoints)

class Items():
    def __init__(self, name) -> None:
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        pass

    def get_name(self):
        return self.name

class Artifact(Items):
    def __init__(self, name) -> None:
        self_isbroken = False
        super().__init__(name)

class Locations:
    def __init__(self, name) -> None:
        self.name = name