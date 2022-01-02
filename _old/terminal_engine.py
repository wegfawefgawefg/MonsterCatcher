import pygame 

import core

FONT_SIZE = 20
SCALE = 1
SCREEN_WIDTH, SCREEN_HEIGHT = [FONT_SIZE*SCALE*dim for dim in [16, 9]]

WINDOW_SCALE = 40
WINDOW_WIDTH, WINDOW_HEIGHT = [WINDOW_SCALE*dim for dim in [16, 9]]

class TerminalEngine:
    def __init__(self, game):
        self.game = game
        self.overworld_buffer = core.OverworldBuffer()
        self.cam = core.Cam(width=self.overworld_buffer.width, height=self.overworld_buffer.height)
        # create low resolution screen to blit to the main screen
        self.screen = pygame.Surface((SCREEN_WIDTH, SCREEN_WIDTH))
        self.window_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.font.init()
        self.game.font = pygame.font.SysFont("monospace", FONT_SIZE)

    def render_map(self):
        for y in range(self.overworld_buffer.height):
            for x in range(self.overworld_buffer.width):
                tile_x = self.cam.rect.x + x
                tile_y = self.cam.rect.y + y
                if 0 <= tile_x < self.game.map.width and 0 <= tile_y < self.game.map.height:
                    tile = self.game.map.tiles[tile_y][tile_x]
                    self.overworld_buffer.buffer[y][x] = tile.char
                else:
                    self.overworld_buffer.buffer[y][x] = " "

    def render_character(self, character, buffer_x, buffer_y):
        if character.render_state in character.pixie.chars:
            char = character.pixie.chars[character.render_state]
        else:
            char = character.pixie.chars["facing_down"]
        self.overworld_buffer.buffer[buffer_y][buffer_x] = char

    def render_player(self):
        cam_x, cam_y = self.cam.to_cam_space(self.game.player.x, self.game.player.y)
        self.render_character(self.game.player, cam_x, cam_y)

    def render_npcs(self):
        for npc in self.game.npcs:
            cam_x, cam_y = self.cam.to_cam_space(npc.x, npc.y)
            if self.cam.contains_cam_space(cam_x, cam_y):
                self.render_character(npc, cam_x, cam_y)

    def render_overworld_by_character(self):
        for y in range(self.overworld_buffer.height):
            for x in range(self.overworld_buffer.width):
                char = self.overworld_buffer.buffer[y][x]
                self.screen.blit(self.game.font.render(char, 1, (255, 255, 255)), (x*FONT_SIZE, y*FONT_SIZE))

    def render_overworld_to_terminal(self):
        print("OVERWORLD\n")
        print("__________")
        print(self.overworld_buffer)

    def render_overworld(self):
        self.render_map()
        self.render_player()
        self.render_npcs()

        # render the overworld_buffer to the pygame screen
        self.screen.fill((0, 0, 0))

        #self.render_overworld_by_character()
        for i, line in enumerate(self.overworld_buffer.as_lines()):
            self.screen.blit(self.game.font.render(line, 1, (255, 255, 255)), (0, i*FONT_SIZE))

        #    all at once
        #self.screen.blit(self.game.font.render(str(self.overworld_buffer), 1, (255, 255, 255)), (0, 0))
        #multiline_test_string = "wow\nthis\nis\nso\nlong"
        #self.screen.blit(self.game.font.render(multiline_test_string, 1, (255, 255, 255)), (0, 0))
        pygame.transform.scale(self.screen, (WINDOW_WIDTH, WINDOW_HEIGHT), self.window_screen)

    def render_main_menu(self):
        print("MAIN MENU\npress enter")

    def render(self, game):
        if game.mode == core.Modes.OVERWORLD:
            self.render_overworld()
        elif game.mode == core.Modes.MAIN_MENU:
            self.render_main_menu()
        pygame.display.flip()
