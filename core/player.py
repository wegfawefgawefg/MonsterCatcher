from core import Character

class Player(Character):
    def __init__(self) -> None:
        pixie = pixies.Player()
        super().__init__(x=4, y=4, motion="static", pixie=pixie)