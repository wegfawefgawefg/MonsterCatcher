from enum import Enum, auto

from pygame.constants import K_0
from pygame.locals import (
    K_q,
    K_i,
    K_RIGHT,
    K_LEFT,
)

from .scene import Scene

class MonsterStats(Scene):
    class States(Enum):
        STATS = auto()
        MOVES = auto()

    def __init__(self, game, parent_scene, monster):
        commands = {
            K_q:self.exit,
            K_RIGHT:self.switch_right,
            K_LEFT:self.switch_left,
            K_i:self.view_inventory,
        }
        super().__init__(game, commands, parent_scene)
        self.monster = monster
        self.state = MonsterStats.States.STATS

    def view_inventory(self):
        from .inventory import Inventory
        self.game.scene = Inventory(self.game, self.parent_scene)

    def switch_right(self):
        if self.state == MonsterStats.States.STATS:
            self.state = MonsterStats.States.MOVES
    def switch_left(self):
        if self.state == MonsterStats.States.MOVES:
            self.state = MonsterStats.States.STATS

    def render(self):
        if self.state == MonsterStats.States.STATS:
            self.game.engine.render_monster_stats()
        elif self.state == MonsterStats.States.MOVES:
            self.game.engine.render_monster_moves()