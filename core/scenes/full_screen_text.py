import random
import time 

from pygame.constants import K_0
from pygame.locals import (
    K_q,
    K_e,
)

from .scene import Scene

class FullScreenText(Scene):
    PLAYER_OFFSET_X = 4
    PLAYER_OFFSET_Y = 4

    def __init__(self, game, parent_scene, text=[]):
        commands = {
            K_q:self.exit,
            K_e:self.go_down,
        }
        super().__init__(game, commands, parent_scene)
        self.text = text
        self.text_index = 0

    def can_go_down(self):
        return self.text_index < len(self.text) - 1

    def go_down(self):
        self.text_index += 1
        if self.text_index >= len(self.text):
            self.text_index = 0
            self.game.scene = self.parent_scene

    def step(self, pressed_keys):
        super().step(pressed_keys)

    def render(self):
        self.game.engine.render_full_screen_text()