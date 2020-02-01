from numpy import array

def split_sequence(sequence, n_steps):
    x, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps
        if end_ix > len(sequence) - 1:
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)

dataset = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

n_steps = 3

x, y = split_sequence(dataset, n_steps)

for i in range(len(x)):
    print(x[i], y[i])
    
print(x.shape)
print(y.shape)
    
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

# model.add(Dense(5, input_dim=3))
model.add(Dense(64, input_shape=(3,)))
model.add(Dense(38))
model.add(Dense(1))

# 모델 요약
model.summary()

model.compile(loss='mse', optimizer='adam', metrics=["mae"]) # kinds of loss = [mse, mae]

# EarlyStopping 선언
from keras.callbacks import EarlyStopping, TensorBoard

early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

tb_hist = TensorBoard(log_dir='./graph', histogram_freq=0, write_grads=True, write_images=True)

# 모델 훈련
model.fit(x, y, epochs=100000, batch_size=1, callbacks=[early_stopping, tb_hist]) # epochs number changeable

# 평가 예측
loss, mse = model.evaluate(x, y, batch_size=1)
print('loss: ', loss)
print('mse: ', mse)

import numpy as np
x_prd = np.array([[90, 100, 110]])
print(x_prd.shape)

y_prd = model.predict(x_prd, batch_size=1)
print("y_prd: ", y_prd)