from core import Move

class Heater(Move):
    def __init__(self):
        self.name = "nibble"
        self.pp = 15
        self.power = 1
        self.accuracy = 1
        self.target = "other"

    def use_in_battle(self, game, battle, user):
        pass
        #return super().use_in_battle(user, target)