import matplotlib.pyplot as plt
import numpy as np


height = [130, 135, 140, 145, 150, 155]           # Список ростов
num = [2, 6, 9, 8, 7, 1]                          # Список количества учеников
x_pos = [i for i, _ in enumerate(height)]         # Перебор ростов
plt.barh(x_pos, num, color='green')               # Построение горизонтальной гистограммы
plt.xlabel("Количество")                          # Подпись оси х
plt.ylabel("Рост")                                # Подпись оси у
plt.title("Рост/количество учеников")             # Подпись графика
plt.yticks(x_pos, height)                         # Значения на оси у
plt.show()                                        # Вывод результата




plt.pie(num, labels=height, autopct='%1.1f%%')       # Создание круговой диаграммы
plt.show()                                           # Вывод результата



# Отобразите точечный график со случайным распределением по осям Х и Y

x = np.random.randn(100)               # Случайное распределение по оси х
y = np.random.randn(100)               # Случайное распределение по оси у
plt.scatter(x, y, color='r')           # Точечный график
plt.show()                             # Вывод результата