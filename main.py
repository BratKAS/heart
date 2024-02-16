import numpy as np
from func import *


input('##################\n\nЭта программа сделает вашу ЭКГ по тачпаду!\n'
      'приложите руку к тачпаду и нажмите ENTER...')
input('\nВы точно положили руку на тачпад?!\nЭто не шутка, тут все серьезно!')

with open('x.txt') as file:
    lines = file.read().strip()

x = lines.split('\n')

with open('y.txt') as file:
    lines = file.read().strip()

y = lines.split('\n')
x, y = [float(xi) for xi in x], [float(yi) for yi in y]


period_index = 255
x_period = x[:period_index]
y_period = y[:period_index]
x_period_end = x_period[-1]
period = 1
x = x_period + [xi + x_period_end - min(x_period) for xi in x]
y = y_period + y
x_range = max(x)
xx = x
for i in range(5):
    xx += [xi + xx[-1] for xi in x]
yy = np.array(y*5)
xx = period * np.array(xx) / x_range

ax = create_animation('$t,\\ c$,', 'Потенциал', 'ЭКГ', marker=None)
i_start = 0
n = len(x)
n_period = len(x_period)
x_end = 0
count = 1

while True:
    i_stop = int(0.1/period * n_period + i_start)

    if i_stop > 2000:
        update(ax, [], [], clear=True)
        i_start = 0
        print('\nВнимание! Очень странная ЭКГ, похоже вы влюблены!!!')
        continue

    x_new = xx[i_start:i_stop]
    update(ax, x_new, yy[i_start:i_stop])
    i_start = i_stop
    if count == n:
        x_max = x_new[-1]
        count = 0
    count += 1

