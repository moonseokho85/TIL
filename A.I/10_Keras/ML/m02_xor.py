from sklearn.svm import LinearSVC, SVC
from sklearn.metrics import accuracy_score

# Data
x_train = [[0, 0], [1, 0], [0, 1], [1, 1]]
y_train = [0, 1, 1, 0]

x_test = [[0, 0], [1, 0], [0, 1], [1, 1]]

# Model
model = SVC()

# Model Fitting
model.fit(x_train, y_train)

# Evaluating and Prediction
y_predict = model.predict(x_test)
print(x_test, "의 예측결과: ", y_predict)
print("acc = ", accuracy_score([0, 1, 1, 0], y_predict))