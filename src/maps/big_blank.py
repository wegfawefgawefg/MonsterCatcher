from pprint import pprint
import random 

import core
from core import Pixie, Animations, States, Warp, Grid

import tiles
import maps

class BigBlank(core.Map):
    def __init__(self, game) -> None:
        name = "big_blank"
        grid = Grid(width=20, height=20)
        grid.fill(0, tiles.Grass)
        grid.fill_hollow_rect(depth=1, width=grid.width, height=grid.height, pos=(0, 0), tile=tiles.Rock)
        grid.set_bottom(0, 4, tiles.Grass)
        grid.set_top(0, 4, None)
        grid.set_top(1, 3, tiles.Rock)
        grid.set_top(1, 5, tiles.Rock)

        for i in range(10):
            x, y = random.randint(5, grid.width - 5), random.randint(5, grid.width - 5)
            grid.set_top(x, y, tiles.Bush)

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
    
    def interact(self, game, interactor):
        self.chat(game, "Hello, adventurer!")

class CCGreeter(core.Character):
    def __init__(self, x, y) -> None:
        super().__init__("person", x, y, 
            pixie=Pixie(animation=Animations.COUNTERCLOCKWISE))
