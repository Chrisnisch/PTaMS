import numpy as np


def search():
    p = 0.1
    h = 0.1
    while p < 1:
        P = simulation(100000, p)
        if 0.5001 < round(P, 4) < 0.5009:
            return p
        elif P < 0.5:
            p += h
        elif P > 0.5:
            p -= h
            h /= 2
            p += h


def simulation(N, P):
    results = []
    for i in range(N):
        for j in range(4):
            if np.random.choice((1, 0), p=(P, 1 - P)) == 1:
                results.append(1)
                break
        else:
            results.append(0)
    return results.count(1) / len(results)


avg = []
for i in range(5):
    avg.append(search())
print(f"Событие происходит хотя бы в одном из четырёх опытов с вероятностью 0.5 "
                  f"при вероятности произойти в одном опыте равной {np.mean(avg)}")
