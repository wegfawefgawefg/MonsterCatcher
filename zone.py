from npcs import *
from tiles import *

class Zone:
    def __init__(self, width, height, tile_grid, npcs) -> None:
        self.width = width
        self.height = height
        self.tile_grid = tile_grid
        self.npcs = npcs

