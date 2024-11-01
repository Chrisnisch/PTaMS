import re
import json
import time
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def digit_on_place(num: str, d: str, i: int):
    num = num[::-1]
    return len(num) >= i and num[i-1] == d


def check(hypotheses, hyp, exp, new_hypotheses):
    if exp['outType'] == 'digit':
        if not digit_on_place(str(hypotheses[hyp][1]), str(exp['outVal']), int(exp['extraParams'])):
            hypotheses[hyp][0] = 0
            if hyp in new_hypotheses:
                del new_hypotheses[hyp]
        else:
            new_hypotheses[hyp] = hypotheses[hyp]
    elif exp['outType'] == 'sum':
        if sum(map(int, str(hypotheses[hyp][1]))) != exp['outVal']:
            hypotheses[hyp][0] = 0
            if hyp in new_hypotheses:
                del new_hypotheses[hyp]
        else:
            new_hypotheses[hyp] = hypotheses[hyp]


def draw_hyp_plot(x, y, k):
    data = {'x': x, 'y': y}
    df = pd.DataFrame(data)

    fig = px.scatter(df, x='x', y='y', labels={'x': 'H_i', 'y': 'P(H_i)'},
                  title=f'Ряд распределения вероятностей апостериорных гипотез после {k} шага')

    fig.show()


main_start = time.time()
data = open('task_1_numbers.txt', 'r')

options = re.findall(r'\d+', data.readline().strip())
Nmin = int(options[0])
Nmax = int(options[1])
Nexp = int(options[2])

prior = 1 / (Nmax - Nmin + 1)
hypotheses = {i: [prior, i] for i in range(Nmin, Nmax + 1)}

_ = data.readline()
del _

new_hypotheses = {}
last_possibles = Nmax - Nmin + 1

hyps_for_draw = {i: [prior] for i in range(Nmin, Nmax + 1)}

number_of_hyps = []

for i in range(Nexp - 2):
    start = time.time()
    """ читаем строку в словарь """
    s = data.readline()
    step = re.search(r'\d+', s).group()
    start_idx = s.find("{")
    end_idx = s.find("}") + 1
    json_str = s[start_idx:end_idx].replace("'", "\"")
    exp = json.loads(json_str)
    del s
    del start_idx
    del end_idx
    del json_str

    if exp['op'] == '-':

        for hyp in hypotheses.keys():
            if hypotheses[hyp][0] != 0:
                hypotheses[hyp][1] = abs(hypotheses[hyp][1] - int(exp['num']))
                check(hypotheses, hyp, exp, new_hypotheses)

    elif exp['op'] == '+':

        for hyp in hypotheses.keys():
            if hypotheses[hyp][0] != 0:
                hypotheses[hyp][1] += int(exp['num'])
                check(hypotheses, hyp, exp, new_hypotheses)

    elif exp['op'] == '*':

        for hyp in hypotheses.keys():
            if hypotheses[hyp][0] != 0:
                hypotheses[hyp][1] *= int(exp['num'])
                check(hypotheses, hyp, exp, new_hypotheses)

    elif exp['op'] == '//':

        for hyp in hypotheses.keys():
            if hypotheses[hyp][0] != 0:
                hypotheses[hyp][1] //= int(exp['num'])
                check(hypotheses, hyp, exp, new_hypotheses)

    elif exp['op'] == 'r':
        for hyp in hypotheses.keys():
            if hypotheses[hyp][0] != 0:
                hypotheses[hyp][1] = hyp

    # probs = []
    for hyp in hypotheses.keys():

        if hypotheses[hyp][0] != 0:
            hypotheses[hyp][0] = 1 / len(new_hypotheses)
            new_hypotheses[hyp][0] = 1 / len(new_hypotheses)

            hyps_for_draw[hyp].append(hypotheses[hyp][0])
        # probs.append(hypotheses[hyp][0])

    if last_possibles != len(new_hypotheses):
        print(f'On step #{step} after "{exp['op']}" operation number of possible numbers: {len(new_hypotheses)}')
    last_possibles = len(new_hypotheses)

    number_of_hyps.append(len(new_hypotheses))

    # if step == '61':
    #     draw_hyp_plot(list(hypotheses.keys()), probs, step)

    if len(new_hypotheses) == 1:
        print(new_hypotheses)
        break

data.close()

number_of_exps = int(step)
steps = [i for i in range(0, number_of_exps+1)]

lengths = {}

for hyp in hyps_for_draw.keys():
    lengths[len(hyps_for_draw[hyp])] = hyp

fig = go.Figure()
for hyp in lengths.values():
    y = hyps_for_draw[hyp]

    for i in range(len(y), int(step)):
        y.append(0)

    fig.add_trace(go.Scatter(x=steps, y=y, mode='lines', name=str(hyp)))

fig.update_layout(title_text='Зависимость вероятностей гипотез от номера опыта')
fig.update_xaxes(title_text='Steps')
fig.update_yaxes(title_text='P(H_i)')
fig.show()

fig = go.Figure(go.Scatter(x=steps, y=number_of_hyps, mode='lines'))
fig.update_layout(title_text='Зависимость количества гипотез от номера опыта')
fig.update_xaxes(title_text='Steps')
fig.update_yaxes(title_text='Hypotheses')
fig.show()

print(f'Programm time: {time.time() - main_start}')
