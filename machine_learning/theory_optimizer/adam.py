"""
Оптимизатор Adam

Adam — один из самых эффективных алгоритмов оптимизации в обучении нейронных сетей.
Он сочетает в себе идеи RMSProp и оптимизатора импульса (momentum).

Чем больше движемся в одну сторону, тем больше шаг и адаптация каждого параметра.

Вместо того чтобы адаптировать скорость обучения параметров на основе среднего первого момента (среднего значения), как в RMSProp,
Adam также использует среднее значение вторых моментов градиентов.
В частности, алгоритм вычисляет экспоненциальное скользящее среднее градиента и квадратичный градиент
"""

from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(64, input_shape=(10,), activation='softmax'))
adam = optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
model.compile(loss='mean_squared_error', optimizer=adam)