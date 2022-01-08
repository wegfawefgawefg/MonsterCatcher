import core
from core import Pixie, Animations, States, Warp
import maps

from tiles import *

class LeftField(core.Map):
    def __init__(self, game) -> None:
        name = "left_field"
        tile_grid = []
        height = 10
        width = 10
        for y in range(height):
            row = []
            for x in range(width):
                if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                    row.append(Rock())
                else:
                    row.append(Grass())
            tile_grid.append(row)
        tile_grid[4][9] = Grass()

        npcs = [
            Greeter(1, 1),
            CCGreeter(1, 8)
        ]
        warps = [Warp(game, pos=(9, 4), destination_map_constructor=maps.BigBlank, destination=(1, 4))]
        super().__init__(game, name, tile_grid, npcs, warps)

class Greeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("greeter", x, y, 
            pixie=Pixie(animation=Animations.CLOCKWISE, size=(0.5, 0.5)))

class CCGreeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("person", x, y, 
            pixie=Pixie(animation=Animations.COUNTERCLOCKWISE))
