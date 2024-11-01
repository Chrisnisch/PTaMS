import random
import numpy as np


def variation():
    n = random.randint(200, 300)
    p = random.uniform(0.001, 0.01)
    k = random.randint(1, 10)
    return n, p, k


def simulation(nall, n, p, k):
    res = 0
    for i in range(nall):
        commutator = 0
        for j in range(n):
            t = np.random.choice([0, 1], p=[1 - p, p])
            if t:
                commutator += 1
        if commutator == k:
            res += 1
    return res / nall


n, p, k = 300, 0.01, 4
for i in range(5):
    avg = 0
    print(f'Количество абонентов: {n}, Вероятность вызова для каждого абонента: {p}')
    for j in range(5):
        avg += simulation(10000, n, p, k)
    print(f'Вероятность что поступит {k} вызова(-ов): {avg / 5}')
    n, p, k = variation()
