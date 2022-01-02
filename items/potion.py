import core

class Potion(core.Item):
    def __init__(self) -> None:
        super().__init__(name="Potion", description="Heals 50 HP", value=50)

    def use(self, character):
        print(f"{character.name} used {self.name}")
