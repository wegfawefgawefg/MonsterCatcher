from zone import Zone

class Map:
    def __init__(self, zone) -> None:
        self.width = zone.width
        self.height = zone.height
        self.tiles = zone.tile_grid