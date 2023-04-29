import matplotlib.pyplot as plt
import numpy as np


# Создать равномерный ряд чисел (от 0 до 15) из 101 числа 
x = np.linspace(0, 15, 101)
y = np.sin(x)


# Отрисовка графика командой plot(), в которую переданы массивы точек для x и y
# С помощью .show() выводится график

plt.figure(figsize=(14, 7))                   # Задание размера полотна в дюймах

plt.plot(x,y , label='sin(x)',
         color='#4b0082',
         linewidth=4,
         marker='h',
         markerfacecolor='lightgreen',
         markeredgewidth=2,
         markersize=10,
         markevery=5
    )

plt.plot(x, np.cos(x)/2, label='cos(x)/2',
         linewidth=3,
         color='lightcoral',
         marker='D',
         markeredgecolor='black',
         markevery=5
    )

plt.title('y = sin(x)')                       # Заголовок графика
plt.xlabel('Переменная X')                    # Надпись для оси x
plt.ylabel('Переменная Y')                    # Надпись для оси y

plt.legend()                                  # Отрисовка названий графиков ("легенды")

plt.grid()                                    # Отрисовка сетки

plt.show()                                    # Вывод графика




# x = np.random.randint(0, 5, 10)                     # Создание первого случайного вектора
# y = np.random.randint(0, 5, 10)                     # Создание второго случайного вектора
# plt.xlabel('x')                                     # Подпись оси х
# plt.ylabel('y')                                     # Подпись оси y
# plt.plot(x, y, color='blue', linestyle='dotted')    # Первый график
# plt.plot(y, x, color='red', linestyle='dashed')     # Второй график
# plt.title("Двойной график")                         # Подпись графика
# plt.show()                                          # Вывод графиков