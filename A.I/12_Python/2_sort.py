# 1차원 배열 정렬
import numpy as np

x = np.array([4, 2, 6, 5, 1, 3, 0])

sorted_x = np.sort(x)
print('sorted_x: ', sorted_x)

# 원래 배열은 그대로, 정렬 결과 복사본 반환
x = np.array([4, 2, 6, 5, 1, 3, 0])

print(np.sort(x))

print(x)

# 배열 자체를 정렬
x = np.array([4, 2, 6, 5, 1, 3, 0])

x.sort()

print(x)