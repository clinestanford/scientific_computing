#!/usr/bin/python

####################################################
# module: diff_eq_sols.py
# description: some solutions to y' = 0.3y.
#
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def diff_eq_sols():
  f1 = lambda t: math.e**(0.3*t)
  f2 = lambda t: 3*(math.e**(0.3*t))
  f3 = lambda t: 5*(math.e**(0.3*t))
  f4 = lambda t: 7*(math.e**(0.3*t))
  f5 = lambda t: 9*(math.e**(0.3*t))
  xvals = np.linspace(-3, 3, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  yvals2 = np.array([f2(x) for x in xvals])
  yvals3 = np.array([f3(x) for x in xvals])
  yvals4 = np.array([f4(x) for x in xvals])
  yvals5 = np.array([f5(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('Solutions to y\' = 0.3y')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.ylim([0, 10])
  plt.xlim([-3, 3])
  plt.grid()
  plt.plot(xvals, yvals1, label='e^{0.3t}', c='r')
  plt.plot(xvals, yvals2, label='3e^{0.3t}', c='g')
  plt.plot(xvals, yvals3, label='5e^{0.3t}', c='b')
  plt.plot(xvals, yvals4, label='7e^{0.3t}', c='m')
  plt.plot(xvals, yvals5, label='9e^{0.3t}', c='r')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  diff_eq_sols()
