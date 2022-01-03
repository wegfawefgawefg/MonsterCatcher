#   Example learn set
#       learn_set={0: moves.Nibble, 1: moves.Shmove})

class Monster:
    def __init__(self, name, stats, can_learn, learn_set, level=None, moves=None):
        self.hp = stats.hp
        self.name = name
        self.stats = stats
        self.learn_set = learn_set
        self.can_learn = can_learn.union(learn_set.values())
        self.pixie = None
        self.set_level(0 or level)
        self.moves = moves or self.get_moves()
        
    @property
    def level(self):
        return self.xp // self.stats.xp_curve

    def set_level(self, level):
        self.xp = level * self.stats.xp_curve

    def get_moves(self):
        return [move for lvl, move in self.learn_set.items() if lvl <= self.level]

