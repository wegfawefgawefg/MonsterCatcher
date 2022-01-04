import time
import math
import os
from pprint import pprint

import pygame 
from pygame.math import Vector2

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
        self.cam = core.Cam(width=Engine.BUFFER_SIZE[0], height=Engine.BUFFER_SIZE[1])
        screen_dims = (Engine.BUFFER_SIZE[0]*Engine.TILE_SIZE, Engine.BUFFER_SIZE[1]*Engine.TILE_SIZE)
        self.screen = pygame.Surface(screen_dims)
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

        self.cam_last_position = None
        self.tile_surface = pygame.Surface(screen_dims)

    def render_frame_rate(self):
        fps = self.game.dt/16*60
        color = (255, 255, 255)
        if fps < 60:    # yellow
            color = (255, 255, 0)
        elif fps < 45:  # red
            color = (255, 0, 0)
        txt = self.font.render(str(fps), 1, color)
        self.screen.blit(txt, (0, 0))

    def center(self, surface, width=True, height=True):
        return (
            (self.screen.get_width() - surface.get_width())/2 if width else 0,
            (self.screen.get_height() - surface.get_height())/2 if height else 0)
    def right_align(self, surface):
        return (self.screen.get_width() - surface.get_width(), 0)

    def wigglezoom(self, surf, pos, rspeed=2, rscale=1, zspeed=2, zscale=0.1, size=1, center=(False, False)):
        surf = pygame.transform.rotozoom(surf, 
            math.sin(time.time()*rspeed)*rscale, 
            math.cos(time.time()*zspeed)*zscale+size)
        self.screen.blit(surf, (
            (pos[0] - surf.get_width()/2) if center[0] else pos[0], 
            (pos[1] - surf.get_height()/2) if center[1] else pos[1]))

    #def render_map(self):
    #    for y in range(Engine.BUFFER_SIZE[1]):
    #        tile_y = self.cam.rect.y + y
    #        for x in range(Engine.BUFFER_SIZE[0]):
    #            tile_x = self.cam.rect.x + x
    #            if 0 <= tile_x < self.game.map.width and 0 <= tile_y < self.game.map.height:
    #                tile = self.game.map.tiles[int(tile_y)][int(tile_x)]
    #                if tile:
    #                    tile.pixie.step(self.game.dt)
    #                    asset_name = core.Pixie.ASSET_NAMES[tile.pixie.state]
    #                    asset = self.assets.tiles[tile.name][asset_name]
    #                    pos = (x*Engine.TILE_SIZE, y*Engine.TILE_SIZE)
    #                    # factor in camera
    #                    pos = (pos[0] - self.cam.rect.x, pos[1] - self.cam.rect.y)
    #                    self.screen.blit(asset, pos)

    #def render_npcs(self):
    #    for npc in self.game.npcs:
    #        cam_x, cam_y = self.cam.to_cam_space(npc.x, npc.y)
    #        if self.cam.contains_cam_space(cam_x, cam_y):
    #            self.render_character(npc, cam_x, cam_y)

        #for y in range(
        #        int(self.cam.rect.y),
        #        int(self.cam.rect.y + self.cam.rect.height + 1)):
        #    if first:
        #        print(y)
        #        first = False
        #    for x in range(
        #            int(self.cam.rect.x),
        #            int(self.cam.rect.x + self.cam.rect.width + 1)):

    def render_map(self):
        self.tile_surface.fill((0, 0, 0))
        for y in range(-1, self.cam.rect.height+1):
            for x in range(-1, self.cam.rect.width+1):
                world_x = self.cam.rect.x + x + 1.0
                world_y = self.cam.rect.y + y + 1.0
                if 0 <= world_x < self.game.map.width and 0 <= world_y < self.game.map.height:
                    tile = self.game.map.tiles[int(world_y)][int(world_x)]
                    if tile:
                        tile.pixie.step(self.game.dt)
                        asset_name = core.Pixie.ASSET_NAMES[tile.pixie.state]
                        asset = self.assets.tiles[tile.name][asset_name]
                        pos = (x*Engine.TILE_SIZE, y*Engine.TILE_SIZE)
                        self.tile_surface.blit(asset, pos)
        # factor in camera offset
        #pos = (
        #    -self.cam.rect.x*Engine.TILE_SIZE, 
        #    -self.cam.rect.y*Engine.TILE_SIZE)
        pos = (0, 0)
        self.screen.blit(self.tile_surface, pos)

    def render_using(self):
        if not self.game.using:
            return

        MAX_USING_LENGTH = Engine.BUFFER_SIZE[0] - 2
        item_name = str(self.game.using)
        if len(item_name) > MAX_USING_LENGTH:
            item_name = item_name[:MAX_USING_LENGTH] + "..."

        color = (0, 255, 0) if self.game.using.can_use_on(self.game, self.game.player, self.game.scene.selected) else (255, 0, 0)
        self.screen.blit(self.font.render(f"{item_name}", 1, color), (0, (Engine.BUFFER_SIZE[1]-1)*Engine.TILE_SIZE))
        num_txt = str(self.game.using.quantity) if self.game.using.consumable else ""
        num_txt = self.font.render(num_txt, 1, (245, 217, 76))
        self.screen.blit(num_txt, (Engine.TILE_SIZE*(Engine.BUFFER_SIZE[0]) - num_txt.get_width(), (Engine.BUFFER_SIZE[1]-1)*Engine.TILE_SIZE))

    def render_character(self, character, x, y):
        asset_name = core.Pixie.ASSET_NAMES[character.pixie.state]
        asset = self.assets.characters[character.name][asset_name]
        _scale = (Engine.TILE_SIZE, Engine.TILE_SIZE)
        pos = (x*Engine.TILE_SIZE, y*Engine.TILE_SIZE)
        shadow = pygame.transform.rotate(asset, -45) #*math.sin(time.time())
        _shadow_scale = (_scale[0], int(_scale[1]*0.5))
        shadow = pygame.transform.scale(shadow, _shadow_scale)
        shadow.set_alpha(128)
        _shadow_pos = (pos[0], pos[1] + _shadow_scale[1])
        self.screen.blit(shadow, _shadow_pos)

        blit = pygame.transform.scale(asset, _scale)
        self.screen.blit(blit, pos)

        # create shadow
        #shadow = pygame.Surface(blit.get_size())
        #shadow.fill((0, 0, 0))
        #self.screen.blit(shadow, pos)


    def render_player(self):
        cam_x, cam_y = self.cam.to_cam_space(self.game.player.x, self.game.player.y)
        self.render_character(self.game.player, cam_x, cam_y)

    def render_npcs(self):
        for npc in self.game.npcs:
            cam_x, cam_y = self.cam.to_cam_space(npc.x, npc.y)
            if self.cam.contains_cam_space(cam_x, cam_y):
                self.render_character(npc, cam_x, cam_y)

    def render_overworld(self):
        #pos = (
        #    self.game.player.x - self.game.scene.PLAYER_OFFSET_X,
        #    self.game.player.y - self.game.scene.PLAYER_OFFSET_Y
        #)
        pos = (
            self.game.player.x,
            self.game.player.y
        )
        spinning_pos = (
            math.sin(time.time())*0.5,
            math.cos(time.time())*0.5,
        )
        pos = (
            pos[0] \
                + spinning_pos[0],
            pos[1] \
                + spinning_pos[1]
        )
        self.game.engine.cam.set_pos(pos[0], pos[1])
        self.render_map()
        self.render_player()
        self.render_npcs()

    def render_menu_title(self, title):
        txt = self.font.render(title, 1, (255, 255, 255))
        self.screen.blit(txt, self.center(txt, height=False))

    def render_inventory(self):
        self.render_menu_title("~Pack~")
        num_displayable_items = Engine.BUFFER_SIZE[1] - 2
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

    def render_monster(self, monster, pos, scale=(1, 1)):
        asset_name = core.Pixie.ASSET_NAMES[monster.pixie.state]
        asset = self.assets.monsters[monster.name][asset_name]
        _scale = (scale[0]*Engine.TILE_SIZE, scale[1]*Engine.TILE_SIZE)
        blit = pygame.transform.scale(asset, _scale)
        self.screen.blit(blit, pos)

    def render_monster_stats(self):
        monster = self.game.scene.monster
        self.render_menu_title(str(monster))
        self.render_right_menu_slide_prompt()
        txt = self.font.render("LVL: " + str(monster.level), 1, (255, 255, 255))
        pos = (self.right_align(txt)[0], Engine.TILE_SIZE*1)
        self.screen.blit(txt, pos)

        txt = "HP: " + str(monster.hp) + "/" + str(monster.stats.hp)
        txt = self.font.render(txt, 1, (255, 255, 255))
        pos = (self.right_align(txt)[0], Engine.TILE_SIZE*2)
        if self.game.scene.selected == core.Stats.STATS.HP:
            self.wigglezoom(txt, pos, rspeed=0.0, zspeed=8, zscale=0.05)
        else:
            self.screen.blit(txt, pos)

        for i, (stat, value) in enumerate(monster.stats.get_pairs()):
            if i == 0:  #    skip HP
                continue
            x, y = 0, Engine.TILE_SIZE*(i+2)
            txt = core.Stats.SHORT_NAMES[stat] + ": " + str(value)
            if self.game.scene.selected == stat:
                x = Engine.TILE_SIZE
                self.wigglezoom(self.font.render(txt, 1, (255, 255, 255)), (x, y), rspeed=0.0, zspeed=8, zscale=0.05)
            else:
                self.screen.blit(self.font.render(txt, 1, (255, 255, 255)), (x, y))

        # draw monster
        self.render_monster(monster, (0, 0),scale=(3, 3))
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
        self.render_frame_rate()
        blit = pygame.transform.scale(self.screen, self.window_screen.get_size())
        #cam = Vector2(self.cam.x, self.cam.y)
        #if not self.cam_last_position:
        #    self.cam_last_position = Vector2(cam.x, cam.y)
        #diff = cam - self.cam_last_position
        #self.window_screen.blit(blit, (diff.x, diff.y))
        self.window_screen.blit(blit, (0, 0))
        pygame.display.flip()

        #self.cam_last_position = (self.cam_last_position + cam) * 0.01
