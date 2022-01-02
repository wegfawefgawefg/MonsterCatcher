import core
import pixies
import monsters
import items

class Player(core.Character):
    def __init__(self) -> None:
        self.x = 4
        self.y = 4
        self.motion = "static"
        self.pixie = pixies.Player()
        self.monsters = [
            monsters.Minno(),
            monsters.Minno(),
            monsters.Minno()
        ]

        self.inventory = [
            items.Potion(),
            items.Potion(),
            items.Potion(),
        ]   