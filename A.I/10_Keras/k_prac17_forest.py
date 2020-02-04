import pandas as pd
import numpy as np

df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', '0D280/0D315 of diluted wines', 'Proline']

print('클래스 레이블', np.unique(df_wine['Class label']))

print(df_wine.head())

from sklearn.ensemble import RandomForestClassifier

# 특성 추출
feat_labels = df_wine.columns[1:]
print(feat_labels)

X, y = df_wine.iloc[:, 1:].values, df_wine[:, 0].values
print(X)
print(X.shape)

# Data Split to Train and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)

print(X_train)
print(X_train.shape)
'''
forest = RandomForestClassifier(n_estimators=500, random_state=1)
forest.fit()
'''