class Motion:
    def __init__(self, pattern="static", speed=1000, direction=None, ) -> None:
        self.pattern = pattern
        self.speed = speed
        self.direction = direction