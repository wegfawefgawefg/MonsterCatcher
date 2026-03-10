from enum import Enum, auto

class Stats:
    class STATS(Enum):
        HP = auto()
        ATTACK = auto()
        DEFENSE = auto()
        SP_ATTACK = auto()
        SP_DEFENSE = auto()
        SPEED = auto()

    class HIDDEN_STATS(Enum):
        XP_CURVE = auto()
        XP_YIELD = auto()

    NAMES = {
        STATS.HP:"HP",
        STATS.ATTACK:"ATTACK",
        STATS.DEFENSE:"DEFENSE",
        STATS.SP_ATTACK:"SP ATTACK",
        STATS.SP_DEFENSE:"SP DEFENSE",
        STATS.SPEED:"SPEED",
        HIDDEN_STATS.XP_CURVE:"XP CURVE",
        HIDDEN_STATS.XP_YIELD:"XP YIELD",
    }

    SHORT_NAMES = {
        STATS.HP:"HP",
        STATS.ATTACK:"ATK",
        STATS.DEFENSE:"DEF",
        STATS.SP_ATTACK:"SP ATK",
        STATS.SP_DEFENSE:"SP DEF",
        STATS.SPEED:"SPD",
        HIDDEN_STATS.XP_CURVE:"XP CURVE",
        HIDDEN_STATS.XP_YIELD:"XP YIELD",
    }

    def __init__(self, hp=5, attack=1, defense=1, sp_attack=1, sp_defense=1, speed=1, xp_curve=10, xp_yield=1):
        self.hp=hp
        self.attack=attack
        self.defense=defense
        self.sp_attack=sp_attack
        self.sp_defense=sp_defense
        self.speed=speed
        self.xp_curve=xp_curve
        self.xp_yield=xp_yield

    def __len__(self):
        return len(Stats.STATS)

    def __getitem__(self, i):
        if 0 <= i < len(Stats.STATS):
            fetching = Stats.STATS(i+1)
            return {
                Stats.STATS.HP:self.hp,
                Stats.STATS.ATTACK:self.attack,
                Stats.STATS.DEFENSE:self.defense,
                Stats.STATS.SP_ATTACK:self.sp_attack,
                Stats.STATS.SP_DEFENSE:self.sp_defense,
                Stats.STATS.SPEED:self.speed,
            }[fetching]

    def get_pairs(self):
        for i in range(len(Stats.STATS)):
            yield (Stats.STATS(i+1), self[i])

if __name__ == "__main__":
    #for stat in Stats.STATS:
    #    print(Stats.NAMES[stat])
    #for i in range(len(Stats.STATS)):
    #    print(Stats.NAMES[Stats.STATS(i+1)])

    stats = Stats()
    for stat, value in stats.get_pairs():
        print(stat, value)