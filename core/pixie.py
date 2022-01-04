import random
from enum import Enum, auto

class Animations(Enum):
    STATIC = auto()
    TWO_STEP = auto()
    THREE_STEP = auto()
    CLOCKWISE = auto()
    COUNTERCLOCKWISE = auto()

class States(Enum):
    STATIC = auto()
    ONE = auto()
    TWO = auto()
    THREE = auto()
    DOWN = auto()
    UP = auto()
    LEFT = auto()
    RIGHT = auto()

class Pixie:
    SEQUENCES = {
        Animations.STATIC: {States.DOWN: States.DOWN},
        Animations.TWO_STEP: {States.ONE: States.TWO, States.TWO: States.ONE},
        Animations.THREE_STEP: {States.ONE: States.TWO, States.TWO: States.THREE, States.THREE: States.ONE},
        Animations.CLOCKWISE: {
            States.DOWN: States.LEFT,
            States.LEFT: States.UP,
            States.UP: States.RIGHT,
            States.RIGHT: States.DOWN,
        },
        Animations.COUNTERCLOCKWISE: {
            States.DOWN: States.RIGHT,
            States.RIGHT: States.UP,
            States.UP: States.LEFT,
            States.LEFT: States.DOWN,
        },
    }

    ASSET_NAMES = {
        States.ONE: "one",
        States.TWO: "two",
        States.THREE: "three",
        States.DOWN: "down",
        States.UP: "up",
        States.LEFT: "left",
        States.RIGHT: "right",
    }

    def __init__(self, animation=None, speed=1000) -> None:
        self.animation = animation
        self.speed = speed
        self.timer = int(random.random() * 1000) if animation else 0
        self.state = random.choice( list(Pixie.SEQUENCES[animation].keys()) ) if animation else States.DOWN

    def step(self, dt):
        if self.animation:
            self.timer -= dt
            if self.timer < 0:
                self.timer += self.speed
                self.state = Pixie.SEQUENCES[self.animation][self.state]
