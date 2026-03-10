from core import Move

class Nibble(Move):
    def __init__(self):
        self.name = "nibble"
        self.pp = 15
        self.power = 1
        self.accuracy = 1
        self.target = "other"