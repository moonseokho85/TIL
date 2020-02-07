import numpy as np
import pandas as pd

kospi200 = np.load('./samsung/data/kospi200.npy')
samsung = np.load('./samsung/data/samsung.npy')

print(samsung)
print(samsung.shape)

print(kospi200)
print(kospi200.shape)

# Split Function
def split_xy5(dataset, time_steps, y_column):
    x, y = list(), list()
               
    for i in range(len(dataset)):
        x_end_number = i + time_steps
        y_end_number = x_end_number + y_column
        
        if y_end_number > len(dataset):
            break
        
        tmp_x = dataset[i:x_end_number, :]
        tmp_y = dataset[x_end_number: y_end_number, 3]
        
        x.append(tmp_x)
        y.append(tmp_y)
        
    return np.array(x), np.array(y)


x, y = split_xy5(samsung, 25, 5)
print(x.shape)
print(y.shape)
print(x[0,:], '/', y[0])

# DataSet Split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3, shuffle=False)

print(x_train.shape)
print(x_test.shape)

# Data Reshape
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))

# Data Preprocessing (StandardScaler)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

print(x_train_scaled[0, :])

# Data Reshape to LSTM
x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 25, 5))
x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 25, 5))

from keras.models import Sequential
from keras.layers import Dense, LSTM

model = Sequential()
model.add(LSTM(64, activation='relu', input_shape=(25, 5)))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(5))

# 모델 요약
model.summary()

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["mae"]) # kinds of loss = [mae, mae]

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1, epochs=1000, batch_size=1, callbacks=[early_stopping])

loss, mae = model.evaluate(x_test_scaled, y_test, batch_size=1)
print('loss: ', loss)
print('mae: ', mae)

y_pred = model.predict(x_test_scaled)

for i in range(5):
    print('종가: ', y_test[i], '/ 예측가: ', y_pred[i])