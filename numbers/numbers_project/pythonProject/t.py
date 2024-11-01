import plotly.graph_objects as go

# Определение функций
def f(x):
    return x ** 2

def g(x):
    return 2 * x + 1

# Создание массива значений x
x = list(range(-10, 11))

# Определение значений функций на заданном массиве x
y_f = [f(xi) for xi in x]
y_g = [g(xi) for xi in x]

# Построение графиков
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y_f, mode='lines', name='f(x) = x^2'))
fig.add_trace(go.Scatter(x=x, y=y_g, mode='lines', name='g(x) = 2x + 1'))

fig.update_layout(title='Графики функций f(x) и g(x)',
                  xaxis_title='x',
                  yaxis_title='y')

fig.show()
