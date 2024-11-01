import random


def simulation(n):
    pmm = 0
    pm = 0
    for i in range(n):
        twins = random.choices(['MM', 'FF', 'MF', 'FM'], [0.51 - 1/6, 0.49 - 1/6, 1/6, 1/6])
        if twins[0] == 'MM':
            pmm += 1
            # pm += 1
        if twins[0][0] == 'M':
            pm += 1
    pmm /= n
    pm /= n
    return pmm / pm


print(simulation(10000000))
