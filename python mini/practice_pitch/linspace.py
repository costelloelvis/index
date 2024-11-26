from numpy import linspace

v0 = 4.5
g = 9.81
t = linspace(0, 1, 1000)
y = v0*t - 0.5*g*t**2

i = 0
while y[i] >= 0:
    i += 1
    print ("y=0 at"), 0.5*(t[i-1] + t[i])

import matplotlib.pyplot as plt
plt.plot(t, y)
plt.plot(t, 0*t, ('g--'))
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()