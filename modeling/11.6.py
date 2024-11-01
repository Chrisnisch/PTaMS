import random

Nall = 1000000
N = 100
max_k = 500


def generate_values():
    m_list = []
    n = N
    while n > 0:
        mi = random.randint(1, n)
        m_list.append(mi)
        n -= mi
    print(f'Список mi\n{m_list}')
    k_list = []
    tickets = []
    for m in m_list:
        ki = random.randint(1, max_k)
        k_list.append(ki)
        for i in range(m):
            tickets.append(ki)
    print(f'Список ki\n{k_list}')
    return m_list, k_list, tickets


def analytic(m_list: list, k_list: list, N):
    return 2 * sum([m_list[i] * k_list[i] for i in range(len(m_list))]) / N


def avg_price(tickets: list):
    sum = 0
    for i in range(Nall):
        sum += random.choice(tickets)
    return sum / Nall


for i in range(10):
    m_list, k_list, tickets = generate_values()
    analytic_price = analytic(m_list, k_list, N)
    model_price = 2 * avg_price(tickets)
    print(f'Стоимость билета, посчитанная на основе моделирования: {model_price}\n'
          f'Стоимость билета, посчитанная по формуле: {analytic_price}\n')
