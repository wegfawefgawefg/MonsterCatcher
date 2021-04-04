import time
from os import system, name
from time import sleep

import keyboard 

from tiles import GrassTile, RockTile
from character import Character, Player

class Map:
    def __init__(self) -> None:
        self.width = 16
        self.height = 16
        self.tiles = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if (y == 0) or (x == 0) or (y == self.width - 1) or (x == self.height - 1):
                    tile = RockTile()
                else:
                    tile = GrassTile()
                row.append(tile)
            self.tiles.append(row)

    def render(self, player, overworld_buffer):
        x1 = player.x - 4
        y1 = player.y - 4
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = x1 + overworld_buffer.width
        y2 = y1 + overworld_buffer.height
        print(f"{x1} {x2} {y1} {y2}")
        for o_y, y in enumerate(range(y1, y2)):
            for o_x, x in enumerate(range(x1, x2)):
                if 0 <= x < self.width and 0 <= y < self.height:
                    tile = self.tiles[y][x]
                    overworld_buffer.buffer[o_y][o_x] = tile.char
                else:
                    overworld_buffer.buffer[o_y][o_x] = " "

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
        self.map = Map()
        self.render_mode = "char"
        self.mode = "overworld"
        self.overworld_buffer = OverworldBuffer()

        self.player = Player()
        self.npcs = []

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
        


