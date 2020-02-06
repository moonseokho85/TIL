import pandas as pd

# Loading Data
wine = pd.read_csv('./data/winequality-white.csv', sep=';', encoding='utf-8')

count_data = wine.groupby('quality')['quality'].count()
print(count_data)

count_data.plot()

import matplotlib.pyplot as plt
plt.savefig('wine-count-plt.png')
plt.show()