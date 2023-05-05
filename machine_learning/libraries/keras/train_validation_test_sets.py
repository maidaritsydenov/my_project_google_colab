"""
Есть набор данных. Его необходимо разделить на три группы:
1. Обучающая выборка - для обучения НС
2. Проверочная выборка - для оценки точности модели
3. Тестовая выборка - для оценки качества модели после обучения при подготовки модели в продакшн.

Как разделить датасет на три группы?
"""

from tensorflow.keras.datasets import mnist # загрузка всего датасет MNIST     
(x, y), (_ , _) = mnist.load_data() # запись в переменные нужных нам частей

# 1. С помощью среза 
x_train = x[:48000]
x_val   = x[48000:54000]
x_test  = x[54000:]

# Как разделить на train и test
# 1. Маска
import random
import numpy as np


    # Процент, который выделяем в тестовую выборку
splitVal = 0.2 

    # Список из случайных значений от 0 до 1, длиной равной х
mask_list = np.random.sample(x.shape[0])

    # Создаём маску True-False для создания проверочной выборки
valMask = mask_list < splitVal 

print(mask_list)
print(len(valMask))
print(valMask[:10])
print(~valMask[:10])


# 2. sklearn 
# импорт библиотеки
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, # ----------------- датасет с изображениям
                                                    y, # ----------------- датасет с метками
                                                    test_size = 0.1, # --- процент тестовых значений
                                                    shuffle=True, # ------ перемешивание
                                                    random_state=42) # --- 

print('Обучающая выборка изображений', len(x_train))
print('Обучающая выборка меток', len(y_train))
print()
print('Тестовая выборка изображений', len(x_test))
print('Тестовая выборка меток', len(y_test))






"""Выделение validation."""
# Валидационную выборку мы вычленяем из обучающей, поэтому нам доступны ровно те же самые методы, что мы рассмотрели выше: маска, train_test_split.

# Но можно использовать более удобную возможность

model.fit(x_train, 
          y_train,
          batch_size=8, 
          epochs=100,
          validation_split=0.2,         # <-- 20% использовать для проверки
          verbose=1)

# ИЛИ
model.fit(x_train, 
          y_train,
          batch_size=8, 
          epochs=100,
          validation_data=(x_train[56000:], y_train[56000:]),
          verbose=1)

# Способы подачи проверочных данных через train_test_split и validation_split содержат автоматическое перемешивание,

