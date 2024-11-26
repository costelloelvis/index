import time
import os
import random

# ASCII art DVD logo
dvd_logo = """
   __
  /  \
 /    \
|  DVD  |
 _____/
"""

# Screen dimensions
width, height = 80, 20

# Initial logo position
x, y = width // 2, height // 2

# Bouncing animation
while True:
    # Clear the screen
    os.system("clear" if os.name == "posix" else "cls")

    # Print the logo at the current position
    print("\n" * y + " " * x + dvd_logo)

    # Move the logo
    dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    x = max(0, min(x + dx, width - len(dvd_logo)))
    y = max(0, min(y + dy, height - len(dvd_logo.splitlines())))

    # Wait a bit
    time.sleep(0.1)