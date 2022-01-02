import core

class Minno(core.Monster):
    def __init__(self) -> None:
        self.name = "Minno"
        self.hp=5
        self.attack=1
        self.sp_attack=1
        self.defense=1
        self.sp_defense=1
        self.speed=5
        self.xp_curve=5
        self.xp_yield=1
        self.can_learn = set(core.moves.DrinkCoffee)
        self.learn_set = {0: core.moves.Nibble, 1: core.moves.Nibble}

        self.pixie = core.pixies.monster.Minno

    def __repr__(self) -> str:
        return self.name