from numpy import array
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Input

# 데이터 준비
x1 = array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [20, 30, 40], [30, 40, 50], [40, 50, 60]])
y1 = array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50, 60, 70])

# x2 = array([[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70], [60, 70, 80], [70, 80, 90], [80, 90, 100], [90, 100, 110], [100, 110, 120], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
# y2 = array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 5, 6, 7])

x2 = array([[10, 20, 30], [20, 30, 40], [30, 40, 50], [40, 50, 60], [50, 60, 70], [60, 70, 80], [70, 80, 90], [80, 90, 100], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
y2 = array([40, 50, 60, 70, 80, 90, 100, 110, 5, 6, 7])

x1 = x1.reshape(x1.shape[0], x1.shape[1], 1)
x2 = x2.reshape(x2.shape[0], x2.shape[1], 1)

# 함수형 모델 
# 시퀀셜 모델의 단점 : 순차적으로 하니까 쉽긴 한데 딱 한가지 모델만 만들어야함
# 함수형 모델은 모델끼리 붙이고 합치고가 가능함 = 앙상블 모델을 구성하는등에 사용

input1 = Input(shape=(3, 1)) # 인풋레이어 정의 
model1 = LSTM(64, activation='relu')(input1) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
model1 = Dense(32)(model1) # 계속 인풋과 아웃풋을 정의

input2 = Input(shape=(3, 1)) # 인풋레이어 정의 
model2 = LSTM(64, activation='relu')(input2) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
model2 = Dense(32)(model2)

# from keras.layers.merge import concatenate # 1. 함수형 concatenate
# merge1 = concatenate([output1, output2])

from keras.layers.merge import Concatenate, Add, Multiply # 2. class형 Concatenate
# merge1 = Concatenate()([output1, output2])
merge1 = Multiply()([model1, model2])

middle1 = Dense(4)(merge1)
middle2 = Dense(7)(middle1)

output1 = Dense(1)(middle2)
output2 = Dense(1)(middle2)

model = Model(inputs = [input1, input2], outputs = [output1, output2]) #하단부에 모델을 정의

# 모델 구성
# model = Sequential()
# model.add(LSTM(64, activation='relu', input_shape=(3, 1))) # 3: column number & 1: 몇개씩 자르는지
# model.add(Dense(128))
# model.add(Dense(256))
# model.add(Dense(512))
# model.add(Dense(256))
# model.add(Dense(128))
# model.add(Dense(64))
# model.add(Dense(32))
# model.add(Dense(1))

model.summary()

model.compile(loss= 'mse', optimizer= 'adam', metrics= ['mae'])

# EarlyStopping 선언
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

# 모델 훈련
model.fit([x1, x2], [y1, y2], epochs= 100000, verbose= 1, batch_size= 3, callbacks=[early_stopping])


# 평가 예측
result = model.evaluate([x1, x2], [y1, y2], batch_size= 3)
print('result: ', result)

x_input1 = array([[6.5, 7.5, 8.5], [50, 60, 70], [70, 80, 90], [100, 110, 120]]) # (3,) -> (1, 3) -> (1, 3, 1)
x_input1 = x_input1.reshape(4, 3, 1)

x_input2 = array([[6.5, 7.5, 8.5], [50, 60, 70], [70, 80, 90], [100, 110, 120]]) # (3,) -> (1, 3) -> (1, 3, 1)
x_input2 = x_input2.reshape(4, 3, 1)

y_predict = model.predict([x_input1, x_input2])
print("y_predict: ", y_predict)
