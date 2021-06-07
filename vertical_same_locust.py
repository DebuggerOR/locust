from chaseable import Chaseable


class VerticalSameVLocust(Chaseable):
    def advance(self, t):
        self._y += t * self._v