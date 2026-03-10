from core import Move, BattleTargets

class DrinkCoffee(Move):
    def __init__(self):
        super().__init__(
            name="drink coffee",
            pp=15,
            power=1,
            accuracy=1,
            target=BattleTargets.SELF
        )

    def use_in_battle(self, game, user, target):
        user.hp += user.max_hp // 4
        user.pp[self.name] -= 1
    
    def use(self, user, target):
        pass
