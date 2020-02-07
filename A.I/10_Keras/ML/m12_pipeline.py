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


model = Pipeline([("scaler", MinMaxScaler()), ('svm', SVC())])

#### Fitting Model
model.fit(x_train, y_train)

print("Test score: ", model.score(x_test, y_test))