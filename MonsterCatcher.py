import time
from os import system, name
import pygame # just for controls

import core
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
    PLAYER_OFFSET_X = 4
    PLAYER_OFFSET_Y = 4
    
    pygame.init()

    game = core.Game()
    engine = core.Engine(game)
    #game.add_map(maps.SaladTown())
    #game.set_current_map("salad_town")
    game.add_map(maps.BigBlank())
    game.set_current_map("big_blank")

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False

        pressed_keys =  pygame.key.get_pressed()
        game.handle_inputs(pressed_keys, dt)
            
        engine.cam.set_pos(game.player.x - PLAYER_OFFSET_X, game.player.y - PLAYER_OFFSET_Y)
        game.step(dt)
        engine.render(game)
        
        #print(f"cam: {cam.rect.x} {cam.rect.y}")
        #print(f"player: {game.player.x} {game.player.y}")
        

    pygame.quit()

