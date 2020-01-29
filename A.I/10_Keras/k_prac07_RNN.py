import numpy as np

timesteps = 100 # 입력 시퀀스에 있는 타임스텝의 수
input_features = 32 # 입력 특성의 차원
output_features = 64 # 출력 특성의 차원

inputs = np.random.random((timesteps, input_features)) # 입력 데이터
print("inputs: ", inputs)
print("Shape of inputs: ", inputs.shape)

state_t = np.zeros((output_features,)) # 초기 상태: 모두 0인 벡터
print("state_t: ", state_t)
print("Shape of state_t: ", state_t.shape)

# 랜덤한 가중치 행렬 생성
W = np.random.random((output_features, input_features))
print("Shape of W: ", W.shape)

U = np.random.random((output_features, output_features))
print("Shape of U: ", U.shape)

b = np.random.random((output_features,))
print("Shape of b: ", b.shape)

successive_outputs = []

for input_t in inputs: # input_t는 크기가 (input_features,)인 벡터
    
    output_t = np.tanh(np.dot(W, input_t) + np.dot(U, state_t) + b) # 입력과 현재 상태(이전 출력)를 연결하여 현재 출력을 얻습니다.
    # print("output_t: ", output_t)
    
    successive_outputs.append(output_t)
    # print("successive_outputs: ", successive_outputs)
    
    state_t = output_t # 다음 타임스텝을 위해 네트워크의 상태를 업데이트 합니다.
    
final_output_sequence = np.stack(successive_outputs, axis= 0) # 최종 출력은 크기가 (timesteps, output_features)인 2D 텐서입니다.