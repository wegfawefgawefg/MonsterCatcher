class Pixie:
    def __init__(self, name, width, height, chars, sprites) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.chars = chars
        self.sprites = sprites

    def __repr__(self):
        return f"{self.name} sprite"