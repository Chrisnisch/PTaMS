import numpy as np
import scipy

num_samples = 1000000


def len_func(x):
    return np.sqrt(x**2 - 2*x + 2)


lengths = []
for i in range(num_samples):
    AM = np.random.uniform(0, 2)
    lengths.append(len_func(AM))

expected_length = np.mean(lengths)

print(f'Мат. ожидание длины отрезка CM: {expected_length} м')
print(f'Мат. ожидание теоретически: {1/2 * scipy.integrate.quad(len_func, 0, 2)[0]}')
