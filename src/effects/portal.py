import random

from core import Effect, Pixie

class Portal(Effect):
    def __init__(self, game, target, duration, color, pos, portal_gun):
        self.delay = 2 if color == "blue" else 1
        self.color = color
        self.portal_gun = portal_gun
        super().__init__(game, f"{self.color}_portal", target, duration, pixie=Pixie(), pos=pos)
    
    def start(self):
        print(f"{self.target} created a {self.color} portal!")
    def run(self):
        characters = self.game.npcs + [self.game.player]
        for character in characters:
            if self.portal_gun.warp_on_cooldown(self.game.time):
                return
            target_color = self.portal_gun.NEXT_PORTAL[self.color]
            if not self.portal_gun.portals[target_color]:
                return
            elif character.x == self.pos[0] and character.y == self.pos[1]:
                target_portal = self.portal_gun.portals[target_color]
                target_portal_pos = target_portal.pos
                #print(f"warping from {self.color} on {self.pos} to {target_portal.color} at {target_portal_pos}")
                character.move(self.game, target_portal_pos[0], target_portal_pos[1])
                self.portal_gun.last_warped_time = self.game.time
    def finish(self):
        print(f"The effects of {self.name} on {self.target.name} have ended.")
