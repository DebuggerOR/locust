# import math
#
# from chaser import Chaser
#
#
# class DPRobot(Chaser):
#     def __init__(self, x, y, fv, r=0):
#         super().__init__(x, y, fv, r)
#         self._T = None
#         self._cur_state = None
#
#     def _create_table(self, chaseables):
#         above = sorted([c for c in chaseables if c.y >= self._y], key=lambda c:c.y)
#         beyond = sorted([c for c in chaseables if c.y < self._y], reverse=True, key=lambda c:c.y)
#
#         self._T = {c1:{c2:None for c2 in chaseables} for c1 in chaseables}
#         self._T[above[0]][beyond[0]] = self._T[beyond[0]][above[0]] = 0
#
#         for i in range(1,len(above)):
#             for j in range(1,len(beyond)):
#                 # should be dynamic values
#                 lowest = beyond[-1].y
#                 highest = above[-1].y
#                 t = 1
#
#                 cur_damage = ((highest - lowest) - (above[i] - beyond[j])) * t
#
#                 self._T[above[i]][beyond[j]] = min(self._T[above[i-1]][beyond[j]] + cur_damage,
#                                                    self._T[above[i]][beyond[j-1]] + cur_damage)
#
#         for i in range(1, len(beyond)):
#             for j in range(1, len(above)):
#                 # should be dynamic values
#                 lowest = beyond[-1].y
#                 highest = above[-1].y
#                 t = 1
#
#                 cur_damage = ((highest - lowest) - (above[j] - beyond[i])) * t
#
#                 self._T[beyond[i]][above[j]] = min(self._T[beyond[i - 1]][above[j]] + cur_damage,
#                                                    self._T[beyond[i]][above[j - 1]] + cur_damage)
#
#     def calc_t(self, chaseables):
#         if not self._T:
#             self._create_table(chaseables)
#             self._cur_state =
#
#
#
#         return time_to_meet, closest
#
#     def advance(self, t):
#         if self._state.state == 'up':
#             self._y += t * self._fv
#         else:
#             self._y -= t * self._fv
#
#     def __str__(self):
#         return 'DPRobot'
