from dp_robot import DPRobot
from environment import Environment
from vertical_same_locust import VerticalSameVLocust
from random import randint, uniform, seed
from greedy_up_robot import GreedyUpRobot
from greedy_down_robot import GreedyDownRobot
from greedy_close_robot import GreedyCloseRobot


def simulate(chasers, chaseables):
    env = Environment(chasers, chaseables)

    while not env.is_finished():
        env.advance()

    env.display()
    print(env.results())


if __name__ == '__main__':
    v = 1
    fv = 2
    a, b = 0, 10
    sd = randint(0,100)
    num_robots = 1
    num_locust = 5

    seed(sd)
    chasers = [GreedyUpRobot(x=1, y=4, fv=fv) for i in range(num_robots)]
    chaseables = [VerticalSameVLocust(x=1, y=randint(a, b), v=v) for i in range(num_locust)]
    print(f'*** running {str(chasers[0])} ***')
    simulate(chasers, chaseables)

    seed(sd)
    chasers = [GreedyDownRobot(x=1, y=4, fv=fv) for i in range(num_robots)]
    chaseables = [VerticalSameVLocust(x=1, y=randint(a, b), v=v) for i in range(num_locust)]
    print(f'*** running {str(chasers[0])} ***')
    simulate(chasers, chaseables)

    seed(sd)
    chasers = [GreedyCloseRobot(x=1, y=4, fv=fv) for i in range(num_robots)]
    chaseables = [VerticalSameVLocust(x=1, y=randint(a, b), v=v) for i in range(num_locust)]
    print(f'*** running {str(chasers[0])} ***')
    simulate(chasers, chaseables)

    seed(sd)
    chasers = [DPRobot(x=1, y=4, fv=fv) for i in range(num_robots)]
    chaseables = [VerticalSameVLocust(x=1, y=randint(a, b), v=v) for i in range(num_locust)]
    print(f'*** running {str(chasers[0])} ***')
    simulate(chasers, chaseables)