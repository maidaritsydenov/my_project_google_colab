"""
Функции активации

Определяют выходное значение нейрона в зависимости от результата взвешенной суммы входов и порогового значения.
Применяются к нейрону после того, просчитанному матричным умножением.
Определяет, передавать ли полученное значение следующему нейрону (активировать его) или нет, и модифицировать ли как-то полученное значение.



Рассмотрим нейрон, у которого взвешенная сумма равна z.

z = Σ (wi * xi + b)

wi - вес
xi - входное значение i-ого входа
b - смещение

Полученный результат передается в функцию активации, которая решает рассматривать этот нейрон как активированный, или его можно игнорировать.
"""


# Сигмоидная функция (англ. sigmoid function), которую также называет логистической (англ. logistic function),
# является гладкой монотонно возрастающей нелинейной функцией.

# Преобразует выходное значение нейрона в значение из диапазона [0, +1], смещает среднее значение с 0 и используется в случаях, когда нужно получить что-то похожее на вероятность.

# Хорошо себя показывает в LSTM-сетках, логистической регрессии.



# Несмотря на множество сильных сторон сигмоидной функции, у нее есть значительный недостаток.
# Производная такой функции крайне мала во всех точках, кроме сравнительно небольшого промежутка - проблема исчезающего градиента.
# Это сильно усложняет процесс улучшения весов с помощью градиентного спуска. Более того, эта проблема усугубляется в случае, если модель содержит много слоев.

# Что касается использования сигмоидной функции, то ее преимущество над другими — в нормализации выходного значения.
# Иногда, это бывает крайне необходимо. К примеру, когда итоговое значение слоя должно представлять вероятность случайной величины.
# Кроме того, эту функцию удобно применять при решении задачи классификации, благодаря свойству "прижимания" к асимптотам.



# Sigmoid - преобразует малые значения (< - 5) в близкие к нулю, а большие значения ( > 5 ) в близкие к единице.
# Вычисляется по программной формуле (Python): sigmoid(x) = 1 / (1 + exp(-x))

# Для бинарной и многокритериальной классификации - функция sigmoid,
