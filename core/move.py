from enum import Enum, auto


class Move:
    class Target(Enum):
        SELF = auto()
        OPPONENT = auto()
        SELF_AND_OPPONENT = auto()
        PLAYER = auto()
        ENEMY_PLAYER = auto()
        BOTH_PLAYERS = auto()
        ALL = auto()
    def __init__(self, name, pp, power, accuracy, target):
        self.name = name
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.target = target
