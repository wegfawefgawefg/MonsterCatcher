from engine import Engine
import time
from os import system, name
from time import sleep

#import keyboard 
import pygame

from character import Player
from zone import SaladTownZone
from map import Map
from cam import Cam

class OverworldBuffer:
    def __init__(self) -> None:
        self.height = 9
        self.width = 10
        self.buffer = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(" ")
            self.buffer.append(row)
        print(f"overworld_dims {len(self.buffer)} {len(self.buffer[0])}")

    def __repr__(self):
        row_strings = []
        for row in self.buffer:
            row_string = "".join(row) + "\n"
            row_strings.append(row_string)
        string_overworld = "".join([row_string for row_string in row_strings])
        return string_overworld

class Game:
    def __init__(self) -> None:
        self.pixies = {}
        self.monsters = {}
        self.render_mode = "char"
        self.mode = "overworld"

        self.player = Player()
        #self.party = Party()

        #   load these from files later
        self.zones = {
            "salad_town": SaladTownZone()
        }

        self.current_zone_name = None
        self.current_zone = None
        self.map = None
        self.npcs = None

    def set_current_zone(self, zone_name):
        self.current_zone_name = zone_name
        self.zone = self.zones[self.current_zone_name]
        self.map = Map(self.zone)
        self.npcs = self.zone.npcs

    def step(self, dt):
        for npc in self.npcs:
            npc.step(dt)

    def load_pixies(self):
        

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def millis():
    return time.time() * 1000

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def handle_inputs(game, pressed_keys):
    if pressed_keys[K_UP]:
        game.player.move_up(game.map, game.npcs)
    if pressed_keys[K_DOWN]:
        game.player.move_down(game.map, game.npcs)
    if pressed_keys[K_LEFT]:
        game.player.move_left(game.map, game.npcs)
    if pressed_keys[K_RIGHT]:
        game.player.move_right(game.map, game.npcs)

if __name__ == "__main__":
    PLAYER_OFFSET_X = 4
    PLAYER_OFFSET_Y = 4

    overworld_buffer = OverworldBuffer()
    engine = Engine()
    game = Game()
    game.load_pixies()
    game.load_moves()
    game.load_monsters()
    game.load_zones()
    game.set_current_zone("salad_town")
    clock = pygame.time.Clock()
    cam = Cam(width=overworld_buffer.width, height=overworld_buffer.height)

    FRAME_RATE = 60
    SCREEN_WIDTH, SCREEN_HEIGHT = 50, 50

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        dt = clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pressed_keys =  pygame.key.get_pressed()
        handle_inputs(game, pressed_keys)
            
        clear()
        cam.set_pos(game.player.x - PLAYER_OFFSET_X, game.player.y - PLAYER_OFFSET_Y)
        game.step(dt)
        engine.render(game, cam, overworld_buffer)
        pygame.display.flip()
        #print(f"cam: {cam.rect.x} {cam.rect.y}")
        #print(f"player: {game.player.x} {game.player.y}")
        

    pygame.quit()

