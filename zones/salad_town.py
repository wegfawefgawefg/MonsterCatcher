from zone import Zone
import tiles
import monsters
from character import Character

class SaladTownZone(Zone):
    def __init__(self) -> None:
        tile_grid = [
            ["rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", ],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "rock"],
            ["rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", ],
        ]
        width = len(tile_grid[0])
        height = len(tile_grid)

        npcs = []
        for i in range(5):
            npcs.append(GreeterNPC(i+1, i+2))
            npcs.append(CCGreeterNPC(i+2, i+2))

        super().__init__(width, height, tile_grid, npcs)

class GreeterNPC(Character):
    def __init__(self, x, y) -> None:
        x, y = x, y
        motion = Motion("rotating", direction="clockwise")
        pixie_name = "greeter"
        super().__init__(x, y, motion)

class CCGreeterNPC(Character):
    def __init__(self, x, y) -> None:
        x, y = x, y
        motion = Motion("rotating", direction="counterclockwise")
        pixie_name = "greeter"
        super().__init__(x, y, motion)