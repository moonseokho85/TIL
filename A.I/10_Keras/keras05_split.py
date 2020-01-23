import numpy as np

# 데이터
x = np.array(range(1, 101))
y = np.array(range(1, 101))

x_train = x[:60]
y_train = y[:60]

x_val = x[60:80]
y_val = y[60:80]

x_test = x[80:]
y_test = y[80:]

# 데이터 확인
# print(x_train)
# print(x_val)
# print(x_test)

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
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=500, batch_size=1) # epochs number changeable

# 평가예측
loss, accuracy = model.evaluate(x_test, y_test, batch_size=1)
print('loss: ', loss)
print('accuracy: ', accuracy)

x_prd = np.array([101, 102, 103])
aaa = model.predict(x_prd, batch_size=1)
print(aaa)
