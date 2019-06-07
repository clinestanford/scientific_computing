#!/usr/bin/python

######################################
# module: e_to_kx_neg.py
# graphs on slide 29 of lecture 7.
# bugs to vladimir kulyukin via canvas.
######################################

import math
import numpy as np
import matplotlib.pyplot as plt

def e_kx():
  f1 = lambda x: math.e**(-5.0*x)
  f2 = lambda x: math.e**(-4.0*x)
  f3 = lambda x: math.e**(-3.0*x)
  f4 = lambda x: math.e**(-2.0*x)
  f5 = lambda x: math.e**(-0.5*x)
  xvals = np.linspace(-3, 3, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  yvals2 = np.array([f2(x) for x in xvals])
  yvals3 = np.array([f3(x) for x in xvals])
  yvals4 = np.array([f4(x) for x in xvals])
  yvals5 = np.array([f5(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('y = e^{kx}, k < 0')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.ylim([0, 10])
  plt.xlim([-3, 3])
  plt.grid()
  plt.plot(xvals, yvals1, label='e^{-5x}', c='red')
  plt.plot(xvals, yvals2, label='e^{-4x}', c='green')
  plt.plot(xvals, yvals3, label='e^{-3x}', c='blue')
  plt.plot(xvals, yvals4, label='e^{-2x}', c='brown')
  plt.plot(xvals, yvals5, label='e^{-0.5x}', c='magenta')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  e_kx()
