class BattleEffect:
    def __init__(self, game, name, target, duration):
        self.game = game
        self.name = name
        self.duration = duration
        self.target = target
    
    @property
    def is_active(self):
        return (self.game.scene.turn - self.creation_turn) < self.duration
    
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

    def swap_in(self, user, target):
        raise NotImplementedError
    def swap_out(self):
        raise NotImplementedError
    def start(self):
        raise NotImplementedError   
    def run(self):
        raise NotImplementedError 
    def finish(self):
        raise NotImplementedError
