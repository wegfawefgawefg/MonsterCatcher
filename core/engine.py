import pygame 

import core

class Engine:
    #BUFFER_SIZE = (10, 9)
    BUFFER_SIZE = (10, 9)
    TILE_SIZE = 16
    SCALE = 5

    def __init__(self):
        self.tile_buffer = core.TileBuffer(*Engine.BUFFER_SIZE)
        self.cam = core.Cam(width=self.tile_buffer.width, height=self.tile_buffer.height)
        self.screen = pygame.Surface((self.tile_buffer.width*Engine.TILE_SIZE, self.tile_buffer.height*Engine.TILE_SIZE))
        self.window_screen = pygame.display.set_mode([Engine.SCALE * dim for dim in self.screen.get_size()])
        pygame.font.init()
        self.font = pygame.font.SysFont("monospace", Engine.TILE_SIZE)

    def render_map(self, game, scene):
        for y in range(self.tile_buffer.height):
            for x in range(self.tile_buffer.width):
                tile_x = self.cam.rect.x + x
                tile_y = self.cam.rect.y + y
                if 0 <= tile_x < game.map.width and 0 <= tile_y < game.map.height:
                    tile = game.map.tiles[tile_y][tile_x]
                    self.tile_buffer.buffer[y][x] = tile.char
                else:
                    self.tile_buffer.buffer[y][x] = " "

    def render_character(self, character, buffer_x, buffer_y):
        if character.render_state in character.pixie.chars:
            char = character.pixie.chars[character.render_state]
        else:
            char = character.pixie.chars["facing_down"]
        self.tile_buffer.buffer[buffer_y][buffer_x] = char

    def render_player(self, game, scene):
        cam_x, cam_y = self.cam.to_cam_space(game.player.x, game.player.y)
        self.render_character(game.player, cam_x, cam_y)

    def render_npcs(self, game, scene):
        for npc in game.npcs:
            cam_x, cam_y = self.cam.to_cam_space(npc.x, npc.y)
            if self.cam.contains_cam_space(cam_x, cam_y):
                self.render_character(npc, cam_x, cam_y)

    def render_overworld(self, game, scene):
        self.render_map(game, scene)
        self.render_player(game, scene)
        self.render_npcs(game, scene)
        for y in range(self.tile_buffer.height):
            for x in range(self.tile_buffer.width):
                char = self.tile_buffer.buffer[y][x]
                self.screen.blit(self.font.render(char, 1, (255, 255, 255)), (x*Engine.TILE_SIZE, y*Engine.TILE_SIZE))

    def render_inventory(self, game, scene):
        self.screen.blit(self.font.render("~Pack~", 1, (255, 255, 255)), (0, 0))
        num_displayable_items = self.tile_buffer.height - 1
        items = game.player.inventory[scene.selected_item_index:scene.selected_item_index+num_displayable_items]
        for i, item in enumerate(items):
            x = 0
            y = (i+1)*Engine.TILE_SIZE
            if i == 0:
                x = Engine.TILE_SIZE
                self.screen.blit(self.font.render(">", 1, (255, 255, 255)), (0, y))
            self.screen.blit(self.font.render(str(item), 1, (255, 255, 255)), (x, y))

    #def render_shop(self):
    #    self.screen.blit(self.font.render("~Shop~", 1, (255, 255, 255)), (0, 0))
    #    num_displayable_items = self.tile_buffer.height - 1
    #    items = game.active_shop.items[game.selected_shop_item_index:game.selected_shop_item_index+num_displayable_items]
    #    for i, item in enumerate(items):
    #        x = 0
    #        y = (i+1)*Engine.TILE_SIZE
    #        if i == 0:
    #            x = Engine.TILE_SIZE
    #            self.screen.blit(self.font.render(">", 1, (255, 255, 255)), (0, y))
    #        self.screen.blit(self.font.render(item, 1, (255, 255, 255)), (x, y))

    def render_party(self, game, scene):
        self.screen.blit(self.font.render("~Monsters~", 1, (255, 255, 255)), (0, 0))
        for i, monster in enumerate(game.player.monsters):
            x = 0
            y = (i+1)*Engine.TILE_SIZE
            if i == scene.selected_monster_index:
                x = Engine.TILE_SIZE
                self.screen.blit(self.font.render(">", 1, (255, 255, 255)), (0, y))
            self.screen.blit(self.font.render(str(monster), 1, (255, 255, 255)), (x, y))

    def render_main_menu(self, game, scene):
        self.screen.blit(self.font.render("MAIN MENU", 1, (255, 255, 255)), (0, 0))
        self.screen.blit(self.font.render("Press Enter", 1, (255, 255, 255)), (0, Engine.TILE_SIZE))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def flip(self):
        pygame.transform.scale(self.screen, self.window_screen.get_size(), self.window_screen)
        pygame.display.flip()
