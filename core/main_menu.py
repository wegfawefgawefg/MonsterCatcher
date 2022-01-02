from pygame.constants import K_0
from pygame.locals import (
    K_RETURN,
)

import core

class MainMenu(core.Scene):
    def __init__(self, game):
        super().__init__(game)

    def step(self, dt, pressed_keys):
        if not self.game.buttons_on_cooldown():
            if pressed_keys[K_RETURN]:
                self.game.start_button_cooldown()
                print("Starting game...")
                self.game.scene = core.Overworld(self.game, parent_scene=self)

    def exit(self):
        self.game.quit()

    def render(self):
        self.game.engine.render_main_menu(self.game, self)