from enum import Enum, auto

class BattleTargets(Enum):
    SELF = auto()
    OPPONENT = auto()
    SELF_AND_OPPONENT = auto()

class Move:
    def __init__(self, name, pp, power, accuracy, target):
        self.name = name
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.target = target

    def get_targets(self, game, battle, user):
        if self.target == BattleTargets.SELF:
            return [user]
        elif self.target == BattleTargets.OPPONENT:
            return [battle.opponent]
        elif self.target == BattleTargets.SELF_AND_OPPONENT:
            return [user, battle.opponent]
        elif self.target == BattleTargets.PLAYER:
            return [game.player]
        elif self.target == BattleTargets.ENEMY_PLAYER:
            return [battle.opponent.player]
        elif self.target == BattleTargets.BOTH_PLAYERS:
            return [game.player, battle.opponent.player]
        elif self.target == BattleTargets.ALL:
            return [user, battle.opponent, game.player, battle.opponent.player]
        else:
            raise Exception("Unknown target: " + self.target)

    def use_in_battle(self, user, target):
        raise NotImplementedError

    def use(self, user, target):
        raise NotImplementedError

class DoNothing(Move):
    def __init__(self):
        super().__init__(
            name="do nothing",
            pp=0,
            power=0,
            accuracy=1,
            target=BattleTargets.SELF
        )

    def use_in_battle(self, game, user, target):
        self.game.scene.announce(f"{user.name} did nothing.")
    
    def use(self, user, target):
        pass
