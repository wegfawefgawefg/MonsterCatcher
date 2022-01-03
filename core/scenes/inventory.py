from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    K_RETURN,
    K_i,
)

from .scene import Scene

class Inventory(Scene):
    def __init__(self, game, parent_scene):
        super().__init__(game, parent_scene)
        self.selected_item_index = 0

    #class Target(Enum):
    #    MONSTER = auto()
    #    ITEM = auto()
    #    TILE = auto()
    #    PLAYER = auto()
    #    CHARACTER = auto()
    #    STAT = auto()
    #    MOVE = auto()
    #    HOLD = auto()
    #    NONE = auto()

    def use_item(self, item, user, target):
        item.use(self, user, target)

    def give_item(self, item, user, target):
        item.drop(user)
        target.pick_up(item)


    def step(self, dt, pressed_keys):
        if not self.game.buttons_on_cooldown():
            if pressed_keys[K_i] or pressed_keys[K_ESCAPE]:
                self.exit()
                self.game.start_button_cooldown()
            if pressed_keys[K_UP]:
                self.selected_item_index -= 1
                if self.selected_item_index < 0:
                    self.selected_item_index = len(self.game.player.inventory) - 1
                self.game.start_button_cooldown()
            elif pressed_keys[K_DOWN]:
                self.selected_item_index += 1
                if self.selected_item_index >= len(self.game.player.inventory):
                    self.selected_item_index = 0
                self.game.start_button_cooldown()
            elif pressed_keys[K_RETURN]:
                print(f"used {self.game.player.inventory[self.selected_item_index]}")
                self.game.start_button_cooldown()

    def render(self):
        self.game.engine.render_inventory(self.game, self)