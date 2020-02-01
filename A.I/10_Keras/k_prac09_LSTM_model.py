import keras
import numpy as np

# 말뭉치를 내려받기
path = keras.utils.get_file('nietzsche.txt', origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt')

text = open(path).read().lower()

print('말뭉치 크기: ', len(text))
print('TEXT: ', text)

maxlen = 60 # 60개의 글자로 된 시퀀스를 추출
step = 3 # 세 글자씩 건너뛰면서 새로운 시퀀스를 샘플링

sentences = [] # 추출한 시퀀스를 담을 리스트

next_chars = [] # 타깃(시퀀스 다음 글자)을 담을 리스트

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
    
print('number of sequence: ', len(sentences))

chars = sorted(list(set(text))) # 말뭉치에서 고유한 글자를 담은 리스트
print('unique word: ', len(chars))

char_indices = dict((char, char.index(char)) for char in chars) # chars 리스트에 있는 글자와 글자의 인덱스를 매핑한 딕셔너리

print('vectorizing...')

# 글자를 원-핫 인코딩하여 0과 1의 이진 배열로 바꿉니다.
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

print("shape of x: ", x.shape)
print("shape of y: ", y.shape)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1
    
print("x: ", x)
print("y: ", y)

from keras import layers

# 모델 형성
model = keras.models.Sequential()
model.add(layers.LSTM(128, input_shape=(maxlen, len(chars))))
model.add(layers.Dense(len(chars), activation='softmax'))

# 모델 컴파일 설정하기
optimizer = keras.optimizers.RMSprop(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)