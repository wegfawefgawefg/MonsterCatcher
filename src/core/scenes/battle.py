from enum import Enum, auto

from pygame.constants import K_0
from pygame.locals import (
    K_RIGHT,
    K_LEFT,
    K_DOWN,
    K_UP,
    K_i,
    K_t,
    K_e,
    K_p,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
)

from core import Stats, BattleTargets
from .scene import Scene

class Battle(Scene):
    class States(Enum):
        CHOOSING_ATTACK = auto()
        CHOOSING_TARGET = auto()
        ANIMATING_OPPONENT_ATTACK = auto()
        ANIMATING_PLAYER_ATTACK = auto()
        ANIMATING_OPPONENT_DAMAGE = auto()
        ANIMATING_PLAYER_DAMAGE = auto()
        ANIMATING_OPPONENT_FLEE = auto()
        ANIMATING_PLAYER_FLEE = auto()
        ANIMATING_EFFECTS = auto()
        ANIMATING_BATTLE_EFFECTS = auto()

    def __init__(self, game, parent_scene, opponent):
        commands = {
            K_RIGHT:self.right,
            K_LEFT:self.left,
            K_UP:self.up,
            K_DOWN:self.down,
            K_1: self.use_move_one,
            K_2: self.use_move_two,
            K_3: self.use_move_three,
            K_4: self.use_move_four,
            K_5: self.choose_next_target,
            K_i:self.view_inventory,
            K_p:self.view_party,
            K_e:self.step_txt,
            K_t:self.use_item,
        }
        super().__init__(game, commands, parent_scene)
        self.player = self.game.player
        self.opponent = opponent
        self.player_monster = self.player.monsters[0]
        self.opponent_monster = opponent.monsters[0]
        self.turn = 0
        self.state = Battle.States.CHOOSING_ATTACK

        self.selected_move = None
        self.next_target_override = False
        self.next_target = None

    def render(self):
        if self.state == Battle.States.CHOOSING_ATTACK:
            self.game.engine.render_battle_moves()
        elif self.state == Battle.CHOOSING_TARGET:
            self.game.engine.render_choosing_battle_targets()

    def announce(self, msg):
        print(msg)

    @property
    def selected(self):
        return self.selected

    def use_useing_on_selected(self):
        if self.selected:
            self.game.use_using(self.game.player, target=self.selected)

    def choose_next_target(self):
        self.state = Battle.States.CHOOSING_TARGET
    def q(self):
        if self.state == Battle.States.CHOOSING_TARGET:
            self.state = Battle.States.CHOOSING_ATTACK
            self.next_target_override = False

    def one(self):
        if self.state == Battle.States.CHOOSING_ATTACK:
            self.use_move(0)
        elif self.state == Battle.States.CHOOSING_TARGET:
            self.next_target = BattleTargets.SELF
            self.next_target_override = True
    def two(self):
        if self.state == Battle.States.CHOOSING_ATTACK:
            self.next_target = BattleTargets.OPPONENT
            self.use_move(1)
    def three(self):
        if self.state == Battle.States.CHOOSING_ATTACK:
            self.next_target = BattleTargets.SELF_AND_OPPONENT
            self.use_move(2)
    def four(self):
        if self.state == Battle.States.CHOOSING_ATTACK:
            self.use_move(3)

    def use_move(self, i):
        if len(self.player_monster.moves) > i:
            self.selected_move = self.player_monster.moves[i]
        else:
            self.selected_move = None
        self.state = Battle.States.CHOOSING_TARGET

    def view_inventory(self):
        from .inventory import Inventory
        self.game.scene = Inventory(self.game, parent_scene=self)
    def view_party(self):
        from .party import Party
        self.game.scene = Party(self.game, parent_scene=self, choose_mode=True)
