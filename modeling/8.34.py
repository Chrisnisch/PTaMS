import random

import numpy as np


def standard_probs():
    return [[0.1, 0.2, 0.3], [0.25, 0.6, 0.9]]


def theory(probs):
    return probs[1][0]*(probs[0][0]*(1 - probs[0][1])*(1 - probs[0][2]) +
                        (1 - probs[0][0])*probs[0][1]*(1 - probs[0][2]) +
                        (1 - probs[0][0])*(1 - probs[0][1])*probs[0][2]) \
        + probs[1][1]*(probs[0][0]*probs[0][1]*(1 - probs[0][2]) + probs[0][0]*(1 - probs[0][1])*probs[0][2]
                       + (1 - probs[0][0])*probs[0][1]*probs[0][2]) \
        + probs[1][2]*probs[0][0]*probs[0][1]*probs[0][2]


def randomize_probs():
    probs = []
    for i in range(2):
        x = []
        for j in range(3):
            x.append(round(random.uniform(0.1, 0.91), 2))
        probs.append(x)
    return probs


def create_model():
    device = [1, 1, 1]  # все лампы работают
    probs = randomize_probs()
    for i in range(3):
        print(f'Вероятность выхода из строя {i + 1} лампы {probs[0][i]}')
    for i in range(3):
        print(f'Вероятность выхода из строя прибора если вышли из строя {i+1} ламп {probs[1][i]}')
    print(f'В теории вероятность {theory(probs)}')
    return device, probs


def simulation(repeats):
    device, probs = create_model()
    statuses = []
    for _ in range(repeats):
        device[0] = np.random.choice([0, 1], p=[probs[0][0], 1 - probs[0][0]])
        device[1] = np.random.choice([0, 1], p=[probs[0][1], 1 - probs[0][1]])
        device[2] = np.random.choice([0, 1], p=[probs[0][2], 1 - probs[0][2]])

        if device.count(0) == 1:
            status = np.random.choice([0, 1], p=[probs[1][0], 1 - probs[1][0]])
        elif device.count(0) == 2:
            status = np.random.choice([0, 1], p=[probs[1][1], 1 - probs[1][1]])
        elif device.count(0) == 3:
            status = np.random.choice([0, 1], p=[probs[1][2], 1 - probs[1][2]])
        else:
            status = 1
        statuses.append(status)
        device = [1, 1, 1]
    # return statuses.count(0) / len(statuses)
    print(f'Вероятность в результате моделирования {statuses.count(0) / len(statuses)}')


for i in range(5):
    simulation(500000)


