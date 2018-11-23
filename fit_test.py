import numpy as np

import matplotlib.pyplot as plt
from scipy import optimize

def sin_func(x, a, b):
    return a*np.sin(b*x)

np.random.seed(0)

size = 200
## generate xdata
xdata = np.linspace(-10, 10, size)

## generate ydata from xdata with some noise added in next step
ydata1 = 2*np.sin(np.pi*xdata*0.5)
ydata2 = ydata1 + np.random.normal(scale=0.2, size=size)

## plot data
# plt.plot(xdata, ydata1) #plots blue line
plt.scatter(xdata, ydata2, c='gray', marker='o', label="data")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend(loc='upper left') #label showing after using this

## fit the data and get the parameters
fit_data = optimize.curve_fit(sin_func, xdata, ydata2)

a, b = fit_data[0]

## plot fitted data on original data
plt.plot(xdata, sin_func(xdata, a, b), c='r', linestyle='dashed', label="fit") #label not showing
# plt.Line2D(xdata, sin_func(xdata, a, b), color='r', linestyle='dashed', label="fit")
plt.legend(loc='upper left') #label showing after using this

# print(fit_data)

plt.show()

    
"""## Plots data in interactive mode!
plt.ion()
for i in range(50):
    y = np.random.random([10,1])
    plt.plot(y)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
"""