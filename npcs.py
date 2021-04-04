from character import Character
from pixies import *

class GreeterNPC(Character):
    def __init__(self) -> None:
        x, y = 2, 2
        motion = "rotating"
        pixie = GreeterPixie()
        super().__init__(x, y, motion, pixie)