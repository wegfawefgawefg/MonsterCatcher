from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_p,
    K_i,
    K_q,
)

from .scene import Scene

class Overworld(Scene):
    PLAYER_OFFSET_X = 4
    PLAYER_OFFSET_Y = 4

    def __init__(self, game, parent_scene):
        commands = {
            K_q:self.exit,
            K_i:self.view_inventory,
            K_p:self.view_party,
            K_UP:self.move_up,
            K_DOWN:self.move_down,
            K_LEFT:self.move_left,
            K_RIGHT:self.move_right
        }
        super().__init__(game, commands, parent_scene)

    def view_inventory(self):
        from .inventory import Inventory
        self.game.scene = Inventory(self.game, parent_scene=self)
    def view_party(self):
        from .party import Party
        self.game.scene = Party(self.game, parent_scene=self)
    def move_up(self):
        self.game.player.move_up(self.game.map, self.game.npcs)
    def move_down(self):
        self.game.player.move_down(self.game.map, self.game.npcs)
    def move_left(self):
        self.game.player.move_left(self.game.map, self.game.npcs)
    def move_right(self):
        self.game.player.move_right(self.game.map, self.game.npcs)

    def step(self, pressed_keys):
        super().step(pressed_keys)
        for npc in self.game.npcs:
            npc.step(self.game.dt)
        self.game.player.step(self.game.dt)
        self.game.engine.cam.set_pos(
            self.game.player.x - Overworld.PLAYER_OFFSET_X, 
            self.game.player.y - Overworld.PLAYER_OFFSET_Y)

    def render(self):
        self.game.engine.render_overworld()