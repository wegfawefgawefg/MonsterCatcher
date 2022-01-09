class Grid:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.layers = []
        self.layers.append([[None for _ in range(width)] for _ in range(height)])
        self.layers.append([[None for _ in range(width)] for _ in range(height)])
        self.active = []
    
    @property
    def depth(self):
        return 2

    def fill(self, depth, tile):
        if 0 <= depth < self.depth:
            for y in range(self.height):
                for x in range(self.width):
                    self.set(depth, x, y, tile)

    def fill_hollow_rect(self, depth, width, height, pos, tile):
        ''' center of rect should not be filled '''
        if 0 <= depth < self.depth:
            for y in range(height):
                for x in range(width):
                    if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                        self.set(depth, pos[0] + x, pos[1] + y, tile)

    def step(self):
        for tile in self.active():
            tile.step()
            if not tile.active:
                self.active.remove(tile)

    def add_to_actives(self, tile):
        if tile.active:
            self.active.append(tile)

    def get_bottom(self, x, y):
        self.get(0, x, y)
    def set_bottom(self, x, y, tile):
        self.set(0, x, y, tile)

    def get(self, z, x, y):
        if 0 <= z < self.depth and 0 <= x < self.width and 0 <= y < self.height:
            return self.layers[z][int(y)][int(x)]
        return None
    def set(self, z, x, y, tile):
        if 0 <= z < self.depth and 0 <= x < self.width and 0 <= y < self.height:
            if tile:
                tile = tile()
                self.add_to_actives(tile)
            self.layers[z][int(y)][int(x)] = tile
        else:
            print(z, x, y)
            raise ValueError("Tile out of bounds.")

    def get_top(self, x, y):
        self.get(self.depth-1, x, y)
    def set_top(self, x, y, tile):
        self.set(self.depth-1, x, y, tile)