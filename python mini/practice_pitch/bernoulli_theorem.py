import numpy as np
import matplotlib.pyplot as plt

# Define the variables
P0 = 100  # initial pressure (Pa)
rho = 1.2  # air density (kg/m^3)
v0 = 10  # initial velocity (m/s)
A = 0.1  # cross-sectional area (m^2)

# Calculate the pressure and velocity using Bernoulli's equation
v = np.linspace(v0, 50, 100)  # velocity range
P = P0 - 0.5 * rho * (v**2 - v0**2)  # pressure calculation

# Create the plot
plt.plot(v, P)
plt.xlabel('Velocity (m/s)')
plt.ylabel('Pressure (Pa)')
plt.title("Bernoulli's Theorem")
plt.grid(True)

# Add a horizontal line for the initial pressure
plt.axhline(y=P0, color='gray', linestyle='--', label='Initial Pressure')

# Add a vertical line for the initial velocity
plt.axvline(x=v0, color='gray', linestyle='--', label='Initial Velocity')

plt.legend()
plt.show()