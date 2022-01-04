import time
import math
import os
from pprint import pprint

import pygame 

import core

class Engine:
    BUFFER_SIZE = (10, 9)
    TILE_SIZE = 16
    SCALE = 5

    class AssetManager:
        def __init__(self):
            self.assets = {}
            path = os.path.dirname(os.path.abspath(__file__))
            asset_path = os.path.join(path, "..","assets")
            self.load_assets(asset_path)

        def load_assets(self, path):
            asset_categories = ["tiles", "monsters", "items", "characters"]
            for category in asset_categories:
                self.assets[category] = self.recurse_dir(os.path.join(path, category))

        def recurse_dir(self, path):
            assets = {}
            for folder in os.listdir(path):
                assets[folder] = {}
                for file in os.listdir(os.path.join(path, folder)):
                    if file.endswith(".png"):
                        im_path = os.path.join(path, folder, file)
                        assets[folder][file[:-4]] = pygame.image.load(im_path).convert_alpha()
            return assets

        @property
        def monsters(self):
            return self.assets["monsters"]
        @property
        def tiles(self):
            return self.assets["tiles"]
        @property
        def items(self):
            return self.assets["items"]
        @property
        def characters(self):
            return self.assets["characters"]

    def __init__(self, game):
        self.game = game
        self.tile_buffer = core.TileBuffer(*Engine.BUFFER_SIZE)
        self.cam = core.Cam(width=self.tile_buffer.width, height=self.tile_buffer.height)
        self.screen = pygame.Surface((self.tile_buffer.width*Engine.TILE_SIZE, self.tile_buffer.height*Engine.TILE_SIZE))
        self.window_screen = pygame.display.set_mode([Engine.SCALE * dim for dim in self.screen.get_size()])
        self.assets = Engine.AssetManager()
        pygame.font.init()
        if BUILTIN:=True:
            self.font = pygame.font.SysFont("monospace", Engine.TILE_SIZE)
        else:
            font = ["font", "pkmngb", "8bitoperator_jve"][-1]
            path = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(path, "..","fonts",f"{font}.ttf")
            self.font = pygame.font.Font(full_path, Engine.TILE_SIZE)

    def center(self, surface, width=True, height=True):
        return (
            (self.screen.get_width() - surface.get_width())/2 if width else 0,
            (self.screen.get_height() - surface.get_height())/2 if height else 0)

    def wigglezoom(self, txt, pos, rspeed=2, rscale=1, zspeed=2, zscale=0.1, size=1, center=(False, False)):
        txt = pygame.transform.rotozoom(txt, 
            math.sin(time.time()*rspeed)*rscale, 
            math.cos(time.time()*zspeed)*zscale+size)
        self.screen.blit(txt, (
            (pos[0] - txt.get_width()/2) if center[0] else pos[0], 
            (pos[1] - txt.get_height()/2) if center[1] else pos[1]))

    def render_map(self):
        for y in range(self.tile_buffer.height):
            tile_y = self.cam.rect.y + y
            for x in range(self.tile_buffer.width):
                tile_x = self.cam.rect.x + x
                if 0 <= tile_x < self.game.map.width and 0 <= tile_y < self.game.map.height:
                    tile = self.game.map.tiles[tile_y][tile_x]
                    if tile:
                        tile.pixie.step(self.game.dt)
                        asset_name = core.Pixie.ASSET_NAMES[tile.pixie.state]
                        asset = self.assets.tiles[tile.name][asset_name]
                        self.screen.blit(asset, (x*Engine.TILE_SIZE, y*Engine.TILE_SIZE))

    def render_using(self):
        if not self.game.using:
            return

        MAX_USING_LENGTH = self.tile_buffer.width - 2
        item_name = str(self.game.using)
        if len(item_name) > MAX_USING_LENGTH:
            item_name = item_name[:MAX_USING_LENGTH] + "..."

        color = (0, 255, 0) if self.game.using.can_use_on(self.game, self.game.player, self.game.scene.selected) else (255, 0, 0)
        self.screen.blit(self.font.render(f"{item_name}", 1, color), (0, (Engine.BUFFER_SIZE[1]-1)*Engine.TILE_SIZE))
        num_txt = str(self.game.using.quantity) if self.game.using.consumable else ""
        num_txt = self.font.render(num_txt, 1, (245, 217, 76))
        self.screen.blit(num_txt, (Engine.TILE_SIZE*(Engine.BUFFER_SIZE[0]) - num_txt.get_width(), (Engine.BUFFER_SIZE[1]-1)*Engine.TILE_SIZE))

    def render_character(self, character, buffer_x, buffer_y):
        asset_name = core.Pixie.ASSET_NAMES[character.pixie.state]
        asset = self.assets.characters[character.name][asset_name]
        self.screen.blit(asset, (buffer_x*Engine.TILE_SIZE, buffer_y*Engine.TILE_SIZE))

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

    def render_menu_title(self, title):
        txt = self.font.render(title, 1, (255, 255, 255))
        self.screen.blit(txt, self.center(txt, height=False))

    def render_inventory(self):
        self.render_menu_title("~Pack~")
        num_displayable_items = self.tile_buffer.height - 2
        items = self.game.player.inventory[self.game.scene.selected_item_index:self.game.scene.selected_item_index+num_displayable_items]
        for i, item in enumerate(items):
            x = 0
            y = (i+1)*Engine.TILE_SIZE
            txt = self.font.render(str(item), 1, (255, 255, 255))
            if i == 0:
                x = Engine.TILE_SIZE
                self.screen.blit(self.font.render(">", 1, (255, 255, 255)), (0, y))
                self.wigglezoom(txt, (x, y), rspeed=0.0, zspeed=8, zscale=0.05)
            else:
                self.screen.blit(txt, (x, y))
        self.render_using()

    def render_right_menu_slide_prompt(self):
        right_arrow = self.font.render(">", 1, (255, 255, 255))
        self.wigglezoom(right_arrow, (Engine.TILE_SIZE*(Engine.BUFFER_SIZE[0]-2), 0), rspeed=0.0, zspeed=8, zscale=0.1)

    def render_left_menu_slide_prompt(self):
        left_arrow = self.font.render("<", 1, (255, 255, 255))
        self.wigglezoom(left_arrow, (Engine.TILE_SIZE, 0), rspeed=0.0, zspeed=8, zscale=0.1)

    def render_monster(self, monster, pos):
        asset_name = core.Pixie.ASSET_NAMES[monster.pixie.state]
        asset = self.assets.monsters[monster.name][asset_name]
        self.screen.blit(asset, pos)

    def render_monster_stats(self):
        monster = self.game.scene.monster
        self.render_menu_title(str(monster))
        self.render_right_menu_slide_prompt()
        self.screen.blit(self.font.render("HP: " + str(monster.hp) + "/" + str(monster.stats.hp), 1, (255, 255, 255)), (0, Engine.TILE_SIZE*1))
        self.screen.blit(self.font.render("LVL: " + str(monster.level), 1, (255, 255, 255)), (0, Engine.TILE_SIZE*2))
        x = 0
        for i, stat in enumerate(core.Stats.STATS[1:-2]):
            y = (i+3)*Engine.TILE_SIZE
            num = monster.stats.__dict__[stat.lower()]
            txt = f"{core.Stats.SHORT_STATS[stat]}: {num}"
            txt = self.font.render(txt, 1, (255, 255, 255))
            self.screen.blit(txt, (x, y))

        # draw monster
        self.render_monster(monster, 
            (Engine.TILE_SIZE*(Engine.BUFFER_SIZE[0]//2), Engine.TILE_SIZE*(Engine.BUFFER_SIZE[1]//2)))
        self.render_using()

    def render_monster_moves(self):
        self.render_menu_title(str(self.game.scene.monster))
        #self.render_right_menu_slide_prompt()
        self.render_left_menu_slide_prompt()
        x = 0
        for i, move in enumerate(self.game.scene.monster.moves):
            y = (i+1)*Engine.TILE_SIZE
            txt = self.font.render(move.name, 1, (255, 255, 255))
            self.screen.blit(txt, (x, y))
        self.render_using()


    def render_party(self):
        self.render_menu_title("~Monsters~")
        for i, monster in enumerate(self.game.player.monsters):
            x = 0
            y = (i+1)*Engine.TILE_SIZE
            txt = self.font.render(str(monster), 1, (255, 255, 255))
            if i == self.game.scene.selected_monster_index:
                x = Engine.TILE_SIZE
                self.screen.blit(self.font.render(">", 1, (255, 255, 255)), (0, y))
                self.wigglezoom(txt, (x, y), rspeed=0.0, zspeed=8, zscale=0.05)
            else:
                self.screen.blit(txt, (x, y))
            self.render_monster(monster, (Engine.TILE_SIZE*(Engine.BUFFER_SIZE[0]-2), y))
        self.render_using()

    def render_main_menu(self):
        txt = self.font.render("Monster Catcher", 1, (255, 255, 255))
        self.screen.blit(txt, (self.screen.get_width()/2 - txt.get_width()/2, Engine.TILE_SIZE*3))
        self.wigglezoom(self.font.render("Press Enter", 1, (255, 255, 255)),
            (self.screen.get_width()/2, Engine.TILE_SIZE*5),
            size=0.7, center=(True, True))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def flip(self):
        pygame.transform.scale(self.screen, self.window_screen.get_size(), self.window_screen)
        pygame.display.flip()
