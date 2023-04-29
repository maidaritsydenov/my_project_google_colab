from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Во входном слое в input_dim подаем вектор из 784 чисел (пиксели 28*28)
# Во выходном слое получаем 10 чисел-вероятностей принадлежности к 10 классам. Вероятность от 0 до 1 (softmax)


# Создание сети прямого распространения
model = Sequential() 
# Добавление полносвязного слоя на 800 нейронов с relu-активацией
model.add(Dense(800, input_dim=784, activation="relu")) 
# Добавление полносвязного слоя на 400 нейронов с relu-активацией
model.add(Dense(400, activation="relu")) 
# Добавление полносвязного слоя на 10 нейронов с softmax-активацией
model.add(Dense(10, activation="softmax")) 