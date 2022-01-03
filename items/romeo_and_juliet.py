import core

class RomeoAndJuliet(core.Item):
    def __init__(self) -> None:
        self.name = "Romeo and Juliet"
        self.description = "A tincture to feign death."
        self.value = 1000

    def use(self, character=None):
        print(f"{character.name} used {self.name}")
