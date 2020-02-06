import pandas as pd

iris_data = pd.read_csv('./data/iris.csv', encoding='utf-8', names=['a', 'b', 'c', 'd', 'y'])

y = iris_data.loc[:, 'y']
x = iris_data.loc[:, ['a', 'b', 'c', 'd']]

print(x)
print(y)

print(x.shape)
print(y.shape)

# Data split to Train and Test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.7, shuffle=True)

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