import core

class Minno(core.Pixie):
    def __init__(self) -> None:
        self.name = "player"
        self.width = 8
        self.height = 8
        self.chars = {
            "small": "m",
            "front": "m",
            "back": "m",
            "facing_down": "m",
            "facing_right": "B",
            "facing_left": "3",
            "facing_up": "w",
        }
        self.sprites = {
            "default": "0x3a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b1"
        }