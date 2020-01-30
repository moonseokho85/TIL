from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM, Reshape, BatchNormalization, Dropout

# 데이터 준비
x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [20, 30, 40], [30, 40, 50], [40, 50, 60]])

y = array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50, 60, 70])

print("shape of x: ", x.shape) 
print("shape of y: ", y.shape)

x = x.reshape(x.shape[0], x.shape[1], 1)

# 모델 구성
model = Sequential()
model.add(LSTM(10, input_shape=(3, 1)))
model.add(Dense(100))
model.add(Dropout(0.2)) # Dropout: 노드 수를 자동으로 줄여 효율화를 높여줍니다.
model.add(Dense(100))
model.add(BatchNormalization()) # BatchNormalization: 가중치를 정규화하여 성능을 더 좋게 합니다.
model.add(Dense(100))
model.add(Dense(100))
model.add(Dense(100))
model.add(Dense(5, activation='linear'))
model.add(Dense(1))

'''
# Reshape 모델 사용
model = Sequential()
model.add(LSTM(10, activation='relu', input_shape=(3, 1)))
model.add(Reshape((3, 1), input_shape=(64,)))
model.add(LSTM(10, activation='relu'))
model.add(Dense(32))
model.add(Dense(1))
'''

model.summary()

model.compile(loss= 'mse', optimizer= 'adam', metrics= ['mae'])

# EarlyStopping 선언
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto') # monitor의 종류: loss, acc, val_loss, val_acc

# 모델 훈련
model.fit(x, y, epochs= 100000, verbose= 1, batch_size= 3, callbacks=[early_stopping]) # 앙상블 모델일 때 입력값을 리스트 형식으로 넣어준다.

# 평가 예측
loss, mae = model.evaluate(x, y, batch_size= 3)
print("loss: ", loss)
print("mae: ", mae)

x_input = array([[6.5, 7.5, 8.5], [50, 60, 70], [70, 80, 90], [100, 110, 120]]) # (3,) -> (1, 3) -> (1, 3, 1)
x_input = x_input.reshape(4, 3, 1)

y_predict = model.predict(x_input)
print("y_predict: ", y_predict)
