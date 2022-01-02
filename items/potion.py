import core

class Potion(core.Item):
    def __init__(self) -> None:
        self.name = "Potion"
        self.description = "A potion that restores HP."
        self.value = 10

    def use(self, character):
        print(f"{character.name} used {self.name}")
