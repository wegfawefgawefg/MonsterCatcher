from core import Pixie

class Tile:
    def __init__(self, name, allows, pixie=Pixie()) -> None:
        self.name = name
        self.allows = allows
        self.pixie = pixie

    def __repr__(self):
        return f"{self.name} tile"