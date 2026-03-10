'''the main game class has a list of active effects, 
it exposes a function to update/check all the effects
the scene is responsible for calling this or not

scene will not call this if you dont want time to pass in that scene
'''

class Effect:
    def __init__(self, game, name, target, duration, unique=False, pixie=None, pos=None):
        self.game = game
        self.name = name
        self.creation_time = self.game.time
        self.duration = duration
        self.unique = unique
        self.target = target
        self.pixie = pixie
        self.pos = pos
        if self.pixie and not self.pos:
            raise Exception("effect must have position if it has a sprite associated with it for rendering")
    
    @property
    def is_active(self):
        return (self.game.time - self.creation_time) < self.duration
    
    def step(self):
        ''' returns True if effect is still active
        returns False otherwise
            may also luckily result in failed effects being removed
        '''
        if self.is_active:
            self.run()
            return True
        else:
            self.finish()
            return False

    def start(self):
        raise NotImplementedError   
    def run(self):
        raise NotImplementedError 
    def finish(self):
        raise NotImplementedError
