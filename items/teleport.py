import random

import core

class Teleport(core.Item):
    def __init__(self) -> None:
        super().__init__(name="teleport", description="warps you to available spot randomly if you can", value=1_000_000, consumable=True)

    def use(self, game, user, target):
        if self.can_use_on(game, user, target):
            xmod, ymod = -100, -100
            while not game.player.move(game, xmod, ymod):
                xmod, ymod = random.randint(0, game.map.width), random.randint(0, game.map.height)
            user.inventory.remove(self)
            self.announce_use(user, target)

    def can_use_on(self, game, user, target):
        return user == game.player and target == game.player

    def announce_use(self, user, target):
        print("holy shit i teleported")
