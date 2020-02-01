from numpy import array
x = array([1, 2, 3, 4, 5])

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(x)
x = sc.transform(x)
print(x)

