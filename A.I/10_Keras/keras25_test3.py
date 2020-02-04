import pandas as pd
import numpy as np

data1 = pd.read_csv('./data/samsung.csv')
data2 = pd.read_csv('./data/kospi200.csv')
print(data1)
print(data2)

data1 = data1.sort_values(by='date', ascending=True)
data2 = data2.sort_values(by='date', ascending=True)

del data1['date']
del data2['date']
print(data1)
print(data2)

data1.astype(float)
data2.astype(float)

data1 = np.asarray(data1)
data2 = np.asarray(data2)
print(data1)
print(data2)

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

x1, y1 = split_sequence(data1, 5)
x2, y2 = split_sequence(data2, 5)

print(x1)
print(y1)
print(x2)
print(y2)

from sklearn.model_selection import train_test_split

x1_train, x1_test, x2_train, x2_test, y1_train, y1_test = train_test_split(x1, x2, y1, train_size=0.6, random_state=66, shuffle=False)
x1_test, x1_val, x2_test, x2_val, y1_test, y1_val = train_test_split(x1_test, x2_test, y1_test, test_size=0.5, random_state=66, shuffle=False)

print(x1_train.shape) # (252, 5, 5)

x1_train = x1_train.reshape(-1, 25)
x1_val = x1_val.reshape(-1, 25)
x1_test = x1_test.reshape(-1, 25)

x2_train = x2_train.reshape(-1, 25)
x2_val = x2_val.reshape(-1, 25)
x2_test = x2_test.reshape(-1, 25)

print(x1_train.shape)


from keras.models import Sequential, Model
from keras.layers import Dense, Input

input1 = Input(shape=(25,)) # 인풋레이어 정의 
dense1 = Dense(64)(input1) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense2 = Dense(32)(dense1) # 계속 인풋과 아웃풋을 정의
dense3 = Dense(16)(dense2)
output1 = Dense(1)(dense3)

input2 = Input(shape=(25,)) # 인풋레이어 정의 
dense21 = Dense(64)(input2) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense23 = Dense(32)(dense21)
output2 = Dense(16)(dense23)

from keras.layers.merge import Concatenate # 2. class형 Concatenate
merge1 = Concatenate()([output1, output2])

middle1 = Dense(32)(merge1)
middle2 = Dense(16)(middle1)
output = Dense(1)(middle2)

model = Model(inputs = [input1, input2], outputs = output)

# 모델 요약
model.summary()

# 훈련
model.compile(loss='mse', optimizer='adam', metrics=["mse"]) # kinds of loss = [mse, mae]

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

model.fit([x1_train, x2_train], [y1_train], validation_data=([x1_val, x2_val], [y1_val]), epochs = 1000, batch_size= 1, callbacks=[early_stopping]) # epochs number changeable

# 평가예측
loss, mse = model.evaluate([x1_test, x2_test], y1_test, batch_size=1)
print('loss: ', loss)
print('mse: ', mse)


from numpy import array

pred1 = array([[   60500,    62600,    60400 ,   62300 ,15339565],
  [   61800 ,   61800  ,  60700 ,   60800, 14916555],
  [   59400 ,   59400  ,  58300 ,   58800, 23664541],
  [   59100 ,   59700 ,   58800,    59100, 16446102],
  [   58800 ,   58800 ,   56800 ,   57200 ,20821939]])

pred2 = array([[   301.79  ,  306.52  ,  301.16  ,  306.08 , 79333.  ],
  [   303.77  ,  304.72  ,  301.71 ,   302.33,  86908.  ],
  [   294.98  ,  296.3   ,  291.3  ,   292.77, 130172.  ],
  [   294.38  ,  295.67  ,  292.45  ,  293.98,  85731.  ],
  [   293.27  ,  294.11  ,  287.09  ,  288.37, 101535.  ]])

pred1 = pred1.reshape(-1, 25)
pred2 = pred2.reshape(-1, 25)

aaa = model.predict([pred1, pred2], batch_size=1)
print("aaa: ", aaa)

y1_prd = model.predict([x1_test, x2_test], batch_size=1)

from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: ", RMSE(y1_test, y1_prd))
