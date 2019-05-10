import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

a = np.cos(2*np.pi*np.linspace(0, 1, 60.))

ax1.plot(range(60), a, '--')
ax2.plot(range(60), np.ones(60), 'o')  # Create a dummy plot
# ax2.cla() # hides the plot
ax2.lines = [10, 20, 30, 50]
plt.show()
"""
data = pd.DataFrame({'x': list(range(1, 20, 1)), 'y': list(
    range(10, 200, 10)), 'z': list(range(100, 2000, 100))})

# data1=data[['x', 'y', 'z']].add(data['x'].values, axis=0)
# data1 = data['x', 'y', 'z']# - data['x']
print(data['x'])
print(data.loc[:, 'x'])
print(data.iloc[:, 0])
# print(data['x'][0:3])
"""
