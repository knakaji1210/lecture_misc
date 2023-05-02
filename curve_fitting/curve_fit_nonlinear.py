# example of non-linear curve fitting

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

list_linear_x = range(0,50,1)

array_x = np.array(list_linear_x)

list_y = []
list_y_fit = []

for num in array_x:
    list_y.append( 3 * np.exp( num /(10 + num) ) + 0.5 * np.random.rand() )

array_y= np.array(list_y)

def nonlinear_fit(x,a,b):
    return  b * np.exp(x / (a+x)  )

param, cov = curve_fit(nonlinear_fit, array_x, array_y)

print(param)

for num in array_x:
    list_y_fit.append( param[1] * np.exp( num /(param[0] + num) ))

array_y_fit= np.array(list_y_fit)

plt.scatter(array_x, array_y)
plt.plot(array_x, array_y_fit)
plt.show()