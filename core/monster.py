class Monster:
    def __init__(self, name, stats, can_learn, learn_set):
        self.name = name
        self.stats = stats
        self.learn_set = learn_set
        self.can_learn = set().update(learn_set.values())
        self.can_learn.update(can_learn)
        self.pixie = None
        