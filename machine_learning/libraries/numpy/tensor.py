import numpy as np


# arr_1 = np.random.randint(-10, 10, 5)
# arr_2 = np.random.randint(-10, 10, 5)
# print(arr_1)
# print(arr_2)

# # .in1d сравнивает два массива. Если элемент из arr_1 есть в arr_2 то true
# print(np.in1d(arr_1, arr_2))
# # .intersect1d выводит одинаковые элементы в массиве
# print(np.intersect1d(arr_1, arr_2))


# array_100 = np.arange(100)                 # Создание массива из ста элементов (один из возможных способов)
# my_array = np.random.uniform(size=(6,6))   # Создание массива 6 на 6


# print(arr_1 + arr_2)                     # Поэлементное сложение двух массивов
# print(arr_1 * arr_2)                     # Поэлементное умножение двух массивов
# print(arr_1 / arr_2)                     # Поэлементное деление первого массива на второй
# print(arr_1 * 5)                         # Умножение каждого элемента массива "arr_1" на число 5
# print(arr_1 / 7)                         # Деление каждого элемента массива "arr_1" на число 7
# print(arr_1 ** 3)                        # Возведение каждого элемента массива "arr_1" в степень 3




# print(numpy_arr.sum())                     # Сумма элементов
# print(numpy_arr.mean())                    # Среднее элементов
# print(numpy_arr.min())                     # Минимальный элемент
# print(numpy_arr.max())                     # Максимальный элемент

# Важный момент: попробуйте в скобках этих команд написать слово axis («ось»).
# Если задать
# axis=1, то команда будет применяться ко всем числам каждой строки,
# axis=0, то ко всем числам каждого столбца:


# .reshape(x, y)                 # Преобразование массива к размерности x*y


# a = np.random.randint(0, 100, (6, 8))       # Создание массива из числовых элементов
# b = np.array(a, dtype='U10')                # Создание массива с теми же значениями, но из текстовых элементов
# b[a > 50] = 'пан'                           # Замена элементов на соответствующие условию
# b[a <= 50] = 'пропал'

a = np.random.randint(15, 38, (3, 4))
b = np.array(a, dtype='U10')


b[a<=30] = 'medium'
b[a>30] = 'large'
b[a<20] = 'small'

print(a)
print(b)