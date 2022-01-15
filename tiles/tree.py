import core
from core import Pixie

class Tree(core.Tile):
    def __init__(self) -> None:
        super().__init__(name="tree", allows=False)
