import core

class JAndJ(core.Item):
    def __init__(self) -> None:
        super().__init__(name="J&J", description="Puts a monster at 1HP", value=100, consumable=True)

    def use(self, game, user, target):
        if self.can_use_on(game, user, target):
            target.hp = 1
            user.inventory.remove(self)
            self.announce_use(user, target)

    def can_use_on(self, game, user, target):
        return user == game.player and isinstance(target, core.Monster) and target.hp > 1
