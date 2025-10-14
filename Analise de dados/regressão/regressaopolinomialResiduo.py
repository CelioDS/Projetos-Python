
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot
from scipy.optimize import curve_fit

# rediscovery regression

# loading data from file
xs,ys = np.genfromtxt("Global_temp_anomaly_1850_2024.csv", delimiter = ",",skip_header=2,
    unpack=True)

print(ys)
def f_obj(x,a,b):
    return a * np.exp(-b*x)
param, _ = curve_fit(f_obj, xs, ys)
a, b = param
print(f' parameter: {param}') # show the parameters
#a, b = param
#print(f'line Y = {a:.5f} * + {b:.5f} ')

#graphic

x_fit = xs # use the same XS values to calculate the fitted function
y_fit = f_obj(x_fit, a ,b,) # calculates  the y-values of the fitted function
rediscovery = y_fit-ys
plt.subplot(2,1,1)
plt.plot(xs, ys,"r.", label="original data" )
plt.plot(x_fit, y_fit, "b--", label="fitted curve")
plt.legend()
plt.xlabel("XS") # places title on X axis
plt.ylabel("YS") # places title on Y axis
plt.subplot(2,1,2)
plt.plot(xs, rediscovery, "k.")
plt.xlabel("XS")
plt.ylabel("rediscovery")
plt.tight_layout()
print(f"B^2 = {np.corrcoef(ys, y_fit)[0,1]**2:3f}")
plt.show()


