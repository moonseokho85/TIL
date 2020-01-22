# 파라미터 튜닝 => loss = 0.0001
import numpy as np

# 데이터
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(x.shape)
# print(y.shape)

# 모델 구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

model.add(Dense(64, input_dim=1))
model.add(Dense(32))
model.add(Dense(18))
model.add(Dense(1))

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["accuracy"]) # kinds of loss = [mse, mae]
model.fit(x, y, epochs=1000, batch_size=1) # epochs number changeable

# 평가예측
loss, accuracy = model.evaluate(x, y, batch_size=1)
print('loss: ', loss)
print('accuracy: ', accuracy)