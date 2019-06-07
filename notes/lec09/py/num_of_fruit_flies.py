#!/usr/bin/python

####################################################
# module: num_of_fruit_flies.py
# description: P(0) = 6; P(t) = Ce^{0.3t}. So that
# P(t) = 6e^{0.3t}
#
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def num_of_fruit_flies():
  f1 = lambda t: 6*math.e**(0.3*t)
  xvals = np.linspace(0, 7, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('y =- 6e^{0.3t}')
  plt.xlabel('x')
  plt.ylabel('y')
  #plt.ylim([0, 10])
  plt.xlim([0, 7])
  plt.grid()
  plt.plot(xvals, yvals1, label='6e^{0.3t}', c='r')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  num_of_fruit_flies()
