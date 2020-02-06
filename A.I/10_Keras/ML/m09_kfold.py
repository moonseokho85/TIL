import pandas as pd

# Loading Data of iris
iris_data = pd.read_csv('./data/iris2.csv', encoding='utf-8')

# Spliting Data to Input data and Label
y = iris_data.loc[:, "Name"]
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]

# Extracting All classifier algorithm
import warnings
warnings.filterwarnings('ignore')
from sklearn.utils.testing import all_estimators
allAlgorithms = all_estimators(type_filter="classifier")

from sklearn.model_selection import KFold
kfold_cv = KFold(n_splits=10, shuffle=True)

print(allAlgorithms)
print(len(allAlgorithms))
print(type(allAlgorithms))

for (name, algorithm) in allAlgorithms:
    
    # Producing each algorithms
    clf = algorithm()
    
    if hasattr(clf, 'score'):
        from sklearn.model_selection import cross_val_score
        scores = cross_val_score(clf, x, y, cv=kfold_cv) # cross_val_score function include model.fit
        import numpy as np
        a = np.array(scores)
        AVG = np.mean(a)
        print(name, "의 정답률: ")
        print(AVG)