from core import Tile
class Grass(Tile):
    def __init__(self) -> None:
        super().__init__(type="grass", allows=True, char=".")

