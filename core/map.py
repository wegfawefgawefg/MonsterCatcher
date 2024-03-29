class TimeTrigger:
    def __init__(self, game, creation_time, duration, callback):
        self.game = game
        self.creation_time = creation_time
        self.duration = duration
        self.callback = callback

    def check(self):
        if (self.game.time - self.creation_time) < self.duration:
            self.callback()
            return True

class PositionTrigger:
    def __init__(self, game, pos, callback):
        self.game = game
        self.pos = pos
        self.callback = callback

    def check(self):
        if (self.game.player.x, self.game.player.y) == self.pos:
            self.callback()

class Warp(PositionTrigger):
    def __init__(self, game, pos, destination=None, destination_map_constructor=None):
        self.game = game
        self.pos = pos
        if destination_map_constructor and not destination:
            raise ValueError("Warps to other map, but destination not specified.")
        self.destination = destination
        self.destination_map_constructor = destination_map_constructor
        super().__init__(game, pos, self.warp)

    def warp(self):
        if self.destination_map_constructor:
            self.game.set_current_map(self.destination_map_constructor(game=self.game))
            self.game.player.move(self.game, self.destination[0], self.destination[1])
        if self.destination:
            self.game.player.move(self.game, self.destination[0], self.destination[1])

class Map:
    def __init__(self, game, name, grid, npcs, warps=[], lock_cam_in=True) -> None:
        self.game = game
        self.name = name
        self.lock_cam_in = lock_cam_in
        if lock_cam_in and (
            (grid.width-1) < self.game.engine.BUFFER_SIZE[0]
            or (grid.height-1) < self.game.engine.BUFFER_SIZE[1]
        ):
            raise ValueError("Map is too too small to fill view.")
        self.grid = grid
        self.npcs = npcs
        self.warps = warps

    @property
    def depth(self):
        return self.grid.depth
    @property
    def width(self) -> int:
        return self.grid.width
    @property
    def height(self) -> int:
        return self.grid.height

    def step():
        NotImplementedError()

    def add_warp(self, warp):
        self.warps.append(warp)

    def check_warps(self):
        for warp in self.warps:
            if (self.game.player.x, self.game.player.y) == warp.pos:
                warp.warp()
