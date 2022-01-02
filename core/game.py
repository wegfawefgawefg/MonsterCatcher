from os import system, name
from time import sleep
from enum import Enum

from pygame.constants import K_0

import core

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_p,
    K_0,
    KEYDOWN,
    QUIT,
    K_RETURN,
    K_t,
    K_i
)

class Modes(Enum):
    OVERWORLD = 1
    PARTY = 2
    MAIN_MENU = 3
    INVENTORY = 4
    BATTLE = 5
    SHOP = 6

class Game:
    BUTTON_COOLDOWN = 100

    def __init__(self) -> None:
        self.pixies = {}
        self.monsters = {}
        self.mode = "char"
        self.mode = Modes.MAIN_MENU

        self.player = core.Player()
        #self.party = Party()

        self.maps = {}

        self.map = None
        self.npcs = None

        self.button_cooldown = 0

        self.selected_inventory_item_index = 0
        self.selected_party_monster_index = 0

    def add_map(self, map):
        if map.name in self.maps:
            raise Exception(f"Map {map.name} already exists...")
        self.maps[map.name] = map

    def set_current_map(self, map_name):
        self.map = self.maps[map_name]
        self.npcs = self.map.npcs

    def step(self, dt):
        for npc in self.npcs:
            npc.step(dt)

    def handle_inputs(self, pressed_keys, dt):
        if self.button_cooldown > 0:
            self.button_cooldown -= dt
            return
        if self.mode == Modes.MAIN_MENU:
            if pressed_keys[K_RETURN]:
                self.mode = Modes.OVERWORLD
                self.button_cooldown = Game.BUTTON_COOLDOWN
        if self.mode == Modes.OVERWORLD:
            if pressed_keys[K_i]:
                self.mode = Modes.INVENTORY
                self.selected_inventory_item_index = 0
                self.button_cooldown = Game.BUTTON_COOLDOWN
            if pressed_keys[K_UP]:
                self.player.move_up(self.map, self.npcs)
                self.button_cooldown = Game.BUTTON_COOLDOWN
            elif pressed_keys[K_DOWN]:
                self.player.move_down(self.map, self.npcs)
                self.button_cooldown = Game.BUTTON_COOLDOWN
            elif pressed_keys[K_LEFT]:
                self.player.move_left(self.map, self.npcs)
                self.button_cooldown = Game.BUTTON_COOLDOWN
            elif pressed_keys[K_RIGHT]:
                self.player.move_right(self.map, self.npcs)
                self.button_cooldown = Game.BUTTON_COOLDOWN
            elif pressed_keys[K_p]:
                self.mode = Modes.PARTY
                self.button_cooldown = Game.BUTTON_COOLDOWN
        elif self.mode == Modes.PARTY:
            if pressed_keys[K_ESCAPE]:
                self.mode = Modes.OVERWORLD
                self.button_cooldown = Game.BUTTON_COOLDOWN
        elif self.mode == Modes.INVENTORY:
            if pressed_keys[K_ESCAPE] or pressed_keys[K_i]:
                self.mode = Modes.OVERWORLD
                self.button_cooldown = Game.BUTTON_COOLDOWN
            if pressed_keys[K_UP]:
                self.selected_inventory_item_index -= 1
                if self.selected_inventory_item_index < 0:
                    self.selected_inventory_item_index = len(self.player.inventory) - 1
                self.button_cooldown = Game.BUTTON_COOLDOWN
            elif pressed_keys[K_DOWN]:
                self.selected_inventory_item_index += 1
                if self.selected_inventory_item_index >= len(self.player.inventory):
                    self.selected_inventory_item_index = 0
                self.button_cooldown = Game.BUTTON_COOLDOWN
        elif self.mode == Modes.PARTY:
            if pressed_keys[K_ESCAPE] or pressed_keys[K_p]:
                self.mode = Modes.OVERWORLD
                self.button_cooldown = Game.BUTTON_COOLDOWN
            if pressed_keys[K_UP]:
                self.selected_party_monster_index -= 1
                if self.selected_party_monster_index < 0:
                    self.selected_party_monster_index = len(self.player.monsters) - 1
                self.button_cooldown = Game.BUTTON_COOLDOWN
            elif pressed_keys[K_DOWN]:
                self.selected_party_monster_index += 1
                if self.selected_party_monster_index >= len(self.player.monsters):
                    self.selected_party_monster_index = 0
                self.button_cooldown = Game.BUTTON_COOLDOWN
                