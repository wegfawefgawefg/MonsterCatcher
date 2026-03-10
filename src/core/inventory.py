from collections import OrderedDict

class Inventory:
    def __init__(self):
        self.items = OrderedDict()

    def __getitem__(self, index):
        return list(self.items)[index]

    def __iter__(self):
        return iter(self.items.values())

    def __len__(self):
        return len(self.items)

    def add(self, item_or_items):
        if isinstance(item_or_items, list):
            for item in item_or_items:
                self.add(item)
        else:
            item = item_or_items
            if item.consumable and item in self.items:
                self.items[item].quantity += 1
            else:
                self.items[item] = item

    def remove(self, item):
        if item.consumable and item.name in self.items:
            self.items[item].quantity -= 1
            if self.items[item].quantity <= 0:
                del self.items[item]
        else:
            del self.items[item]