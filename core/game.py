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
    
)

class Modes(Enum):
    OVERWORLD = 1
    PARTY = 2
    MAIN_MENU = 3

class Game:
    def __init__(self) -> None:
        self.pixies = {}
        self.monsters = {}
        self.render_mode = "char"
        self.mode = Modes.MAIN_MENU

        self.player = core.Player()
        #self.party = Party()

        self.zones = {}

        self.current_zone_name = None
        self.current_zone = None
        self.map = None
        self.npcs = None

    def set_current_zone(self, zone_name):
        self.current_zone_name = zone_name
        self.zone = self.zones[self.current_zone_name]
        self.map = core.Map(self.zone)
        self.npcs = self.zone.npcs

    def step(self, dt):
        for npc in self.npcs:
            npc.step(dt)

    def handle_inputs(self, pressed_keys):
        if self.mode == Modes.MAIN_MENU:
            if pressed_keys[K_RETURN]:
                print("potato")
                self.mode = Modes.OVERWORLD
        if self.mode == Modes.OVERWORLD:
            if pressed_keys[K_UP]:
                self.player.move_up(self.map, self.npcs)
            elif pressed_keys[K_DOWN]:
                self.player.move_down(self.map, self.npcs)
            elif pressed_keys[K_LEFT]:
                self.player.move_left(self.map, self.npcs)
            elif pressed_keys[K_RIGHT]:
                self.player.move_right(self.map, self.npcs)
            elif pressed_keys[K_p]:
                self.render_mode == Modes.PARTY
        elif self.mode == Modes.PARTY:
            if pressed_keys[K_ESCAPE]:
                self.render_mode == Modes.OVERWORLD