import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображения
image = cv2.imread('img.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Преобразование изображения в бинарное
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)


# Поиск контуров на изображении
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# cont = cv2.drawContours(thresh, contours, -1, (0, 255, 0), 2)  # Цвет контура: зеленый, толщина линии: 2
# cv2.imshow('test', cont)
# cv2.waitKey(0)

# Инициализация списка для хранения координат точек
data = {}

count = 0
for contour in contours:
    data[count] = [], []
    for point in contour:
        data[count][0].append(point[0][0])
        data[count][1].append(578-point[0][1])

    count += 1
print(data)

fig, ax = plt.subplots()
# for i in data.keys():
#     ax.plot(data[i][0], data[i][1])
i = 2
x, y = np.array(data[i][0]), np.array(data[i][1])
n = len(x)
assert n == len(y)
start_index = np.argmin(x)
end_index = start_index - n//2

x = x[start_index:end_index:-1]
y = y[start_index:end_index:-1]
miny_index = np.argmin(y)

indices_to_remove = [miny_index + i for i in range(-8, 8)]
x = np.delete(x, indices_to_remove)
y = np.delete(y, indices_to_remove)

miny_index = np.argmin(y) + 1
x = np.insert(x, miny_index, 249)
y = np.insert(y, miny_index, -140)

ax.plot(x[0], y[0], marker='o')

ax.plot(x, y)
plt.show()

# Сохранение координат в текстовый файл
with open('x.txt', 'w') as file:
    for point in x:
        file.write(f'{point}\n')

# Сохранение координат в текстовый файл
with open('y.txt', 'w') as file:
    for point in y:
        file.write(f'{point}\n')
