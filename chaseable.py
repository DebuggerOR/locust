from abc import ABC


class Chaseable(ABC):
    def __init__(self, x, y, v=0):
        self._x = x
        self._y = y
        self._v = v

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def v(self):
        return self._v

    @property
    def advance(self, t):
        pass

    # def __str__(self):
    #     return f'Chaseable({round(self._x,2)},{round(self._y,2)})'

    def __hash__(self):
        return hash(str(self))
