from pprint import pprint

import core

inv = core.Inventory()

#   item constructor example
#       def __init__(self, name, description, value, consumable=True, quantity=1) -> None:
class Potion(core.Item):
    def __init__(self) -> None:
        super().__init__("potion", "A potion that restores HP.", 10, True, 1)
inv.add(Potion())
inv.add(Potion())
inv.add(Potion())
pprint(inv.items)
inv.remove(Potion())
inv.remove(Potion())
inv.remove(Potion())
pprint(inv.items)
for item in inv:
    print(f"{item.name}: {item.quantity}")

