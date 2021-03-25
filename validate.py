import json
import argparse

from colorama import Fore, Back, Style

def print_line():
    print( '-' * 40)

REQUIRED_GAME_KEYS = [
    "title", 
    "sprite_scale",
    "maps",
    "tile_defs",
    "npc_defs",
    "monster_defs",
    "tile_sprite_defs",
    "anim_tile_sprite_defs",
    "sprite_defs",
    "sprite_set_defs",
    "anim_sprite_set_defs",
]

REQUIRED_MAP_KEYS = [
    "title", 
    "sprite_scale",
    "maps",
    "tile_defs",
    "npc_defs",
    "monster_defs",
    "tile_sprite_defs",
    "anim_tile_sprite_defs",
    "sprite_defs",
    "sprite_set_defs",
    "anim_sprite_set_defs",
]

def validate_game(game):
    game_level_errors = []
    for key in REQUIRED_GAME_KEYS:
        if key not in game:
            game_level_errors.append(f"no {key}")
    
    map_level_errors = {}
    for map in game["maps"]:
        map_level_errors[map] = []
        for key in REQUIRED_MAP_KEYS:
            if key not in map:
                map_level_errors[map].append(f"no {key}")

def main(args):
    with open(args.filename, "r") as f:
        game = json.load(f)

    validate_game(game)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the game json filename/location")
    args = parser.parse_args()
    main(args)