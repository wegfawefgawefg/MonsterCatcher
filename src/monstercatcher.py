import pygame
from pygame.locals import QUIT

import core
import engine
import maps
from player import Player


FRAME_RATE = 60


def main() -> None:
    pygame.init()
    game = core.Game(engine=engine.Engine)
    game.player = Player()
    game.set_current_map(maps.BigBlank(game))

    clock = pygame.time.Clock()
    running = True
    while game.running and running:
        dt = clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()
        game.step(dt, pressed_keys)
        game.render()

    pygame.quit()


if __name__ == "__main__":
    main()
