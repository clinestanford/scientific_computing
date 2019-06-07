#!/usr/bin/python

####################################################
# module: strontium90.py
# description: exponential decay model of
# the half-life of strontium 90 with P_0 = 100 grams
#
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

# returns an exponential decay model of strontium 90
# given original mass in grams.
def s90(P0):
  return lambda t: P0*(math.e**(-0.0244*t))

def strontium90():
  f1 = s90(100)
  xvals = np.linspace(0, 200, 100000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('y = s90 decay')
  plt.xlabel('years')
  plt.ylabel('grams')
  #plt.ylim([0, 5])
  plt.xlim([0, 200])
  plt.grid()
  plt.plot(xvals, yvals1, label='s90 decay', c='r')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  strontium90()
