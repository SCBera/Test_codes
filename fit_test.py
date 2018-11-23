import numpy as np

import matplotlib.pyplot as plt
from scipy import optimize
#"""
def sin_func(x, a, b):
    return a*np.sin(b*x)

# def plot_show():
np.random.seed(0)

size = 200
#generate xdata
xdata = np.linspace(-10, 10, size)
#generate ydata from xdata
ydata1 = 2*np.sin(np.pi*xdata*0.5)
ydata2 = ydata1 + np.random.normal(scale=0.2, size=size)
#plot data
# plt.plot(xdata, ydata1)
plt.scatter(xdata, ydata2, c='gray', marker='o', label="data")
# plt.ion()
    # plt.show()
    # plt.pause(10)

    # return 
    # plt.draw()
    # plt.clf()
#fit the data and get the parameters
fit_data = optimize.curve_fit(sin_func, xdata, ydata2)

a, b = fit_data[0]

#plot fitted data on original data
plt.plot(xdata, sin_func(xdata, a, b), c='r', label="fit")
print(fit_data)

# while True:
plt.show()
# plt.pause(2)

    
"""
plt.ion()
for i in range(50):
    y = np.random.random([10,1])
    plt.plot(y)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
"""