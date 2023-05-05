import numpy as np


arr = np.random.randint(1, 11, (60, 28, 28))
arr_org = arr.reshape(arr.shape[0], -1)
print(arr_org.shape)