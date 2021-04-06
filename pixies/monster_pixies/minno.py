from pixie import Pixie

class MinnoPixie(Pixie):
    def __init__(self) -> None:
        name = "player"
        width = 8
        height = 8
        chars = {
            "small": "m",
            "front": "m",
            "back": "m",
            "facing_down": "m",
            "facing_right": "B",
            "facing_left": "3",
            "facing_up": "w",
        }
        sprites = {
            "default": "0x3a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b103a2b1"
        }
        super().__init__(name, width, height, chars, sprites)

say()
move_to()