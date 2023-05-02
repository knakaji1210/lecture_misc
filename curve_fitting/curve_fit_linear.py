# example of linear curve fitting

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

list_linear_x = range(0,50,1)

array_error = np.random.normal(size=len(list_linear_x))

array_x = np.array(list_linear_x)
array_y = array_x + array_error

def linear_fit(x, a, b):
    return a*x + b

param, cov = curve_fit(linear_fit, array_x, array_y)

array_y_fit = param[0] * array_x + param[1]

plt.scatter(array_x, array_y)
plt.plot(array_x, array_y_fit)
plt.show()