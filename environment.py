import matplotlib.pyplot as plt
import numpy as np


class Environment:
    def __init__(self, chasers, chaseables):
        self._chasers = chasers
        self._chaseables = chaseables
        self._step = 0
        self._damage = 0
        self._num_steps = len(self._chaseables)

    def __calc_t(self):
        ts, kills = zip(*[chaser.calc_t(self._chaseables) for chaser in self._chasers])
        i = np.argmin(ts)
        return ts[i], kills[i]

    def advance(self):
        t, killed = self.__calc_t()

        self._step += 1
        self._damage += t * len(self._chaseables)

        for chaser in self._chasers:
            chaser.advance(t)
        for chaseable in self._chaseables:
            chaseable.advance(t)

        print(f'step {self._step} \t\t acc damage={round(self._damage,2)} \t\t t={round(t,2)} \t\t killed ' + str(
            killed))
        self._chaseables.remove(killed)

        plt.subplot(1, self._num_steps, self._step)
        plt.ylim(0, 25)

        if self._chaseables:
            X, Y = zip(*[(c.x, c.y) for c in self._chaseables])
            plt.scatter(X, Y, c='red')

        X, Y = zip(*[(c.x, c.y) for c in self._chasers])
        plt.scatter(X, Y, c='blue')

    def is_finished(self):
        return not self._chaseables

    def display(self):
        plt.show()

    def results(self):
        return f'steps: {self._step} \t\t accumulated damage: {round(self._damage, 2)}'
