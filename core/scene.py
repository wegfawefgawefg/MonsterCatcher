#from enum import Enum

#class Scenes(Enum):
#    OVERWORLD = 1
#    PARTY = 2
#    MAIN_MENU = 3
#    INVENTORY = 4
#    BATTLE = 5
#    SHOP = 6
#    MONSTER_VIEWER = 7
#    PARTY_VIEWER = 8
#    MONSTER_SELECT = 8

class Scene:
    def __init__(self, game, parent_scene=None):
        self.game = game
        self.parent_scene = parent_scene

    def handle_inputs(self, inputs):
        raise NotImplementedError

    def exit(self):
        if self.parent_scene:
            self.game.scene = self.parent_scene

    def render(self, engine):
        raise NotImplementedError