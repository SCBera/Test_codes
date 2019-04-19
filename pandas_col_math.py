import pandas as pd
import numpy as np

data = pd.DataFrame({'x':[1,2,3], 'y':[2,3,4], 'z':[10,20,30]})

data1 = data[['x','y', 'z']].add(data['x'].values, axis=0)
# data1 = data['x', 'y', 'z']# - data['x']
print(data1)
