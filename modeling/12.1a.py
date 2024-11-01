import numpy as np
import random
import plotly.graph_objs as go


def inv_dist_function(z):
    if z < 0:
        return 0
    elif 0 <= z <= 1:
        return z
    elif z > 1:
        return 1


def theory_density(x):
    if 0 <= x <= 1:
        return 1
    return 0


# генерация СВ с помощью обратной функции распределения
Z = []
X = []
n = 1000000  # объем выборки
for i in range(n):
    z = round(random.random(), 4)
    Z.append(z)
    X.append(inv_dist_function(z))
Z.sort()
X.sort()  # получим вариационный ряд

fig = go.Figure(go.Scatter(x=X, y=Z))
fig.update_layout(title_text='Выборка СВ', xaxis_title='x=G(z)', yaxis_title='z')
fig.show()

# график теоретической плотности распределения
x = np.arange(-10, 11, step=0.001)
fig = go.Figure(go.Scatter(x=x, y=[theory_density(x_i) for x_i in x], mode='lines'))
fig.update_layout(title_text='Плотность', xaxis_title='x', yaxis_title='f(x)')
fig.show()

m = 10

main_interval = np.linspace(0, 1, num=n)

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

print(draw_x)
print(hm_values)
fig = go.Figure(data=[go.Bar(x=draw_x, y=hm_values, width=1/m)])
fig.update_layout(title='Оценка плотности распределения', xaxis_title='x', yaxis_title='φ(x)')
fig.show()
