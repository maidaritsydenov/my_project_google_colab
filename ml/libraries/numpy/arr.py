import numpy as np


# my_list = [1, 2, 3, 4, 5]                 # Задание списка чисел с названием my_list
# numpy_arr = np.array(my_list)             # Вызов np.array() превращает список в массив чисел


# От 1 до (не включая) 11 - границы массива, а число 5 - общее кол-во чисел
# arr = np.random.randint(1, 6, 5) 

# Создай три массива 2 на 2. Числа от -5 до 5
# tensor = np.random.randint(-5, 5, (3, 2, 2))
# print(tensor)

# .ndim сообщает, сколько измерений в тензоре;
# .shape сообщает форму массива: насколько каждое из измерений велико в высоту/ширину/глубину (т.е. по столбцам, строкам и слоям);
# .size сообщает, сколько в тензоре всего занятых мест.:

# print(tensor.ndim)
# print(tensor.shape)
# print(tensor.size)


# array_1D = np.random.randint(-5, 5, 4)                        # Задается одномерный массив
# print(array_1D)

# array_3D = random_matrix = np.random.randint(-5, 5, (5, 2))   # Задается двумерный массив
# print(array_3D)

# array_5D = np.random.randint(-5, 5, (2, 2, 2, 2, 2))          # Задается пятимерный массив
# print(array_5D)


arr1 = np.random.randint(0,1,5)
arr2 = np.random.randint(1,2,5)
arr3 = np.random.randint(3,4,5)

print(arr1, arr2, arr3)

null_vector = np.zeros(5, dtype=int)                       # Создание вектора, заполненного нулями
one_vector = np.ones(5, dtype=int)                         # Создание вектора, заполненного единицами
three_vector = np.full(5, 3)                               # Создание вектора, заполненного тройками

print(null_vector, one_vector, three_vector)               # Вывод результата


rand_arr = np.random.random(10)                            # Выводит тип данных # float64, 64 - занимаемая память элемента
print(rand_arr.dtype)


# .allclose(arr1, arr2)           # Получение массива сравнения. True если массивы равны