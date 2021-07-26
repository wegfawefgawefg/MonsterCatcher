import core
class Grass(core.Tile):
    def __init__(self) -> None:
        super().__init__(name="grass", allows=True, char=".")

