import pandas as pd
import numpy as np

data = pd.read_csv('./data/samsung.csv')
print(data)

data = data.sort_values(by='date', ascending=True)

del data['date']
print(data)

data.astype(float)

data = np.asarray(data)
print(data)

from numpy import array

def split_sequence(sequence, n_steps):
    x, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps
        if end_ix > len(sequence) - 1:
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix][3]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)

x, y = split_sequence(data, 5)
print(x)
print(y)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6, random_state=66, shuffle=False)
x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size=0.5, random_state=66, shuffle=False)

print(x_train.shape) # (252, 5, 5)


from keras.models import Sequential
from keras.layers import Dense, LSTM
model = Sequential()

model.add(LSTM(64, activation='relu', input_shape=(5, 5), return_sequences=True)) # 3: column number & 1: 몇개씩 자르는지
model.add(LSTM(32, activation='relu'))
model.add(Dense(128, input_shape=(25,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# 모델 요약
model.summary()

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["mse"]) # kinds of loss = [mse, mae]

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=1000, batch_size=1, callbacks=[early_stopping]) # epochs number changeable

# 평가예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1)
print('loss: ', loss)
print('mse: ', mse)

from numpy import array

# [   60500,    62600  ,  60400  ,  62300, 15339565],

# 2월 4일 종가 예측
pred = array([[61800, 61800, 60700, 60800, 14916555],
              [59400, 59400, 58300, 58800, 23664541],
              [59100, 59700, 58800, 59100, 16446102],
              [58800, 58800, 56800, 57200, 20821939],
              [57100, 59000, 56800, 58900, 16537065]])

pred = pred.reshape((1, 5, 5))
aaa = model.predict(pred, batch_size=1)
print('aaa: ', aaa)

y_prd = model.predict(x_test, batch_size=1)

from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: ", RMSE(y_test, y_prd))
