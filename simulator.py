from environment import Environment
from vertical_locust import VerticalSameVLocust
from random import randint, uniform, seed
from vertical_robot import GreedyUpRobot, GreedyDownRobot, GreedyRobot, DPRobot
from chaser import State


def simulate(chasers, chaseables):
    env = Environment(chasers, chaseables)

    env.display()
    while not env.is_finished():
        env.advance()

    print(env.results())


if __name__ == '__main__':
    v = 1
    fv = 2
    a, b = 0, 10
    sd = randint(0,100)
    num_robots = num_locust = 5

    print('*** running GreedyUpRobot ***')
    seed(sd)
    state = State('up')
    chasers = [GreedyUpRobot(x=i, y=4, fv=fv, r=0, state=state) for i in range(num_robots)]
    chaseables = [VerticalSameVLocust(x=i, y=randint(a, b), v=v) for i in range(num_locust)]
    simulate(chasers, chaseables)

    print('*** running GreedyDownRobot ***')
    seed(sd)
    state = State('down')
    chasers = [GreedyDownRobot(x=i, y=4, fv=fv, r=0, state=state) for i in range(num_robots)]
    chaseables = [VerticalSameVLocust(x=i, y=randint(a, b), v=v) for i in range(num_locust)]
    simulate(chasers, chaseables)

    print('*** running GreedyRobot ***')
    seed(sd)
    state = State({i: 'up' for i in range(num_robots)})
    chasers = [GreedyRobot(x=i, y=4, fv=fv, r=0, state=state) for i in range(num_robots)]
    chaseables = [VerticalSameVLocust(x=i, y=randint(a, b), v=v) for i in range(num_locust)]
    simulate(chasers, chaseables)

    # print('*** running DPRobot ***')
    # seed(sd)
    # state = State({i: 'up' for i in range(num_robots)})
    # chasers = [DPRobot(x=i, y=4, fv=fv, r=0, state=state) for i in range(num_robots)]
    # chaseables = [VerticalSameVLocust(x=i, y=randint(a, b), v=v) for i in range(num_locust)]
    # simulate(chasers, chaseables)