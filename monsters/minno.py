import core
import moves

class Minno(core.Monster):
    def __init__(self, 
        learn_set=None,
        level=5,
    ):
        super().__init__(
            name="minno", 
            stats=core.stats.Stats(hp=5, attack=1, defense=1, sp_attack=1, sp_defense=1, speed=1, xp_curve=5, xp_yield=1), 
            can_learn=set([moves.DrinkCoffee]), 
            learn_set={
                1: moves.Nibble(), 
                2: moves.Shmove(), 
                3: moves.DrinkCoffee(),
                4: moves.GetHype(),
                99: moves.PassAway()
            },
            level=level,
            pixie=core.Pixie(),
        )

    def __repr__(self) -> str:
        return self.name