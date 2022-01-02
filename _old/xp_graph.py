{"base":10, "speed":2.0, "acc":0.9}

import matplotlib.pyplot as plt

class Curve:
    def __init__(self, base, speed, acc=0.0, jerk=0.0, minimum=0.0, maximum=None):
        self.base = base
        self.speed = speed
        self.acc = acc
        self.jerk = jerk

        self.minimum = minimum
        self.maximum = maximum

    def at(self, x):
        stat = self.base +\
            self.speed * x +\
            self.acc * x**2 +\
            self.jerk * x**3
        stat = max(stat, self.minimum)
        if self.maximum:
            stat = min(stat, self.maximum)
        return stat

linear = Curve(10, 5, maximum=50)
charmander = Curve(-140, 15.0, 15.0)
graphed = linear
ys = []
for i in range(0, 101):
    y = graphed.at_level(i)
    ys.append(y)

plt.plot(ys)
plt.show()