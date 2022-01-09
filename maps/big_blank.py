from pprint import pprint

import core
from core import Pixie, Animations, States, Warp, Grid

from tiles import *
import maps

class BigBlank(core.Map):
    def __init__(self, game) -> None:
        name = "big_blank"
        grid = Grid(width=20, height=20)
        grid.fill(0, Grass)
        grid.fill_hollow_rect(depth=1, width=grid.width, height=grid.height, pos=(0, 0), tile=Rock)
        grid.set_bottom(0, 4, Grass)
        grid.set_top(0, 4, None)
        grid.set_top(1, 3, Rock)
        grid.set_top(1, 5, Rock)
        npcs = [
            Greeter(1, 1),
            CCGreeter(1, 8)
        ]
        warps = [Warp(game, pos=(0, 4), destination_map_constructor=maps.Cave, destination=(8, 4))]
        super().__init__(game, name, grid, npcs, warps)

class Greeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("greeter", x, y, 
            pixie=Pixie(animation=Animations.CLOCKWISE))

class CCGreeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("person", x, y, 
            pixie=Pixie(animation=Animations.COUNTERCLOCKWISE))
