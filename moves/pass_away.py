from core import Move

class PassAway(Move):
    def __init__(self):
        self.name = "pass_away"
        self.pp = 1
        self.power = 0
        self.accuracy = 1
        self.target = Move.Target.SELF
        self.effect = []