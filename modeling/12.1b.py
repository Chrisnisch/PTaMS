from math import pi, exp
import random
import plotly.graph_objs as go
import numpy as np


def dens_func(x):
    """ плотность вероятности нормального распределения """
    return (2*pi)**(-1/2) * exp(- x**2/2)


n = 1000000

""" Генерация СВ Х методом исключения """
X = []
a = -3
b = 3
fm = (2 * pi) ** (-1 / 2)
for i in range(n):
    z1, z2 = random.random(), random.random()
    X1, X2 = a + (b - a)*z1, fm*z2
    while X2 >= dens_func(X1):
        z1, z2 = random.random(), random.random()
        X1, X2 = a + (b - a) * z1, fm * z2
    X.append(X1)

X.sort()  # вариационный ряд

fig = go.Figure(go.Scatter(x=X, y=[dens_func(x_i) for x_i in X]))
fig.show()

""" Построение гистограммы для оценки плотности """
m = 100
main_interval = np.linspace(X[0], X[-1], num=n)

x_m_1 = 0
delta = round(len(main_interval) / m)
x_m = delta
hm_values = []
draw_x = [main_interval[x_m_1]]

for i in range(m):
    interval = main_interval[x_m_1:x_m]
    n_m = 0
    draw_x.append(main_interval[x_m])

    for x in X:
        if interval[0] < x <= interval[-1]:
            n_m += 1
    hm_values.append(n_m / (n * delta))

    x_m_1 = x_m

    if x_m + delta < len(main_interval):
        x_m += delta
    else:
        x_m = n-1

fig = go.Figure(data=[go.Bar(x=draw_x, y=hm_values)])
fig.update_layout(title='Оценка плотности распределения', xaxis_title='x', yaxis_title='φ(x)')
fig.show()

