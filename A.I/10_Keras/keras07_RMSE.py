import numpy as np

# 데이터
x = np.array(range(1, 101))
y = np.array(range(1, 101))

# 데이터 Set 나누기
from sklearn.model_selection import train_test_split

# 내가 짠 코드
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)
# x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.25, shuffle=False)

# 더 좋은 코드
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6, random_state=66, shuffle=False)
x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size=0.5, random_state=66, shuffle=False)

# 데이터 확인
# print(x_train)
# print(x_test)
# print(x_val)

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
model.compile(loss='mse', optimizer='adam', metrics=["mse"]) # kinds of loss = [mse, mae]
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=100, batch_size=1) # epochs number changeable

# 평가예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1)
print('loss: ', loss)
print('mse: ', mse)

x_prd = np.array([101, 102, 103])
aaa = model.predict(x_prd, batch_size=1)
print(aaa)

y_prd = model.predict(x_test, batch_size=1)

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: ", RMSE(y_test, y_prd))