from random import uniform, random
from math import pi, exp
import scipy


def dens_func(x, z):
    return 1 / (sigma * (2*pi)**1/2) * exp(- (x - z)**2/(2*sigma**2))


r = 0.5
l = 1
sigma = 1
n = 1000000
a = -3
b = 3
fm = (2 * pi) ** (-1 / 2)
result = []
analytic_result = []
for i in range(n):
    z = uniform(-l, l)
    z1, z2 = random(), random()
    X1, X2 = a + (b - a)*z1, fm*z2
    while X2 >= dens_func(X1, z):
        z1, z2 = random(), random()
        X1, X2 = a + (b - a) * z1, fm * z2
    if abs(X1) > r:
        result.append(1)

print(f'P = {result.count(1) / n}')


def integrand(z):
    return (1 - 1/2 * (scipy.stats.norm.cdf(0.5 - z) + scipy.stats.norm.cdf(-0.5 - z)))**2


p = 1 - 1/2 * (scipy.integrate.quad(integrand, -1, 1))[0]
print(p)