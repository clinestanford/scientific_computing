#!/usr/bin/python

####################################################
# module: diff_eq2.py
# description: solution to y' = 3y, y(0) = 2.
#
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def diff_eq2():
  f1 = lambda t: 2*math.e**(0.3*t)
  xvals = np.linspace(-10, 10, 100000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('y = 2e^{3t}')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.ylim([0, 5])
  plt.xlim([-5, 5])
  plt.grid()
  plt.plot(xvals, yvals1, label='2e^{3t}', c='r')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  diff_eq2()
