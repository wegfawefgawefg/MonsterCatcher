import time
from os import system, name

import pygame   #   keyboard

import core
import zones
import tiles

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def millis():
    return time.time() * 1000

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

if __name__ == "__main__":
    PLAYER_OFFSET_X = 4
    PLAYER_OFFSET_Y = 4

    overworld_buffer = core.OverworldBuffer()
    engine = core.Engine()
    game = core.Game()
    game.zones["salad_town"] = zones.SaladTown()
    game.set_current_zone("salad_town")
    clock = pygame.time.Clock()
    cam = core.Cam(width=overworld_buffer.width, height=overworld_buffer.height)

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
        game.handle_inputs(pressed_keys)
            
        clear()
        cam.set_pos(game.player.x - PLAYER_OFFSET_X, game.player.y - PLAYER_OFFSET_Y)
        game.step(dt)
        engine.render(game, cam, overworld_buffer)
        pygame.display.flip()
        #print(f"cam: {cam.rect.x} {cam.rect.y}")
        #print(f"player: {game.player.x} {game.player.y}")
        

    pygame.quit()

