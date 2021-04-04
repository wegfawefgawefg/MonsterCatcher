from tiles import GrassTile, RockTile

class Zone:
    def __init__(self, width, height, tile_grid, npcs) -> None:
        self.width = width
        self.height = height
        self.tile_grid = tile_grid
        self.npcs = npcs

class SaladTownZone(Zone):
    def __init__(self) -> None:
        width = 16
        height = 16

        tile_grid = []
        for y in range(height):
            row = []
            for x in range(width):
                if (y == 0) or (x == 0) or (y == width - 1) or (x == height - 1):
                    tile = RockTile()
                else:
                    tile = GrassTile()
                row.append(tile)
            self.tile_grid.append(row)

        num_npcs = 2
        npcs = []
        for _ in range(num_npcs):
            npc = NPC()
            npcs.append(npc)

        super().__init__(
            width, 
            height, 
            tile_grid
            npcs)