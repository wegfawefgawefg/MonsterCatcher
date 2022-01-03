from enum import Enum, auto

class Item:
    class Target(Enum):
        MONSTER = auto()
        ITEM = auto()
        TILE = auto()
        PLAYER = auto()
        CHARACTER = auto()
        STAT = auto()
        MOVE = auto()
        HOLD = auto()
        NONE = auto()

    def __init__(self, name, description, value) -> None:
        self.name = name
        self.description = description
        self.value = value
        self.useable_in_battle = False

    def __repr__(self) -> str:
        return self.name

    def use(self, game, character, target):
        print(f"{character.name} used {self.name} on {target.name}")
    
    def drop(self, character):
        print(f"{character.name} dropped {self.name}")

    def pick_up(self, character):
        print(f"{character.name} picked up {self.name}")
