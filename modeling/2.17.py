from statistics import mean
import numpy as np
from matplotlib import pyplot


def task2a(n):
    return n / (2 * n - 1)


def task2b(n):
    return (n - 1) / (2 * n - 1)


def draw(teams):
    perm = list(np.random.permutation(teams))
    if (perm.index(0) < (len(teams) / 2) and perm.index(1) < (len(teams) / 2)) or \
            (perm.index(0) >= (len(teams) / 2) and perm.index(1) >= (len(teams) / 2)):
        return 1
    elif (perm.index(0) < (len(teams) / 2) <= perm.index(1)) or (perm.index(0) >= (len(teams) / 2) > perm.index(1)):
        return 2


def modeling(sim_num, teams):
    results = []
    for i in range(sim_num):
        results.append(draw(teams))
    return results


if __name__ == '__main__':
    N = []
    fa = []
    fb = []
    for n in range(6, 32, 2):
        number_of_teams = n
        N.append(n)
        print("Число команд: ", number_of_teams, "\nКоманды делятся на 2 подгруппы")
        print("Вероятность, что две наиболее сильные команды окажутся в разных подгруппах "
              "(вычисление по формуле, полученной аналитически):\n", task2a(number_of_teams // 2))
        print("Вероятность, что две наиболее сильные команды окажутся в одной подгруппе "
              "(вычисление по формуле, полученной аналитически):\n", task2b(number_of_teams // 2), "\n")

        print("Моделирование:")
        teams = [x for x in range(0, number_of_teams)]  # за наиболее сильные команды берем 0 и 1
        Nall = 100000
        Pa = []
        Pb = []
        for i in range(20):
            model = modeling(Nall, teams)
            pa = model.count(2) / len(model)
            Pa.append(pa)
            Pb.append(1 - pa)
        print("Вероятность, что две наиболее сильные команды окажутся в разных подгруппах,"
              " вычисленная на основе моделирования:\n", mean(Pa))
        print("Вероятность, что две наиболее сильные команды окажутся в одной подгруппе,"
              " вычисленная на основе моделирования:\n", mean(Pb))
        fa.append(mean(Pa))
        fb.append(mean(Pb))
    pyplot.plot(N, fa)
    pyplot.plot(N, fb)
    pyplot.show()
