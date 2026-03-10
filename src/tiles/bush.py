import core
from core import Pixie

class Bush(core.Tile):
    def __init__(self) -> None:
        super().__init__(name="bush", allows=False)
