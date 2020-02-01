from numpy import array

def split_sequence2(sequence, n_steps):
    x, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps
        if end_ix > len(sequence):
            break
        seq_x, seq_y = sequence[i:end_ix, :-1], sequence[end_ix-1, -1]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)

in_seq1 = array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
in_seq2 = array([15, 25, 35, 45, 55, 65, 75, 85, 95, 105])
out_seq = array([in_seq1[i] + in_seq2[i] for i in range(len(in_seq1))])

print(in_seq1.shape) # (10,)
print(out_seq.shape) # (10,)

in_seq1 = in_seq1.reshape(len(in_seq1), 1)
in_seq2 = in_seq2.reshape(len(in_seq2), 1)
out_seq = out_seq.reshape(len(out_seq), 1)

print(in_seq1.shape) # (10, 1)
print(in_seq2.shape) # (10, 1)
print(out_seq.shape) # (10, 1)

import numpy as np
dataset = np.hstack((in_seq1, in_seq2, out_seq))

print(dataset)

n_steps = 3

x, y = split_sequence2(dataset, n_steps)

for i in range(len(x)):
    print(x[i], y[i])
    
print(x.shape)
print(y.shape)

from keras.models import Sequential
from keras.layers import Dense, LSTM
model = Sequential()

# model.add(Dense(5, input_dim=3))
model.add(LSTM(32, activation='relu', input_shape=(3, 2)))
model.add(Dense(64))
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
loss, mae = model.evaluate(x, y, batch_size=1)
print('loss: ', loss)
print('mae: ', mae)

x_prd = array([[90, 95], [100, 105], [110, 115]])
print(x_prd.shape)

x_prd = x_prd.reshape((1, 3, 2))
print(x_prd)

y_prd = model.predict(x_prd, batch_size=1)
print('y_prd: ', y_prd)