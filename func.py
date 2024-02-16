import matplotlib.pyplot as plt


data = {}


def create_animation(xlabel='x', ylabel='y', title='', **kwargs):
    """
    Функция создает окно для анимации (построения графика в режиме реального времени),
    для обновления переменных нужно использовать функцию update.
    :param xlabel: Название оси х (по умолчанию "х").
    :param ylabel: Название оси y (по умолчанию "y").
    :param title: Название графика (по умолчанию пустая строка).
    """
    fig, ax = plt.subplots()
    global data
    data[ax] = {1: ([], [])}
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    if 'marker' in kwargs:
        line, = ax.plot([], [],  **kwargs)
    else:
        line, = ax.plot([], [], marker='.', **kwargs)
    if 'label' in kwargs:
        ax.legend()
    dot, = ax.plot([], [], marker='o', color='red', markersize=6)
    plt.ion()
    plt.draw()
    plt.pause(0.1)
    return ax


def update(ax, x, y, line_number=1, clear=False):
    """
    Функция, с помощью которой пользователь может изменить данные на анимации.
    :param ax: оси, для которых нужно обновить данные
    :param x: Число или список для обновления значений xdata.
    :param y: Число или список для обновления значений ydata.
    :param line_number: Номер линии, которую нужно обновить (отсчет от 1-го)
    :param clear: Удаляет старые данные с графика, если True (по умолчанию False).
    """
    global data
    if clear:
        data[ax][line_number][0].clear()
        data[ax][line_number][1].clear()

    if isinstance(x, (int, float)):
        data[ax][line_number][0].append(x)
    else:
        for xi in x:
            data[ax][line_number][0].append(xi)

    if isinstance(y, (int, float)):
        data[ax][line_number][1].append(y)
    else:
        for yi in y:
            data[ax][line_number][1].append(yi)

    lines = ax.get_lines()
    line = lines[2*(line_number-1)]
    dot = lines[2*line_number-1]
    n = min(len(data[ax][line_number][0]), len(data[ax][line_number][1]))
    line.set_data(data[ax][line_number][0][:n], data[ax][line_number][1][:n])
    dot.set_data(data[ax][line_number][0][n - 1:n], data[ax][line_number][1][n - 1:n])

    ax.set_ylim(-150, 350)

    if data[ax][line_number][0]:
        max_x = max(data[ax][line_number][0])
        if max_x < 1:
            ax.set_xlim(0, 1)
        else:
            ax.set_xlim(0, max_x)
            # ax.relim()
            # ax.autoscale_view()

    plt.draw()
    plt.pause(0.1)
