import numpy as np


matrix = np.random.randint(-10, 10, (5, 5))
# Срез первых трех слоев
print(matrix[:3])

# Срез первого столбца
print(matrix[:, 0])

# Взять элемент второй строки третьего столбца
print(matrix[1, 2])