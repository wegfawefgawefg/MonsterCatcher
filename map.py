from zone import Zone

class Map:
    def __init__(self, zone) -> None:
        self.width = zone.width
        self.height = zone.height
        self.tiles = zone.tile_grid

    def render(self, player, overworld_buffer):
        x1 = player.x - 4
        y1 = player.y - 4
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = x1 + overworld_buffer.width
        y2 = y1 + overworld_buffer.height
        print(f"{x1} {x2} {y1} {y2}")
        for o_y, y in enumerate(range(y1, y2)):
            for o_x, x in enumerate(range(x1, x2)):
                if 0 <= x < self.width and 0 <= y < self.height:
                    tile = self.tiles[y][x]
                    overworld_buffer.buffer[o_y][o_x] = tile.char
                else:
                    overworld_buffer.buffer[o_y][o_x] = " "