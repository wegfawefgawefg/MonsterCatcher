import core
import effects

class Vitamins(core.Item):
    def __init__(self) -> None:
        super().__init__(name="vitamins", description="regenerate health slowly", value=15, consumable=True)

    def use(self, game, user, target):
        if self.can_use_on(game, user, target):
            game.register_effect(effects.Regening(game, target, 30))
            user.inventory.remove(self)
            self.announce_use(user, target)

    def can_use_on(self, game, user, target):
        return user == game.player and isinstance(target, core.Monster) and target.hp > 1
