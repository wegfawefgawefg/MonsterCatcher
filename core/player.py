import core
import pixies
import monsters
import items

class Player(core.Character):
    def __init__(self) -> None:
        pixie = pixies.Player()
        super().__init__(x=4, y=4, motion="static", pixie=pixie)
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