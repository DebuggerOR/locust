from abc import ABC


class Chaser(ABC):
    def __init__(self, x, y, fv, r, state=None):
        self._x = x
        self._y = y
        self._fv = fv
        self._r = r
        self._state = state

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def fv(self):
        return self._fv

    @property
    def r(self):
        return self._r

    def advance(self,t):
        pass

    def calc_t(self,chaseables):
        pass

    def __str__(self):
        return f'Chaser({self._x},{self._y})'


class State:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    def set_state(self, state):
        self._state = state
