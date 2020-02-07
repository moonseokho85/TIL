import pandas as pd

#### Loading Data of iris ####
iris_data = pd.read_csv('./data/iris2.csv', encoding='utf-8')

#### Spliting Data to Input data and Label ####
y = iris_data.loc[:, "Name"]
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]

#### Spliting Data to Train and Test set ####
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

#### Extracting All classifier algorithm ####
warnings.filterwarnings('ignore')
from sklearn.utils.testing import all_estimators
allAlgorithms = all_estimators(type_filter="classifier")
print(allAlgorithms)
print(len(allAlgorithms))
print(type(allAlgorithms))

for (name, algorithm) in allAlgorithms:
    
    # Producing each algorithms
    clf = algorithm()
    
    # Fitting and predicting
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    
    # Scoring models
    from sklearn.metrics import accuracy_score
    print(name, "의 정답률: ", accuracy_score(y_test, y_pred))