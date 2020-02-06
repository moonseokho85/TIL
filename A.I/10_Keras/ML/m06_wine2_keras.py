import pandas as pd

# Loading Data
wine = pd.read_csv('./data/winequality-white.csv', sep=';', encoding='utf-8')

# Defining data
y = wine['quality']
x = wine.drop('quality', axis=1)
print(x.shape)
print(y.shape)
# Split Data to Train and Test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# One-Hot Encoding
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
print(y_train)
print(y_test)
print(y_train.shape)
print(y_test.shape)

# Model
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(256, input_shape=(11, ), activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Model Compiling
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Model Fitting
model.fit(x_train, y_train, batch_size=5, epochs=200, validation_split=0.2)

# Print Result
print("\n Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))

'''
# Making model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

# Fitting Model
model.fit(x_train, y_train)

# Scoring Model
aaa = model.score(x_test, y_test)
print("aaa: ", aaa)

from sklearn.metrics import accuracy_score
y_pred = model.predict(x_test)
print("정답률: ", accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
'''