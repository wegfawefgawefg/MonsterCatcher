from enum import Enum, auto

from pygame.constants import K_0
from pygame.locals import (
    K_q,
    K_i,
    K_t,
    K_RIGHT,
    K_LEFT,
    K_DOWN,
    K_UP,
)

from core import Stats
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
            K_UP:self.select_up,
            K_DOWN:self.select_down,
            K_i:self.view_inventory,
            K_t:self.use_useing_on_selected,
        }
        super().__init__(game, commands, parent_scene)
        self.monster = monster
        self.state = MonsterStats.States.STATS
        self.selected_thing_index = -1

    @property
    def selected(self):
        if self.selected_thing_index < 0:
            return self.monster
        if self.state == MonsterStats.States.STATS:
            return Stats.STATS(self.selected_thing_index+1)
        elif self.state == MonsterStats.States.MOVES:
            return self.monster.moves[self.selected_thing_index]

    def use_useing_on_selected(self):
        if self.selected:
            self.game.use_using(self.game.player, target=self.selected)

    def view_inventory(self):
        from .inventory import Inventory
        self.game.scene = Inventory(self.game, self.parent_scene)

    def switch_right(self):
        if self.state == MonsterStats.States.STATS:
            self.state = MonsterStats.States.MOVES
            self.selected_thing_index = -1
    def switch_left(self):
        if self.state == MonsterStats.States.MOVES:
            self.state = MonsterStats.States.STATS
            self.selected_thing_index = -1
    def select_up(self):
        self.selected_thing_index -= 1
        self.selected_thing_index = max(self.selected_thing_index, -1)
    def select_down(self):
        self.selected_thing_index += 1
        if self.state == MonsterStats.States.MOVES:
            self.selected_thing_index = min(self.selected_thing_index, len(self.monster.moves) - 1)
        elif self.state == MonsterStats.States.STATS:
            self.selected_thing_index = min(self.selected_thing_index, len(self.monster.stats) - 1)

    def render(self):
        if self.state == MonsterStats.States.STATS:
            self.game.engine.render_monster_stats()
        elif self.state == MonsterStats.States.MOVES:
            self.game.engine.render_monster_moves()