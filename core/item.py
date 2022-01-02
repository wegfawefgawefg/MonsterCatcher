class Item:
    def __init__(self, name, description, value) -> None:
        self.name = name
        self.description = description
        self.value = value

    def __repr__(self) -> str:
        return self.name

    def use(self, character):
        print(f"{character.name} used {self.name}")
    
    def drop(self, character):
        print(f"{character.name} dropped {self.name}")

    def pick_up(self, character):
        print(f"{character.name} picked up {self.name}")
