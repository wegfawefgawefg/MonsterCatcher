import core
import monsters
import items

class Player(core.Character):
    def __init__(self) -> None:
        super().__init__(name="player", x=5, y=5)
        self.monsters = [
            monsters.Minno(),
            monsters.Minno(),
            monsters.Minno()
        ]
        self.inventory.add(items.Potion())
        self.inventory.add(items.Potion())
        self.inventory.add(items.Potion())
        self.inventory.add(items.JAndJ())
        self.inventory.add(items.Teleport())
        for _ in range(10):
            self.inventory.add(items.Viagra())
            self.inventory.add(items.Vitamins())
        self.inventory.add(items.PortalGun())
        self.inventory.add(items.Axe())