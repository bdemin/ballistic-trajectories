import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g


v0_list = np.arange(40, 100, step = 10)

theta = np.pi/4

time_vector = np.linspace(0, 50, num = 1000)

for v0 in v0_list: # Calculate trajectory for every initial speed
    x1 = []
    y1 = []
    for t in time_vector:
        x = (v0*t) * np.cos(theta) # Get positions at every point in time
        y = (v0*t) * np.sin(theta) - (0.5*g) * (t**2)
        x1.append(x)
        y1.append(y)
        
    plt.plot(x1, y1) # Plot for every angle

plt.show()
