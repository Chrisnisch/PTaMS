import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Параметры гамма-распределения
alpha = 2.0
beta = 1.0

# Генерация выборки из гамма-распределения
gamma_rv = stats.gamma(alpha, scale=1/beta)
sample = gamma_rv.rvs(size=1000)

# Визуализация плотности вероятности
x = np.linspace(0, 10, 1000)
pdf = gamma_rv.pdf(x)

plt.figure(figsize=(8, 5))
plt.hist(sample, bins=30, density=True, alpha=0.6, color='g', label='Гистограмма выборки')
plt.plot(x, pdf, 'r-', lw=2, label='Теоретическая плотность')
plt.title('Гамма-распределение')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.show()
