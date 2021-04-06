from pixie import Pixie

class GreeterPixie(Pixie):
    def __init__(self) -> None:
        name = "greeter"
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