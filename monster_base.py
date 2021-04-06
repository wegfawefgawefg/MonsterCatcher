from pixies import *
from moves import *

class Stats:
    def __init__(self, hp=1, attack=1, sp_attack=1, defense=1, sp_defense=1, speed=1, xp_curve=10, xp_yield=1):
        self.hp = hp
        self.attack = attack
        self.sp_attack = sp_attack
        self.defense = defense
        self.sp_defense = sp_defense
        self.speed = speed
        self.xp_curve = xp_curve
        self.xp_yield = xp_yield
class MonsterBase:
    def __init__(self, name, stats, can_learn, learn_set):
        self.name = name
        self.stats = stats
        self.learn_set = learn_set
        self.can_learn = set().update(learn_set.values())
        self.can_learn.update(can_learn)
        self.pixie = None



