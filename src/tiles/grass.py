import random

import core
from core import Pixie, Animations, States

class Grass(core.Tile):
    def __init__(self):
        super().__init__(name="grass", allows=True,
            pixie=Pixie(animation=random.choice([Animations.STATIC, Animations.TWO_STEP])))
