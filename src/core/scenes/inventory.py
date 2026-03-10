from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    K_r,
    K_q,
    K_p,
)

from .scene import Scene

class Inventory(Scene):
    def __init__(self, game, parent_scene):
        commands = {
            K_q:self.exit,
            K_UP:self.move_up,
            K_DOWN:self.move_down,
            K_r:self.set_using,
            K_p:self.view_party,
        }
        super().__init__(game, commands, parent_scene)
        self.selected_item_index = 0

    @property
    def selected(self):
        return self.game.player.inventory[self.selected_item_index]

    def view_party(self):
        from .party import Party
        self.game.scene = Party(self.game, self.parent_scene)

    def move_up(self):
        self.selected_item_index -= 1
        if self.selected_item_index < 0:
            self.selected_item_index = len(self.game.player.inventory) - 1

    def move_down(self):
        self.selected_item_index += 1
        if self.selected_item_index >= len(self.game.player.inventory):
            self.selected_item_index = 0

    def set_using(self):
        self.game.using = self.selected
        self.game.start_button_cooldown()

    def render(self):
        self.game.engine.render_inventory()