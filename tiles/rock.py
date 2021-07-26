import core
class Rock(core.Tile):
    def __init__(self) -> None:
        super().__init__(name="rock", allows=False, char="o")