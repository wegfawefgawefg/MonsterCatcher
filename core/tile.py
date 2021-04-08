class Tile:
    def __init__(self, type, allows, char, sprite=None) -> None:
        self.type = type
        self.allows = allows
        self.char = char
        self.sprite = None

    def __repr__(self):
        return f"{self.type} tile"