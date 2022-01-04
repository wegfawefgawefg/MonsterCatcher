import core

class Potion(core.Item):
    def __init__(self) -> None:
        super().__init__(name="Potion", description="Heals a monster 10 HP", value=10, consumable=True)

    def use(self, game, user, target):
        if self.can_use_on(game, user, target):
            target.hp += 10
            user.inventory.remove(self)
            self.announce_use(user, target)

    def can_use_on(self, game, user, target):
        return user == game.player and isinstance(target, core.Monster)
