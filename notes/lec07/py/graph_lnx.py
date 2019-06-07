#!/usr/bin/python

######################################
# module: graph_lnx.py
# graph on slide 43 of lecture 7.
# bugs to vladimir kulyukin via canvas.
######################################

import math
import numpy as np
import matplotlib.pyplot as plt

def graph_lnx():
  lnx = lambda x: math.log(x, math.e)
  xvals = np.linspace(0.01, 10, 10000)
  yvals2 = np.array([lnx(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('y = ln(x)')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  #plt.plot(xvals, yvals1, label='e^x', c='red')
  plt.plot(xvals, yvals2, label='lnx', c='green')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  graph_lnx()
