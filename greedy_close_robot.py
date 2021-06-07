import math

from chaser import Chaser


class GreedyCloseRobot(Chaser):
    def __init__(self, x, y, fv):
        super().__init__(x, y, fv)
        self._direction = None

    def calc_t(self, chaseables):
        chaseables = [c for c in chaseables if c.x == self._x]

        if not chaseables:
            return math.inf, None

        closest = chaseables[0]
        for chaseable in chaseables:
            if abs(chaseable.y - self._y) < abs(closest.y - self._y):
                closest = chaseable

        if closest.y < self._y:
            self._direction = 'down'
            delta_y = self._y - closest.y
            time_to_meet = delta_y / (self._fv + closest.v)
        else:
            self._direction = 'up'
            delta_y = closest.y - self._y
            time_to_meet = delta_y / (self._fv - closest.v)

        return time_to_meet, closest

    def advance(self, t):
        if self._direction == 'up':
            self._y += t * self._fv
        else:
            self._y -= t * self._fv

    def __str__(self):
        return 'GreedyCloseRobot'