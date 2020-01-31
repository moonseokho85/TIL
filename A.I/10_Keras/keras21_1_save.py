import numpy as np

# 데이터
x = np.array([range(1, 101), range(101, 201), range(301, 401)])
y = np.array([range(101, 201)])
y2 = np.array(range(101, 201))

print(x.shape) # (3, 100)
print(y.shape) # (1, 100)

x = np.transpose(x) # x = x.reshape((10, 2))
y = np.transpose(y) # y = y.reshape((10, 2))

print(x.shape) # (100, 3)
print(y.shape) # (100, 1)

# 데이터 Set 나누기
from sklearn.model_selection import train_test_split
# 내가 짠 코드
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)
# x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.25, shuffle=False)
# 더 좋은 코드
x_train, x_test, y_train, y_test = train_test_split(x, y2, train_size=0.6, random_state=66, shuffle=False)
x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size=0.5, random_state=66, shuffle=False)

# 데이터 확인
# print(x_train)
# print(x_test)
# print(x_val)

# 모델 구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

# model.add(Dense(5, input_dim=3))
model.add(Dense(64, input_shape=(3,)))
model.add(Dense(38))
model.add(Dense(1))

# 모델 요약
model.summary()

# 모델 저장하기
model.save('./save/savetest01.h5')
print('Successfully saved')