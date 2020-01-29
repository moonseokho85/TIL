import numpy as np
# 데이터 정제
x1 = np.array([range(1,101), range(101,201), range(301,401)])
x2 = np.array([range(1001,1101), range(1101,1201), range(1301,1401)])

# y1 = np.array([range(101,201)])

y1 = np.array([range(1,101), range(101,201), range(301,401)])
y2 = np.array([range(1001,1101), range(1101,1201), range(1301,1401)])
y3 = np.array([range(1,101), range(101,201), range(301,401)])

# 행과열 변환
x1 = np.transpose(x1)
x2 = np.transpose(x2)
y1 = np.transpose(y1)
y2 = np.transpose(y2)
y3 = np.transpose(y3)

# 데이터 Set 나누기
from sklearn.model_selection import train_test_split

x1_train, x1_test, x2_train, x2_test, y1_train, y1_test, y2_train, y2_test, y3_train, y3_test = train_test_split(x1, x2, y1, y2, y3, train_size=0.6, random_state=66, shuffle = False)
x1_val, x1_test, x2_val, x2_test, y1_val, y1_test, y2_val, y2_test, y3_val, y3_test = train_test_split(x1_test, x2_test, y1_test, y2_test, y3_test, test_size=0.5, random_state=66, shuffle = False)

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
output1 = Dense(11)(dense3)

input2 = Input(shape=(3,)) #인풋레이어 정의 
dense21 = Dense(7)(input2) #차이점은 꼬랑지에 앞에 변수명을 넣어줘야함, 앙상블모델에서 필수적인 요소
dense23 = Dense(4)(dense21)
output2 = Dense(5)(dense23)

from keras.layers.merge import concatenate
merge1 = concatenate([output1, output2])

middle1 = Dense(4)(merge1)
middle2 = Dense(7)(middle1)
middle3 = Dense(1)(middle2) # 현재 merge된 마지막 레이어

output_1 = Dense(30)(middle3) # 1번째 아웃풋 모델
output_1 = Dense(3)(output_1)

output_2 = Dense(30)(middle3) # 2번째 아웃풋 모델
output_2 = Dense(5)(output_2)
output_2 = Dense(3)(output_2)

output_3 = Dense(30)(middle3) # 3번째 아웃풋 모델
output_3 = Dense(3)(output_3)


model = Model(inputs = [input1, input2], outputs = [output_1, output_2, output_3]) #하단부에 모델을 정의

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
model.compile(loss= 'mse', optimizer= 'adam', metrics= ['acc'])
model.fit([x1_train, x2_train], [y1_train, y2_train, y3_train], validation_data=([x1_val, x2_val], [y1_val, y2_val, y3_val]), epochs = 100, batch_size=58) # 앙상블 모델일 때 입력값을 리스트 형식으로 넣어준다.

# 평가 예측
result = model.evaluate([x1_test, x2_test], [y1_test, y2_test, y3_test], batch_size = 1)
print('result: ', result)


x1_prd = np.array([[201,202,203], [204,205,206], [207,208,209]]) # 한개가 더 늘어나야함
x2_prd = np.array([[1201,1202,1203], [1204,1205,1206], [1207,1208,1209]])

x1_prd = np.transpose(x1_prd)
x2_prd = np.transpose(x2_prd)

aaa = model.predict([x1_prd, x2_prd], batch_size=1)
print(aaa)

# bbb = model.predict(x, batch_size=1)
# print(bbb)

y_predict = model.predict([x1_test, x2_test], batch_size=1)
print(np.asarray(y_predict).shape) # (20, 3) * 3 list
print(y_predict[0])

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

rmse1 = RMSE(y1_test, y_predict[0])
rmse2 = RMSE(y2_test, y_predict[1])
rmse3 = RMSE(y3_test, y_predict[2])
rmse = (rmse1 + rmse2 + rmse3) / 3
print('RMSE: ', rmse)

# R2 구하기
from sklearn.metrics import r2_score
r2_y_predict1 = r2_score(y1_test, y_predict[0])
r2_y_predict2 = r2_score(y2_test, y_predict[1])
r2_y_predict3 = r2_score(y3_test, y_predict[2])
r2_y_predict = (r2_y_predict1 + r2_y_predict2 + r2_y_predict3) / 3
print("R2: ", r2_y_predict)
