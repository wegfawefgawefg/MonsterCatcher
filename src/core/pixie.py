import random
from enum import Enum, auto

class Animations(Enum):
    STATIC = auto()
    TWO_STEP = auto()
    THREE_STEP = auto()
    CLOCKWISE = auto()
    COUNTERCLOCKWISE = auto()
    WALKING_RIGHT = auto()
    WALKING_LEFT = auto()
    WALKING_UP = auto()
    WALKING_DOWN = auto()

class States(Enum):
    STATIC = auto()
    ONE = auto()
    TWO = auto()
    THREE = auto()
    DOWN = auto()
    UP = auto()
    LEFT = auto()
    RIGHT = auto()
    UP_TWO = auto()
    DOWN_TWO = auto()
    LEFT_TWO = auto()
    RIGHT_TWO = auto()

class Pixie:
    SIZE_LIMIT = 3
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
        Animations.WALKING_RIGHT: {
            States.RIGHT: States.RIGHT_TWO,
            States.RIGHT_TWO: States.RIGHT,
        },
        Animations.WALKING_LEFT: {
            States.LEFT: States.LEFT_TWO,
            States.LEFT_TWO: States.LEFT,
        },
        Animations.WALKING_UP: {
            States.UP: States.UP_TWO,
            States.UP_TWO: States.UP,
        },
        Animations.WALKING_DOWN: {
            States.DOWN: States.DOWN_TWO,
            States.DOWN_TWO: States.DOWN,
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
        States.UP_TWO: "up_two",
        States.DOWN_TWO: "down_two",
        States.LEFT_TWO: "left_two",
        States.RIGHT_TWO: "right_two",
    }

    def __init__(self, animation=None, speed=1000, size=(1.0, 1.0)) -> None:
        self.size = size
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

    def set_size(self, size):
        '''Takes in a tuple of floats, (width, height)'''
        self.size = (min(max(0.0, size[0]), 3), min(max(0.0, size[1]), 3))