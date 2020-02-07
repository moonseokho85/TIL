import pandas as pd

# Loading Data of iris
iris_data = pd.read_csv('./data/iris2.csv', encoding='utf-8')

# Spliting Data to Input data and Label
y = iris_data.loc[:, "Name"]
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
# print(x)
print(x.shape) # (150, 4)
# print(y)
print(y.shape) # (150, )

# Spliting Data to Train and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, train_size=0.7, shuffle=True)
print(x_train.shape) # (105, 4)
print(x_test.shape) # (45, 4)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.svm import SVC
pipe = Pipeline([("scaler", MinMaxScaler()), ('svm', SVC())])

#### Fitting Model ####
pipe.fit(x_train, y_train)

print("Test score: ", pipe.score(x_test, y_test))

print(sorted(pipe.get_params().keys()))

# Parameter
param_grid = {'svm__C': [0.001, 0.01, 0.1, 1, 10, 100],
              'svm__gamma': [0.001, 0.01, 0.1, 1, 10, 100]}

# K-Fold
from sklearn.model_selection import KFold
kfold_cv = KFold(n_splits=5, shuffle=True)

# GridSearch
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
model = GridSearchCV(pipe, param_grid, cv=kfold_cv)
model.fit(x_train, y_train)
print("Optimal parameter: ", model.best_estimator_)

# Evaluating in optimal parameter
y_pred = model.predict(x_test)
from sklearn.metrics import accuracy_score
print('Final accuracy: ', accuracy_score(y_test, y_pred))