from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, BatchNormalization, Dense, Flatten


# На входной слой подаем изображение 28 на 28 пикселей в 3 канала (цветное изображение)
# Его обрабатывает свертка размером 3 на 3 пискеля
# MaxPooling2D сжимает изображение
# Dropout - регуляризаиця (Отлючение части нейронов для предотвращения эффекта переобучения)
# BatchNormalization - Пакетная нормализация

# На выходе линейный слой Dense - 10 нейронов = вероятности 10 классов

model = Sequential()

model.add(BatchNormalization())
model.add(Conv2D(256, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 3)))
model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3))) # Укажем pool_size=(3, 3)    81*54
model.add(Dropout(0.3))

model.add(Flatten())
model.add(Dense(2048, activation='elu'))
model.add(Dense(4096, activation='elu'))
model.add(Dense(10, activation='softmax')) # Выходной полносвязный слой с количеством нейронов равным количесту классов
