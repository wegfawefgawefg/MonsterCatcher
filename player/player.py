import core
import pixies
import monsters
import items

class Player(core.Character):
    def __init__(self) -> None:
        super().__init__(x=4, y=4, motion=core.Motion(), pixie=pixies.Player())
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