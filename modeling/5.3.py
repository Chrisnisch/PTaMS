import numpy as np


def create_matrix_of_probs(n):
    matrix = np.random.rand(n, n)  # Генерируем матрицу с случайными числами от 0 до 1
    matrix = matrix / np.sum(matrix)  # Делим каждый элемент матрицы на сумму всех элементов, чтобы получить сумму 1
    print("Квадрат с вероятностями:\n", matrix)
    return matrix


def throw_the_ball(square):
    p = square.copy()

    # Создаем массив для индексов i и j
    indexes = np.array([[i, j] for i in range(n) for j in range(n)])

    # Случайно выбираем индексы i и j в соответствии с вероятностями Pij
    selected_index = np.random.choice(np.arange(n * n), p=p.flatten())
    i, j = indexes[selected_index]
    return i, j


def modeling(simulations_num, square):

    horizontals = []
    for c in range(simulations_num):
        i, j = throw_the_ball(square)
        horizontals.append(i)
    Pk_modeling = []
    for k in range(len(square)):
        pk = horizontals.count(k) / len(horizontals)
        Pk_modeling.append(pk)
    # for i in range(len(Pk_theory)):
    #     print(f"Теоретическая вероятность попадания шарика в {i} горизонталь: {Pk_theory[i]}")
    #     print(f'Фактическая вероятность попадания шарика в {i} горизонталь: {Pk_modeling[i]}')
    return Pk_modeling


n = int(input("Введите сторону квадрата: "))  # Размер квадрата
Nall = 100000  # количество прогонов для одного моделирования
# modeling(Nall, n)
square = create_matrix_of_probs(n)
while np.sum(square) != 1:
    print("Это плохая матрица")
    square = create_matrix_of_probs(n)
repeat = 20
Pk_modeling_all = [0]*n
Pk_theory = []
for i in range(repeat):
    t = modeling(Nall, square)
    for j in range(n):
        Pk_theory.append(sum(square[j]))
        Pk_modeling_all[j] += t[j]
for i in range(n):
    print(f"Теоретическая вероятность попадания шарика в {i} горизонталь: {Pk_theory[i]}")
    print(f'Фактическая вероятность попадания шарика в {i} горизонталь: {Pk_modeling_all[i] / repeat}')
