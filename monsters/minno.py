import moves

class Minno:
    name = "Minno"
    hp=5
    attack=1
    sp_attack=1
    defense=1
    sp_defense=1
    speed=5
    xp_curve=5
    xp_yield=1
    can_learn = set(moves.DrinkCoffee)
    learn_set = {0: moves.Nibble, 1: moves.Nibble}