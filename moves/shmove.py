from core import Move

class Shmove(Move):
    def __init__(self):
        self.name = "shmove"
        self.pp = 10
        self.power = 0
        self.accuracy = 1
        self.target = Move.Target.SELF
        self.effect = []