from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    K_RETURN,
    K_p,
)

from .scene import Scene
from .monster_stats import MonsterStats

class Party(Scene):
    def __init__(self, game, parent_scene):
        super().__init__(game, parent_scene)
        self.selected_monster_index = 0

    def step(self, dt, pressed_keys):
        if not self.game.buttons_on_cooldown():
            if pressed_keys[K_p] or pressed_keys[K_ESCAPE]:
                self.exit()
                self.game.start_button_cooldown()
            if pressed_keys[K_UP]:
                self.selected_monster_index -= 1
                if self.selected_monster_index < 0:
                    self.selected_monster_index = len(self.game.player.inventory) - 1
                self.game.start_button_cooldown()
            elif pressed_keys[K_DOWN]:
                self.selected_monster_index += 1
                if self.selected_monster_index >= len(self.game.player.inventory):
                    self.selected_monster_index = 0
                self.game.start_button_cooldown()
            elif pressed_keys[K_RETURN]:
                print(f"selected {self.game.player.monsters[self.selected_monster_index]}")
                self.game.scene = MonsterStats(self.game, self, self.game.player.monsters[self.selected_monster_index])
                self.game.start_button_cooldown()

    def render(self):
        self.game.engine.render_party(self.game, self)