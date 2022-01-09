import random
from enum import Enum, auto
import math

from .pixie import Pixie, Animations, States
from .inventory import Inventory

class Directions(Enum):
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    UP = auto()

class Character:
    def __init__(self, name, x, y, pixie=Pixie()) -> None:
        self.name = name
        self.x, self.y = x, y
        self.pixie = pixie
        self.facing = Directions.DOWN

        self.inventory = Inventory()
        self.monsters = []

    def __repr__(self) -> str:
        return f"{self.name}"

    def step(self, dt):
        self.pixie.step(dt)

    def move(self, game, x, y):
        map, npcs = game.map, game.npcs
        #   is new spot on map?
        if x < 0 or x >= map.width or y < 0 or y >= map.height:
            return False
        #   tile collisions
        bottom_tile = map.grid.get(0, x, y)
        if bottom_tile and not bottom_tile.allows:
            return False
        top_tile = map.grid.get(1, x, y)
        if top_tile and not top_tile.allows:
            return False
        #   npc collisions
        npc_already_there = any(npc.x == x and npc.y == y for npc in npcs)
        if npc_already_there:
            return False
        if game.player.x == x and game.player.y == y:
            return False
        self.x, self.y = x, y
        return True
    
    def move_down(self, game):
        self.facing = Directions.DOWN
        self.pixie.state = States.DOWN
        self.move(game, self.x, self.y+1)

    def move_left(self, game):
        self.facing = Directions.LEFT
        self.pixie.state = States.LEFT
        self.move(game, self.x-1, self.y)

    def move_right(self, game):
        self.facing = Directions.RIGHT
        self.pixie.state = States.RIGHT
        self.move(game, self.x+1, self.y)

    def move_up(self, game):
        self.facing = Directions.UP
        self.pixie.state = States.UP
        self.move(game, self.x, self.y-1)

    def wander(self, game):
        if random.random() < 0.01:
            random.choice([self.move_up, self.move_down, self.move_left, self.move_right])(game)