from core import Move

class DrinkCoffee(Move):
    def __init__(self):
        self.name = "drink coffee"
        self.pp = 15
        self.power = 1
        self.accuracy = 1
        self.target = "self"
        self.effect = []