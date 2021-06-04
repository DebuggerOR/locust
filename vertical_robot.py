from chaser import Chaser
from operator import attrgetter
import math


class DPRobot(Chaser):
    def __init__(self, x, y, fv, r, state):
        super().__init__(x, y, fv, r, state)
        self._T = None

    def _create_table(self, chaseables):
        above = sorted([c for c in chaseables if c.y >= self._y], key=lambda c:c.y)
        beyond = sorted([c for c in chaseables if c.y < self._y], reverse=True, key=lambda c:c.y)

        self._T = {c1:{c2:None for c2 in chaseables} for c1 in chaseables}
        self._T[above[0]][beyond[0]] = self._T[beyond[0]][above[0]] = 0

        for i in range(1,len(above)):
            for j in range(1,len(beyond)):
                self._T[above[i]][beyond[j]] = min(self._T[above[i-1]][beyond[j]],
                                                   self._T[above[i]][beyond[j-1]])

        for i in range(1, len(beyond)):
            for j in range(1, len(above)):
                self._T[beyond[i]][above[j]] = min(self._T[beyond[i - 1]][above[j]],
                                                   self._T[beyond[i]][above[j - 1]])

    def calc_t(self, chaseables):
        if not self._T:
            self._create_table(chaseables)

        chaseables = [c for c in chaseables if c.x == self._x]

        if not chaseables:
            return math.inf, None

        closest = chaseables[0]
        for chaseable in chaseables:
            if abs(chaseable.y - self._y) < abs(closest.y - self._y):
                closest = chaseable

        if closest.y < self._y:
            self._state.state[self._x] = 'down'
            delta_y = self._y - closest.y
            time_to_meet = delta_y / (self._fv + closest.v)

            return time_to_meet, closest

        self._state.state[self._x] = 'up'
        delta_y = closest.y - self._y
        time_to_meet = delta_y / (self._fv - closest.v)

        return time_to_meet, closest

    def advance(self, t):
        if self._state.state == 'up':
            self._y += t * self._fv
        else:
            self._y -= t * self._fv


class GreedyUpRobot(Chaser):
    def _try_up(self, chaseables):
        up_chaseables = [c for c in chaseables if c.y >= self._y]
        if not up_chaseables:
            self._state.set_state('down')
            return math.inf, None

        up_cur_chaseables = [c for c in up_chaseables if c.x == self._x]
        if not up_cur_chaseables:
            return math.inf, None

        closest = min(up_cur_chaseables, key=attrgetter('y'))

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

        if self._state.state == 'up':
            time_to_meet, closest = self._try_up(chaseables)

        if self._state.state == 'down':
            time_to_meet, closest = self._try_down(chaseables)

        return time_to_meet, closest

    def advance(self, t):
        if self._state.state == 'up':
            self._y += t * self._fv
        else:
            self._y -= t * self._fv


class GreedyDownRobot(Chaser):
    def _try_up(self, chaseables):
        chaseables = [c for c in chaseables if c.x == self._x]
        if not chaseables:
            return math.inf, None

        closest = min(chaseables, key=attrgetter('y'))

        delta_y = closest.y - self._y
        time_to_meet = delta_y / (self._fv - closest.v)

        return time_to_meet, closest

    def _try_down(self, chaseables):
        down_chaseables = [c for c in chaseables if c.y <= self._y]
        if not down_chaseables:
            self._state.set_state('up')
            return math.inf, None

        down_cur_chaseables = [c for c in down_chaseables if c.x == self._x]
        if not down_cur_chaseables:
            return math.inf, None

        closest = max(down_cur_chaseables, key=attrgetter('y'))

        delta_y = self._y - closest.y
        time_to_meet = delta_y / (self._fv + closest.v)

        return time_to_meet, closest

    def calc_t(self, chaseables):
        time_to_meet, closest = math.inf, None

        if self._state.state == 'down':
            time_to_meet, closest = self._try_down(chaseables)

        if self._state.state == 'up':
            time_to_meet, closest = self._try_up(chaseables)

        return time_to_meet, closest

    def advance(self, t):
        if self._state.state == 'up':
            self._y += t * self._fv
        else:
            self._y -= t * self._fv


class GreedyRobot(Chaser):
    def calc_t(self, chaseables):
        chaseables = [c for c in chaseables if c.x == self._x]

        if not chaseables:
            return math.inf, None

        closest = chaseables[0]
        for chaseable in chaseables:
            if abs(chaseable.y - self._y) < abs(closest.y - self._y):
                closest = chaseable

        if closest.y < self._y:
            self._state.state[self._x] = 'down'
            delta_y = self._y - closest.y
            time_to_meet = delta_y / (self._fv + closest.v)

            return time_to_meet, closest

        self._state.state[self._x] = 'up'
        delta_y = closest.y - self._y
        time_to_meet = delta_y / (self._fv - closest.v)

        return time_to_meet, closest

    def advance(self, t):
        if self._state.state == 'up':
            self._y += t * self._fv
        else:
            self._y -= t * self._fv
