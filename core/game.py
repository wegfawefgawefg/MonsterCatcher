from os import system, name
from time import sleep

#from character import Player
#from zone import SaladTownZone
#from map import Map
#from cam import Cam

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
        pass
