import numpy as np
import pandas as pd

kospi200 = np.load('./samsung/data/kospi200.npy')
samsung = np.load('./samsung/data/samsung.npy')

print(samsung)
print(samsung.shape)

print(kospi200)
print(kospi200.shape)

def split_xy5(dataset, time_steps, y_column):
    x, y = list(), list()
               
    for i in range(len(dataset)):
        x_end_number = i + time_steps
        y_end_number = x_end_number + y_column
        
        if y_end_number > len(dataset):
            break
        
        tmp_x = dataset[i:x_end_number, :]
        tmp_y = dataset[x_end_number: y_end_number, 3]
        
        x.append(tmp_x)
        y.append(tmp_y)
        
    return np.array(x), np.array(y)

x, y = split_xy5(samsung, 5, 1)
print(x.shape)
print(y.shape)
print(x[0,:], '/', y[0])
