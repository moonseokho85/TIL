# 케라스에서 MNIST 데이터셋을 적재합니다.
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 훈련 데이터를 살펴봅니다.
print("shape: ", train_images.shape)
print("label_count: ", len(train_labels))
print(train_labels)
print(train_labels.shape)

# 테스트 데이터를 살펴봅니다.
print("shape: ", test_images.shape)
print("label_count: ", len(test_labels))
print(test_labels)
print(test_labels.shape)

# 모델 구성
from keras import models
from keras import layers

network = models.Sequential()

network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

# 모델 요약
network.summary()

# 컴파일 단계
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# 이미지 데이터 준비하기
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_labels = test_images.astype('float32') / 255

# 레이블 준비하기
from keras.utils import to_categorical

train_images = to_categorical(train_labels)
test_images = to_categorical(test_labels)

# 모델 훈련
network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('accuracy: ', test_acc)
