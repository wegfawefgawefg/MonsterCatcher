from core import Move, BattleTargets

class Shmove(Move):
    def __init__(self):
        self.name = "shmove"
        self.pp = 10
        self.power = 0
        self.accuracy = 1
        self.target = BattleTargets.SELF
        self.effect = []