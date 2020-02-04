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

x_train = x_train.reshape(-1, 25)
x_val = x_val.reshape(-1, 25)
x_test = x_test.reshape(-1, 25)
print(x_train.shape)


from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

model.add(Dense(16, input_shape=(25,)))
model.add(Dense(8))
model.add(Dense(1))

# 모델 요약
model.summary()

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["mse"]) # kinds of loss = [mse, mae]

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=150, mode='auto')

model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=1000, batch_size=1, callbacks=[early_stopping]) # epochs number changeable

# 평가예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1)
print('loss: ', loss)
print('mse: ', mse)

from numpy import array
pred = array([[   60500,    62600  ,  60400  ,  62300, 15339565],
  [   61800 ,   61800 ,   60700   , 60800, 14916555],
  [   59400 ,   59400  ,  58300   , 58800, 23664541],
  [   59100 ,   59700  ,  58800  ,  59100, 16446102],
  [   58800 ,   58800  ,  56800  ,  57200, 20821939]])

pred = pred.reshape(-1, 25)
aaa = model.predict(pred, batch_size=1)
print('aaa: ', aaa)

y_prd = model.predict(x_test, batch_size=1)

from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: ", RMSE(y_test, y_prd))
