import core
import effects

class PortalGun(core.Item):
    NEXT_PORTAL = {
        "blue": "orange",
        "orange": "blue"
    }
    WARP_COOLDOWN = 2
    def __init__(self) -> None:
        self.next_portal = "blue"
        self.portals = {
            "blue": None,
            "orange": None
        }
        self.last_warped_time = 0
        super().__init__(name="portal gun", description="create portals", value=1_000_000_000, consumable=False)

    # add infinte durations

    def warp_on_cooldown(self, now):
        return now - self.last_warped_time < PortalGun.WARP_COOLDOWN

    def use(self, game, user, target):
        if self.can_use_on(game, user, target):
            if self.portals[self.next_portal]:
                self.portals[self.next_portal].duration = 0
            self.portals[self.next_portal] = effects.Portal(game, user, duration=9999999, 
                color=self.next_portal,
                pos=(game.player.x, game.player.y),
                portal_gun=self)
            game.register_effect(self.portals[self.next_portal])
            self.announce_use(user, target)
            self.next_portal = PortalGun.NEXT_PORTAL[self.next_portal]

    def can_use_on(self, game, user, target):
        return user == game.player and target == game.player

    def announce_use(self, user, target):
        print(f"{self.next_portal} portal set")
