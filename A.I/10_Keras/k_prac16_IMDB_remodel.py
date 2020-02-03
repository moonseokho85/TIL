from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

print(train_data[0])
print(train_labels[0])

print(max([max(sequence) for sequence in train_data]))
'''
word_index = imdb.get_word_index # word_index는 단어와 정수 인덱스를 매핑한 딕셔너리입니다.
# print(word_index)

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# print(reverse_word_index)

decoded_review = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]]) # 리뷰를 디코딩합니다. 0, 1, 2는 '패딩', '문서 시작', '사전에 없음'을 위한 인덱스이므로 3을 뺍니다.
# print(decoded_review)
'''

import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1. # result[i]에서 특정 인덱스의 위치를 1로 만듭니다.
    return results

x_train = vectorize_sequences(train_data)

x_test = vectorize_sequences(test_data)

print(x_train[0]) # (10000, )

# train_labes 타입 확인
print(train_labels.dtype)

y_train = np.asarray(train_labels).astype('float32')

y_test = np.asarray(test_labels).astype('float32')

from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

model.fit(x_train, y_train, epochs=4, batch_size=512)
print('Training finish')

results = model.evaluate(x_test, y_test)
print(results)

y_pred = model.predict(x_test)
print(y_pred)