#!/usr/bin/python

#################################
# module: car_deaths_plot.py
# description: car-accident-related deaths
# bugs to vladimir kulyukin via canvas.
#################################

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 10, 15, 17, 18, 19])
y = np.array([46.8, 43.4, 45.3, 43.9, 39.7, 35.9])

plt.scatter(x, y)
plt.title('Car-Accident-Related Deaths in U.S.')
plt.xlabel('x (years since 1990)')
plt.ylabel('y (deaths (in thousands)')
plt.autoscale(tight=True)
plt.xlim([0, 20])
plt.ylim([0, 50])
plt.grid()
plt.show()
