import math
import time 
from core import Effect

class Swelling(Effect):
    def __init__(self, game, target, duration):
        super().__init__(game, "swelling", target, duration)
    
    def start(self):
        print(f"{self.target} is swelling!")
    def run(self):
        self.target.pixie.set_size(
            [math.sin(time.time()*4)*0.3+1.0,]*2
        )
    def finish(self):
        print(f"The effects of {self.name} on {self.target.name} have ended.")
