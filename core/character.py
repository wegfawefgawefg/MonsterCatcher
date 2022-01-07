import random
import math
from collections import OrderedDict

from .pixie import Pixie, Animations, States

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

class Character:
    def __init__(self, name, x, y, pixie=Pixie()) -> None:
        self.name = name
        self.x, self.y = x, y
        self.pixie = pixie

        self.inventory = Inventory()
        self.monsters = []

    def step(self, dt):
        self.pixie.step(dt)

    def move(self, game, x, y):
        map, npcs = game.map, game.npcs
        #   is new spot on map?
        if not (0 <= x < map.width) or not (0 <= y < map.width):
            return
        #   tile collisions
        if not map.tiles[y][x].allows:
            return
        #   npc collisions
        npc_already_there = any(npc.x == x and npc.y == y for npc in npcs)
        if npc_already_there:
            return
        self.x, self.y = x, y
    
    def move_down(self, game):
        self.pixie.state = States.DOWN
        self.move(game, self.x, self.y+1)

    def move_left(self, game):
        self.pixie.state = States.LEFT
        self.move(game, self.x-1, self.y)

    def move_right(self, game):
        self.pixie.state = States.RIGHT
        self.move(game, self.x+1, self.y)

    def move_up(self, game):
        self.pixie.state = States.UP
        self.move(game, self.x, self.y-1)

    def wander(self, game):
        if random.random() < 0.01:
            random.choice([self.move_up, self.move_down, self.move_left, self.move_right])(game)