from zone import Zone

class Map:
    def __init__(self, zone) -> None:
        self.width = zone.width
        self.height = zone.height
        self.tiles = zone.tile_grid

    def render(self, player, overworld_buffer):
        print(f"player: {player.x}, {player.y}")
        for y in range(overworld_buffer.height):
            for x in range(overworld_buffer.width):
                tile_x = player.x - 4 + x
                tile_y = player.y - 4 + y
                if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
                    tile = self.tiles[tile_y][tile_x]
                    overworld_buffer.buffer[y][x] = tile.char
                else:
                    overworld_buffer.buffer[y][x] = " "