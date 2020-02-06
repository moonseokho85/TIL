import numpy as np
import tensorflow as tf

seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

# Data Load
dataset = np.loadtxt('./data/pima-indians-diabetes.csv', delimiter=',')
X = dataset[:, 0:8]
Y = dataset[:, 8]

print(X)

# Model
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Model Compiling
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Model Fitting
model.fit(X, Y, batch_size=10, epochs=200)

# Print Result
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))
