import core
from core import Pixie

class Rock(core.Tile):
    def __init__(self) -> None:
        super().__init__(name="rock", allows=False)
