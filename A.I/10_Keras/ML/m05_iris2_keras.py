import pandas as pd

iris_data = pd.read_csv('./data/iris3.csv', encoding='utf-8', names=['a', 'b', 'c', 'd', 'y'])

y = iris_data.loc[1:, 'y']
x = iris_data.loc[1:, ['a', 'b', 'c', 'd']]

print(x)
print(y)

print(x.shape)
print(y.shape)

# Data split to Train and Test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.7, shuffle=True)

# One-Hot Encoding
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
print(y_train)
print(y_test)

# Model
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(64, input_shape=(4, ), activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(4, activation='softmax'))

# Model Compiling
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Model Fitting
model.fit(x_train, y_train, batch_size=10, epochs=200)

# Print Result
print("\n Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))

y_pred = model.predict(x_test)
print(y_pred)

'''
# Model
from sklearn.svm import SVC
clf = SVC()

# Model Fitting
clf.fit(x_train, y_train)

# Prediction
y_pred = clf.predict(x_test)

# Accuracy Check
from sklearn.metrics import accuracy_score
print('정답률: ', accuracy_score(y_test, y_pred))
'''