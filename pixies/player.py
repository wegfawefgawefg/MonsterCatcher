from pixie import Pixie

class PlayerPixie(Pixie):
    def __init__(self) -> None:
        name = "player"
        width = 8
        height = 8
        chars = {
            "facing_down": "v",
            "facing_right": ">",
            "facing_left": "<",
            "facing_up": "^",
        }
        sprites = {
            "default": "0x3a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b1"
        }
        super().__init__(name, width, height, chars, sprites)