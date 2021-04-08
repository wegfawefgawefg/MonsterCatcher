from core import Tile
class Rock(Tile):
    def __init__(self) -> None:
        super().__init__(type="rock", allows=False, char="o")