import math as mt
import numpy as np
x = 3
y = np.sin(x)
print (y)
y = np.sin ( x )
print(y)

import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.plot()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()