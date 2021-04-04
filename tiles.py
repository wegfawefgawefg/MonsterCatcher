from typing import AbstractSet

class Tile:
    def __init__(self, type, allows, char, sprite=None) -> None:
        self.type = type
        self.allows = allows
        self.char = char
        self.sprite = None

    def __repr__(self):
        return f"{self.type} tile"

class GrassTile(Tile):
    def __init__(self) -> None:
        super().__init__(type="grass", allows=True, char=".")

class RockTile(Tile):
    def __init__(self) -> None:
        super().__init__(type="rock", allows=False, char="o")