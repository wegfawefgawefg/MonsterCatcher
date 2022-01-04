import core
import monsters
import items

class Player(core.Character):
    def __init__(self) -> None:
        super().__init__(name="player", x=4, y=4)
        self.monsters = [
            monsters.Minno(),
            monsters.Minno(),
            monsters.Minno()
        ]
        potions = [items.Potion()]*3
        self.inventory.add(potions)
