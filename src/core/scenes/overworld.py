import random
import time 

from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_p,
    K_i,
    K_q,
    K_t,
    K_f,
    K_e,
)

from .scene import Scene

class Overworld(Scene):
    PLAYER_OFFSET_X = 4
    PLAYER_OFFSET_Y = 4

    def __init__(self, game, parent_scene):
        commands = {
            K_i:self.view_inventory,
            K_p:self.view_party,
            K_UP:self.move_up,
            K_DOWN:self.move_down,
            K_LEFT:self.move_left,
            K_RIGHT:self.move_right,
            K_t:self.use_useing_on_selected,
            K_f:self.use_in_front,
            K_e:self.interact,
        }
        super().__init__(game, commands, parent_scene)
        self.extra_selected = None

    @property
    def selected(self):
        return self.game.player

    @property
    def other_selected(self):
        return self.game.map.grid.get_top(*self.game.player.looking_at())

    def interact(self):
        npc_in_front = None
        spot_in_front = self.game.player.looking_at()
        for npc in self.game.npcs:
            if npc.x == spot_in_front[0] and npc.y == spot_in_front[1]:
                npc_in_front = npc
                break
        if npc_in_front:
            self.game.interact(self.game.player, npc_in_front)

    def use_useing_on_selected(self):
        if self.selected:
            self.game.use_using(self.game.player, target=self.selected)

    def use_in_front(self):
        print("use in front")
        self.game.use_using(self.game.player, target=self.other_selected)

    def view_inventory(self):
        from .inventory import Inventory
        self.game.scene = Inventory(self.game, parent_scene=self)
    def view_party(self):
        from .party import Party
        self.game.scene = Party(self.game, parent_scene=self)
    def move_up(self,):
        self.game.player.move_up(self.game)
    def move_down(self):
        self.game.player.move_down(self.game)
    def move_left(self):
        self.game.player.move_left(self.game)
    def move_right(self):
        self.game.player.move_right(self.game)

    def step(self, pressed_keys):
        super().step(pressed_keys)
        for npc in self.game.npcs:
            npc.step(self.game.dt)
            npc.wander(self.game)
        self.game.player.step(self.game.dt)
        self.game.map.check_warps()

        #smooth cam will happen later
        #self.game.engine.cam.set_pos(
        #    self.game.engine.cam.x + (self.game.player.x - self.game.engine.cam.x) / 4, 
        #    self.game.engine.cam.y + (self.game.player.y - self.game.engine.cam.y) / 4)

    def render(self):
        self.game.engine.render_overworld()