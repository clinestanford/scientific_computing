#!/usr/bin/python

####################################################
# module: learning_curve.py
# description: learning curve simulation
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def learning_curve(M, k):
  f1 = lambda t: M*(1.0 - (math.e**(-k*t)))
  xvals = np.linspace(0, 200, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('Learning Syllables')
  plt.xlabel('t (time)')
  plt.ylabel('Syllables Memorized')
  #plt.ylim([0, 10])
  plt.xlim([0, 25])
  plt.grid()
  plt.plot(xvals, yvals1, label='v(t) = ' + str(M) + '(1 - e^{-' + str(k) + 't})', c='g')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  learning_curve(50, 0.25)
