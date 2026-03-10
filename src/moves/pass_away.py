from core import Move, BattleTargets

class PassAway(Move):
    def __init__(self):
        self.name = "pass_away"
        self.pp = 1
        self.power = 0
        self.accuracy = 1
        self.target = BattleTargets.SELF
        self.effect = []