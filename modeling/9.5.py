import random
import time

import numpy as np


def passengers_choice(train):
    for i in range(12):
        index = random.choice(range(0, 6))
        train[index] += 1


def situation_a(train):
    for i in range(6):
        if train[i] != 2:
            return 0
    return 1


def situation_b(train):
    train.sort()
    if train == [0, 1, 2, 2, 3, 4]:
        return 2
    return 0


def simulation(repeats):
    for i in range(repeats):
        train = [0] * 6
        passengers_choice(train)
        t = situation_a(train)
        if t == 1:
            res.append(t)
        else:
            res.append(situation_b(train))


res = []
avg_a, avg_b = [], []
for i in range(10):
    simulation(1000000)
    avg_a.append(res.count(1) / len(res))
    avg_b.append(res.count(2) / len(res))
    res = []
print(f'Вероятность, что в каждый вагон войдёт по два пассажира {np.mean(avg_a)}\n'
      f'Вероятность, что в один вагон никто не зайдет, в другой вагон зайдет один пассажир и т.д. {np.mean(avg_b)}')

