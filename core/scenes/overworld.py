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

from .scene import Scene
from .inventory import Inventory
from .party import Party

class Overworld(Scene):
    PLAYER_OFFSET_X = 4
    PLAYER_OFFSET_Y = 4

    def __init__(self, game, parent_scene):
        super().__init__(game, parent_scene)

    def step(self, dt, pressed_keys):
        if not self.game.buttons_on_cooldown():
            if pressed_keys[K_ESCAPE]:
                self.exit()
                self.game.start_button_cooldown()
            if pressed_keys[K_i]:
                self.game.scene = Inventory(self.game, parent_scene=self)
                self.game.start_button_cooldown()
            elif pressed_keys[K_p]:
                self.game.scene = Party(self.game, parent_scene=self)
                self.game.start_button_cooldown()
            #elif pressed_keys[K_s]:
            #    self.game.scene = core.Shop(self.game, parent_scene=self)
            #    self.game.start_button_cooldown()
            if pressed_keys[K_UP]:
                self.game.player.move_up(self.game.map, self.game.npcs)
                self.game.start_button_cooldown()
            elif pressed_keys[K_DOWN]:
                self.game.player.move_down(self.game.map, self.game.npcs)
                self.game.start_button_cooldown()
            elif pressed_keys[K_LEFT]:
                self.game.player.move_left(self.game.map, self.game.npcs)
                self.game.start_button_cooldown()
            elif pressed_keys[K_RIGHT]:
                self.game.player.move_right(self.game.map, self.game.npcs)
                self.game.start_button_cooldown()

        for npc in self.game.npcs:
            npc.step(dt)
        self.game.player.step(dt)
        self.game.engine.cam.set_pos(
            self.game.player.x - Overworld.PLAYER_OFFSET_X, 
            self.game.player.y - Overworld.PLAYER_OFFSET_Y)

    def render(self):
        self.game.engine.render_overworld(self.game, self)