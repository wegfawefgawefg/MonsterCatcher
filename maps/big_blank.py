import core
from core import Pixie, Animations, States, Warp

from tiles import *
import maps

class BigBlank(core.Map):
    def __init__(self, game) -> None:
        name = "big_blank"
        tile_grid = [
            [Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(),        Rock(),     Rock(),  Rock(),     Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
            [Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(),  Grass(),    Grass(), Grass(),    Rock()],
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
        warps = [Warp(game, pos=(0, 4), destination_map_constructor=maps.LeftField, destination=(8, 4))]
        super().__init__(game, name, tile_grid, npcs, warps)

class Greeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("greeter", x, y, 
            pixie=Pixie(animation=Animations.CLOCKWISE))

class CCGreeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("person", x, y, 
            pixie=Pixie(animation=Animations.COUNTERCLOCKWISE))
