from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Data
x_train = [[0, 0], [1, 0], [0, 1], [1, 1]]
y_train = [0, 1, 1, 0]

x_test = [[0, 0], [1, 0], [0, 1], [1, 1]]

# List to Array
from numpy import array

x_train = array(x_train)
y_train = array(y_train)
x_test = array(x_test)

print(x_train.shape)

# Model
# model = LinearSVC()
# model = KNeighborsClassifier(n_neighbors=1)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(2, )))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Model Compiling
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

# Model Fitting
model.fit(x_train, y_train, batch_size=1, epochs=100)

# Evaluating and Prediction
result = model.evaluate(x_test, y_train)
print("result: ", result)

y_predict = model.predict(x_test)
print(x_test, "의 예측결과: ", y_predict)
print("acc = ", accuracy_score([0, 1, 1, 0], y_predict))
