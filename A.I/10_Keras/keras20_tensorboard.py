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

model.compile(loss='mse', optimizer='adam', metrics=["mse"]) # kinds of loss = [mse, mae]

# EarlyStopping 선언
from keras.callbacks import EarlyStopping, TensorBoard

early_stopping = EarlyStopping(monitor='loss', patience=1000, mode='auto')

tb_hist = TensorBoard(log_dir='./graph', histogram_freq=0, write_grads=True, write_images=True)

# 모델 훈련
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=100000, batch_size=1, callbacks=[early_stopping, tb_hist]) # epochs number changeable

# 평가 예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1)
print('loss: ', loss)
print('mse: ', mse)
# print('rmse: ', np.sqrt(mse)) # RMSE 구하는 또 다른 방법

x_prd = np.array([[201, 202, 203], [204, 205, 206], [207, 208, 209]])
print(x_prd.shape)
x_prd = np.transpose(x_prd)
print(x_prd.shape)

aaa = model.predict(x_prd, batch_size=1)
print(aaa)

y_predict = model.predict(x_test, batch_size=1)

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: ", RMSE(y_test, y_predict))

# R2 구하기 (회귀 모델의 성능을 측정하기 위해 평균값으로 예측하는 단순 모델에 비해  상대적으로 얼마나 성능이 나오는지를 측정합니다.)
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2: ", r2_y_predict)
