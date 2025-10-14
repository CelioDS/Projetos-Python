from operator import truediv

import numpy as np
import matplotlib.pyplot as plt
# polynomial regression (3rd order)

# loading data from file
xs,ys = np.genfromtxt("Global_temp_anomaly_1850_2024.csv", delimiter = ",",skip_header=2,
    unpack=True)

param = np.polyfit(xs, ys, 3) # curve fitting
print(f' parameter: {param}') # show the parameters
#a, b = param
#print(f'line Y = {a:.5f} * + {b:.5f} ')

#graphic

x_fit = xs # use the same XS values to calculate the fitted function
y_fit = np.polyval(param, x_fit) # calculates  the y-values of the fitted function
plt.figure()
plt.plot(xs, ys,"r.", label="original data" )
plt.plot(x_fit, y_fit, "b--", label="fitted curve")
plt.xlabel("XS") # places title on X axis
plt.ylabel("YS") # places title on Y axis
plt.legend()
print(f"B^2 = {np.corrcoef(ys, y_fit)[0,1]**2:3f}")
plt.show()


