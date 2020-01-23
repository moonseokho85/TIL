import numpy as np

# 데이터
x_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x_test = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
y_test = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
x_val = np.array([101, 102, 103, 104, 105])
y_val = np.array([101, 102, 103, 104, 105])

# 데이터 확인
# print(x.shape)
# print(y.shape)

# 모델 구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

# model.add(Dense(5, input_dim=1))
model.add(Dense(5, input_shape=(1,)))
model.add(Dense(2))
model.add(Dense(3))
model.add(Dense(1))

# 모델 요약
model.summary()

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["accuracy"]) # kinds of loss = [mse, mae]
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=1000, batch_size=1) # epochs number changeable

# 평가예측
loss, accuracy = model.evaluate(x_test, y_test, batch_size=1)
print('loss: ', loss)
print('accuracy: ', accuracy)

x_prd = np.array([11, 12, 13])
aaa = model.predict(x_prd, batch_size=1)
print(aaa)