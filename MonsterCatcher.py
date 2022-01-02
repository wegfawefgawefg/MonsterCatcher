import time
from os import system, name
import pygame # just for controls

import core
from player import Player
import maps
import tiles

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def millis():
    return time.time() * 1000

from pygame.locals import (
    K_q,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

FRAME_RATE = 60

if __name__ == "__main__":
    pygame.init()
    game = core.Game(engine=core.Engine())
    game.player = Player()
    game.add_map(maps.BigBlank())
    game.set_current_map("big_blank")

    clock = pygame.time.Clock()
    while game.running:
        dt = clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    game.quit()
            elif event.type == QUIT:
                game.quit()

        pressed_keys = pygame.key.get_pressed()
        game.step(dt, pressed_keys)
        game.render()
        
    pygame.quit()

