# 행렬 계산
import numpy as np

x4 = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
print(x4.ndim) # 3
print(x4.shape) # (2, 2, 2)

x5 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(x5.ndim) # 2
print(x5.shape) # (3, 5)