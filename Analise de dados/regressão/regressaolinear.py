import numpy as np
import matplotlib.pyplot as plt
# linear regression


xs = np.array([0,2,5])
ys = np.array([-3.1, 2.6, 13.4])
param = np.polyfit(xs, ys, 1) # curve fitting
print(f' parameter: {param}') # show the parameters
a, b = param
print(f'line Y = {a:.5f} * + {b:.5f} ')

#graphic

x_fit = np.linspace(-0.1, 5.1, 1000)
y_fit = np.polyval(param, x_fit)
plt.plot(xs, ys,"r.", label="original data" )
plt.plot(x_fit, y_fit, "b--", label="fitted curve")
plt.legend()
plt.show()


