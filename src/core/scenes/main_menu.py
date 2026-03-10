from pygame.constants import K_0, K_ESCAPE
from pygame.locals import (
    K_RETURN,
    K_d,
)

from core.scenes.full_screen_text import FullScreenText

from .scene import Scene
from .overworld import Overworld

class MainMenu(Scene):
    def __init__(self, game):
        commands = {
            K_RETURN:self.start_game,
            K_d:self.launch_test,
            K_ESCAPE:self.exit,
        }
        super().__init__(game, commands)

    def launch_test(self):
        text = [
            "You think about the",
            "possibilities of",
            "your life."
        ]
        self.game.scene = FullScreenText(self.game, parent_scene=self, text=text)

    def start_game(self):
        self.game.scene = Overworld(self.game, parent_scene=self)

    def exit(self):
        self.game.quit()

    def render(self):
        self.game.engine.render_main_menu()