#!/usr/bin/python

####################################################
# module: glucose_infusion.py
# description: glucose infusion model
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def glucose_infusion(r, lmbda):
  f1 = lambda t: (lmbda/r)*(1.0 - (math.e**(-lmbda*t)))
  xvals = np.linspace(0, 200, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('Continuous Glucose Infusion')
  plt.xlabel('t (time)')
  plt.ylabel('Excess Glucose')
  #plt.ylim([0, 10])
  plt.xlim([0, 25])
  plt.grid()
  plt.plot(xvals, yvals1, label='v(t) = ' + str(r) + '/' + str(lmbda) + '(1 - e^{-' + str(lmbda) + 't})', c='m')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  glucose_infusion(10, 0.5)
