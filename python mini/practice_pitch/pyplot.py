import matplotlib.pyplot as plt

x = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 100, 81, 64, 49, 36, 25, 16,  9,  1]


plt.plot(x , y)
plt.xlabel('Time(s)')
plt.ylabel('Temperature(degC)')
plt.show()