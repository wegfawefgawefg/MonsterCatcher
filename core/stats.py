class Stats:
    STATS = ["HP", "ATTACK", "DEFENSE", "SP_ATTACK", "SP_DEFENSE", "SPEED", "XP_CURVE", "XP_YIELD"]
    SHORT_STATS = {"HP": "HP", "ATTACK": "ATK", "DEFENSE": "DEF", "SP_ATTACK": "SPATK", "SP_DEFENSE": "SPDEF", "SPEED": "SPD", "XP_CURVE": "GROW", "XP_YIELD": "XPY"}
    def __init__(self, hp=5, attack=1, defense=1, sp_attack=1, sp_defense=1, speed=1, xp_curve=10, xp_yield=1):
        self.hp=hp
        self.attack=attack
        self.defense=defense
        self.sp_attack=sp_attack
        self.sp_defense=sp_defense
        self.speed=speed
        self.xp_curve=xp_curve
        self.xp_yield=xp_yield