class Tile:
    def __init__(self, name, allows, char, sprite=None) -> None:
        self.name = name
        self.allows = allows
        self.char = char
        self.sprite = None

    def __repr__(self):
        return f"{self.name} tile"