import random


def random_numbers():
    n = random.randint(5, 20)
    m = random.randint(5, 20)
    k = random.randint(5, 20)
    return n, m, k


def create_model():
    n, m, k = random_numbers()
    print(f'Количество урн: {n}\nВ каждой урне {m} чёрных шаров и {k} белых')
    boxes = []
    box = []
    for i in range(n):
        for j in range(k):
            box.append("black")
        for j in range(m):
            box.append("white")
        boxes.append(box)
    return boxes


def simulation(repeat, boxes):
    last_ball = []
    first_ball = []
    for i in range(repeat):
        for i in range(len(boxes) - 1):
            ball = random.choice(boxes[i])
            if i == 0:
                first_ball.append(ball)
            boxes[i+1].append(ball)
        last_ball.append(random.choice(boxes[-1]))
    return first_ball, last_ball


def variation():
    Nall = 1000000
    first, last = simulation(Nall, create_model())
    first_prob = first.count("white") / len(first)
    last_prob = last.count("white") / len(last)
    print(f'Вероятность вытащить белый шар из первой урны:\t   {first_prob}\nВероятность вытащить '
          f'белый шар из последней урный: {last_prob}')


for _ in range(5):
    variation()
