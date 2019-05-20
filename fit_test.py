import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from lmfit import Model
from lmfit.models import GaussianModel, ConstantModel, VoigtModel, LorentzianModel


def sine_func(x, a, b):
    return a*np.sin(b*x)

def Gauss(x, a, xc, sigma, bl):
    """ returns a gaussiun function where a is amplitude, x0 is peak position, sigma  is the peak width, bl is offset.
    """
    return a * np.exp(-(x - xc) ** 2 / (2 * sigma ** 2)) + bl

def fit_scipy_opt(xdata, ydata):
    fit_params = optimize.curve_fit(sine_func, xdata, ydata, p0=[1,0.3])
    return fit_params[0]

def fit_lm_sin(xdata, ydata):
    sinemodel = Model(sine_func)
    params = sinemodel.make_params(a=1, b=0.1)
    result = sinemodel.fit(ydata, params, x=xdata)
    # result = sinemodel.fit(ydata, x=xdata, a=1, b=0.1) #params not required this way

    return result

def fit_gauss(x,y,inits):
    fit_params = optimize.curve_fit(Gauss, x, y, p0=inits)
    # fit_params = optimize.curve_fit(Gauss, x, y, p0=[4, 40000, 4000, 0])
    return fit_params

def fit_lm_g(x,y,inits): ##https://stackoverflow.com/questions/44573896/python-fit-gaussian-to-noisy-data-with-lmfit
    # gmodel = LorentzianModel()
    # gmodel = VoigtModel()
    gmodel = GaussianModel()
    cmodel = ConstantModel()
    model = gmodel + cmodel
    params = model.make_params(sigma = inits[2], amplitude = inits[0], center  = inits[1])
    result = model.fit(y, params, x=x)
    # print(params)
    return result

np.random.seed(0)

size = 200
## generate xdata
xdata = np.linspace(-100, 100, size)

## generate ydata from xdata and added some noise
ydata1 = Gauss(xdata, 10,15,10,-5)
# ydata1 = 1*np.sin(np.pi*xdata*0.1)
ydata2 = ydata1 + np.random.normal(scale=0.5, size=size)

## plot data
plt.plot(xdata, ydata1, 'k-', label=" actual data") #plots blue line
plt.plot(xdata, ydata2, '-', c='gray', label="data with noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend(loc='upper left') #label showing after using this

## fit the data and get the parameters
a, xc, sigma, bl = fit_gauss(xdata, ydata2, [2,0,10,0])[0]
reslt = fit_lm_g(xdata, ydata2, [2,0,10,0])
# a, b = fit_scipy_opt(xdata, ydata2)
# reslt = fit_lm_sin(xdata, ydata2)
print(reslt.fit_report())

## plot fitted data on original data
# plt.plot(xdata, Gauss(xdata, a, xc, sigma, bl), c='r', linestyle='dashed', label="fit") #label not showing
plt.plot(xdata, reslt.best_fit, c='r', linestyle='dashed', label="fit") #label not showing
# plt.plot(xdata, reslt.best_fit, c='r', linestyle='dashed', label="fit") #label not showing
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