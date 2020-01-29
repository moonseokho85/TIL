import numpy as np
# 데이터 정제
x1 = np.array([range(1,101), range(101,201), range(301,401)])
x2 = np.array([range(1001,1101), range(1101,1201), range(1301,1401)])
y1 = np.array([range(101,201)])

# 행과열 변환
x1 = np.transpose(x1)
x2 = np.transpose(x2)
y1 = np.transpose(y1)

# 데이터 Set 나누기
from sklearn.model_selection import train_test_split

x1_train, x1_test, x2_train, x2_test, y1_train, y1_test = train_test_split(x1, x2, y1, train_size=0.6, random_state=66, shuffle = False)
x1_val, x1_test, x2_val, x2_test, y1_val, y1_test = train_test_split(x1_test, x2_test, y1_test, test_size=0.5, random_state=66, shuffle = False)

# 모델 구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input

# 함수형 모델 
# 시퀀셜 모델의 단점 : 순차적으로 하니까 쉽긴 한데 딱 한가지 모델만 만들어야함
# 함수형 모델은 모델끼리 붙이고 합치고가 가능함 = 앙상블 모델을 구성하는등에 사용

input1 = Input(shape=(3,)) # 인풋레이어 정의 
dense1 = Dense(5)(input1) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense2 = Dense(2)(dense1) # 계속 인풋과 아웃풋을 정의
dense3 = Dense(3)(dense2)
output1 = Dense(1)(dense3)

input2 = Input(shape=(3,)) # 인풋레이어 정의 
dense21 = Dense(7)(input2) # 차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense23 = Dense(4)(dense21)
output2 = Dense(5)(dense23)

# 앙상블을 쓰는 이유: 두 개의 인덱스와 크기가 다른 데이터를 같게 만들려면 시간이 걸리지만 앙상블을 써서 다른 모델로 결과를 내면 좀 더 쉽게 결과를 낼 수 있습니다.

# from keras.layers.merge import concatenate # 1. 함수형 concatenate
# merge1 = concatenate([output1, output2])

from keras.layers.merge import Concatenate # 2. class형 Concatenate
merge1 = Concatenate()([output1, output2])

middle1 = Dense(4)(merge1)
middle2 = Dense(7)(middle1)
output = Dense(1)(middle2)

model = Model(inputs = [input1, input2], outputs = output) #하단부에 모델을 정의

'''
# Sequential Model
model = Sequential() 
model.add(Dense(32, input_dim = 3))
#model.add(Dense(5, input_shape = (3,)))
model.add(Dense(18))
model.add(Dense(9))
model.add(Dense(5))
model.add(Dense(1))
'''
# 모델 요약
model.summary()
# 훈련 / compile = 사람말을 기계에게 알려주기
# mse = 손실은 낮으면 좋다 여러가지가 있음
# optimizer = 통상적으로 80%으로 먹혀 들어감 대게 이걸 사용

# model.fit = 훈련
model.compile(loss='mse', optimizer = 'adam', metrics = ['mse'])
model.fit([x1_train, x2_train], [y1_train], validation_data=([x1_val, x2_val], [y1_val]), epochs = 100, batch_size= 1) # 앙상블 모델일 때 입력값을 리스트 형식으로 넣어준다.

# 평가 예측
loss, mse = model.evaluate([x1_test, x2_test], [y1_test], batch_size= 1)
print('mse: ', mse)

x1_prd = np.array([[201,202,203], [204,205,206], [207,208,209]]) #한개가 더 늘어나야함
x2_prd = np.array([[1201,1202,1203], [1204,1205,1206], [1207,1208,1209]])

x1_prd = np.transpose(x1_prd)
x2_prd = np.transpose(x2_prd)

aaa = model.predict([x1_prd, x2_prd], batch_size=1)
print("aaa: ", aaa)

# bbb = model.predict(x, batch_size=1)
# print(bbb)

y_predict = model.predict([x1_test, x2_test], batch_size=1)
print("y_predict: ", y_predict)

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE:", RMSE(y1_test, y_predict))

# R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y1_test, y_predict)
print("R2: ", r2_y_predict)
