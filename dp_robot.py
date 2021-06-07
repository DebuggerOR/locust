import math

from chaser import Chaser
from chaseable import Chaseable


class DPRobot(Chaser):
    def __init__(self, x, y, fv, r=0):
        super().__init__(x, y, fv, r)
        self._T = None
        self._cur_state = Chaseable(x,y)
        self._direction = 'up'

    def _create_table(self, chaseables):
        X = sorted([c for c in chaseables if c.y >= self._y], key=lambda c:c.y)
        Y = sorted([c for c in chaseables if c.y < self._y], reverse=True, key=lambda c:c.y)

        X = [self._cur_state] + X
        Y = [self._cur_state] + Y

        T = {c1: {c2: {'t': 0, 'damage': 0, 'kill': None} for c2 in X+Y} for c1 in X+Y}

        # state[i,j] means that the area between l_i and l_j is clear and the robot located at l_i's place
        # t is the time of the last chase, damage is the accumulated damage and kill is the current chased locust
        # self._T[X[0]] = {Y[0]: {'t': 0, 'damage': 0, 'kill': None}}
        # self._T[Y[0]] = {X[0]: {'t': 0, 'damage': 0, 'kill': None}}


        for i in range(1,len(X)):
            for j in range(1,len(Y)):
                # robot located in x_i
                num_living_locust = len(chaseables) + 2 - (i + j)

                time_reaching_from_x = self._time_to_meet(X[i-1],X[i])
                time_reaching_from_y = self._time_to_meet(Y[j],X[i])

                damage_reaching_from_x = T[X[i-1]][Y[j]]['damage'] + num_living_locust * time_reaching_from_x
                damage_reaching_from_y = T[Y[j]][X[i-1]]['damage'] + num_living_locust * time_reaching_from_y

                if damage_reaching_from_x < damage_reaching_from_y:
                    T[X[i]][Y[j]] = {'t': time_reaching_from_x, 'damage': damage_reaching_from_x, 'kill': X[i]}
                else:
                    T[X[i]][Y[j]] = {'t': time_reaching_from_y, 'damage': damage_reaching_from_y, 'kill': X[i]}

                # robot located in y_j
                time_reaching_from_x = self._time_to_meet(X[i], Y[j])
                time_reaching_from_y = self._time_to_meet(Y[j-1], Y[j])

                damage_reaching_from_x = T[X[i]][Y[j-1]]['damage'] + num_living_locust * time_reaching_from_x
                damage_reaching_from_y = T[Y[j-1]][X[i]]['damage'] + num_living_locust * time_reaching_from_y

                if damage_reaching_from_x < damage_reaching_from_y:
                    T[Y[j]][X[i]] = {'t': time_reaching_from_x, 'damage': damage_reaching_from_x, 'kill': Y[j]}
                else:
                    T[Y[j]][X[i]] = {'t': time_reaching_from_y, 'damage': damage_reaching_from_y, 'kill': Y[j]}

        self._T = T

    def _time_to_meet(self, source, target):
        if source.y < target.y:
            delta_y = target.y - source.y
            time_to_meet = delta_y / (self._fv + target.v)
        else:
            delta_y = source.y - target.y
            time_to_meet = delta_y / (self._fv - target.v)

        return time_to_meet


    def calc_t(self, chaseables):
        if not self._T:
            self._create_table(chaseables)
        print(self._T[self._cur_state])
        t,k = self._T[self._cur_state]['t'],self._T[self._cur_state]['kill']

        if k.y >= self._y:
            self._direction = 'up'
        else:
            self._direction = 'down'

        return t,k

    def advance(self, t):
        if self._direction == 'up':
            self._y += t * self._fv
        else:
            self._y -= t * self._fv

    def __str__(self):
        return 'DPRobot'
