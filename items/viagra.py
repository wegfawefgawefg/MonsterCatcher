import random

import core

import effects

class Viagra(core.Item):
    def __init__(self) -> None:
        super().__init__(name="viagra", description="makes u big", value=1_000_000, consumable=True)

    def use(self, game, user, target):
        if self.can_use_on(game, user, target):
            game.register_effect(effects.Swelling(game, target, 20))
            user.inventory.remove(self)
            self.announce_use(user, target)

    # grow 

    def unuse(self, game, user, target):
        if self.can_unuse_on(game, user, target):
            game.player.pixie.set_size((game.player.pixie.size[0] / 2, game.player.pixie.size[1] / 2))

    def can_use_on(self, game, user, target):
        return user == game.player and user == game.player

    def announce_use(self, user, target):
        print("me so horny me love u rong time")
