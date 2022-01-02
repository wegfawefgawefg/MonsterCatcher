import pygame 

import core

class Engine:
    #BUFFER_SIZE = (10, 9)
    BUFFER_SIZE = (10, 9)
    TILE_SIZE = 16
    SCALE = 5

    def __init__(self, game):
        self.game = game
        self.tile_buffer = core.TileBuffer(*Engine.BUFFER_SIZE)
        self.cam = core.Cam(width=self.tile_buffer.width, height=self.tile_buffer.height)
        self.screen = pygame.Surface((self.tile_buffer.width*Engine.TILE_SIZE, self.tile_buffer.height*Engine.TILE_SIZE))
        self.window_screen = pygame.display.set_mode([Engine.SCALE * dim for dim in self.screen.get_size()])
        pygame.font.init()
        self.game.font = pygame.font.SysFont("monospace", Engine.TILE_SIZE)

    def render_map(self):
        for y in range(self.tile_buffer.height):
            for x in range(self.tile_buffer.width):
                tile_x = self.cam.rect.x + x
                tile_y = self.cam.rect.y + y
                if 0 <= tile_x < self.game.map.width and 0 <= tile_y < self.game.map.height:
                    tile = self.game.map.tiles[tile_y][tile_x]
                    self.tile_buffer.buffer[y][x] = tile.char
                else:
                    self.tile_buffer.buffer[y][x] = " "

    def render_character(self, character, buffer_x, buffer_y):
        if character.render_state in character.pixie.chars:
            char = character.pixie.chars[character.render_state]
        else:
            char = character.pixie.chars["facing_down"]
        self.tile_buffer.buffer[buffer_y][buffer_x] = char

    def render_player(self):
        cam_x, cam_y = self.cam.to_cam_space(self.game.player.x, self.game.player.y)
        self.render_character(self.game.player, cam_x, cam_y)

    def render_npcs(self):
        for npc in self.game.npcs:
            cam_x, cam_y = self.cam.to_cam_space(npc.x, npc.y)
            if self.cam.contains_cam_space(cam_x, cam_y):
                self.render_character(npc, cam_x, cam_y)

    def render_overworld(self):
        self.render_map()
        self.render_player()
        self.render_npcs()
        for y in range(self.tile_buffer.height):
            for x in range(self.tile_buffer.width):
                char = self.tile_buffer.buffer[y][x]
                self.screen.blit(self.game.font.render(char, 1, (255, 255, 255)), (x*Engine.TILE_SIZE, y*Engine.TILE_SIZE))

    def render_inventory(self):
        self.screen.blit(self.game.font.render("~Pack~", 1, (255, 255, 255)), (0, 0))
        num_displayable_items = self.tile_buffer.height - 1
        items = self.game.player.inventory[self.game.selected_inventory_item_index:self.game.selected_inventory_item_index+num_displayable_items]
        for i, item in enumerate(items):
            x = 0
            y = (i+1)*Engine.TILE_SIZE
            if i == 0:
                x = Engine.TILE_SIZE
                self.screen.blit(self.game.font.render(">", 1, (255, 255, 255)), (0, y))
            self.screen.blit(self.game.font.render(item, 1, (255, 255, 255)), (x, y))

    #def render_shop(self):
    #    self.screen.blit(self.game.font.render("~Shop~", 1, (255, 255, 255)), (0, 0))
    #    num_displayable_items = self.tile_buffer.height - 1
    #    items = self.game.active_shop.items[self.game.selected_shop_item_index:self.game.selected_shop_item_index+num_displayable_items]
    #    for i, item in enumerate(items):
    #        x = 0
    #        y = (i+1)*Engine.TILE_SIZE
    #        if i == 0:
    #            x = Engine.TILE_SIZE
    #            self.screen.blit(self.game.font.render(">", 1, (255, 255, 255)), (0, y))
    #        self.screen.blit(self.game.font.render(item, 1, (255, 255, 255)), (x, y))

    def render_party(self):
        self.screen.blit(self.game.font.render("~Monsters~", 1, (255, 255, 255)), (0, 0))
        for i, monster in enumerate(self.game.player.monsters):
            x = 0
            y = (i+1)*Engine.TILE_SIZE
            if i == self.game.selected_party_monster_index:
                x = Engine.TILE_SIZE
                self.screen.blit(self.game.font.render(">", 1, (255, 255, 255)), (0, y))
            self.screen.blit(self.game.font.render(monster, 1, (255, 255, 255)), (x, y))

    def render_main_menu(self):
        self.screen.blit(self.game.font.render("MAIN MENU", 1, (255, 255, 255)), (0, 0))
        self.screen.blit(self.game.font.render("Press Enter", 1, (255, 255, 255)), (0, Engine.TILE_SIZE))

    def render(self, game):
        self.screen.fill((0, 0, 0))
        if game.mode == core.Modes.OVERWORLD:
            self.render_overworld()
        elif game.mode == core.Modes.MAIN_MENU:
            self.render_main_menu()
        elif game.mode == core.Modes.PARTY:
            self.render_party()
        elif game.mode == core.Modes.SHOP:
            self.render_shop()
        elif game.mode == core.Modes.INVENTORY:
            self.render_inventory()
        #elif game.mode == core.Modes.BATTLE:
        #    self.render_battle()
        pygame.transform.scale(self.screen, self.window_screen.get_size(), self.window_screen)
        pygame.display.flip()
