import time
from os import system, name
from time import sleep

import keyboard 

from character import Character, Player
from zone import Zone 
from map import Map

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
        self.overworld_buffer = OverworldBuffer()

        self.player = Player()

        #   load these from files later
        self.zones = {
            "salad_town": Zone()
        }

        self.current_zone_name = None
        self.current_zone = None
        self.map = None
        self.npcs = None

    def load_zone(self, zone):
        self.current_zone_name = zone
        self.zone = self.zones[self.current_zone_name]
        self.map = Map(self.zone)
        self.npcs = self.zone.get_npcs()

    def render_npcs(self):
        pass

    def render(self):
        if self.mode == "overworld":
            self.map.render(self.player, self.overworld_buffer)
            self.player.render(self.overworld_buffer)
        

            print("OVERWORLD\n")
            print("__________")
            print(self.overworld_buffer)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if __name__ == "__main__":
    game = Game()
    game.load_zone("salad_town")

    while True:
        clear()
        game.render()
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



