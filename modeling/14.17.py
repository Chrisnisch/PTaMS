from math import pi, exp, sqrt
from random import random
import plotly.graph_objs as go
import numpy as np
import scipy.stats as stats

# Параметры нормального распределения
mu = 3
sigma = 1

def dens_func(x):
    """ Плотность вероятности нормального распределения """
    return (2*pi)**(-1/2) * exp(- (x - mu)**2 / (2 * sigma**2))

def generate_x():
    """ Генерация СВ Х методом исключения """
    a = 0
    b = 6
    fm = (2 * pi) ** (-1 / 2)
    z1, z2 = random(), random()
    X1, X2 = a + (b - a)*z1, fm*z2
    while X2 >= dens_func(X1):
        z1, z2 = random(), random()
        X1, X2 = a + (b - a) * z1, fm * z2
    return X1

def f1(x):
    c = 0
    for i in range(len(well_details)):
        if well_details[i] < x:
            c += 1
        else:
            break
    return c / len(well_details)

def f2(x):
    c = 0
    for i in range(len(bad_details)):
        if bad_details[i] < x:
            c += 1
        else:
            break
    return c / len(bad_details)

# Моделирование
n = 100000
well_details = []
bad_details = []
a = 1
b = 5

for i in range(n):
    deviation = generate_x()
    if a < deviation < b:
        well_details.append(deviation)
    elif deviation > b:
        bad_details.append(deviation)

well_details.sort()
bad_details.sort()

# Аналитические функции распределения
def analytical_f1(x, a, b, mu, sigma
                  ):
    """Аналитическая функция распределения для годных деталей"""
    return (stats.norm.cdf((x - mu) / sigma) - stats.norm.cdf((a - mu) / sigma)) / \
        (stats.norm.cdf((b - mu) / sigma) - stats.norm.cdf((a - mu) / sigma))


def analytical_f2(x, b, mu, sigma):
    """Аналитическая функция распределения для деталей, подлежащих переделке"""
    return (stats.norm.cdf((x - mu) / sigma) - stats.norm.cdf((b - mu) / sigma)) / \
        (1 - stats.norm.cdf((b - mu) / sigma))

    # Создание графиков


x = np.linspace(0, 6, num=1000)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=[f1(x_i) for x_i in x], mode='lines', name='Моделирование (годные детали)'))
fig1.add_trace(go.Scatter(x=x, y=[analytical_f1(x_i, a, b, mu, sigma) for x_i in x], mode='lines',
                          name='Аналитическое решение (годные детали)', line=dict(dash='dash')))
fig1.update_layout(title='Сравнение моделирования и аналитического решения (годные детали)', xaxis_title='x',
                   yaxis_title='F(x)')
fig1.show()

fig2 = go.Figure()
fig2.add_trace(
    go.Scatter(x=x, y=[f2(x_i) for x_i in x], mode='lines', name='Моделирование (детали подлежащие переделке)'))
fig2.add_trace(go.Scatter(x=x, y=[analytical_f2(x_i, b, mu, sigma) for x_i in x], mode='lines',
                          name='Аналитическое решение (детали подлежащие переделке)', line=dict(dash='dash')))
fig2.update_layout(title='Сравнение моделирования и аналитического решения (детали подлежащие переделке)',
                   xaxis_title='x', yaxis_title='F(x)')
fig2.show()