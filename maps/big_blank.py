import core
import pixies
from tiles import *

class BigBlank(core.Map):
    def __init__(self) -> None:
        name = "big_blank"
        tile_grid = [
            [Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(),],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Rock()],
            [Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(), Rock(),],
        ]
        width = len(tile_grid[0])
        height = len(tile_grid)

        npcs = []
        for i in range(5):
            npcs.append(Greeter(i+1, i+2))
            npcs.append(CCGreeter(i+2, i+2))

        super().__init__(name, width, height, tile_grid, npcs)

class Greeter(core.Character):
    def __init__(self, x, y) -> None:
        x, y = x, y
        motion = core.Motion("rotating", direction="clockwise")
        pixie = pixies.npc.Greeter()
        super().__init__(x, y, motion, pixie)

class CCGreeter(core.Character):
    def __init__(self, x, y) -> None:
        x, y = x, y
        motion = core.Motion("rotating", direction="counterclockwise")
        pixie = pixies.npc.Greeter()
        super().__init__(x, y, motion, pixie)