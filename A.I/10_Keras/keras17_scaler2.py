from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

# 데이터
x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [20000, 30000, 40000], [30000, 40000, 50000], [40000, 50000, 60000], [100, 200, 300]])

y = array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50000, 60000, 70000, 400])

# 데이터 전처리
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import RobustScaler, MaxAbsScaler

sc = StandardScaler() # 표준화
sc.fit(x)
x = sc.transform(x)

mms = MinMaxScaler() # 정규화 (데이터를 0 ~ 1 사이로 재조정)
mms.fit(x)
x = mms.transform(x)

print(x)

# x = x.reshape(x.shape[0], x.shape[1], 1)

# Train / Test 으로 분리
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75, random_state=66, shuffle=False)

print(x_train.shape)

x_train = sc.transform(x_train)
x_train = mms.transform(x_train)

x_test = sc.transform(x_test)
x_test = mms.transform(x_test)

# 모델 생성
from keras.models import Sequential, Model
from keras.layers import Dense, Input, LSTM

model = Sequential()
model.add(LSTM(128, activation='relu', input_shape=(3, 1), return_sequences=True)) # 3: column number & 1: 몇개씩 자르는지
model.add(LSTM(64, activation='relu'))
# model.add(Dense(128))
# model.add(Dense(64))
# model.add(Dense(64))
# model.add(Dense(64))
# model.add(Dense(64))
# model.add(Dense(64))
# model.add(Dense(64))
# model.add(Dense(32))
model.add(Dense(1))

# 모델 요약
model.summary()

model.compile(loss='mse', optimizer = 'adam', metrics = ['mae'])

# Early_Stopping
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)

# 모델 학습
model.fit(x_train, y_train, epochs = 100000, batch_size=1, callbacks=[early_stopping])

x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

# 모델 평가
loss, mae = model.evaluate(x_test, y_test, batch_size=1)
print('loss: ' , loss)
print('mae: ', mae)

# 예측
y_predict = model.predict(x_test, batch_size=1)

# R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2: ", r2_y_predict)

import numpy as np
x_prd = np.array([[250, 260, 270]]) #한개가 더 늘어나야함
# x_prd = np.transpose(x_prd)

x_prd = sc.transform(x_prd)
x_prd = mms.transform(x_prd)

x_prd = x_prd.reshape(x_prd.shape[0], x_prd.shape[1], 1)

aaa = model.predict(x_prd, batch_size=1)
print("aaa: ", aaa)