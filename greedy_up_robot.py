import math
from operator import attrgetter

from chaser import Chaser


class GreedyUpRobot(Chaser):
    def __init__(self, x, y, fv):
        super().__init__(x, y, fv)
        self._direction = 'up'

    def _try_up(self, chaseables):
        chaseables = [c for c in chaseables if c.y >= self._y and c.x == self._x]
        if not chaseables:
            self._direction = 'down'
            return math.inf, None

        closest = min(chaseables, key=attrgetter('y'))

        delta_y = closest.y - self._y
        time_to_meet = delta_y / (self._fv - closest.v)

        return time_to_meet, closest

    def _try_down(self, chaseables):
        chaseables = [c for c in chaseables if c.x == self._x]
        if not chaseables:
            return math.inf, None

        closest = max(chaseables, key=attrgetter('y'))

        delta_y = self._y - closest.y
        time_to_meet = delta_y / (self._fv + closest.v)

        return time_to_meet, closest

    def calc_t(self, chaseables):
        time_to_meet, closest = math.inf, None

        if self._direction == 'up':
            time_to_meet, closest = self._try_up(chaseables)

        if self._direction == 'down':
            time_to_meet, closest = self._try_down(chaseables)

        return time_to_meet, closest

    def advance(self, t):
        if self._direction == 'up':
            self._y += t * self._fv
        else:
            self._y -= t * self._fv

    def __str__(self):
        return 'GreedyUpRobot'