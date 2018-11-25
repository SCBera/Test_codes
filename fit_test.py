import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from lmfit import Model

def sine_func(x, a, b):
    return a*np.sin(b*x)

def fit_scipy_opt(xdata, ydata):
    fit_params = optimize.curve_fit(sine_func, xdata, ydata, p0=[1,0.3])
    return fit_params[0]

def fit_lm(xdata, ydata):
    sinemodel = Model(sine_func)
    params = sinemodel.make_params(a=1, b=0.1)
    result = sinemodel.fit(ydata, params, x=xdata)
    # result = sinemodel.fit(ydata, x=xdata, a=1, b=0.1) #params not required this way

    return result

np.random.seed(0)

size = 200
## generate xdata
xdata = np.linspace(-10, 10, size)

## generate ydata from xdata and added some noise
ydata1 = 1*np.sin(np.pi*xdata*0.1)
ydata2 = ydata1 + np.random.normal(scale=0.05, size=size)

## plot data
plt.plot(xdata, ydata1, label="data") #plots blue line
plt.scatter(xdata, ydata2, c='gray', marker='o', label="data with noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend(loc='upper left') #label showing after using this

## fit the data and get the parameters
a, b = fit_scipy_opt(xdata, ydata2)
reslt = fit_lm(xdata, ydata2)
print(a, b, reslt.fit_report())

## plot fitted data on original data
# plt.plot(xdata, sine_func(xdata, a, b), c='r', linestyle='dashed', label="fit") #label not showing
plt.plot(xdata, reslt.best_fit, c='r', linestyle='dashed', label="fit") #label not showing
plt.legend(loc='upper left') #label showing after using this

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