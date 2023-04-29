"""
Импульсный оптимизатор

Стохастический градиентный спуск - Stochasticу Gradient descent (SGD)
"""

# Берем случайные объекты, подаем их в модель и получаем предсказание, считаем функцию потерь, обновляем веса,
# повторяем снова до тех пор пока функция ошибки не окажется в точке минимума.

# Есть три варианта:

# 1. Подаем по одному объекту набора данных. У каждой подачи своя функция ошибки, чуть отличная от других.
# Это может быть горбик на линии, немного другой изгиб графика и пр.
# Видно, что линия долго "блуждает", прежде чем попасть в минимум.

# 2. BatchGD
# Подаем весь набор данных полностью (может требовать большие вычислительные мощности).
# При этом все ошибки усредняются, их графики становятся идентичными. Линия движения от текущей точки до минимума почти прямая, минимум отклонений от курса.


# 3. Mini-batchGD.
# Подаем набор данных партиями, батчами (их размер оптимизируется под имеющиеся вычислительные мощности).
# При этом все ошибки внутри батча усредняются, имеют идентичные графики, но между разными батчами есть небольшие отличия.
# Линия движения от текущей точки до минимума с небольшими отклонениями.
# Размер батча часто бывает степенью числа 2 (32,64,128), данные в батч выбираются случайным образом
# (при застревании в локальных минимумах некоторые шумные данные могут привести к выходу из этих минимумов).
# Такой подход объединяет в себе устойчивость однопакетной подачи и эффективность подачи всего пакета.
# Это наиболее распространенная реализация градиентного спуска, используемая в области глубокого обучения.



# Основная проблема - попадание функции в локальные минимумы вместо нахождения глобального.
# Для ее решения используются модификации стохастического градиента, использующие скользящее среднее градиентов.



# 1-я модификация Оптимизатор импульса (Momentum)
# Показывает меньшее количество колебаний, нежели SGD, помогает ускорить обучение. Учитывает прошлые градиенты, чтобы сгладить обновление.
# Основная идея в том, что мы ускоряемся (увеличиваем шаг), если движемся в одном направлении и замедляемся, если "путь" меняется.

# При SGD с импульсом (или SGD with momentum) на каждой новой итерации оптимизации используется скользящее среднее градиента.
# Движение в направлении среднего прошлых градиентов добавляет в алгоритм оптимизации эффект импульса,
# что позволяет скорректировать направление очередного шага, относительно исторически доминирующего направления.
# Для этих целей достаточно использовать приближенное скользящее среднее и не хранить все предыдущие значения градиентов, для вычисления «честного среднего».



# 2-я модификация SGD. Оптимизатор импульса (Nesterov Momentum)
# Nesterov accelerated gradient отличается от метода с импульсом, его особенностью является вычисление градиента при обновлении.
# Эта точка берётся впереди по направлению движения накопленного градиента. Отличие от обычного momentum на картинке ниже.


# Пример использования оптимизатора SGD:

from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(64, input_shape=(10,), activation='softmax'))
sgd = optimizers.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error', optimizer=sgd)

