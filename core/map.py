class Map:
    def __init__(self, name, tile_grid, npcs) -> None:
        self.name = name
        self.tiles = tile_grid
        self.npcs = npcs

    @property
    def width(self) -> int:
        return len(self.tiles[0])
    @property
    def height(self) -> int:
        return len(self.tiles)
    
