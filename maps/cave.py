import core
from core import Pixie, Animations, States, Warp, Grid
import maps

from tiles import *

class Cave(core.Map):
    def __init__(self, game) -> None:
        name = "left_field"
        grid = Grid(width=10, height=10)
        grid.fill(0, Grass)
        grid.fill_hollow_rect(depth=1, width=10, height=10, pos=(0, 0), tile=Rock)
        grid.set_bottom(9, 4, Grass)
        grid.set_top(9, 4, None)
        npcs = [
            Greeter(1, 1),
            CCGreeter(1, 8)
        ]
        warps = [Warp(game, pos=(9, 4), destination_map_constructor=maps.BigBlank, destination=(1, 4))]
        super().__init__(game, name, grid, npcs, warps, lock_cam_in=False)

class Greeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("greeter", x, y, 
            pixie=Pixie(animation=Animations.CLOCKWISE, size=(0.5, 0.5)))

class CCGreeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("person", x, y, 
            pixie=Pixie(animation=Animations.COUNTERCLOCKWISE))
