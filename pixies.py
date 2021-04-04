class Pixie:
    def __init__(self, name, width, height, chars, sprites) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.chars = chars
        self.sprites = sprites

    def __repr__(self):
        return f"{self.name} sprite"

class GreeterPixie(Pixie):
    def __init__(self) -> None:
        name = "greeter"
        width = 8
        height = 8
        chars = {
            "default": "M",
            "directional": {
                "facing_down": "<",
                "facing_right": ">",
                "facing_left": "<",
                "facing_up": "^",
            }
        }
        sprites = {
            "default": "0x3a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b1"
        }
        super().__init__(name, width, height, chars, sprites)

class PlayerPixie(Pixie):
    def __init__(self) -> None:
        name = "player"
        width = 8
        height = 8
        chars = {
            "default": "P",
            "directional": {
                "facing_down": "<",
                "facing_right": ">",
                "facing_left": "<",
                "facing_up": "^",
            }
        }
        sprites = {
            "default": "0x3a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b1"
        }
        super().__init__(name, width, height, chars, sprites)