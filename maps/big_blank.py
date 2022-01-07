import core
from core import Pixie, Animations, States

from tiles import *

class BigBlank(core.Map):
    def __init__(self) -> None:
        name = "big_blank"
        tile_grid = [
            [Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(),        Rock(),     Rock(),  Rock(),     Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(),        Rock(),     Rock(),  Rock(),     Rock()],
        ]
        npcs = [
            Greeter(1, 1),
            CCGreeter(1, 8)
        ]
        super().__init__(name, tile_grid, npcs)

class Greeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("greeter", x, y, 
            pixie=Pixie(animation=Animations.CLOCKWISE))

class CCGreeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("person", x, y, 
            pixie=Pixie(animation=Animations.COUNTERCLOCKWISE))
