from sklearn.datasets import load_boston
boston = load_boston()

# Loading data
x = boston.data
y = boston.target

print(x)
print(x.shape)

print(y)
print(y.shape)

# Spliting Data to Train and Test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Making up model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Fitting Model
model.fit(x_train, y_train)

# Predicting model
accuracy = model.score(x_test, y_test)
print("Accuracy of the LinearRegression: ", accuracy)

# Making up model
from sklearn.linear_model import Ridge
model = Ridge()

# Fitting Model
model.fit(x_train, y_train)

# Predicting model
accuracy = model.score(x_test, y_test)
print("Accuracy of the Ridge: ", accuracy)

# Making up model
from sklearn.linear_model import Lasso
model = Lasso()

# Fitting Model
model.fit(x_train, y_train)

# Predicting model
accuracy = model.score(x_test, y_test)
print("Accuracy of the Lasso: ", accuracy)
