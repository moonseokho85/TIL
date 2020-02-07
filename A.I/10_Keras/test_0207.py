import requests
import bs4
import pandas as pd
import time

price_url = 'https://fchart.stock.naver.com/sise.nhn?symbol=005930&timeframe=day&count=1500&requestType=0'
price_data = requests.get(price_url)
# print(price_data)

price_data_bs = bs4.BeautifulSoup(price_data.text, 'lxml')
# print(price_data_bs)

item_list = price_data_bs.find_all('item')
# print(item_list)

temp = item_list[0]['data']
temp.split('|')
# print(temp)

for item in item_list:
    temp_data = item['data']
    datas = temp_data.split('|')
#     print(datas[0], datas[1], datas[2], datas[3], datas[4], datas[5])
    
date_list = []
start_price = []
high_price = []
low_price = []
end_price = []
tx_amount = []

for item in item_list:
    temp_data = item['data']
    datas = temp_data.split('|')
    date_list.append(datas[0])
    start_price.append(datas[1])
    high_price.append(datas[2])
    low_price.append(datas[3])
    end_price.append(datas[4])
    tx_amount.append(datas[5])
    
df = pd.DataFrame({'시가': start_price, '고가': high_price, '저가': low_price, '종가': end_price, '거래량': tx_amount}, index=date_list)
# print(df)

df.drop('20200207', inplace=True)
# print(df)

df = df.astype(float)

# print(df.dtypes)

import numpy as np
data = np.asarray(df)
# print(data)

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

x1, y1 = split_sequence(data, 5)
# print(x1)
print(y1)

price_url = 'https://fchart.stock.naver.com/sise.nhn?symbol=KPI200&timeframe=day&count=1500&requestType=0'
price_data = requests.get(price_url)
# print(price_data)

price_data_bs = bs4.BeautifulSoup(price_data.text, 'lxml')
# print(price_data_bs)

item_list = price_data_bs.find_all('item')
# print(item_list)

temp = item_list[0]['data']
temp.split('|')
# print(temp)

for item in item_list:
    temp_data = item['data']
    datas = temp_data.split('|')
#     print(datas[0], datas[1], datas[2], datas[3], datas[4], datas[5])
    
date_list = []
start_price = []
high_price = []
low_price = []
end_price = []
tx_amount = []

for item in item_list:
    temp_data = item['data']
    datas = temp_data.split('|')
    date_list.append(datas[0])
    start_price.append(datas[1])
    high_price.append(datas[2])
    low_price.append(datas[3])
    end_price.append(datas[4])
    tx_amount.append(datas[5])
    
df = pd.DataFrame({'시가': start_price, '고가': high_price, '저가': low_price, '종가': end_price, '거래량': tx_amount}, index=date_list)
# print(df)

df.drop('20200207', inplace=True)
# print(df)

df = df.astype(float)

# print(df.dtypes)

import numpy as np
data2 = np.asarray(df)
# print(data2)

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

x2, y2 = split_sequence(data2, 5)
# print(x2)
# print(y2)

from sklearn.model_selection import train_test_split

x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, train_size=0.7, random_state=66, shuffle=False)
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, train_size=0.7, random_state=66, shuffle=False)

# print(x_train.shape)

#### Scaler ####
# Data Reshape
x1_train = np.reshape(x1_train, (x1_train.shape[0], x1_train.shape[1] * x1_train.shape[2]))
x1_test = np.reshape(x1_test, (x1_test.shape[0], x1_test.shape[1] * x1_test.shape[2]))

x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2]))
x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2]))

# Data Preprocessing (StandardScaler)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x1_train)
x1_train = scaler.transform(x1_train)
x1_test = scaler.transform(x1_test)

scaler.fit(x2_train)
x2_train = scaler.transform(x2_train)
x2_test = scaler.transform(x2_test)

# Data Reshape to LSTM
x1_train = np.reshape(x1_train, (x1_train.shape[0], 25, 1))
x1_test = np.reshape(x1_test, (x1_test.shape[0], 25, 1))

x2_train = np.reshape(x2_train, (x2_train.shape[0], 25, 1))
x2_test = np.reshape(x2_test, (x2_test.shape[0], 25, 1))

#### DL ####
from keras.models import Sequential, Model
from keras.layers import Dense, Input, LSTM, Dropout

input1 = Input(shape=(25, 1)) # 인풋레이어 정의 
dense1 = LSTM(64)(input1) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense1 = Dropout(0.3)(dense1)
dense1 = Dense(32)(dense1) # 계속 인풋과 아웃풋을 정의
dense1 = Dense(16)(dense1)
output1 = Dense(1)(dense1)

input2 = Input(shape=(25, 1)) # 인풋레이어 정의 
dense2 = LSTM(64)(input2) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense2 = Dropout(0.3)(dense2)
dense2 = Dense(32)(dense2)
output2 = Dense(16)(dense2)

from keras.layers.merge import Concatenate # 2. class형 Concatenate
merge1 = Concatenate()([output1, output2])

middle1 = Dense(32)(merge1)
middle2 = Dense(16)(middle1)
output = Dense(1)(middle2)

model = Model(inputs = [input1, input2], outputs = output)

# from keras.utils import multi_gpu_model
# model = multi_gpu_model(model, gpus=4)

# 모델 요약
model.summary()

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["mae"]) # kinds of loss = [mse, mae]

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=50, mode='auto')

model.fit([x1_train, x2_train], y1_train, validation_split=0.2, epochs=1000, batch_size=50, callbacks=[early_stopping]) # epochs number changeable

# 평가예측
loss, mae = model.evaluate([x1_test, x2_test], y1_test, batch_size=50)
print('loss: ', loss)
print('mae: ', mae)

pred1 = array([[   58800.  ,  58800.  ,  56800.  ,  57200., 20821939.],
              [   57800.  ,  58400.  ,  56400.  ,  56400., 19749457.],
              [   55500.  ,  57400. ,   55200.  ,  57200., 23995260.],
              [   57100.   , 59000. ,   56800.   , 58900., 21800192.],
              [   60000.   , 60200.  ,  58900.   , 59500., 19278165.]])

pred2 = array([[280.17, 286.24, 279.78 ,285.05, 111063],
[ 285.19 ,291.38 ,285.11, 290.68, 105451],
 [293.57 ,294.26 ,290.3 ,292.02, 102639],
[294.74 ,300.98, 294.32, 300.65, 110215],
[299.59 ,300.05 ,296.17 ,296.94 ,58618]])

pred1 = pred1.reshape((1, 25, 1))
pred2 = pred2.reshape((1, 25, 1))

goal = model.predict([pred1, pred2], batch_size=50)
print('goal: ', goal)

y_prd = model.predict(x_test, batch_size=50)

from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: ", RMSE(y_test, y_prd))

##### 정답 : 60,000