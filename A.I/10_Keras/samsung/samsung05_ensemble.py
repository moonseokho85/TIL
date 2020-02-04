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

x1, y1 = split_xy5(samsung, 5, 1)
x2, y2 = split_xy5(kospi200, 5, 1)

print(x1.shape)
print(y1.shape)
print(x1[0,:], '/', y1[0])

print(x2.shape)
print(y2.shape)
print(x2[0,:], '/', y2[0])

# DataSet Split
from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=1, test_size=0.3, shuffle=False)

from sklearn.model_selection import train_test_split
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=1, test_size=0.3, shuffle=False)

print(x1_train.shape)
print(x1_test.shape)

print(x2_train.shape)
print(x2_test.shape)

# Data Reshape (461, 5, 5) -> (461, 25)
x1_train = np.reshape(x1_train, (x1_train.shape[0], x1_train.shape[1] * x1_train.shape[2]))
x1_test = np.reshape(x1_test, (x1_test.shape[0], x1_test.shape[1] * x1_test.shape[2]))

x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2]))
x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2]))

# Data Preprocessing (StandardScaler)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x1_train)
x1_train_scaled = scaler.transform(x1_train)
x1_test_scaled = scaler.transform(x1_test)

scaler = StandardScaler()
scaler.fit(x2_train)
x2_train_scaled = scaler.transform(x2_train)
x2_test_scaled = scaler.transform(x2_test)

print(x1_train_scaled[0, :])

# Data Reshape
x1_train_scaled = np.reshape(x1_train_scaled, (x1_train_scaled.shape[0], 5, 5))
x1_test_scaled = np.reshape(x1_test_scaled, (x1_test_scaled.shape[0], 5, 5))

x2_train_scaled = np.reshape(x2_train_scaled, (x2_train_scaled.shape[0], 5, 5))
x2_test_scaled = np.reshape(x2_test_scaled, (x2_test_scaled.shape[0], 5, 5))

from keras.models import Sequential, Model
from keras.layers import Dense, Input, LSTM

input1 = Input(shape=(5, 5)) # 인풋레이어 정의 
dense1 = LSTM(64)(input1) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense1 = Dense(32)(dense1) # 계속 인풋과 아웃풋을 정의
dense1 = Dense(16)(dense1)
output1 = Dense(1)(dense1)

input2 = Input(shape=(5, 5)) # 인풋레이어 정의 
dense2 = LSTM(64)(input2) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense2 = Dense(32)(dense2)
output2 = Dense(16)(dense2)

from keras.layers.merge import Concatenate # 2. class형 Concatenate
merge1 = Concatenate()([output1, output2])

middle1 = Dense(32)(merge1)
middle2 = Dense(16)(middle1)
output = Dense(1)(middle2)

model = Model(inputs = [input1, input2], outputs = output)

# 모델 요약
model.summary()

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["mae"]) # kinds of loss = [mae, mae]

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

model.fit([x1_train_scaled, x2_train_scaled], y1_train, validation_split=0.2, verbose=1, epochs=1000, batch_size=1, callbacks=[early_stopping])

loss, mae = model.evaluate([x1_test_scaled, x2_test_scaled], y1_test, batch_size=1)
print('loss: ', loss)
print('mae: ', mae)

y_pred = model.predict([x1_test_scaled, x2_test_scaled])

for i in range(5):
    print('종가: ', y1_test[i], '/ 예측가: ', y_pred[i])