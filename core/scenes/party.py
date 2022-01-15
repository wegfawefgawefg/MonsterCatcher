from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_t,
    K_q,
    K_e,
    K_i,
)

from .scene import Scene

class Party(Scene):
    def __init__(self, game, parent_scene, choose_mode=False):
        commands = {
            K_q:self.exit,
            K_UP:self.select_up,
            K_DOWN:self.select_down,
            K_t:self.use_useing_on_selected,
            K_e:self.view_stats,
            K_i:self.view_inventory,
        }
        super().__init__(game, commands, parent_scene)
        self.selected_monster_index = 0
        
    @property
    def selected(self):
        return self.game.player.monsters[self.selected_monster_index]

    def view_inventory(self):
        from .inventory import Inventory
        self.game.scene = Inventory(self.game, self.parent_scene)

    def view_stats(self):
        from .monster_stats import MonsterStats
        self.game.scene = MonsterStats(self.game, self, self.game.player.monsters[self.selected_monster_index])

    def use_useing_on_selected(self):
        if self.selected:
            self.game.use_using(self.game.player, target=self.selected)

    def select_up(self):
        self.selected_monster_index -= 1
        if self.selected_monster_index < 0:
            self.selected_monster_index = len(self.game.player.monsters) - 1

    def select_down(self):
        self.selected_monster_index += 1
        if self.selected_monster_index >= len(self.game.player.monsters):
            self.selected_monster_index = 0


    #def step(self, dt, pressed_keys):
    #    if self.game.buttons_on_cooldown():
    #        return
    #    if pressed_keys[Party.BACK_BUTTON]:
    #        self.exit()
    #        self.game.start_button_cooldown()
    #    if pressed_keys[K_t]:
    #        if self.selected:
    #            self.game.use_using(self.game.player, target=self.selected)
    #        self.game.start_button_cooldown()
    #    if pressed_keys[K_UP]:
    #        self.selected_monster_index -= 1
    #        if self.selected_monster_index < 0:
    #            self.selected_monster_index = len(self.game.player.monsters) - 1
    #        self.game.start_button_cooldown()
    #    elif pressed_keys[K_DOWN]:
    #        self.selected_monster_index += 1
    #        if self.selected_monster_index >= len(self.game.player.monsters):
    #            self.selected_monster_index = 0
    #        self.game.start_button_cooldown()
    #    elif pressed_keys[K_RETURN]:
    #        print(f"selected {self.game.player.monsters[self.selected_monster_index]}")
    #        self.game.scene = MonsterStats(self.game, self, self.game.player.monsters[self.selected_monster_index])
    #        self.game.start_button_cooldown()

    def render(self):
        self.game.engine.render_party()