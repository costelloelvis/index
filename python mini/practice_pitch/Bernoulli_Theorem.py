import math

# Function to calculate pressure using Bernoulli's theorem
def bernoulli_theorem(v, p, rho, g, h):
    """
    v: velocity of the fluid
    p: pressure of the fluid
    rho: density of the fluid
    g: acceleration due to gravity
    h: height above a reference plane (potential energy term)
    """
    kinetic_energy = 0.5 * rho * v**2  # Kinetic energy term
    potential_energy = rho * g * h     # Potential energy term
    total_pressure = p + kinetic_energy + potential_energy
    return total_pressure

# Example usage:
velocity = 10.0   # m/s
pressure = 100000 # Pa (assuming atmospheric pressure as a base)
density = 1.2     # kg/m^3 (air density at sea level)
gravity = 9.81    # m/s^2 (acceleration due to gravity)
height = 20.0     # m

total_pressure = bernoulli_theorem(velocity, pressure, density, gravity, height)
print(f"Total pressure according to Bernoulli's theorem: {total_pressure} Pa")