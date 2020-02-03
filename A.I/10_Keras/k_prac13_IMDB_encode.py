from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

print(train_data[0])
print(train_labels[0])

print(max([max(sequence) for sequence in train_data]))

word_index = imdb.get_word_index # word_index는 단어와 정수 인덱스를 매핑한 딕셔너리입니다.
# print(word_index)

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# print(reverse_word_index)

decoded_review = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]]) # 리뷰를 디코딩합니다. 0, 1, 2는 '패딩', '문서 시작', '사전에 없음'을 위한 인덱스이므로 3을 뺍니다.
# print(decoded_review)

