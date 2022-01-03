from enum import Enum, auto

from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    K_RETURN,
    K_p,
)

from .scene import Scene

class MonsterStats(Scene):
    class States(Enum):
        STATS = auto()
        MOVES = auto()

    def __init__(self, game, parent_scene, monster):
        super().__init__(game, parent_scene)
        self.monster = monster
        self.state = MonsterStats.States.STATS

    def step(self, dt, pressed_keys):
        if not self.game.buttons_on_cooldown():
            if pressed_keys[K_p] or pressed_keys[K_ESCAPE]:
                self.exit()
                self.game.start_button_cooldown()
            if self.state == MonsterStats.States.STATS:
                if pressed_keys[K_RIGHT]:
                    self.state = MonsterStats.States.MOVES
                    self.game.start_button_cooldown()
            elif self.state == MonsterStats.States.MOVES:
                if pressed_keys[K_LEFT]:
                    self.state = MonsterStats.States.STATS
                    self.game.start_button_cooldown()

    def render(self):
        if self.state == MonsterStats.States.STATS:
            self.game.engine.render_monster_stats(self.game, self)
        elif self.state == MonsterStats.States.MOVES:
            self.game.engine.render_monster_moves(self.game, self)