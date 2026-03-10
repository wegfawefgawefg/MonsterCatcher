from core import Effect

class Regening(Effect):
    def __init__(self, game, target, duration):
        super().__init__(game, "regening", target, duration)
    
    def start(self):
        print(f"{self.target} is regening!")
    def run(self):
        self.target.hp = min(self.target.hp + 1.0 * self.game.dtf, self.target.stats.hp)
    def finish(self):
        print(f"The effects of {self.name} on {self.target.name} have ended.")
