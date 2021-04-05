from engine import Engine
import time
from os import system, name
from time import sleep

import keyboard 

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
        self.render_mode = "char"
        self.mode = "overworld"

        self.player = Player()

        #   load these from files later
        self.zones = {
            "salad_town": SaladTownZone()
        }

        self.current_zone_name = None
        self.current_zone = None
        self.map = None
        self.npcs = None

    def load_zone(self, zone_name):
        self.current_zone_name = zone_name
        self.zone = self.zones[self.current_zone_name]
        self.map = Map(self.zone)
        self.npcs = self.zone.npcs

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if __name__ == "__main__":
    PLAYER_OFFSET_x = 4
    PLAYER_OFFSET_Y = 4

    overworld_buffer = OverworldBuffer()
    engine = Engine()
    game = Game()
    game.load_zone("salad_town")
    cam = Cam(width=overworld_buffer.width, height=overworld_buffer.height)

    while True:
        cam.set_pos(game.player.x - PLAYER_OFFSET_x, game.player.y - PLAYER_OFFSET_Y)

        clear()
        engine.render(game, cam, overworld_buffer)
        if keyboard.read_key() == "w":
            game.player.move_up(game.map, game.npcs)
        elif keyboard.read_key() == "a":
            game.player.move_left(game.map, game.npcs)
        elif keyboard.read_key() == "s":
            game.player.move_down(game.map, game.npcs)
        elif keyboard.read_key() == "d":
            game.player.move_right(game.map, game.npcs)
        print(f"player: {game.player.x} {game.player.y}")
        time.sleep(0.1)



