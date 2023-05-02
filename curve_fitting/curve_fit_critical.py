# example of non-linear curve fitting

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

pc = 0.6
range_l = int(pc*100-50)
range_u = int(pc*100)

list_x = [i / 100 for i in range(range_l,range_u,1)]
array_x = np.array(list_x)

print(array_x)

list_y = []
list_y_fit = []

for num in array_x:
    list_y.append(3*(pc - num)**(-1) + 0.5 * np.random.rand())

array_y= np.array(list_y)

def power_fit(x, a, b):
    return  a*(pc - x)**b

param, cov = curve_fit(power_fit, array_x, array_y, p0=[3, -1])

print(param)

for num in array_x:
    list_y_fit.append( param[0]*(pc - num)**param[1] )

array_y_fit= np.array(list_y_fit)

plt.scatter(array_x, array_y, c='red')
plt.plot(array_x, array_y_fit)
plt.show()