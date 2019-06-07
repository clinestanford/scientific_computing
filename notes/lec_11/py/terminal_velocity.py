#!/usr/bin/python

####################################################
# module: terminal_velocity.py
# description: terminal velocity simulation
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def terminal_velocity(M, k):
  f1 = lambda t: M*(1.0 - (math.e**(-k*t)))
  xvals = np.linspace(0, 200, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('Terminal Velocity')
  plt.xlabel('t (time)')
  plt.ylabel('Downward Velocity')
  #plt.ylim([0, 10])
  plt.xlim([0, 25])
  plt.grid()
  plt.plot(xvals, yvals1, label='v(t) = ' + str(M) + '(1 - e^{-' + str(k) + 't})', c='b')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  terminal_velocity(100, 0.5)
  terminal_velocity(100, 0.25)
  terminal_velocity(100, 0.125)
