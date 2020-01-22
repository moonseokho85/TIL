# batch_size default

import numpy as np

# 데이터
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 모델 구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

model.add(Dense(5, input_dim=1))
model.add(Dense(3))
model.add(Dense(1))

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["acc"]) # kinds of loss = [mse, mae]
model.fit(x, y, epochs=100) # epochs number changeable

# 평가예측
loss, acc = model.evaluate(x, y)
print('acc: ', acc)

x_prd = np.array([11, 12, 13])
aaa = model.predict(x_prd)
print(aaa)

bbb = model.predict(x)
print(bbb)