#!/usr/bin/python

####################################################
# module: diff_eq3.py
# description: solution to P(t) = P_{0}e^{kt}, P(0) = 20,
# P(5) = 400.
#
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def diff_eq3():
  f1 = lambda t: 20*(math.e**((math.log(20.0)/5.0)*t))
  xvals = np.linspace(0, 5, 100000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('y = 20e^{(ln(20)/5)t}')
  plt.xlabel('x')
  plt.ylabel('y')
  #plt.ylim([0, 5])
  plt.xlim([0, 5])
  plt.grid()
  plt.plot(xvals, yvals1, label='y = 20e^{(ln(20)/5)t}', c='g')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  diff_eq3()
