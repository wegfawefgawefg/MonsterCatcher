from os import system, name
from time import sleep

from pygame.constants import K_0
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
    K_i,
    K_s,
)

from .scenes.main_menu import MainMenu

class Game:
    BUTTON_COOLDOWN = 100

    def __init__(self, engine=None) -> None:
        self.running = True
        self.engine = engine(game=self) if engine else None
        self.pixies = {}
        self.monsters = {}
        self.maps = {}

        self.scene = MainMenu(self)
        self.player = None
        self.map = None
        self.npcs = None
        self.using = None

        self.button_cooldown = 0

        self.selected_inventory_item_index = 0
        self.selected_party_monster_index = 0
        self.selected_shop_item_index = 0

        self.effects = []

    def register_effect(self, effect, args):
        pass
        #time, duration, effect, args
        #self.effects.append(())

    #def check_effects():
    #    for effect in self.effects:
    #        time

    def set_using(self, thing):
        self.using = thing

    def use(self, item, user, target):
        item.use(self, user, target)
    def use_using(self, user, target):
        if self.using:
            self.use(self.using, user, target)
            if self.using.consumable and self.using.quantity <= 0:
                self.using = None

    def buttons_on_cooldown(self):
        return self.button_cooldown > 0

    def start_button_cooldown(self):
        self.button_cooldown = Game.BUTTON_COOLDOWN

    def add_map(self, map):
        if map.name in self.maps:
            raise Exception(f"Map {map.name} already exists...")
        self.maps[map.name] = map

    def set_current_map(self, map_name):
        self.map = self.maps[map_name]
        self.npcs = self.map.npcs

    def step(self, dt, pressed_keys):
        if not self.engine:
            raise Exception("Engine not set")
        if not self.player:
            raise Exception("Player not set")
        if not self.scene:
            raise Exception("No active scenes...")
        self.dt = dt
        self.dtf = dt / 1000.0
        if self.button_cooldown > 0:
            self.button_cooldown -= dt
            return
        self.scene.step(pressed_keys)

    def render(self):
        if not self.engine:
            return
        self.engine.clear()
        self.scene.render()
        self.engine.flip()

    def quit(self):
        self.running = False


    