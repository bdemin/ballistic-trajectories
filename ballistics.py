import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g


v0_list = np.arange(40, 100, step = 10)

theta = np.pi/4

time_vector = np.linspace(0, 50, num = 1000)

for v0 in v0_list: # Calculate trajectory for every initial velocity
    x1 = []
    y1 = []
    for t in time_vector:
        x = (v0*t) * np.cos(theta)
        y = (v0*t) * np.sin(theta) - (0.5*g) * (t**2)
        x1.append(x)
        y1.append(y)
        
    # Remove negative y values
    p = [i for i, j in enumerate(y1) if j < 0]                         
    for i in sorted(p, reverse = True):
        del x1[i]
        del y1[i]

    plt.plot(x1, y1, label = 'V0 = {}'.format(v0))


plt.legend()
plt.show()
