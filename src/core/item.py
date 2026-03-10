
import core
#from enum import Enum, auto
#class Target(Enum):
#    MONSTER = auto()
#    ITEM = auto()
#    TILE = auto()
#    PLAYER = auto()
#    CHARACTER = auto()
#    STAT = auto()
#    MOVE = auto()
#    HOLD = auto()
#    NONE = auto()

class Item:
    def __init__(self, name, description, value, consumable=True, quantity=1) -> None:
        self.name = name
        self.description = description
        self.value = value
        self.useable_in_battle = False
        self.quantity = quantity
        self.consumable = consumable

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)

    def __repr__(self) -> str:
        return self.name

    def can_use_on(self, game, user, target):
        return False

    def announce_use(self, user, target):
        print(f"{user.name} used {self.name} on {target.name}")

    def use(self, game, user, target):
        if self.consumable:
            user.inventory.remove(self)
        print(f"{user.name} used {self.name} on {target.name}")
    
    def drop(self, character):
        print(f"{character.name} dropped {self.name}")

    def pick_up(self, character):
        print(f"{character.name} picked up {self.name}")
