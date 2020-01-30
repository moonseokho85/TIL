
import numpy as np
#1. 데이터 정제
x = np.array([range(1,101), range(101,201), range(301,401)])
y = np.array([range(101,201)])
#y2 = np.array(range(101, 201))

print(x.shape) #(3,100)
print(y.shape) #(1,100)
#print(y2.shape) #(100,)


x = np.transpose(x)  #행과열 변환
y = np.transpose(y)

print(x.shape) #(2,10)
print(y.shape) #(2,10)

from sklearn.model_selection import train_test_split

#X_train, X_test = train_test_split(x, test_size=0.6)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6, random_state=66,shuffle = False)

x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size=0.5, random_state=66,shuffle = False)

#####################

#2. 모델구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input
#model = Sequential() 

#함수형 모델 
# 시퀀셜 모델의 단점 : 순차적으로 하니까 쉽긴 한데 딱 한가지 모델만 만들어야함
# 함수형 모델은 모델끼리 붙이고 합치고가 가능함 = 앙상블 모델을 구성하는등에 사용


# input1 = Input(shape=(3,)) # 인풋레이어 정의 
# dense1 = Dense(5)(input1) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
# dense2 = Dense(2)(dense1) # 계속 인풋과 아웃풋을 정의
# dense3 = Dense(3)(dense2)
# output1 = Dense(1)(dense3)

input1 = Input(shape=(3,)) # 인풋레이어 정의 
x = Dense(5)(input1) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
x = Dense(2)(x) # 계속 인풋과 아웃풋을 정의
x = Dense(3)(x)
output1 = Dense(1)(x)

model = Model(inputs = input1, outputs = output1) # 함수형 모델의 특징: 하단부에 모델을 정의


'''
#시퀀셜 모델
model.add(Dense(32, input_dim = 3))
#model.add(Dense(5, input_shape = (3,)))
model.add(Dense(18))
model.add(Dense(9))
model.add(Dense(5))
model.add(Dense(1))
'''

model.summary()
##훈련 / compile = 사람말을 기계에게 알려주기
# mse = 손실은 낮으면 좋다 여러가지가 있음
# optimizer = 통상적으로 80%으로 먹혀 들어감 대게 이걸 사용

#3. model.fit = 훈련
model.compile(loss='mse', optimizer = 'adam', metrics = ['mse'])
model.fit(x_train, y_train, validation_data=(x_val,y_val), epochs = 100, batch_size=58)

#4. 평가 예측
loss, mse = model.evaluate(x_test,y_test, batch_size = 1)
print('mse: ' , mse)

x_prd = np.array([[201,202,203], [204,205,206],[207,208,209]]) #한개가 더 늘어나야함
x_prd = np.transpose(x_prd)

aaa = model.predict(x_prd, batch_size=1)
print(aaa)

# bbb = model.predict(x, batch_size=1)
# print(bbb)

y_predict = model.predict(x_test, batch_size=1)
# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE:", RMSE(y_test, y_predict))

#R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2: ", r2_y_predict)
