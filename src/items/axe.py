import core
import effects
import tiles

class Axe(core.Item):
    def __init__(self) -> None:
        super().__init__(name="axe", description="cut trees", value=5000, consumable=False)

    def use(self, game, user, target):
        if self.can_use_on(game, user, target):
            x, y = game.player.looking_at()
            game.map.grid.set_top(x, y, None)
            self.announce_use(user, target)

    def can_use_on(self, game, user, target):
        return user == game.player and isinstance(target, tiles.Bush) 

    def announce_use(self, user, target):
        print("You swing your axe at the bush... and it falls to the ground.")