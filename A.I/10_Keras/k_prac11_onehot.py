import numpy as np

# 데이터
samples = ['The cat sat on the mat.', 'The dog ate my homework.']

print(len(samples))

# 데이터에 있는 모든 토큰의 인덱스를 구축합니다.
token_index = {}
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index) + 1

# 샘플을 벡터로 변환합니다. 각 샘플에서 max_length까지 단어만 사용합니다.
max_length = 10

# 결과를 저장할 배열입니다.
results = np.zeros(shape=(len(samples), max_length, max(token_index.values()) + 1))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        results[i, j, index] = 1.