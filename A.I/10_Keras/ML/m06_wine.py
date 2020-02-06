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
