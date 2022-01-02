class Map:
    def __init__(self, name, width, height, tile_grid, npcs) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.tiles = tile_grid
        self.npcs = npcs

