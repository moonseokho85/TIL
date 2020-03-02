# np.sort(x)[::-1] : 정렬을 한 후 mirror view 생성

import numpy as np

x = np.array([4, 2, 6, 5, 1, 3, 0])

x_reverse_1 = np.sort(x)[::-1] # mirror view
print('x_reverse_1: ', x_reverse_1)

# x[np.argsort(-x)] : np.argsort() 로 index를 받아서 indexing 해오기

x = np.array([4, 2, 6, 5, 1, 3, 0])
print('np.argsort(-x): ', np.argsort(-x))

x_reverse_2 = x[np.argsort(-x)] # copy of reversed sorting
print('x_reverse_2: ', x_reverse_2)